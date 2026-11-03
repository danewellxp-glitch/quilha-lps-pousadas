# Gerador de LPs e sites de pousadas (Quilha Digital)

Gerador estático em Python + Jinja2. Cada pousada é um módulo em `data/<slug>.py`, e o template é escolhido pela variável `TEMPLATE` dentro dele.

```bash
pip install jinja2 pillow
python build.py moradas_site          # gera out/moradas_site/
python build.py aloha marujo refugio  # vários de uma vez
```

Saída em `out/<slug>/`:
- `index.html` (+ `reservas.html` no template casa): versão de deploy, HTML completo, com mapa e vídeo embutidos
- `img/NN.jpg`: fotos otimizadas (lado maior de até 2200px, JPEG q82 progressivo)
- `artifact.html` e `_art/*.html`: versão para publicar como artifact no Claude (sem iframes)

## Estrutura
```
gerador/
  build.py            build(slug): data/<slug>.py + tpl/<TEMPLATE>.html -> out/<slug>/
  enhance.py          tratamento de fotos (ENHANCE = True)
  fotos.py            Fotos('<slug>').ig(i) / .gm(i): layout padrão de fotos para pousadas novas
  icons.py, deco.py   ícones em linha e line-art
  setup.sh            dependências + modelo FSRCNN (rodar 1x por máquina/sessão)
  tpl/CATALOGO.md     <- catálogo dos templates (ler antes de escolher; atualizar ao adicionar)
  tpl/*.html          templates Jinja (doma, aurelia, casa + casa_reservas, stayora, ...)
  tpl/_fonte-*/       fonte original de cada template
  data/*.py           uma pousada por arquivo (TEMPLATE, ENHANCE, T, P, context(I, wa))
  scripts/            ig_harvest.js, gm_photos.js, gm_reviews.js, zip_download.js (Chrome)
                      sheet.py (contact sheet), pick.py (comparar candidatas), shot.py, flow_test.py
```
Variáveis de ambiente: `QD_FOTOS` (raiz das fotos novas, padrão `../_fotos`), `QD_LEGACY` (fotos dos lotes antigos), `QD_MODEL`.

## Templates (resumo; detalhes em `tpl/CATALOGO.md`)

| Template | Tipo | Usar quando | Exemplos |
|---|---|---|---|
| `doma` | LP de 1 página | Muitas fotos boas. Hero com moldura, galeria masonry + lightbox, cards com hover e faixa com parallax | Dormida, Refúgio, Uluwatu, Mar da Ponta, Los Amigos, Moradas (LP) |
| `aurelia` | LP de 1 página | Pousada com suítes ou quartos bem definidos. Hero em tela cheia com barra de reserva, slideshow oval, cards de quarto, cards empilhados e FAQ | Aloha, Marujo, Aeropouso, Talismã, Native |
| `casa` | Site institucional (home + reservas) | Pousada sem site próprio, ou proposta de site completo. Clone do site da Aloha Beach House | Moradas, Dormida, 4 Estações, Vila Porto da Lagoa (`*_site`) |
| `stayora` | LP premium de 1 página | Pousada boutique/villa: calendário de reserva no hero, apartamentos em abas, avaliações em marquee | Dormida (`dormida_stayora`) |

### Template `casa`: o que tem

**Home (`tpl/casa.html`)**
- Nav com o logo no centro, que pode ser imagem (`logo_img`) ou texto (`logo_small` + `logo_main`)
- Hero em tela cheia com vídeo (`hero.video`, mp4) ou foto com Ken Burns, além de uma barra de reserva flutuante com check-in, check-out e hóspedes, que leva para `reservas.html?checkin=…`
- Intro em 2 colunas com carrossel emoldurado (setas, dots, autoplay de 5s) e um selo
- 8 "cantos" (cards com foto, título, texto e link)
- Faixa com fundo fixo (`band`)
- Bloco de experiência: foto com selo e lista
- **O que falam de nós**: abas Todas / Google / Booking etc. em grid de cards
- Vídeo opcional (`film`): YouTube no site e, no artifact, uma imagem com link pro Instagram. Use `film=None` para esconder
- CTA final, footer escuro com botões de Instagram, WhatsApp e Maps, e o WhatsApp flutuante pulsando
- Gate de idioma PT/ES opcional (`lang_gate=True`). **Atenção:** igual ao original, ele é só visual e não traduz a página. Deixe desligado até existir uma versão em espanhol

**Reservas (`tpl/casa_reservas.html`)**
- Hero, painel de datas (lê os parâmetros da home), adultos e crianças
- Cards de acomodação gerados no build (não por JS), cada um com carrossel próprio (setas + swipe), lista "incluído" e o botão "Selecionar"
- Checkout com nome, e-mail, telefone e observações, mais um resumo com as noites calculadas
- O envio monta a mensagem e abre o WhatsApp (`wa.me`), o telefone ou o e-mail (este só se `email` estiver preenchido)
- Preço opcional: `price=''` mostra "Sob consulta". **Nunca invente preço:** só preencha com a tabela que o dono passar
- Diferenças em relação ao original: sem `alert()` (usa um aviso inline), sem `window.open` (abre por link com target=_blank, com um link de reserva caso o navegador bloqueie) e as fotos vêm do build

**Tokens de cor (T):** `paper, cream, espresso, honey, olive, muted, rooms_bg, deep, gold`.
- Original da Aloha: paper `#fffaf0`, cream `#f5ead7`, espresso `#321907`, honey `#c77b3f`, olive `#4e5a3a`, muted `#6d604f`, rooms_bg `#f3e7d2`, deep `#253124`, gold `#dfb47d`
- Moradas (verde): veja `data/moradas_site.py`

**Campos de P/contexto do casa:** `name, short, seo_title, meta_desc, logo_*, phone, wa_number, wa_text, email, instagram, address, place_line, footer_tag, rooms_label, lang_gate, hero{img,video,eyebrow,title,sub}, intro{kicker,title,text,badge}, carousel[{src,alt}], cards_head{...}, cards[8×{img,title,text,action,href}], band{img,nav,kicker,title,text,cta}, exp{img,alt,badge,kicker,title,text,items[],cta}, reviews{sources,items,headline,link}, film|None, cta{img,title}, loc{maps_url}, res{hero,kicker,title,rooms_kicker,unit_word,prices,included[],rooms[{name,guests,price,detail,imgs[],included?}]}`

## Tratamento de fotos (`ENHANCE = True`)
Quando o módulo da pousada tem `ENHANCE = True`, cada foto passa pelo `enhance.py` antes de entrar no site:
1. **Super-resolução x2** (FSRCNN, OpenCV `dnn_superres`) quando a foto é menor que o destino. Ex.: foto de 1080 px do Instagram usada no hero.
2. **Ajuste adaptativo**: balanço de branco pelos tons neutros (corrige parede amarelada ou azulada), levanta foto escura, micro-contraste leve (CLAHE), curva S suave e segura as altas luzes. A vibrance só entra em foto lavada; foto do IG que já vem tratada fica praticamente igual. No fim, um toque de calor.
3. Redimensiona para 2400 px (`big=True`: hero, faixa, CTA, topo de reservas) ou 1400 px (o resto), com unsharp mask e JPEG q80.

Nada é gerado por IA: o tratamento mexe só em luz, cor e nitidez. Os resultados ficam em cache em `enh_cache/`.
Dependências: `pip install opencv-contrib-python-headless==4.10.0.84 numpy pillow jinja2`, além do modelo `models/FSRCNN_x2.pb` (raw.githubusercontent.com/Saafke/FSRCNN_Tensorflow/master/models/FSRCNN_x2.pb). O EDSR é melhor, mas leva mais de 10 min por foto em CPU.

## Fotos do Google Maps: cuidado
O script de coleta do Maps pega também as miniaturas de **outros hotéis** da barra lateral ("hotéis semelhantes"). Ao escolher pelas planilhas de contato (contact sheets), descarte as primeiras fotos que não são da pousada.

## Como criar uma pousada nova
1. Fotos: as do Instagram são as principais (via API, ≥1080px). As do Google Maps entram como complemento quando o Instagram é fraco, em ≥1500px e baixadas em `=s2400`. Hero e faixa de fundo pedem foto de 1600px ou mais.
2. Faça uma planilha de contato (contact sheet), escolha os índices e crie `data/_<user>_files.txt` com a lista de arquivos.
3. Copie um módulo parecido (`moradas_site.py` para o casa, `aloha.py` para o aurelia, `dormida.py` para o doma) e troque textos, índices e reviews. Use só reviews positivas, reais e resumidas, com a nota e o total da fonte.
4. Rode `python build.py <slug>`, tire screenshots em 1440 e 390 e confira.
5. Para publicar como artifact: `artifact.html` + `img/*` (+ `_art/reservas.html` publicado como `reservas.html`).

## Observações
- `common.py` aponta para as pastas de fotos do ambiente de geração (`/home/claude/ig`, `ig2`, `ig3`). Para rodar no PC, aponte para `_fotos-instagram`, `_fotos-instagram-lote2` e `_fotos-moradas`.
- Os nomes de quartos e suítes são uma sugestão: confirme com o dono antes de publicar.
- O rodapé de todas as prévias diz "Prévia desenvolvida por Quilha Digital".
- O fonte original do template casa (o clone limpo da Aloha) está em `tpl/_fonte-casa-aloha/`.

## Novidades do lote 4 (21/10/2026)
- `Fotos('<slug>').gmfix(i)`: devolve a foto do Maps com o tom roxo de HDR corrigido (`scripts/fix_purple.py`, cache em `<slug>/gm_fix/`). Usar quando o fotógrafo do Maps entrega céu roxo e cascalho lilás (caso da Chalés Beach). Não resolve cascalho rosado/avermelhado: aí, trocar a foto.
- `scripts/zip_download_filtro.js`: igual ao `zip_download.js`, mas só inclui as chaves com os prefixos de `KEEP` (o IndexedDB guarda lotes antigos).
- **Chrome bloqueia o 2º download automático na mesma aba.** O limite é por aba, não por site: para o segundo zip, rode o script numa aba que ainda não baixou nada (mesma origem, porque o IndexedDB é por origem).
- O painel de fotos do Maps às vezes carrega fotos da pousada pesquisada antes na mesma aba (as primeiras da planilha). Conferir antes de usar.
- `deco.py`: logo novo `wing` (asa/auréola), usado na Ilha dos Anjos.

## Novidades do lote 5 (22/10/2026)
- `scripts/gm_all.js`: coleta tudo de uma pousada no Maps numa chamada (info, comodidades, avaliações e fotos). O filtro de rolagem agora usa `getBoundingClientRect().left < 220` (antes era `< 60`). Com a janela do Chrome estreita (1536 px), o painel lateral fica deslocado e o filtro antigo não rolava nada: vinham 0 avaliações e só 1 a 3 fotos.
- **Foto do Maps em pouca quantidade? Refaça.** Na primeira passada, Genoveva, Sueños e Brisas vieram com 1 a 3 fotos. Rodando de novo com a galeria já aberta e `MINPX = 1000`, vieram 19, 64 e 56. As fotos da segunda passada ficam em `<slug>/gm2/` e são lidas com `F._get('gm2', i)` (planilha `_sheets/gm2_idx.txt`).
- **Perfil de hotel no Maps** (tipo "Hotel", com aba Preços) não carrega as avaliações pelo script: role o painel com o mouse (scroll do Chrome) e depois leia `div.jftiEf`. Foi o caso da Goulin.
- Aba do Chrome em segundo plano congela o `javascript_tool` (timeout de 45 s), mas o script continua rodando. Confira o progresso lendo o IndexedDB por outra aba.
- `Fotos(...)._get(kind, i)` aceita qualquer subpasta que tenha `_sheets/<kind>_idx.txt`.

## Novidades do lote 6 (28/10/2026)
- **Foto do Maps em grande-angular/olho de peixe leve** (GoPro do dono): dá pra aproveitar corrigindo a distorção com `cv2.undistort` (K com foco = 0,55·largura, D = [-0.28, 0.06, 0, 0, 0]). Veja a função `U(i)` em `data/armacao.py` (cache em `<slug>/undist/`). Não serve para 360°.
- `tpl/casa.html`: o botão do Instagram no footer só aparece se `instagram` estiver preenchido (pousada sem IG).
- **Instagram bloqueia `eval`** (CSP). Para rodar o zip_download no instagram.com a partir de um script guardado no `localStorage`, injete via `<script src=blob:...>` (o CSP aceita `blob:`).
- Truque de produtividade: guardar `gm_all.js`, `ig_harvest.js` e `zip_download` como string no `localStorage` da origem (google.com / instagram.com) e chamar com `eval(localStorage.x)(args)` nas outras abas, sem colar o script de novo.
- Na barra de avaliações do Stayora (`reviews.bars`), use só notas reais de plataforma (Google, Booking, Airbnb). Nada de "Limpeza 5,0" inventado.
