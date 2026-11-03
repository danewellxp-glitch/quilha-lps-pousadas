"""Pousada Praia Campeche (R. Lomba do Sabão, 175, Campeche, Florianópolis) — site no template 'casa' (home + reservas).
Fotos: Google Maps 2ª passada (gm2; idx 0-2, 19, 56 e 67 são de outros lugares). Pousada da família de Dona Icléia e Seu Paulo
(citados em avaliação). Apartamentos com quarto, sala com sofá-cama, banheiro e cozinha; café da manhã; ~100 m da praia."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Praia+Campeche+R.+Lomba+do+Sab%C3%A3o+175'
F = Fotos('praiacampeche')

T = dict(paper='#f9f8f4', cream='#e9eef0', espresso='#1f2a30', honey='#d0753f', olive='#2a7590',
         muted='#5f6a70', rooms_bg='#eef2f3', deep='#183440', gold='#f0b27f')

P = dict(
    slug='praiacampeche', name='Pousada Praia Campeche', short='Praia Campeche',
    seo_title='Pousada Praia Campeche | Apartamentos a 100 m da praia, Florianópolis',
    logo_small='Pousada', logo_main='Praia Campeche', logo_img='',
    meta_desc='Pousada Praia Campeche: apartamentos com cozinha a cerca de 100 metros da Praia do Campeche, com café da manhã, estacionamento amplo e atendimento de família.',
    phone='(48) 3338-2026', wa_number='554833382026', email='',
    wa_text='Olá! Vim pelo site da Pousada Praia Campeche e queria consultar disponibilidade.',
    instagram='',
    address='R. Lomba do Sabão, 175 · Campeche, Florianópolis/SC · CEP 88063-198',
    place_line='Campeche · Florianópolis · SC',
    footer_tag='Apartamentos com cozinha, café da manhã e a Praia do Campeche a um minuto.', checkin='14h', checkout='12h',
    rooms_label='Apartamentos', lang_gate=False,
)


def context(I, wa):
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(34, True), video='', eyebrow='Campeche · Florianópolis',
                     title='A Praia do Campeche<br>a um minuto',
                     sub='Apartamentos com cozinha, café da manhã caprichado e a passarela da praia logo ao lado.')
    p['intro'] = dict(kicker='A pousada', title='Uma pousada de família na entrada da praia',
                      text='A Pousada Praia Campeche fica na Rua Lomba do Sabão, ao lado de uma das entradas da Praia do Campeche. O prédio é claro e arejado, com apartamentos que têm quarto, sala com sofá-cama, banheiro e cozinha equipada. Tem café da manhã servido todo dia, estacionamento amplo e quem recebe é a própria família, com aquele clima de casa de praia.',
                      badge='A ~100 m da areia')
    car = [6, 34, 13, 26, 10, 22, 45, 29, 58, 76]
    p['carousel'] = [dict(src=G(i), alt='Pousada Praia Campeche') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo pra curtir o Campeche sem pressa',
                           text='Seja um feriado em família, um carnaval na praia ou uma semana de descanso, a pousada tem o que você precisa.')
    cards = [
        (6, 'Prédio claro e arejado', 'Apartamentos com sacada, janelas grandes e muita luz natural.', 'Conhecer', '#pousada'),
        (58, 'Cozinha equipada', 'Fogão, geladeira, panelas e bancada de granito em cada apartamento.', 'Ver apartamentos', 'reservas.html'),
        (13, 'Café da manhã', 'Pães, bolos, frutas e frios servidos todas as manhãs.', 'Conhecer', '#pousada'),
        (22, 'Passarela pra praia', 'A trilha de madeira até a areia começa logo ao lado da pousada.', 'Como chegar', '#contato'),
        (26, 'Sala com sofá-cama', 'Espaço extra pra família, com TV e porta pro corredor.', 'Ver apartamentos', 'reservas.html'),
        (9, 'Estacionamento amplo', 'Vaga pro carro dentro do terreno, sem dor de cabeça.', 'Reservar', 'reservas.html'),
        (20, 'Vista do mar', 'Do deck dá pra ver o mar e a Ilha do Campeche no horizonte.', 'Conhecer', '#pousada'),
        (76, 'Ilha do Campeche', 'O paraíso de água cristalina, com passeios de barco saindo da praia.', 'Explorar', '#experiencias'),
    ]
    p['cards'] = [dict(img=G(i), title=t, text=x, action=a, href=h) for i, t, x, a, h in cards]
    p['band'] = dict(img=G(31, True), nav='O Campeche', kicker='Pousada Praia Campeche',
                     title='Uma das praias mais<br>bonitas da Ilha.',
                     text='Mar azul, areia branca, ondas pra surfar e a Ilha do Campeche bem na frente. Na volta, o apartamento te espera com tudo pronto.',
                     cta='Explorar a região')
    p['exp'] = dict(img=G(16), alt='Praia do Campeche com a ilha ao fundo', badge='Campeche',
                    kicker='Na vizinhança', title='O Sul da Ilha pra explorar',
                    text='Do Campeche dá pra chegar rápido às praias e trilhas mais bonitas do Sul da Ilha, e o bairro tem mercado, restaurantes e tudo o que você precisa.',
                    items=['Praia do Campeche a cerca de 100 m', 'Passeio de barco até a Ilha do Campeche',
                           'Morro das Pedras, Armação e Lagoinha do Leste por perto', 'Cerca de 15 min do aeroporto'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Magali B.', 'A pousada está muito bem localizada, bem pertinho da praia, além de ser muito confortável, com ar-condicionado, bom espaço, banheiro com bom equipamento e cozinha própria.'),
        ('Aninha S.', 'Sul da ilha, melhor lugar, e a pousada da Dona Icléia, melhor hospedagem. Localização, conforto e limpeza. Café da manhã ótimo, colchão ótimo, deck com vista pro mar lindo.'),
        ('Douglas B.', 'Gosto muito de passar o carnaval na pousada. Oferece um excelente café da manhã, raridade nas pousadas de Santa Catarina, e também tem limpeza diária do apartamento.'),
        ('Edilson S.', 'Atendimento acolhedor. Limpeza e higiene ótimas. Aptos com quarto, sala, banheiro e cozinha completa. Local tranquilo, sem barulho, a meia quadra da praia.'),
        ('Nivaldo C.', 'Lugar acolhedor, bem localizado e com um café da manhã excelente. Os donos são fantásticos, tratamento VIP.'),
        ('Guilherme D.', 'Ótima pousada, muito bem localizada, bem próxima à Praia do Campeche. Possui amplo estacionamento e local muito aconchegante.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,5 no Google · 163 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 163 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=G(77, True), title='Bora pro Campeche?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=G(53, True), kicker='Reserve sua estadia', title='Dias de praia no Campeche.<br>Com tudo pertinho.',
        rooms_kicker='Nossos apartamentos', unit_word='Apartamento', prices=False,
        included=['Café da manhã', 'Cozinha equipada', 'Ar-condicionado', 'Banheiro privativo', 'Wi-Fi', 'Estacionamento'],
        rooms=[
            dict(name='Apartamento Casal', guests=2, price='',
                 detail='Quarto de casal, sala com TV, banheiro e cozinha equipada. Perfeito pra um casal curtir a praia.',
                 imgs=[G(10), G(64), G(26), G(58), G(21)]),
            dict(name='Apartamento Família', guests=4, price='',
                 detail='Quarto com duas camas, sala com sofá-cama e cozinha completa. Espaço pra família toda.',
                 imgs=[G(4), G(45), G(24), G(82), G(93)]),
            dict(name='Apartamento Superior', guests=4, price='',
                 detail='No andar de cima, com mais luz e ventilação, sacada e o mesmo conforto de casa com cozinha.',
                 imgs=[G(57), G(102), G(20), G(73), G(6)]),
        ])
    return p
