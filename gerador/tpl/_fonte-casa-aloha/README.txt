Aloha Beach House — clone limpo (sem metadados)
================================================

Conteúdo
---------
index.html      → página inicial (gate de idioma, hero, carrossel, seções, footer, WhatsApp)
reservas.html   → fluxo de reservas (datas, cabanas, preços, formulário → WhatsApp/e-mail/telefone)

Sem React, Vite, HTTrack, Cloudflare challenge ou scripts RSC.
CSS e JS embutidos nos HTMLs.

Como usar
---------
1. Coloque as imagens na mesma pasta dos HTMLs (ou ajuste os caminhos).
2. Abra index.html no navegador ou hospede em qualquer servidor estático.
3. reservas.html funciona isolado e também a partir do link da home.

WhatsApp: +55 48 99180-1910
E-mail:   pousadaalohapraiadorosa@gmail.com

Imagens necessárias (caminhos usados no HTML)
---------------------------------------------
Raiz:
  aloha-logo-ivory.png
  aloha-logo-brown.png   (opcional, reservas)
  favicon.svg
  aloha-hero.mp4         (vídeo do hero / gate de idioma)
  hero.png               (fallback do hero de reservas)
  carousel-1.jpg … carousel-11.jpg
  beach-service.png
  canto-acomodacoes.jpg
  canto-piscina.jpg
  canto-cafe.jpg
  canto-churrasqueira.jpg
  canto-localizacao.jpg
  canto-pet-friendly.jpg
  canto-estacionamento.jpg
  canto-limpeza.jpg

Pastas por cabana (reservas):
  big-island/   big-1.jpg … big-17.jpg
  molokai/      molokai-1.jpg … molokai-hero.jpg
  waimea/       waimea-*.webp
  hawaii/
  kailua/
  kauai/
  kona/
  niihau/
  oahu/
  lanai/
  maui/

Se alguma imagem faltar, o layout continua funcionando.

Observações
-----------
- Preços em reservas.html são os "a partir de" do mês de referência do site original.
  Valores finais e disponibilidade são confirmados pela equipe via WhatsApp/telefone/e-mail.
- Gate de idioma usa sessionStorage (não reaparece na mesma sessão).
- Nenhuma referência a alohapraiadorosa.com.br, Framer, Vinext ou HTTrack no código.
