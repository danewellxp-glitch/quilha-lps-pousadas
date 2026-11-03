"""Índices de fotos do lote 3 (4 Estações, Vila Porto da Lagoa)."""
import os
B = os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'l3')


def _idx(sheet, folder):
    d = {}
    for l in open(os.path.join(B, 'sheets', sheet)).read().strip().split('\n'):
        p = l.split('\t'); d[int(p[0])] = os.path.join(B, folder, p[1])
    return d


_c = {}


def pic(kind, i):
    """kind: e=gm 4 Estações, ie=IG 4 Estações, v=gm Vila, iv=IG Vila"""
    m = {'e': ('gm_pousada4estacoescampeche_idx.txt', 'gm/pousada4estacoescampeche'),
         'ie': ('ig4e_idx.txt', 'ig/pousada4estacoescampeche'),
         'v': ('gm_vilaportodalagoa_idx.txt', 'gm/vilaportodalagoa'),
         'iv': ('ig_vilaportodalagoa_idx.txt', 'ig/vilaportodalagoa')}
    if kind not in _c: _c[kind] = _idx(*m[kind])
    return _c[kind][i]
