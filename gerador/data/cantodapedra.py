"""Pousada Morada Canto da Pedra (Praia do Rosa, Imbituba) — LP no template 'aurelia'.
Obs.: o site do Instagram (moradacantodapedra.com.br) está fora do ar (DNS não resolve)."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('cantodapedra')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Morada+Canto+da+Pedra+Praia+do+Rosa'

T = dict(gold='#d0743a', gold2='#efa86f', dark='#23301f', darker='#161f13', cream='#f8f3ea', cream2='#eee2cc',
         sage='#5e7f4a', text='#1f241c', muted='#5d6157', line='#d8c3a1')

P = dict(
    slug='cantodapedra', name='Pousada Morada Canto da Pedra', brand='Canto da Pedra', place_short='Praia do Rosa, SC',
    meta_desc='Pousada Morada Canto da Pedra, no centrinho da Praia do Rosa: apartamentos com cozinha, varanda com rede, churrasqueira, estacionamento interno e pet friendly, com trilha até a praia. Nota 4,8 no Google.',
    phone='(48) 99925-0960', wa_number='5548999250960', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Morada Canto da Pedra e queria consultar disponibilidade.',
    instagram='moradacantoda',
    address='R. da Pousada Mirante, 2 - Ibiraquera, Imbituba - SC, 88780-000',
    footer_tag='O lugar certo no paraíso do Rosa. Aconchego, segurança e tranquilidade.',
    room_word='Apartamento', rooms_label='Apartamentos', rooms_eyebrow='Apartamentos da Canto da Pedra', rooms_title='Nossas acomodações',
    rooms_sub='Apartamentos com cozinha equipada e varanda com rede, pra ficar no Rosa com cara de casa.',
    tagline='Pertinho do centrinho, com trilha até a praia e rede na varanda.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar ao Rosa.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(27, True), alt='Praia do Rosa vista do alto do costão', eyebrow='Bem-vindo à Canto da Pedra',
                     title='O lugar certo no paraíso do Rosa',
                     sub='Apartamentos com cozinha e varanda com rede, pertinho do centrinho e a uma trilha da Praia do Rosa.',
                     cta='Conhecer os apartamentos')
    p['about'] = dict(eyebrow='Morada Canto da Pedra · Praia do Rosa', title='Aconchego, segurança e tranquilidade',
                      text='A Canto da Pedra é uma pousada clássica do Rosa, num prédio colorido cercado de flores. Os apartamentos têm cozinha equipada e varanda com rede, tem churrasqueira e estacionamento dentro da pousada, e os pets são bem-vindos. Quem recebe é a Lu, que dá as melhores dicas de trilhas e passeios, e muitos hóspedes voltam todo ano.',
                      sign='Lu', role='Anfitriã',
                      imgs=[dict(src=s, alt='Pousada Morada Canto da Pedra') for s in (g(9), G(43), G(16), G(26))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Morada Canto da Pedra.')
    p['rooms'] = [
        dict(name='Apartamento Casal', img=G(9), badge='Com cozinha',
             text='Quarto de casal com janela pro verde, cozinha equipada e varanda com rede.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='kitchen', text='Cozinha'), dict(icon='leaf', text='Varanda com rede')],
             wa=rw('Apartamento Casal')),
        dict(name='Apartamento com Sala', img=G(12), badge='Mais espaço',
             text='Sala com sofá, cozinha com mesa de jantar e quarto separado, pra quem vem em família.',
             meta=[dict(icon='area', text='Sala e quarto'), dict(icon='kitchen', text='Cozinha equipada'), dict(icon='users', text='Família')],
             wa=rw('Apartamento com Sala')),
        dict(name='Apartamento com Churrasqueira', img=G(15), badge='Churrasqueira',
             text='Apartamento com churrasqueira na sacada, pra fazer o churrasco olhando pro verde.',
             meta=[dict(icon='food', text='Churrasqueira'), dict(icon='kitchen', text='Cozinha'), dict(icon='paw', text='Aceita pets')],
             wa=rw('Apartamento com Churrasqueira')),
    ]
    p['exp'] = dict(eyebrow='A experiência Canto da Pedra', title='Viver o Rosa a pé',
                    sub='Da varanda com rede ao pôr do sol no costão, tudo fica pertinho.',
                    cards=[dict(icon='hike', title='Trilha até a praia', kicker='Natureza', text='Uma trilha tranquila e ecológica leva até a Praia do Rosa, entre o verde e o mar.'),
                           dict(icon='pin', title='Pertinho do centrinho', kicker='Localização', text='Mercado, bares e restaurantes do centrinho do Rosa ficam a uma caminhada.'),
                           dict(icon='paw', title='Pet friendly', kicker='Seu pet junto', text='A Canto da Pedra aceita pets, e o estacionamento fica dentro da pousada.'),
                           dict(icon='food', title='Churrasqueira', kicker='Fim de tarde', text='Churrasqueira pra reunir a família depois da praia.')])
    gal = [('G', 5), ('G', 44), ('G', 14), ('G', 25), ('G', 32), ('G', 21), ('G', 15), ('G', 40), ('G', 10), ('G', 22), ('G', 35), ('G', 4)]
    p['gallery'] = dict(title='Um olhar sobre a Canto da Pedra', sub='Varandas com rede, jardim florido e as paisagens do Rosa.',
                        imgs=[dict(src=G(i), alt='Pousada Morada Canto da Pedra') for k, i in gal])
    google = [
        ('Dani', 'Pousada super bem equipada, pertinho do centrinho e perto da praia. Tem churrasqueira e o estacionamento é dentro da área da pousada. Lugar acolhedor, aceita pets e a Lu é super simpática. Quando viemos ao Rosa sempre ficamos aqui.'),
        ('Carolina O.', 'A melhor do Rosa. Super bem localizada, preços justos, limpa e organizada. Sem contar que a proprietária, a Lu, é um amor, super atenciosa.'),
        ('Luiz V.', 'Muito massa. Ótima localização. Próxima de supermercado, bares etc. Trilha tranquila e ecológica para chegar na linda Praia do Rosa. Wi-Fi pega sem problemas!'),
        ('Ismael C.', 'Lugar tranquilo, ambiente familiar. A dona, Sra. Luciana, é uma pessoa muito legal e dá ótimas dicas de passeios.'),
        ('Leandro C.', 'A dona, assim como sua pousada, são uns amores. Sou cliente fiel, já fui algumas vezes e com certeza voltarei.'),
        ('Mariana R.', 'A estadia foi maravilhosa! A Lu foi muito atenciosa. Apartamento muito bem localizado. Voltarei!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=G(39), headline='4,8 no Google · 51 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='A praia fica longe?', a='A Praia do Rosa fica a uma trilha tranquila de distância, e o centrinho dá pra fazer a pé.'),
        dict(q='Os apartamentos têm cozinha?', a='Sim, todos os apartamentos têm cozinha equipada.'),
        dict(q='A pousada aceita pets?', a='Sim, os pets são bem-vindos. Conte pra gente o porte do seu pet quando for reservar.'),
        dict(q='Tem estacionamento?', a='Sim, o estacionamento fica dentro da pousada.'),
        dict(q='Qual o horário de check-in e check-out?', a='Combine o horário de chegada e saída com a Lu pelo WhatsApp.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('anchor', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
