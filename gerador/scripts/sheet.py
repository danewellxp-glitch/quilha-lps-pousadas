import sys, glob, os
from PIL import Image, ImageDraw, ImageFont
d=sys.argv[1]; out=sys.argv[2]
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
# uso: python scripts/sheet.py <pasta de fotos> <saida sem extensao>  ->  <saida>_0.jpg ... + <saida>_idx.txt
fs=sorted(glob.glob(d+'/*.jpg'))
from PIL import UnidentifiedImageError
ok=[]
for f in fs:
    try: Image.open(f).size; ok.append(f)
    except Exception: print('ignorado (corrompido):', f)
fs=ok
cols=6; tw=260; th=260
font=ImageFont.load_default(size=22) if hasattr(ImageFont,'load_default') else None
pages=[fs[i:i+36] for i in range(0,len(fs),36)]
for pi,pg in enumerate(pages):
    rows=(len(pg)+cols-1)//cols
    S=Image.new('RGB',(cols*tw,rows*th),'white'); dr=ImageDraw.Draw(S)
    for i,f in enumerate(pg):
        im=Image.open(f); im.thumbnail((tw-6,th-6))
        x=(i%cols)*tw; y=(i//cols)*th
        S.paste(im,(x+3,y+3))
        idx=fs.index(f)
        dr.rectangle([x+3,y+3,x+60,y+30],fill='black'); dr.text((x+7,y+5),str(idx),fill='yellow',font=font)
    S.save(f'{out}_{pi}.jpg',quality=80)
with open(out+'_idx.txt','w') as fh:
    for i,f in enumerate(fs):
        w,h=Image.open(f).size; fh.write(f'{i}\t{os.path.basename(f)}\t{w}x{h}\n')
