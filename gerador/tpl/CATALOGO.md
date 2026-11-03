# Catálogo de templates do gerador

Fonte única de verdade sobre os templates disponíveis. A skill lê este arquivo para escolher o template, e todo template novo entra aqui com uma linha na tabela e uma seção própria.

| id | Tipo | Páginas | Quando usar | Módulo de exemplo |
|---|---|---|---|---|
| `doma` | LP de 1 página | index | Muitas fotos boas, pousada charmosa e menor. Galeria masonry com lightbox. | `data/dormida.py`, `data/refugio.py` |
| `aurelia` | LP de 1 página | index | Suítes bem definidas, pousada com piscina/estrutura. Barra de reserva no hero, FAQ. | `data/aloha.py`, `data/marujo.py` |
| `casa` | Site institucional | index + reservas | Pousada **sem site próprio** ou proposta de site completo. Fluxo de reserva em 2 páginas. | `data/moradas_site.py`, `data/vila_porto_site.py` |
| `stayora` | LP premium de 1 página | index | Pousada com cara de boutique ou de villa, fotos bonitas de fim de tarde, anfitrião marcante. Calendário de reserva no hero. | `data/dormida_stayora.py` |

---

## doma
- **Origem:** clone do Villa Doma (Framer/Grok).
- **Seções:** hero com moldura e parallax, intro, sobre + 3 diferenciais, comodidades, galeria masonry + lightbox, experiências (cards com descrição no hover), faixa com parallax, localização (mapa no site), avaliações em abas, CTA.
- **T:** `bg, text, muted_text, accent, accent_ink, sage, label, band, line, card`

## aurelia
- **Origem:** clone do Aurelia (Framer/Grok).
- **Seções:** hero em tela cheia + barra de reserva (WhatsApp), slideshow oval, cards de suíte, cards empilhados (sticky), galeria que desentorta ao rolar, avaliações em slider com abas, FAQ.
- **T:** `gold, gold2, dark, darker, cream, cream2, sage, text, muted, line`
- **Extra:** usa `deco.py` (palmeiras em line-art) e `logo()`.

## casa
- **Origem:** clone limpo do site da Aloha Beach House (`tpl/_fonte-casa-aloha/`).
- **Páginas:** `casa.html` gera `index.html`, e `casa_reservas.html` gera `reservas.html` (registrado em `PAGES` no build.py).
- **Seções:** hero (vídeo ou foto com Ken Burns) + barra de reserva, intro com carrossel emoldurado, 8 "cantos", faixa com fundo fixo, experiência, avaliações em abas, vídeo opcional, CTA, footer. Reservas: datas, cards com carrossel, checkout que vai pro WhatsApp, telefone ou e-mail.
- **T:** `paper, cream, espresso, honey, olive, muted, rooms_bg, deep, gold`
- **Atenção:** preço só com tabela do dono (`price=''` mostra "Sob consulta"). `lang_gate` vem desligado, porque não traduz nada.

## stayora
- **Origem:** template Framer "Stayora" (stayora.framer.website, de levindbr), reescrito do zero sem o runtime do Framer. Fonte do export em `tpl/_fonte-stayora/`.
- **Seções:** hero com moldura (cantos arredondados), prova social (avatares + nota) e **calendário de reserva em vidro escuro** (seleção de período + hóspedes, que vai pro WhatsApp); sobre (2 fotos + card com contador); comodidades em pílulas (8 visíveis, "ver todas"); espaços em carrossel centralizado com contador 01/05 e barra; anfitrião (foto + card + citação); apartamentos em **seção escura com abas** e grade estilo planta (3ª célula com foto); experiências em bento; avaliações com números, barras por plataforma e **marquee** infinito; FAQ rolável; CTA com reserva sobre foto; footer escuro.
- **Efeitos:** Lenis, reveal, títulos que **acendem palavra por palavra** conforme a rolagem (`.lit`), topbar fixa que aparece depois do hero, contadores animados.
- **Fonte:** Manrope (Google Fonts).
- **T:** `bg, alt, ink, ink2, muted, dim, dark, card, accent, line` (paleta original neutra: `#f7f7f7 / #ebecef / #0b0c0e`).
- **Campos:** veja `data/dormida_stayora.py` (nav, hero.avatars/proof, about.stat_*, amenities [ícone, texto], spaces, host, plan.rooms[cells×5], exp.big/wide/list/small, reviews.bars/items[color], faq, cta).
- **Atenção:** a citação do anfitrião (`host.quote`) deve ser **real**, de preferência um trecho de avaliação atribuído no `host.text`. Nunca inventar fala do dono. `plan` e `host` são opcionais (`None`).
- **Licença:** é um template de marketplace com licença "Single-Use" no Framer. Usamos só como referência visual e o código é nosso, mas vale conferir os termos antes de usar em vários clientes.

---

## Como adicionar um template novo
1. Guarde a fonte original em `tpl/_fonte-<id>/` (HTML exportado, prints, link da prévia).
2. Estude o original rodando de verdade (prévia ao vivo no Chrome): seções, efeitos, interações, mobile.
3. Escreva `tpl/<id>.html` em Jinja: sem runtime do Framer ou React, CSS/JS inline, tokens de cor via `T`, conteúdo via `p.*`. Bibliotecas só de CDN permitida (jsdelivr/cdnjs/unpkg) e fontes do Google Fonts.
   - O primeiro bloco precisa ser `<title>`/`<meta>`/`<link>` + `<style>...</style>`. O build separa no primeiro `</style>` para montar o `<head>`.
   - Nada de `alert()` nem `window.open`: abra links com `<a target=_blank>` criado via JS (funciona no artifact).
   - Respeite `prefers-reduced-motion`, testes em 1440 e 390 px, e o rodapé "Prévia desenvolvida por Quilha Digital".
   - Se tiver mais de uma página, registre em `PAGES` no `build.py`.
4. Crie um módulo de demo `data/<pousada>_<id>.py` com uma pousada real que já tenha fotos.
5. Rode `python build.py <slug>`, tire screenshots (desktop/mobile), teste as interações e publique como artifact.
6. Adicione a linha na tabela acima e a seção do template.
