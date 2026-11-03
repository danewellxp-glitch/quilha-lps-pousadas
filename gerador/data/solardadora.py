"""Pousada Solar da Dora (Praia da Daniela, Florianópolis) — LP no template 'aurelia'."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('solardadora')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Solar+da+Dora+Daniela+Florian%C3%B3polis'

T = dict(gold='#b9784a', gold2='#e2ad80', dark='#1f3b3a', darker='#142826', cream='#f8f3ea', cream2='#efe4d2',
         sage='#4f8a83', text='#1c2423', muted='#5b6463', line='#dbc7aa')

P = dict(
    slug='solardadora', name='Pousada Solar da Dora', brand='Solar da Dora', place_short='Daniela, Florianópolis',
    meta_desc='Pousada Solar da Dora, na Praia da Daniela, em Florianópolis: apartamentos completos, piscina, área gourmet com churrasqueira e decoração praiana, a duas ruas do mar. Nota 4,8 no Google.',
    phone='(48) 99983-1364', wa_number='5548999831364', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Solar da Dora e queria consultar disponibilidade.',
    instagram='pousadasolardadora',
    address='Av. das Pitangueiras, 1186 - Daniela, Florianópolis - SC, 88053-050',
    footer_tag='Apartamentos completos, piscina e a Praia da Daniela a duas ruas.',
    room_word='Apartamento', rooms_label='Apartamentos', rooms_eyebrow='Apartamentos do Solar', rooms_title='Nossas acomodações',
    rooms_sub='Mini apartamentos completos, com cozinha equipada, ar-condicionado, TV e roupa de cama e banho.',
    tagline='A praia mais calma do norte da Ilha, com a casa da Dona Dora como base.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar à Daniela.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(2, True), alt='Mar calmo da Daniela emoldurado pelas árvores do manguezal', eyebrow='Bem-vindo ao Solar da Dora',
                     title='Seu lar de verão na Praia da Daniela',
                     sub='Apartamentos completos, piscina e decoração praiana, a duas ruas do mar mais calmo do norte da Ilha.',
                     cta='Conhecer os apartamentos')
    p['about'] = dict(eyebrow='Solar da Dora · Daniela', title='Recebidos como se fosse em casa',
                      text='O Solar da Dora é uma pousada familiar, feita com capricho em cada detalhe: piscina com nichos de pedra, área gourmet com churrasqueira, cantinhos de leitura e decoração praiana. Quem recebe são a Dona Dora e o Seu Gilberto Palhares, e muitos hóspedes voltam todos os anos pra Daniela só pra estar com eles.',
                      sign='Dora & Gilberto', role='Anfitriões',
                      imgs=[dict(src=s, alt='Pousada Solar da Dora') for s in (g(6), G(0), g(35), g(37))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada Solar da Dora.')
    p['rooms'] = [
        dict(name='Apartamento Casal', img=G(2), badge='Até 2 hóspedes',
             text='Quarto com cama de casal, enxoval caprichado, ar-condicionado e cozinha equipada no apartamento.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Ar-condicionado'), dict(icon='kitchen', text='Cozinha')],
             wa=rw('Apartamento Casal')),
        dict(name='Apartamento com Sala', img=G(17), badge='Mais espaço',
             text='Sala com TV e mesa de jantar integrada à cozinha, pra quem vem pra temporada.',
             meta=[dict(icon='area', text='Sala integrada'), dict(icon='tv', text='TV'), dict(icon='kitchen', text='Cozinha equipada')],
             wa=rw('Apartamento com Sala')),
        dict(name='Apartamento Família', img=G(7), badge='Família',
             text='Espaço pra família, com quarto, sala e cozinha completa. Conte quantas pessoas vêm e a gente indica o melhor.',
             meta=[dict(icon='users', text='Família'), dict(icon='bath', text='Banheiro privativo'), dict(icon='wifi', text='Wi-Fi')],
             wa=rw('Apartamento Família')),
    ]
    p['exp'] = dict(eyebrow='A experiência Solar da Dora', title='Os dias na Daniela',
                    sub='Praia calma pela manhã, piscina à tarde e churrasco no fim do dia.',
                    cards=[dict(icon='wave', title='Mar calmo e raso', kicker='Praia da Daniela', text='A Daniela é uma das praias mais tranquilas da Ilha, ideal pra criança e pra quem gosta de nadar sem onda.'),
                           dict(icon='pool', title='Piscina com nichos', kicker='Na pousada', text='Piscina cercada de deck de madeira e nichos de pedra com plantas, pra relaxar depois da praia.'),
                           dict(icon='food', title='Área gourmet', kicker='Churrasco', text='Cozinha gourmet com churrasqueira e mesa grande, pra reunir a família e os amigos.'),
                           dict(icon='leaf', title='Manguezal e pôr do sol', kicker='Natureza', text='Na ponta da Daniela, o manguezal encontra a baía e o pôr do sol pinta o mar de laranja.')])
    gal = [('g', 7), ('g', 5), ('G', 2), ('g', 3), ('G', 15), ('g', 29), ('g', 33), ('G', 13), ('g', 34), ('g', 4), ('g', 24), ('G', 5)]
    p['gallery'] = dict(title='Um olhar sobre o Solar', sub='Piscina, área gourmet, detalhes da decoração e a Praia da Daniela.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Solar da Dora') for k, i in gal])
    google = [
        ('Mariana B.', 'A pousada da Dora é uma experiência aconchegante que traz paz e alegria! Os quartos são mini apartamentos completos, há piscina, área de leitura e descanso e fica a 2 ruas da praia da Daniela.'),
        ('Paulo C.', 'Eu e minha esposa nos hospedamos na pousada da dona Dora e seu Palhares há muitos anos. É como se fosse a nossa casa. A pousada é impecável e bem próxima à praia.'),
        ('Christine A.', 'A pousada é um capricho, bem cuidada, com decoração praiana, um espaço agradável, uma área de churrasqueira e piscina muito boa, e apartamentos bem equipados. A Dona Dora é uma simpatia.'),
        ('Sabrina G.', 'Encontramos um ambiente delicadamente decorado, agradável e confortável! Excelente escolha para hospedagem de nossa família! Gilberto e Dora são pessoas simpáticas e atenciosas.'),
        ('Cláudio P.', 'Já são 3 anos que vamos para a Daniela e nossa estadia é maravilhosa, atendimento sensacional, os proprietários sempre solícitos, ambiente familiar.'),
        ('Adriano E.', 'Ficamos encantados com a receptividade, limpeza e o carinho com cada detalhe. Certamente voltaremos!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=g(17), headline='4,8 no Google · 47 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='A praia fica longe?', a='Não. A pousada fica a duas ruas da Praia da Daniela, dá pra ir a pé até o mar.'),
        dict(q='Os apartamentos têm cozinha?', a='Sim. São mini apartamentos completos, com cozinha equipada, geladeira e utensílios.'),
        dict(q='Tem piscina e churrasqueira?', a='Sim. A pousada tem piscina e área gourmet com churrasqueira para os hóspedes.'),
        dict(q='Qual o horário de check-in e check-out?', a='Combine o horário de chegada e saída com a gente pelo WhatsApp.'),
        dict(q='A pousada é boa para famílias?', a='Muito. A Daniela tem mar calmo e raso, ótimo pra crianças, e a pousada tem clima familiar.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('hibiscus', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
