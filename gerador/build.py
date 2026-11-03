"""Build the 5 pousada landing pages from templates + per-pousada data modules.

Outputs:
  out/<slug>/index.html          -> deploy-ready (full HTML doc, Google Maps iframe)
  out/<slug>/img/*.jpg           -> optimised photos
  art/<slug>.html                -> artifact version (no doctype, no iframe), uses img/<slug>/...
"""
import json, os, sys, shutil, importlib, datetime, urllib.parse
from PIL import Image, ImageOps
from jinja2 import Environment, FileSystemLoader
sys.path.insert(0, os.path.dirname(__file__))
from icons import icon, star_fill

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'out')
env = Environment(loader=FileSystemLoader(os.path.join(BASE, 'tpl')), autoescape=True)
env.globals.update(icon=icon, stars=star_fill, year=datetime.date.today().year)


# templates with more than one page: [(template, output name)]
PAGES = {'casa': [('casa', 'index'), ('casa_reservas', 'reservas')]}


def prep_img(src, dst, maxside=2200, q=82):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im).convert('RGB')
    im.thumbnail((maxside, maxside), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)
    return im.size


def wa(number, text):
    return f"https://wa.me/{number}?text={urllib.parse.quote(text)}"


def build(slug):
    mod = importlib.import_module(f'data.{slug}')
    p, t, tpl = mod.P, mod.T, mod.TEMPLATE
    odir = os.path.join(OUT, slug); idir = os.path.join(odir, 'img')
    if os.path.isdir(odir): shutil.rmtree(odir)
    os.makedirs(idir)
    cache = {}

    enh = getattr(mod, 'ENHANCE', False)

    def I(src, name=None, maxside=2200, big=False, crop=None):
        """copy+optimise src photo, return (img/<name>.jpg, w, h).
        ENHANCE=True no módulo: passa pelo tratamento (enhance.py) com cache em enh_cache/."""
        key = (src, big, crop)
        if key in cache: return cache[key]
        name = name or f"{len(cache)+1:02d}"
        dst = os.path.join(idir, name + '.jpg')
        if enh:
            import hashlib, enhance
            target = 2400 if big else 1400
            h = hashlib.md5(f'{src}|{target}|{crop}|v4'.encode()).hexdigest()[:16]
            cpath = os.path.join(BASE, 'enh_cache', h + '.jpg')
            if not os.path.exists(cpath):
                os.makedirs(os.path.dirname(cpath), exist_ok=True)
                enhance.enhance(src, cpath, target=target, crop=crop)
            shutil.copy(cpath, dst)
            w, hh = Image.open(dst).size
        else:
            w, hh = prep_img(src, dst, maxside)
        cache[key] = (f"img/{name}.jpg", w, hh)
        return cache[key]

    ctx = mod.context(I, wa)
    ctx['wa_link'] = wa(p['wa_number'], p['wa_text'])
    ctx.update({k: v for k, v in p.items() if k not in ctx})
    # reviews helpers
    rv = ctx['reviews']
    heads = {'all': rv['headline']}
    for s in rv['sources']: heads[s['key']] = s.get('head', rv['headline'])
    rv['heads_json'] = json.dumps(heads, ensure_ascii=False)
    if 'gallery' in ctx:
        ctx['gallery']['all_json'] = json.dumps([g['src'] for g in ctx['gallery']['imgs']])
    extra = getattr(mod, 'extra', lambda: {})()

    pages = PAGES.get(tpl, [(tpl, 'index')])

    def wrap(html):
        head, _, body = html.partition('</style>')
        return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + head + '</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')

    for mode in ('site', 'art'):
        for i, (tname, fname) in enumerate(pages):
            html = env.get_template(tname + '.html').render(
                p=ctx, t=t, embed_map=(mode == 'site'), home_href=('index.html' if mode == 'site' else './'), **extra)
            if mode == 'site':
                open(os.path.join(odir, fname + '.html'), 'w').write(wrap(html))
            elif i == 0:
                open(os.path.join(odir, 'artifact.html'), 'w').write(html)
            else:  # extra pages of the artifact are published as full documents
                adir = os.path.join(odir, '_art'); os.makedirs(adir, exist_ok=True)
                open(os.path.join(adir, fname + '.html'), 'w').write(wrap(html))
    tot = sum(os.path.getsize(os.path.join(idir, f)) for f in os.listdir(idir))
    print(slug, tpl, len(os.listdir(idir)), 'imgs', round(tot / 1048576, 1), 'MB')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        build(s)
