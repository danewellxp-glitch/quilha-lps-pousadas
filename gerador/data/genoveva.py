"""Pousada Genoveva / Residencial Genoveva (Ponta das Canas, Florianópolis) — LP no template 'doma'.
Obs.: o @pousadagenoveva é outra pousada (Farol de Santa Marta). Esta é administrada pela família Neves (@hotelarianeves)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('genoveva')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Genoveva+Ponta+das+Canas+Florian%C3%B3polis'

T = dict(bg='#f6f8f4', text='#16261d', muted_text='#56635a', accent='#1f7a4d', accent_ink='#fbfff8', sage='#f2c45a',
         label='#e07a3f', band='#e3efe8', line='rgba(22,38,29,.14)', card='#ecf1ea')

P = dict(
    slug='genoveva', name='Pousada Genoveva', logo_small='Residencial', logo_main='Genoveva',
    meta_desc='Pousada Genoveva, em Ponta das Canas, no norte de Florianópolis: apartamentos com cozinha equipada e varanda, a uma quadra da praia, com estacionamento, segurança 24 horas e o atendimento da família Neves. Nota 4,9 no Google.',
    phone='(48) 98424-0172', wa_number='5548984240172', email='',
    wa_text='Olá! Vim pelo site da Pousada Genoveva e queria consultar disponibilidade.',
    instagram='hotelarianeves', footer_tag='Apartamentos a uma quadra da praia de Ponta das Canas.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    gi = lambda src: I(src)
    p = dict(P)
    p['hero'] = dict(img=g(9, True), alt='Praia de Ponta das Canas vista do alto, com mar azul e o morro ao fundo',
                     title='A uma quadra da praia de Ponta das Canas',
                     sub='Apartamentos completos com varanda, num lugar tranquilo e seguro, pra férias em família no norte da Ilha')
    p['intro'] = ['A Genoveva fica numa rua calma de Ponta das Canas, a cerca de 100 metros da praia. Os apartamentos têm cozinha equipada, ar-condicionado, TV, Wi-Fi e roupa de cama e banho, e muitos têm varanda com rede olhando pro jardim.',
                  'Por perto tem supermercado, farmácia, hortifrúti e ponto de ônibus. Quem recebe é a família Neves, o Tino, a Elaine e o Eduardo, que há anos acolhem hóspedes do Brasil e da Argentina que voltam temporada após temporada.']
    p['about'] = dict(label='A pousada', title='Férias em família, perto do mar',
                      sub='Um residencial pequeno, bem cuidado e com clima de casa.',
                      img=G(16), alt='Vista da pousada com telhados, árvores e o mar ao fundo',
                      feats=[dict(icon='wave', title='A uma quadra da praia', text='Cerca de 100 m até a areia de Ponta das Canas, de mar calmo e água quentinha.'),
                             dict(icon='kitchen', title='Apartamentos completos', text='Cozinha equipada, ar-condicionado, TV, Wi-Fi e roupa de cama e banho.'),
                             dict(icon='shield', title='Seguro e tranquilo', text='Estacionamento no local e segurança 24 horas, numa rua sossegada.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi'), ('snow', 'Ar-condicionado'), ('car', 'Estacionamento'), ('kitchen', 'Cozinha equipada'),
        ('leaf', 'Varanda com rede'), ('shield', 'Segurança 24 horas'), ('paw', 'Aceita pets'), ('users', 'Ideal para crianças'),
        ('plane', 'Traslado do aeroporto'), ('lang', 'Hablamos español')]]
    gal = [('G', 3), ('G', 4), ('G', 10), ('G', 7), ('g', 11), ('G', 9), ('G', 12), ('G', 6), ('g', 31), ('G', 8), ('g', 45), ('G', 11)]
    gimgs = []
    for k, i in gal:
        src, w, h = gi(F._get('gm2', i) if k == 'G' else F.ig(i))
        gimgs.append(dict(src=src, w=w, h=h, alt='Pousada Genoveva'))
    p['gallery'] = dict(title='Por dentro da Genoveva', sub='Apartamentos com cozinha, varanda com rede e o jardim entre os blocos.', imgs=gimgs)
    p['exp'] = dict(title='O melhor do norte da Ilha',
                    sub='Ponta das Canas tem mar calmo, pôr do sol na baía e vizinhas lindas como a Lagoinha do Norte.',
                    cards=[dict(img=g(69), alt='Vista da Lagoinha do Norte do alto do morro', title='Lagoinha do Norte',
                                text='Pequena, de água quente e cercada de verde, fica a poucos minutos da pousada.'),
                           dict(img=g(44), alt='Pôr do sol sobre o mar de Ponta das Canas', title='Pôr do sol na baía',
                                text='O sol se põe no mar, com os barcos de pesca ancorados na frente da praia.'),
                           dict(img=g(45), alt='Canoa de pesca na areia', title='Passeios de barco',
                                text='Os passeios de escuna e as praias de Canasvieiras e Cachoeira do Bom Jesus ficam ao lado.')])
    p['band'] = g(1, True)
    p['loc'] = dict(title='Em Ponta das Canas', area='Ponta das Canas · Florianópolis',
                    address='Rua Alcides Bonatelli, 143 - Ponta das Canas, Florianópolis - SC, 88056-720',
                    maps_q='Pousada Genoveva, Rua Alcides Bonatelli 143, Florianópolis', maps_url=MAPS,
                    getting=['Praia de Ponta das Canas: cerca de 100 m', 'Supermercado, farmácia e ônibus: a poucas quadras', 'Aeroporto de Florianópolis: cerca de 40 km'],
                    nearby=['Lagoinha do Norte', 'Praia Brava e Ingleses', 'Canasvieiras e Cachoeira do Bom Jesus'])
    google = [
        ('Gabriela M.', 'É um lugar lindo, perfeito para famílias, a poucos passos da praia, acolhedor e com todas as comodidades necessárias para as suas férias. Cordialidade e simpatia são marcas registradas de Tino, Elaine e Celma.'),
        ('Viky G.', 'A duas quadras da praia, a três de supermercados e farmácia. A pousada tem estacionamento e segurança 24 horas. Recebemos o apartamento em perfeitas condições, com cozinha totalmente equipada, TV e Wi-Fi.'),
        ('Daniela M.', 'Excelente pousada, fui 2 vezes com minha família passar férias em Ponta das Canas. Tranquila, ambiente familiar, a metros da praia, a atenção e o trato da Eliane são super cordiais!'),
        ('María D.', 'A apenas um quarteirão da praia e do centro de Ponta das Canas. Tino e Elaine sempre estiveram atentos a todas as nossas necessidades. Fomos quase 10 anos seguidos.'),
        ('Félix C.', 'Já me hospedei na Genoveva três vezes e espero voltar. Como sempre, fomos recebidos com uma acolhida incrivelmente calorosa. Com certeza continuaremos voltando e recomendando.'),
        ('Máiquel T.', 'Ótima experiência, lugar com ótima localização e muito seguro, a 100 metros da praia. Super recomendo.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(sub='Famílias do Brasil e da Argentina voltam ano após ano.',
                        headline='4,9 no Google · 47 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,9', '4,9 no Google · 47 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Vem pra Ponta das Canas?', sub='Fale direto com a família Neves pelo WhatsApp e garanta seu apartamento.')
    return p
