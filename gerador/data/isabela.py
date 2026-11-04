"""Pousada Isabela (R. Ruth Pereira, 318, Ingleses do Rio Vermelho, Florianópolis) — site no template 'casa' (home + reservas).
@aluguel_ingleses (1.089 seg.; o @pousada_isabela é OUTRA pousada, de Urubici) · Google 4,8 (67) · Facebook 100% recomendam (10,
página pousadaisabelanapraiadosingleses) · sem Booking/Airbnb · sem site próprio (Google aponta pro Facebook). Anfitriões: Cláudia e
o marido José Augusto (7 reviews; 1 review diz "Zé Roberto"), moram na propriedade. Aptos de 1 e 2 quartos (FB/Mais Pousadas),
~280 m da praia. Fotos: Google Maps (gm; 2-6, 8, 10, 45, 53, 58, 59 descartadas: anúncio, outros lugares, pessoas, borradas).
Nomes/capacidade dos aptos não publicados: cards por tipo (1 e 2 quartos), fotos ilustrativas, sem capacidade — confirmar com a Cláudia."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Isabela+R.+Ruth+Pereira+318+Ingleses+Florian%C3%B3polis'
FB = 'https://www.facebook.com/pousadaisabelanapraiadosingleses/reviews'
F = Fotos('isabela')

# azul-petróleo do mar + verde do vidro da fachada + amarelo do sol do logo
T = dict(paper='#f7f9f8', cream='#e4efed', espresso='#13313a', honey='#c9861f', olive='#1d6f6c',
         muted='#566a6e', rooms_bg='#e9f1ef', deep='#0d3a44', gold='#f3c552')

# Contraste do texto sobre foto: as fotos são de praia com céu claro, então o sombreamento padrão (marrom, leve)
# fica fraco. Aqui o véu vai pro azul-petróleo, mais denso atrás do texto, com sombra no título.
EXTRA_CSS = """
.hero-img,.hero-video{filter:brightness(.97) saturate(1.05) contrast(1.03)}
.hero-shade{background:radial-gradient(ellipse 58% 42% at 50% 44%,#0a2a3380 0%,#0a2a3340 60%,#0a2a3300 100%),linear-gradient(#081f2780 0%,#081f2700 26%,#081f2700 60%,#081f2799 100%)}
.hero-content{text-shadow:0 2px 6px #04141acc,0 6px 30px #04141a99}
.hero .eyebrow{display:inline-block;background:#0b2f38b3;padding:7px 14px;border-radius:999px;text-shadow:none;letter-spacing:.2em}
.hero .primary{background:#0b2f3880;border-color:#fff}
.nav{background:linear-gradient(#071c23b3,#071c2300)}
.nav a,.nav button{text-shadow:0 1px 8px #04141acc}
.rosa{background:linear-gradient(90deg,color-mix(in srgb,var(--deep) 92%,transparent) 0%,color-mix(in srgb,var(--deep) 78%,transparent) 45%,color-mix(in srgb,var(--deep) 20%,transparent) 100%),url(BAND) 50%/cover fixed}
.rosa h2,.rosa p{text-shadow:0 2px 14px #04141a99}
.final-cta{background:radial-gradient(ellipse 55% 60% at 50% 50%,#0a2e3799,#0a2e3733),url(CTA) 50% 60%/cover}
.final-cta p{text-shadow:0 2px 14px #04141acc}
.rv .stars.rec{color:var(--olive);letter-spacing:.04em;font-size:13px;font-weight:700}
@media (max-width:760px){.hero .eyebrow{letter-spacing:.12em;font-size:11px}.rosa{background:linear-gradient(color-mix(in srgb,var(--deep) 88%,transparent),color-mix(in srgb,var(--deep) 70%,transparent)),url(BAND) 50%/cover}}
"""

EXTRA_CSS_RES = """
.reserve-hero{background:linear-gradient(90deg,#0b2f38f0 0%,#0b2f38c7 50%,#0b2f3833 100%),url(RESHERO) 50%/cover}
.reserve-hero h1,.reserve-hero p{text-shadow:0 2px 14px #04141aaa}
@media (min-width:1001px){.booking-rooms{grid-template-columns:repeat(2,minmax(0,420px));justify-content:center}}
@media (max-width:760px){.reserve-hero{background:linear-gradient(#0b2f38e6,#0b2f38b3),url(RESHERO) 50%/cover}}
"""

P = dict(
    slug='isabela', name='Pousada Isabela', short='Pousada Isabela',
    seo_title='Pousada Isabela | Apartamentos a 280 m da Praia dos Ingleses, Florianópolis',
    logo_small='Pousada', logo_main='Isabela', logo_img='',
    meta_desc='Pousada Isabela: apartamentos de 1 e 2 quartos com cozinha e ar-condicionado a 280 metros da Praia dos Ingleses, no norte de Florianópolis. Ambiente familiar, seguro, com sala de jogos e churrasqueira.',
    phone='(48) 99681-1218', wa_number='5548996811218', email='claudiassilva2011@gmail.com',
    wa_text='Olá, Cláudia! Vim pelo site da Pousada Isabela e queria consultar disponibilidade.',
    instagram='aluguel_ingleses',
    address='R. Ruth Pereira, 318 · Ingleses do Rio Vermelho, Florianópolis/SC · CEP 88058-640',
    place_line='Praia dos Ingleses · Florianópolis · SC',
    footer_tag='Apartamentos completos a 280 m da Praia dos Ingleses, com o cuidado de quem mora ali.',
    checkin='', checkout='',
    rooms_label='Apartamentos', lang_gate=False,
)


def context(I, wa):
    G = lambda i, big=False, crop=None: I(F.gm(i), big=big, crop=crop)[0]
    p = dict(P)
    band, cta, reshero = G(61, True), G(48, True), G(15, True)
    p['extra_css'] = EXTRA_CSS.replace('BAND', band).replace('CTA', cta) + EXTRA_CSS_RES.replace('RESHERO', reshero)
    p['hero'] = dict(img=G(30, True), video='', eyebrow='Praia dos Ingleses · Florianópolis',
                     title='A 280 metros<br>do mar dos Ingleses',
                     sub='Apartamentos completos de 1 e 2 quartos, com cozinha, ar-condicionado e quem recebe é a própria família.')
    p['intro'] = dict(kicker='A pousada', title='Um residencial de família, pertinho da praia',
                      text='A Pousada Isabela fica na Rua Ruth Pereira, no coração dos Ingleses, no norte da Ilha. São apartamentos de 1 e 2 quartos, no térreo ou com sacada, com cozinha equipada e ar-condicionado. A Cláudia e o José Augusto moram no residencial e cuidam de tudo de perto há mais de 16 anos: portão eletrônico, câmeras, sala de jogos e churrasqueira pra família aproveitar.',
                      badge='280 m da areia')
    car = [7, 23, 14, 9, 17, 36, 39, 20, 41, 35, 33]
    NOSTAMP = {46: (0, 0, 1, .93), 7: (0, 0, 1, .9), 0: (0, 0, 1, .9)}  # carimbo de data no canto inferior
    GG = lambda i, big=False: G(int(str(i).lstrip('f')), big, NOSTAMP.get(int(str(i).lstrip('f'))))
    p['carousel'] = [dict(src=GG(i), alt='Pousada Isabela, Praia dos Ingleses') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo pra férias de praia sem preocupação',
                           text='Seja uma semana em família, o Réveillon ou o Carnaval nos Ingleses, o apartamento te espera pronto pra usar.')
    cards = [
        ('f46', 'Residencial seguro', 'Portão eletrônico e câmeras de segurança, num ambiente tranquilo e familiar.', 'Conhecer', '#pousada'),
        (9, 'Quartos com ar', 'Quartos claros e arejados, com ar-condicionado e roupa de cama.', 'Ver apartamentos', 'reservas.html'),
        (17, 'Cozinha completa', 'Fogão, geladeira, micro-ondas e utensílios: dá pra cozinhar como em casa.', 'Ver apartamentos', 'reservas.html'),
        (36, 'Sala de jogos', 'Mesa de sinuca pra animar as noites da criançada e dos adultos.', 'Conhecer', '#pousada'),
        (28, 'Churrasqueira', 'Espaço de churrasco pra reunir a família depois da praia.', 'Reservar', 'reservas.html'),
        (54, 'Chegada com carinho', 'Hóspedes contam do cartão de boas-vindas e dos bombons com o nome de cada um.', 'Ver avaliações', '#avaliacoes'),
        (23, 'Térreo ou sacada', 'Apartamentos no térreo ou no andar de cima, com sacada de vidro.', 'Ver apartamentos', 'reservas.html'),
        (63, 'Praia dos Ingleses', 'Mar calmo, areia larga e o costão ao lado, a poucos minutos a pé.', 'Explorar', '#regiao'),
    ]
    p['cards'] = [dict(img=GG(i), title=t, text=x, action=a, href=h) for i, t, x, a, h in cards]
    p['band'] = dict(img=band, nav='Os Ingleses', kicker='Norte da Ilha',
                     title='Mar calmo, areia larga<br>e o pôr do sol no costão.',
                     text='Os Ingleses é uma das praias mais procuradas por famílias em Floripa. Mercado, farmácia e padaria ficam perto da pousada, então dá pra fazer tudo a pé e esquecer o carro.',
                     cta='Explorar a região')
    p['exp'] = dict(img=G(19), alt='Costão da Praia dos Ingleses', badge='Ingleses',
                    kicker='Na vizinhança', title='O norte da Ilha pra explorar',
                    text='Dos Ingleses dá pra chegar rápido ao Santinho, às dunas e aos costões, e o bairro tem tudo o que a família precisa no dia a dia.',
                    items=['Praia dos Ingleses a cerca de 280 m', 'Mercado, farmácia e padaria por perto',
                           'Praia do Santinho logo ao lado', 'Cerca de 33 km do Centro e 43 km do aeroporto'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Raissa D.', 'Lugar agradável, pertinho da praia, com supermercado, farmácia e padaria perto. Ambiente familiar, limpo e aconchegante. A Cláudia é um amor de pessoa, nos recebeu muito bem.'),
        ('Erondina C.', 'Na chegada, um cartãozinho de boas-vindas e bombons com o nome de todos os hóspedes. Uma dedicação pensada com carinho, local arejado e ainda um espaço pro churrasquinho.'),
        ('Juan P.', 'Fui recebida calorosamente e ganhei até um presente de boas-vindas. Foram prestativos a estadia toda, até num apagão durante uma tempestade. Excelente custo-benefício e localização.'),
        ('Josiane S.', 'Ambiente muito acolhedor, tudo limpo e organizado. Dona Cláudia e o esposo são muito queridos e atenciosos, ambiente familiar do jeito que gostamos.'),
        ('Rodrigo F.', 'O espaço é ótimo, limpo e o atendimento dos anfitriões é excelente. Dá pra ir à praia a pé tranquilamente. A sala de jogos e a churrasqueira são um diferencial.'),
        ('Lily F.', 'Uma pousada excelente, administrada pelos proprietários, que moram no local e estão sempre à disposição dos hóspedes.'),
        ('Ever I.', 'Os proprietários foram incrivelmente simpáticos, o apartamento estava muito limpo e aconchegante. Éramos três famílias em dois apartamentos e foi perfeito.'),
        ('Tiago Z.', 'Adoramos a pousada: super segura, apartamentos completos e ótima localização. Anfitriões super simpáticos. Obrigado, Cláudia!'),
        ('Lau B.', 'Tudo exatamente como nas fotos! Super segura, perto da praia, com máquina de lavar e tudo o que você precisa pra estadia.'),
    ]
    facebook = [
        ('Leandro B.', 'Fomos muito bem recebidos pela Cláudia e pelo José Augusto. O local é muito bem cuidado e organizado, apartamento limpo, bem equipado e aconchegante.'),
        ('Osmar G.', 'Atendimento nota 10, ótimo preço, local agradável e seguro. Já me hospedei lá diversas vezes e recomendo.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    items += [dict(key='facebook', text=t, author=a, source='Facebook', stars=0) for a, t in facebook]
    # intercala um do Facebook no meio pra aba "Todas" não ficar só Google
    items = items[:3] + items[-2:-1] + items[3:6] + items[-1:] + items[6:-2]
    p['reviews'] = dict(headline='4,8 no Google · 67 avaliações  ·  100% recomendam no Facebook', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '4,8 no Google · 67 avaliações'),
                                                ('facebook', 'Facebook', '100%', '100% recomendam no Facebook · 10 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=cta, title='Bora pros Ingleses?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=reshero, kicker='Reserve sua estadia', title='Férias nos Ingleses.<br>Com cara de casa.',
        rooms_kicker='Nossos apartamentos', unit_word='Apartamento', prices=False,
        included=['Cozinha equipada', 'Ar-condicionado', 'Roupa de cama', 'Banheiro privativo', 'Wi-Fi', 'Estacionamento'],
        rooms=[
            dict(name='Apartamento 1 quarto', guests='', price='',
                 detail='Quarto de casal com ar-condicionado, cozinha completa com mesa e banheiro privativo. Ideal pra casal ou dupla de amigos.',
                 imgs=[G(9), G(17), G(21), G(51), G(29)]),
            dict(name='Apartamento 2 quartos', guests='', price='',
                 detail='Dois quartos, cozinha completa e espaço pra família toda curtir a praia. Opções no térreo ou com sacada.',
                 imgs=[G(20), G(18), G(26), G(49), G(35)]),
        ])
    return p
