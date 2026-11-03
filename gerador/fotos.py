"""Fotos das pousadas no layout padrão (use em toda pousada nova).

<QD_FOTOS>/<slug>/ig/*.jpg          fotos do Instagram (originais da API, >=1080px)
<QD_FOTOS>/<slug>/gm/*.jpg          fotos do Google Maps (=s2400)
<QD_FOTOS>/<slug>/_sheets/ig_idx.txt   gerado por scripts/sheet.py (índice -> arquivo)
<QD_FOTOS>/<slug>/_sheets/gm_idx.txt

Uso no data/<slug>.py:
    from fotos import Fotos
    F = Fotos('minhapousada')
    F.ig(12)  -> caminho da foto 12 da planilha de contato do Instagram
    F.gm(5)   -> caminho da foto 5 da planilha do Google Maps
"""
import os

ROOT = os.environ.get('QD_FOTOS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_fotos'))


class Fotos:
    def __init__(self, slug, root=None):
        self.base = os.path.join(root or ROOT, slug)
        self._idx = {}

    def _get(self, kind, i):
        if kind not in self._idx:
            p = os.path.join(self.base, '_sheets', f'{kind}_idx.txt')
            d = {}
            for l in open(p, encoding='utf-8').read().strip().split('\n'):
                c = l.split('\t'); d[int(c[0])] = os.path.join(self.base, kind, c[1])
            self._idx[kind] = d
        return self._idx[kind][i]

    def ig(self, i): return self._get('ig', i)

    def gm(self, i): return self._get('gm', i)

    def gmfix(self, i):
        """Foto do Maps com correção do tom roxo de HDR (scripts/fix_purple.py). Cache em <slug>/gm_fix/."""
        src = self.gm(i)
        out = os.path.join(self.base, 'gm_fix', os.path.basename(src))
        if not os.path.exists(out):
            import sys
            sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))
            from fix_purple import fix
            os.makedirs(os.path.dirname(out), exist_ok=True)
            fix(src, out)
        return out
