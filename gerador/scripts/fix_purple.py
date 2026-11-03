"""Corrige o tom roxo/lilás de fotos HDR (céu roxo, cascalho lilás) que vêm de alguns fotógrafos no Google Maps.
Uso: python scripts/fix_purple.py <entrada.jpg> <saida.jpg> [forca=1.0]
Puxa os tons entre azul-violeta e magenta (hue 255-335°) para o azul e tira saturação dos tons lilás claros.
"""
import sys
import cv2
import numpy as np


def fix(src, dst, k=1.0):
    im = cv2.imread(src)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    # OpenCV hue 0-180. Faixa roxa ~128-168 (256-336 graus)
    w = np.clip((h - 122) / 10, 0, 1) * np.clip((172 - h) / 8, 0, 1) * k
    target = 112.0  # azul ~224 graus
    h2 = h - w * 0.85 * (h - target)
    # tons lilás pouco saturados (cascalho, nuvem) perdem saturação; céu saturado mantém mais
    low = np.clip((140 - s) / 90, 0, 1)
    s2 = s * (1 - w * (0.25 + 0.5 * low))
    hsv2 = np.stack([h2, s2, v], -1).clip(0, 255)
    hsv2[..., 0] = hsv2[..., 0].clip(0, 179)
    out = cv2.cvtColor(hsv2.astype(np.uint8), cv2.COLOR_HSV2BGR)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 95])


if __name__ == '__main__':
    fix(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 1.0)
