"""Pousada da Ilha (R. Rodolfo Hickel, 524, Canasvieiras, Florianópolis) — LP no template 'doma' (sem seção de quartos:
as fotos de quarto no Maps são poucas e antigas). Fotos: Google Maps 2ª passada (gm2). Site antigo pousadailha.com.br fora do ar.
Dono citado nas avaliações: Juliano. Uma avaliação recente diz que agora pertence aos Flats Amsterdam (há foto de banner
'Flat Amsterdam Comfort Canasvieiras') — confirmar o nome na ligação."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('pousadadailha')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+da+Ilha+R.+Rodolfo+Hickel+524+Canasvieiras'

T = dict(bg='#fbf7ee', text='#1d2430', muted_text='#5a6170', accent='#1d4f86', accent_ink='#fdf8ec', sage='#f2c14e',
         label='#c0762a', band='#f4e6c4', line='rgba(29,36,48,.14)', card='#f4eddc')

P = dict(
    slug='pousadadailha', name='Pousada da Ilha', logo_small='Pousada', logo_main='da Ilha',
    meta_desc='Pousada da Ilha em Canasvieiras, Florianópolis: ambiente familiar, piscina, churrasqueira e café da manhã, a menos de duas quadras da praia.',
    phone='(48) 3266-4808', wa_number='554832664808', email='',
    wa_text='Olá! Vim pelo site da Pousada da Ilha e queria consultar disponibilidade.',
    instagram='', footer_tag='Ambiente familiar e o melhor custo-benefício de Canasvieiras.',
)


def context(I, wa):
    g = lambda i: I(F._get('gm2', i))[0]
    gi = lambda i: I(F._get('gm2', i))
    p = dict(P)
    p['hero'] = dict(img=g(17), alt='Pátio com piscina da Pousada da Ilha',
                     title='Canasvieiras do jeito que a família gosta',
                     sub='Piscina, churrasqueira e café da manhã, a menos de duas quadras da praia e do centrinho')
    p['intro'] = ['A Pousada da Ilha é aquele lugar simples e acolhedor onde a gente se sente em casa. Os apartamentos ficam em volta de um pátio colorido com piscina, mesinhas e azulejos, e quem recebe são os próprios donos.',
                  'Daqui dá pra fazer tudo a pé: a Praia de Canasvieiras fica a cerca de 150 metros, e padaria, mercado, farmácia e restaurantes estão logo ali.']
    p['about'] = dict(label='A pousada', title='Simples, limpa e familiar',
                      sub='Muitos hóspedes voltam todo ano, e não é por acaso: atendimento de família e preço justo.',
                      img=g(37), alt='Piscina com deck de madeira no pátio',
                      feats=[dict(icon='pool', title='Piscina no pátio', text='Deck de madeira, cadeiras e mesas pra aproveitar o sol entre um mergulho e outro.'),
                             dict(icon='food', title='Churrasqueira e cozinha', text='Espaço com churrasqueira e mesa comunitária pra preparar uma refeição com a turma.'),
                             dict(icon='bed', title='Apartamentos arejados', text='Com ar-condicionado, TV, frigobar e banheiro privativo. Alguns com sacada.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('pool', 'Piscina'), ('car', 'Estacionamento'),
        ('coffee', 'Café da manhã'), ('food', 'Churrasqueira e cozinha compartilhada'), ('tv', 'TV e frigobar nos quartos'),
        ('users', 'Ideal para famílias e crianças'), ('clock', 'Check-in 14h · check-out 10h'), ('wave', 'Praia a ~150 m')]]
    gal = [5, 92, 27, 23, 53, 30, 47, 113]
    p['gallery'] = dict(title='Cada canto da pousada', sub='O pátio, a piscina, o café e a praia de Canasvieiras logo ali.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Pousada da Ilha') for i in gal])
    p['exp'] = dict(title='Além da pousada',
                    sub='Canasvieiras tem praia calma, passeios de escuna e um centrinho cheio de opções. Pergunte que a gente indica.',
                    cards=[dict(img=g(47), alt='Faixa de areia da Praia de Canasvieiras', title='Praia de Canasvieiras',
                                text='Mar calmo e morno, perfeito pra crianças, a cerca de 150 metros da pousada.'),
                           dict(img=g(87), alt='Escuna navegando em Canasvieiras', title='Passeio de escuna',
                                text='Os passeios de barco pirata saem da própria praia rumo às ilhas e fortalezas da baía norte.'),
                           dict(img=g(79), alt='Fim de tarde na praia', title='Fim de tarde',
                                text='Pôr do sol na beira do mar e depois o agito dos bares e restaurantes do centrinho.')])
    p['band'] = g(91)
    p['loc'] = dict(title='No coração de Canasvieiras', area='Canasvieiras · Norte da Ilha',
                    address='R. Rodolfo Hickel, 524 - Canasvieiras, Florianópolis - SC, 88054-040',
                    maps_q='Pousada da Ilha, R. Rodolfo Hickel 524, Canasvieiras, Florianópolis', maps_url=MAPS,
                    getting=['Praia de Canasvieiras: cerca de 150 m', 'Centro de Florianópolis: cerca de 30 min de carro', 'Aeroporto de Florianópolis: cerca de 40 min de carro'],
                    nearby=['Centrinho de Canasvieiras', 'Praias de Jurerê e Ponta das Canas', 'Passeios de escuna pela baía norte'])
    items = [
        ('Rodrigo e Elisangela', 'A pousada é excelente! Um ambiente simples, mas bem decorado. A simpatia dos proprietários também é um grande diferencial. Dá para fazer tudo em Canasvieiras a pé.'),
        ('Cláudia H.', 'Ótima pousada. Atendente educada, quarto limpo e bem arejado, lugar tranquilo e silencioso, bom para dormir. A 4 minutos da praia e perto de tudo.'),
        ('Eddie J.', 'Pousada honesta, limpa e familiar. Ótimo custo-benefício. Fica a uma quadra da praia e a duas do comércio. Nos sentimos em casa e fomos muito bem recebidos.'),
        ('Lilian L.', 'Ambiente familiar, quartos limpos, ótimo atendimento e orientação pros passeios. Já estive duas vezes e voltarei com certeza. Melhor custo-benefício.'),
        ('Juliana', 'A pousada é ótima, possui quartos amplos, com banheiros muito bons. Excelente custo-benefício para famílias e amigos, a menos de duas quadras da praia.'),
        ('Andréia P.', 'Pousada muito bacana. Próximo de tudo: mar, mercados, centrinho. Ótimo atendimento dos proprietários. Super recomendo.'),
        ('Júlio C.', 'Fica num local tranquilo e próximo da praia de Canasvieiras. Além disso, possui estacionamento, piscina e local para refeições.'),
        ('Cássio M.', 'Ótima pousada, atenciosos, com piscina, perto da praia e o melhor custo-benefício de Canasvieiras.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    p['reviews'] = dict(sub='Mais de 200 avaliações de hóspedes que voltam ano após ano.', headline='4,5 no Google · 208 avaliações',
                        link=MAPS, sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 208 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Bora pra Canasvieiras?', sub='Fale direto com a gente pelo WhatsApp e garanta sua data perto da praia.')
    return p
