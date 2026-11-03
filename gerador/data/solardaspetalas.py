"""Solar das Pétalas Guest House (Lagoa da Conceição, Florianópolis) — LP no template 'doma'."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('solardaspetalas')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Solar+das+P%C3%A9talas+Guest+House+Lagoa+da+Concei%C3%A7%C3%A3o'

T = dict(bg='#fbf8f1', text='#1c2135', muted_text='#585e72', accent='#2b5aa3', accent_ink='#fff8e8', sage='#f0c94d',
         label='#d0662a', band='#e5edf8', line='rgba(28,33,53,.14)', card='#f2eee3')

P = dict(
    slug='solardaspetalas', name='Solar das Pétalas Guest House', logo_small='Guest House', logo_main='Solar das Pétalas',
    meta_desc='Solar das Pétalas Guest House, no centrinho da Lagoa da Conceição, em Florianópolis: casa colorida, quartos aconchegantes, deck com jardim e as praias do leste da Ilha por perto. Nota 4,5 no Google e 8,6 no Booking.',
    phone='(48) 99186-4137', wa_number='5548991864137', email='',
    wa_text='Olá! Vim pelo site da Solar das Pétalas Guest House e queria consultar disponibilidade.',
    instagram='solardaspetalasguesthouse', footer_tag='Uma casa colorida no coração da Lagoa da Conceição.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    gi = lambda src: I(src)
    p = dict(P)
    p['hero'] = dict(img=g(60, True), alt='Sala de estar da Solar das Pétalas, com parede laranja, sofás e macramê',
                     title='Uma casa colorida no centrinho da Lagoa',
                     sub='Guest house charmosa, numa rua tranquila, a poucos passos dos bares e restaurantes da Lagoa da Conceição')
    p['intro'] = ['A Solar das Pétalas é uma casa de paredes azuis e laranja, cheia de plantas, murais e cantinhos pra conversar. Fica numa rua calma, mas bem no centrinho da Lagoa da Conceição, perto de mercados, farmácias, bares e restaurantes.',
                  'Daqui você chega rápido às praias do leste da Ilha, como Joaquina, Praia Mole, Galheta e Barra da Lagoa, e volta pra descansar num quarto aconchegante, com o clima de casa que os hóspedes sempre comentam.']
    p['about'] = dict(label='A casa', title='Charme, cor e boas-vindas',
                      sub='Uma guest house pequena, com decoração cheia de personalidade e hóspedes do mundo todo.',
                      img=G(9), alt='Entrada azul da Solar das Pétalas, com deck de madeira e plantas',
                      feats=[dict(icon='pin', title='No centrinho da Lagoa', text='Rua tranquila, mas a poucos passos de bares, restaurantes, mercados e farmácias.'),
                             dict(icon='bed', title='Quartos aconchegantes', text='Suítes e estúdio com banheiro privativo, TV, frigobar e chaleira. Alguns com cozinha.'),
                             dict(icon='leaf', title='Deck e jardim', text='Área externa com deck de madeira, plantas e cantinhos pra ler ou trabalhar.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('car', 'Estacionamento'), ('paw', 'Aceita pets'),
        ('coffee', 'Café da manhã opcional'), ('kitchen', 'Cozinha em alguns quartos'), ('key', 'Entrada com senha, sem horário'),
        ('plane', 'Traslado do aeroporto'), ('tv', 'TV, frigobar e chaleira'), ('clock', 'Check-in 14h · check-out 11h')]]
    gal = [('G', 7), ('g', 0), ('g', 59), ('g', 62), ('g', 61), ('G', 14), ('g', 47), ('g', 52), ('g', 51), ('g', 9), ('g', 28), ('g', 49)]
    gimgs = []
    for k, i in gal:
        src, w, h = gi(F.gm(i) if k == 'G' else F.ig(i))
        gimgs.append(dict(src=src, w=w, h=h, alt='Solar das Pétalas Guest House'))
    p['gallery'] = dict(title='Cada canto tem uma cor', sub='Murais, plantas, deck de madeira e quartos com cara de casa.', imgs=gimgs)
    p['exp'] = dict(title='A Lagoa e o leste da Ilha',
                    sub='A guest house é o ponto de partida perfeito pra conhecer as praias, as trilhas e a vida do centrinho da Lagoa.',
                    cards=[dict(img=g(30), alt='Vista da janela para os telhados e o morro da Lagoa', title='Centrinho da Lagoa',
                                text='Bares, restaurantes, feirinha e o pôr do sol na beira da lagoa, tudo a uma caminhada.'),
                           dict(img=g(64), alt='Costão e mar azul no leste da Ilha', title='Praias do leste',
                                text='Joaquina, Praia Mole, Galheta e Barra da Lagoa a poucos minutos da pousada.'),
                           dict(img=g(5), alt='Cachoeira em meio à mata', title='Trilhas e natureza',
                                text='Trilhas, cachoeiras e passeios pela Ilha, com as dicas de quem conhece a região.')])
    p['band'] = g(63, True)
    p['loc'] = dict(title='No coração da Lagoa', area='Lagoa da Conceição · Florianópolis',
                    address='R. Afonso Luís Borba, 155 - Lagoa da Conceição, Florianópolis - SC, 88062-040',
                    maps_q='Solar das Pétalas Guest House, R. Afonso Luís Borba 155, Florianópolis', maps_url=MAPS,
                    getting=['Centrinho da Lagoa: a poucos passos', 'Joaquina e Praia Mole: poucos minutos de carro', 'Aeroporto de Florianópolis: cerca de 16 km'],
                    nearby=['Lagoa da Conceição e o centrinho', 'Joaquina, Praia Mole e Galheta', 'Gravatá e Barra da Lagoa'])
    google = [
        ('Fernanda L.', 'A localização é TOP, bem no centrinho da Lagoa, porém uma rua bem tranquila. A pousada é super charmosa. O quarto muito confortável e extremamente limpo. Chuveiro muito bom. Ótimo custo-benefício.'),
        ('Alessandra M.', 'Este GuestHouse é encantador e com uma decoração simples mas de muito bom gosto. O grande diferencial está no tratamento diferenciado dado aos hóspedes.'),
        ('Eudóxio J.', 'Este GuestHouse apresenta muitas vantagens: excelente localização (bem no centrinho da Lagoa), bom atendimento e cordialidade, boas acomodações.'),
        ('Lilian V.', 'Café da manhã simples e gostoso, o quarto bem aconchegante... Silencioso e agradável. Bacana que temos a chave e liberdade de ir e vir sem horário.'),
    ]
    booking = [
        ('Fabiana', 'A localização é perfeita, perto de tudo e do principal, o centrinho da Lagoa. A vista para o morro era linda.'),
        ('Raphaela', 'Ótima localização, fácil acesso a outras regiões e a vários pontos turísticos. O Flávio nos deu várias dicas de locais a visitar e onde comer.'),
        ('Katia', 'Quarto confortável, banheiro amplo, excelente localização, acesso à propriedade por senha, sem necessidade de porteiro.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    for k, (a, t) in enumerate(booking):
        rv.insert(1 + 2 * k, dict(key='booking', text=t, author=a, source='Booking', stars=5))
    p['reviews'] = dict(sub='Hóspedes do Brasil e do mundo todo elogiam a localização, o charme e o atendimento.',
                        headline='4,5 no Google · 76 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 76 avaliações'),
                                                ('booking', 'Booking', '8,6', '8,6 no Booking · 76 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Vem pro Solar?', sub='Fale direto com a gente pelo WhatsApp e garanta seu quarto no centrinho da Lagoa.')
    return p
