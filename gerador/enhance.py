"""Tratamento de fotos para os sites (Quilha).

enhance(src, dst, target=2200, look='praia')
  1. super-resolução EDSR x2 (OpenCV dnn_superres) quando o lado maior < target
  2. balanço de branco suave (gray-world parcial), CLAHE leve na luminância,
     curva S suave, recuperação de altas luzes, vibrance (satura mais o que está lavado),
     leve calor ("praia")
  3. redimensiona para target (Lanczos) e aplica unsharp mask
Sem IA generativa: nada é inventado na foto, só luz, cor e nitidez.
"""
import os, sys, time
import numpy as np, cv2
from PIL import Image, ImageOps, ImageFilter

MODEL = os.environ.get('QD_MODEL', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'FSRCNN_x2.pb'))
_sr = None


def _get_sr():
    global _sr
    if _sr is None:
        _sr = cv2.dnn_superres.DnnSuperResImpl_create()
        _sr.readModel(MODEL); _sr.setModel('fsrcnn', 2)
    return _sr


def sr2x(bgr, tile=360, pad=12):
    """Super-resolução x2 em tiles (memória/CPU)."""
    sr = _get_sr()
    h, w = bgr.shape[:2]
    out = np.zeros((h * 2, w * 2, 3), np.uint8)
    for y in range(0, h, tile):
        for x in range(0, w, tile):
            y0, x0 = max(0, y - pad), max(0, x - pad)
            y1, x1 = min(h, y + tile + pad), min(w, x + tile + pad)
            r = sr.upsample(np.ascontiguousarray(bgr[y0:y1, x0:x1]))
            ty, tx = (y - y0) * 2, (x - x0) * 2
            th, tw = min(tile, h - y) * 2, min(tile, w - x) * 2
            out[y * 2:y * 2 + th, x * 2:x * 2 + tw] = r[ty:ty + th, tx:tx + tw]
    return out


def grade(rgb, warmth=0.025, clahe=1.3):
    """Ajuste adaptativo: só corrige o que precisa (fotos do IG já vêm tratadas)."""
    f = rgb.astype(np.float32) / 255.0
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(np.float32) / 255.0
    sat, val = hsv[..., 1], hsv[..., 2]
    # balanço de branco pelos tons neutros (parede branca, piso, céu nublado)
    neu = (sat < 0.12) & (val > 0.3) & (val < 0.95)
    if neu.mean() > 0.04:
        m = f[neu].mean(0); g = m.mean()
        cast = np.abs(m / g - 1).max()
        if cast > 0.025:
            f = np.clip(f * (1 + 0.6 * (g / np.maximum(m, 1e-3) - 1)), 0, 1)
    # exposição: levanta foto escura (gamma), segura foto estourada
    L = f.mean()
    if L < 0.42:
        f = f ** (0.42 / max(L, 0.2)) ** 0.6
    # CLAHE leve na luminância (micro-contraste)
    lab = cv2.cvtColor((f * 255).astype(np.uint8), cv2.COLOR_RGB2LAB)
    Lc = lab[..., 0]
    cl = cv2.createCLAHE(clipLimit=clahe, tileGridSize=(8, 8)).apply(Lc)
    lab[..., 0] = cv2.addWeighted(Lc, 0.5, cl, 0.5, 0)
    f = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB).astype(np.float32) / 255.0
    # curva S suave + segura as altas luzes
    f = f + 0.10 * (f - 0.5) * (1 - np.abs(2 * f - 1))
    f = np.where(f > 0.88, 0.88 + (f - 0.88) * 0.7, f)
    # vibrance adaptativa: foto lavada ganha cor, foto já saturada fica como está
    vib = float(np.clip(0.38 - sat.mean() * 0.9, 0, 0.25))
    mx, mn = f.max(2, keepdims=True), f.min(2, keepdims=True)
    lum = f.mean(2, keepdims=True)
    f = lum + (f - lum) * (1 + vib * (1 - (mx - mn)))
    # leve calor
    f[..., 0] *= 1 + warmth; f[..., 2] *= 1 - warmth * 0.8
    return (np.clip(f, 0, 1) * 255).astype(np.uint8)


def enhance(src, dst, target=2200, q=80, warmth=0.03, crop=None):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if crop:  # (l, t, r, b) em fração
        W, H = im.size
        im = im.crop((int(crop[0] * W), int(crop[1] * H), int(crop[2] * W), int(crop[3] * H)))
    rgb = np.asarray(im)
    if max(rgb.shape[:2]) < target * 0.92:
        bgr = sr2x(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    rgb = grade(rgb, warmth=warmth)
    out = Image.fromarray(rgb)
    out.thumbnail((target, target), Image.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=45, threshold=3))
    out.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)
    return out.size


if __name__ == '__main__':
    t = time.time(); print(enhance(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 2200), round(time.time() - t, 1), 's')
