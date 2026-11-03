# quilha-lps-pousadas

Gerador de LPs e sites de prévia para pousadas (prospecção da Quilha Digital). Fonte de verdade usada pela skill `sites-pousadas-quilha`, em qualquer computador.

- `gerador/` — build (Jinja + Pillow + OpenCV), templates em `gerador/tpl/`, catálogo em `gerador/tpl/CATALOGO.md`, um módulo por pousada em `gerador/data/`.
- `REGISTRO.md` — pousadas que já têm prévia.

Uso rápido:

```bash
cd gerador && bash setup.sh
export QD_FOTOS=/caminho/das/fotos   # <slug>/{ig,gm}/
python build.py <slug>               # -> out/<slug>/
```

Fotos e saídas (`out/`, `enh_cache/`) não são versionadas. Detalhes em `gerador/LEIA-ME-gerador.md`.
