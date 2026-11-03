"""Pousada Moradas do Moçambique — site institucional no template 'casa' (home + reservas)."""
import os
from common import review_sources
from data.moradas import MAPS, ig, gm, context as _doma_context  # reuse photo index + reviews

TEMPLATE = 'casa'

T = dict(paper='#fbf8f1', cream='#ebe4d2', espresso='#22301f', honey='#b5762a', olive='#4e5a3a',
         muted='#5e6658', rooms_bg='#f3efe4', deep='#17211a', gold='#dcbc85')

P = dict(
    slug='moradas_site', name='Pousada Moradas do Moçambique', short='Moradas',
    seo_title='Pousada Moradas do Moçambique | Rio Vermelho, Florianópolis',
    logo_small='Pousada', logo_main='Moradas', logo_img='',
    meta_desc='Pousada Moradas do Moçambique no Rio Vermelho, Florianópolis: flats com cozinha, chalé de madeira, jardim com redes e a Praia do Moçambique pertinho. Nota 4,7 no Google.',
    phone='(48) 98495-1131', wa_number='5548984951131', email='',
    wa_text='Olá! Vim pelo site da Pousada Moradas do Moçambique e queria consultar disponibilidade.',
    instagram='pousadamoradasdomocambique',
    address='Servidão Altino Manoel Claudino, 634 · São João do Rio Vermelho, Florianópolis/SC',
    place_line='Rio Vermelho · Florianópolis · SC',
    footer_tag='Natureza, sossego e a Praia do Moçambique logo ali.',
    rooms_label='Acomodações', lang_gate=False,
)


def context(I, wa):
    g = lambda i: I(ig(i))[0]
    G = lambda i: I(gm(i))[0]
    base = _doma_context(lambda *a, **k: ('', 0, 0), wa)  # only to reuse the reviews block
    p = dict(P)
    p['hero'] = dict(img=G(39), video='', eyebrow='Rio Vermelho · Norte da Ilha',
                     title='Entre o parque<br>e o mar',
                     sub='Flats com cozinha e um chalé de madeira, a poucos minutos da Praia do Moçambique.')
    p['intro'] = dict(kicker='A pousada', title='Um lugar pra descansar de verdade',
                      text='Numa rua tranquila do São João do Rio Vermelho, a Moradas reúne flats completos, um chalé de madeira e um jardim amplo com redes. Quem recebe é o Anderson, com dicas de trilhas, praias e restaurantes do norte da Ilha.',
                      badge='Jeito Moradas de receber')
    car = [('G', 9), ('g', 22), ('G', 29), ('g', 44), ('G', 7), ('g', 26), ('G', 54), ('g', 13), ('G', 36), ('g', 45)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Moradas do Moçambique') for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo pensado para a sua estadia',
                           text='Do flat com cozinha ao chalé com rede, cada espaço foi feito pra você se sentir em casa perto da praia.')
    cards = [
        ('g', 26, 'Flats com cozinha', 'Cozinha equipada, geladeira, TV, ar-condicionado e banheiro privativo.', 'Ver acomodações', 'reservas.html'),
        ('G', 29, 'Chalé de madeira', 'Cama no mezanino, rede na sala e ducha externa no meio do verde.', 'Ver o chalé', 'reservas.html'),
        ('G', 0, 'Jardim com redes', 'Gramado amplo, varandas com redes e sombra pra ler um livro sem pressa.', 'Conhecer', '#pousada'),
        ('G', 54, 'Quiosque e churrasqueira', 'Espaço coberto com mesa e churrasqueira para os hóspedes.', 'Conhecer', '#pousada'),
        ('g', 40, 'Ducha ao ar livre', 'Volta da praia com ducha de madeira no jardim, do jeitinho de casa de praia.', 'Conhecer', '#pousada'),
        ('g', 38, 'Parque do Rio Vermelho', 'Trilhas na sombra dos pinheirais e da mata, a poucos minutos da pousada.', 'Experiências', '#experiencias'),
        ('g', 16, 'Praia do Moçambique', 'A maior praia da Ilha, com cara de praia selvagem, a cerca de 1,8 km.', 'Como chegar', '#contato'),
        ('G', 21, 'Wi-Fi e estacionamento', 'Wi-Fi gratuito e estacionamento privativo dentro da pousada.', 'Reservar', 'reservas.html'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=G(9), nav='O jardim', kicker='Moradas do Moçambique',
                     title='Redes, verde<br>e silêncio.',
                     text='Aqui o dia começa devagar: café na varanda, rede no jardim e o barulho do mar ao fundo. À noite, churrasco no quiosque e céu estrelado.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(37), alt='Praia do Moçambique', badge='Praia do Moçambique',
                    kicker='Experiências', title='O norte da Ilha começa aqui',
                    text='O Moçambique ainda tem cara de praia selvagem: mar aberto, areia sem fim e ondas boas pro surf. Em volta, o parque, a Barra da Lagoa e a Lagoa da Conceição.',
                    items=['Praia do Moçambique a cerca de 1,8 km', 'Trilhas do Parque Estadual do Rio Vermelho',
                           'Barra da Lagoa e Lagoa da Conceição a poucos minutos', 'Dicas do Anderson para praias, trilhas e restaurantes'],
                    cta='Pedir dicas pelo WhatsApp')
    p['reviews'] = base['reviews']
    p['reviews']['items'] = [r for i, r in enumerate(p['reviews']['items']) if i not in (6, 7)][:6]  # 6 = two full rows
    p['film'] = None
    p['cta'] = dict(img=G(7), title='Pronto pra desacelerar no Rio Vermelho?')
    p['loc'] = dict(maps_url=MAPS)
    # reservas page
    room = lambda *ids: [(G(i) if k == 'G' else g(i)) for k, i in ids]
    p['res'] = dict(
        hero=G(0), kicker='Reserve seu refúgio', title='Alguns dias no Rio Vermelho.<br>Uma pausa de verdade.',
        rooms_kicker='Nossas acomodações', unit_word='Acomodação', prices=False,
        included=['Wi-Fi gratuito', 'Estacionamento privativo', 'Roupa de cama e banho', 'Jardim, redes e churrasqueira'],
        rooms=[
            dict(name='Flat Casal', guests=2, price='', detail='Cama de casal, cozinha equipada, TV, ar-condicionado e varanda com rede.',
                 imgs=room(('g', 22), ('g', 24), ('g', 26), ('g', 28), ('g', 13))),
            dict(name='Flat Família', guests=4, price='', detail='Cama de casal e de solteiro, cozinha completa e espaço para a família.',
                 imgs=room(('g', 9), ('g', 8), ('g', 1), ('g', 7), ('G', 9))),
            dict(name='Chalé de Madeira', guests=2, price='', detail='Cama no mezanino, rede na sala, minicozinha e ducha externa no jardim.',
                 imgs=room(('g', 42), ('g', 44), ('g', 45), ('g', 40), ('G', 29))),
        ])
    return p
