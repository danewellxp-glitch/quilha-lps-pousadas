"""Pousada Amar (Ibiraquera, Praia do Rosa) — site institucional no template 'casa' (home + reservas)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Amar+Praia+do+Rosa+Ibiraquera'
F = Fotos('amar')

T = dict(paper='#fbf7ee', cream='#f3e6c4', espresso='#2b2a24', honey='#d08f17', olive='#2f7f74',
         muted='#6a6355', rooms_bg='#f4ead2', deep='#1d3a36', gold='#f2c14e')

P = dict(
    slug='amar', name='Pousada Amar', short='Amar',
    seo_title='Pousada Amar | Cabanas de madeira na Praia do Rosa',
    logo_small='Pousada', logo_main='Amar', logo_img='',
    meta_desc='Pousada Amar, em Ibiraquera, na Praia do Rosa: cabanas de madeira feitas à mão, piscina com cascata, fogueira, cesta de café da manhã e pet friendly. Nota 5,0 no Google.',
    phone='(48) 99131-0990', wa_number='5548991310990', email='',
    wa_text='Olá! Vim pelo site da Pousada Amar e queria consultar disponibilidade.',
    instagram='pousadaamar',
    address='Ibiraquera · Praia do Rosa, Imbituba/SC · CEP 88780-000',
    place_line='Ibiraquera · Praia do Rosa · SC',
    footer_tag='Amor e aconchego dentro da natureza.', checkin='14h', checkout='12h',
    rooms_label='Cabanas', lang_gate=False,
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(21, True), video='', eyebrow='Ibiraquera · Praia do Rosa',
                     title='Amor e aconchego<br>dentro da natureza',
                     sub='Cabanas de madeira feitas à mão, piscina com cascata e fogueira sob as estrelas.')
    p['intro'] = dict(kicker='A pousada', title='Pequena, caprichada e feita com amor',
                      text='A Amar é uma pousada de poucas cabanas, em Ibiraquera, na região da Praia do Rosa. Cada cabana tem ar-condicionado, TV, sofá-cama e cozinha equipada, com varanda e rede. Em volta, piscina com cascata, fogueira, espaço gourmet com churrasqueira e um jardim cheio de vida. Quem recebe são a Lu e o Flávio, junto com o Thor e a Cacau, os pets da casa.',
                      badge='Pet friendly')
    car = [('g', 44), ('g', 2), ('g', 7), ('g', 41), ('G', 10), ('g', 37), ('g', 57), ('g', 56), ('g', 55), ('g', 23)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Amar') for k, i in car]
    p['cards_head'] = dict(kicker='Cada detalhe', title='Do café na cesta à fogueira',
                           text='Os anfitriões capricham em tudo: da decoração da cabana às dicas de praias e trilhas.')
    cards = [
        ('g', 17, 'Cabanas feitas à mão', 'Cabanas de madeira com varanda e rede, ar-condicionado, TV e cozinha equipada.', 'Ver cabanas', 'reservas.html'),
        ('G', 13, 'Piscina com cascata', 'Piscina com deck de madeira e cascata, rodeada de verde.', 'Conhecer', '#pousada'),
        ('g', 6, 'Fogueira', 'A fogueira acende à noite, com cadeiras em volta e o céu estrelado.', 'Conhecer', '#pousada'),
        ('g', 37, 'Espaço gourmet', 'Cozinha compartilhada colorida, com churrasqueira e mesa pra turma toda.', 'Conhecer', '#pousada'),
        ('G', 11, 'Cesta de café da manhã', 'Café fresquinho servido numa cesta, pra tomar no jardim ou na varanda.', 'Consultar', '#contato'),
        ('g', 33, 'Pet friendly', 'Seu pet é bem-vindo. O Thor e a Cacau adoram receber visita.', 'Consultar', '#contato'),
        ('g', 34, 'Datas especiais', 'Aniversário ou lua de mel? A cabana pode ser decorada pra surpreender.', 'Consultar', '#contato'),
        ('g', 27, 'Transfer pras praias', 'Transfer pras praias e pro centrinho do Rosa, além de dicas de trilhas.', 'Consultar', '#contato'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=g(29, True), nav='A região', kicker='Pousada Amar',
                     title='Entre a lagoa<br>e o mar do Rosa.',
                     text='Ibiraquera fica entre a lagoa, as dunas e as praias do Rosa, da Luz e da Barra. Perto da pousada tem mercado, padaria e academia.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(13), alt='Cauda de baleia-franca no mar da região', badge='Temporada de baleias',
                    kicker='Experiências', title='Praias, dunas e baleias',
                    text='A região da Praia do Rosa tem trilhas, dunas, lagoas e praias de surf. No inverno, as baleias-francas visitam a costa de Imbituba.',
                    items=['Praia do Rosa e centrinho', 'Lagoa de Ibiraquera e Barra', 'Dunas e trilhas no costão',
                           'Observação de baleias-francas (temporada de inverno)'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Franciele R.', 'Uma experiência incrível, começando pela recepção da Lu e do Flávio. Fomos recebidos com champanhe, frutas e decoração romântica na nossa cabana. O café da manhã é servido em uma cesta, tudo fresquinho e delicioso.'),
        ('Vinicius C.', 'A pousada é um lugar muito agradável, bem equipado, bem conservado, com piscina, local calmo e seguro. Os proprietários capricham muito. Neste ano já fui três vezes e vou continuar indo.'),
        ('Willian A.', 'Lugar incrível! Paz indescritível! Cabanas super bem equipadas, piscina ótima, churrasqueira boa pra fazer o clássico churras gaúcho, anfitriões mega atenciosos.'),
        ('Carolina G.', 'Pousada aconchegante, limpa, organizada, confortável e com utensílios pensados nos mínimos detalhes. Café da manhã ótimo e serviço de transfer ágil e seguro para as praias locais e centrinho.'),
        ('Tuani S.', 'A estadia foi excelente do início ao fim. A cabana é muito aconchegante, limpa, bem decorada e equipada com tudo que necessitamos. O café da manhã é excepcional.'),
        ('Bianca G.', 'É simples, aconchegante e organizada! Tem todos os recursos para se ter conforto: split, wi-fi gratuito, piscina, cozinha equipada, espaço coletivo para socializar.'),
        ('Luciana M.', 'Lugar lindo, com uma vibe muito alto astral, aconchegante, extremamente limpo e cheio de detalhes. E o café da manhã maravilhoso.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='5,0 no Google · 42 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '5,0', '5,0 no Google · 42 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=g(2, True), title='Vem viver a Amar?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=g(44, True), kicker='Reserve sua cabana', title='Alguns dias no Rosa.<br>Com amor e aconchego.',
        rooms_kicker='Nossas cabanas', unit_word='Cabana', prices=False,
        included=['Ar-condicionado e TV', 'Cozinha equipada', 'Wi-Fi gratuito', 'Piscina com cascata', 'Varanda com rede', 'Pet friendly'],
        rooms=[
            dict(name='Cabana Casal', guests=2, price='',
                 detail='Cabana de madeira com cama de casal, ar-condicionado, TV e cozinha equipada, com varanda e rede.',
                 imgs=[g(56), G(4), G(8), g(7), g(34)]),
            dict(name='Cabana com Sofá-cama', guests=4, price='',
                 detail='Cama de casal e sofá-cama, cozinha completa e varanda com rede, pra família ou amigos.',
                 imgs=[g(54), g(23), g(17), g(44), g(41)]),
        ])
    return p
