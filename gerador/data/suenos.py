"""Pousada Sueños de Verano (Ponta das Canas, Florianópolis) — LP no template 'aurelia'."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('suenos')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Sue%C3%B1os+de+Verano+Ponta+das+Canas'

T = dict(gold='#c8955a', gold2='#e7c08c', dark='#14263a', darker='#0c1826', cream='#f6f1e8', cream2='#eadfcd',
         sage='#3f6f8a', text='#18202a', muted='#5a6170', line='#d6c6a8')

P = dict(
    slug='suenos', name='Pousada Sueños de Verano', brand='Sueños de Verano', place_short='Ponta das Canas, Floripa',
    meta_desc='Pousada Sueños de Verano, pé na areia em Ponta das Canas, no norte de Florianópolis: piscina com vista pro mar, sauna, quartos modernos e um portão direto pra praia. Só para adultos. Nota 9,3 no Booking.',
    phone='(48) 99840-7081', wa_number='5548998407081', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Sueños de Verano e queria consultar disponibilidade.',
    instagram='suenos_de_verano',
    address='R. Dep. Fernando Viégas, 264 - Ponta das Canas, Florianópolis - SC, 88056-730',
    footer_tag='Pé na areia em Ponta das Canas. Só para adultos.',
    room_word='Quarto', rooms_label='Quartos', rooms_eyebrow='Quartos da Sueños', rooms_title='Nossas acomodações',
    rooms_sub='Quartos novos e espaçosos, com ar-condicionado, TV, frigobar e roupa de cama de hotel.',
    tagline='Piscina com vista pro mar, sauna e a praia a um portão de distância.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar a Ponta das Canas.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(26, True), alt='Piscina da Sueños de Verano ao pôr do sol, com palmeiras e o mar ao fundo', eyebrow='Bienvenidos · Bem-vindos',
                     title='Pé na areia em Ponta das Canas',
                     sub='Uma pousada só para adultos, com piscina de frente pro mar, sauna e um portão que abre direto na praia.',
                     cta='Conhecer os quartos')
    p['about'] = dict(eyebrow='Sueños de Verano · Ponta das Canas', title='Feita pra quem quer descansar de verdade',
                      text='A Sueños fica na parte mais tranquila de Ponta das Canas, de frente pra uma faixa de areia extensa e de mar calmo. Tudo é novo e bem cuidado: piscina com vista pro mar, canteiros floridos, salão de café envidraçado, sauna e banho turco. A Lorena e o Miguel recebem cada hóspede de perto, em português ou espanhol.',
                      sign='Lorena & Miguel', role='Anfitriões',
                      imgs=[dict(src=G(i), alt='Pousada Sueños de Verano') for i in (2, 9, 21, 22)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada Sueños de Verano.')
    p['rooms'] = [
        dict(name='Suíte Premium', img=G(5), badge='Vista privilegiada',
             text='Nossa suíte mais especial, com cama de casal, armários, frigobar e acabamento novo. Ideal pra uma viagem a dois.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Ar-condicionado'), dict(icon='tv', text='TV e frigobar')],
             wa=rw('Suíte Premium')),
        dict(name='Quarto Duplo', img=G(23), badge='Até 2 hóspedes',
             text='Cama de casal grande e futon, ar-condicionado, TV, frigobar, chaleira e cofre.',
             meta=[dict(icon='bed', text='Casal + futon'), dict(icon='users', text='2 hóspedes'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Quarto Duplo')),
        dict(name='Apartamento com Sala', img=G(32), badge='Mais espaço',
             text='Quarto com sala integrada, sofá, mesinha e banheiro amplo, pra estadias mais longas.',
             meta=[dict(icon='area', text='Sala integrada'), dict(icon='bath', text='Banheiro amplo'), dict(icon='wifi', text='Wi-Fi')],
             wa=rw('Apartamento com Sala')),
    ]
    p['exp'] = dict(eyebrow='A experiência Sueños', title='Dias de verão, do jeito certo',
                    sub='Do café com vista pro mar ao pôr do sol na piscina, cada detalhe é pensado pra relaxar.',
                    cards=[dict(icon='wave', title='Acesso direto à praia', kicker='Pé na areia', text='Uma passarela de madeira leva do jardim até a areia de Ponta das Canas, de mar calmo e água quentinha.'),
                           dict(icon='pool', title='Piscina com vista', kicker='Fim de tarde', text='A piscina fica de frente pro mar. No fim do dia, o sol se põe atrás dos barcos da baía.'),
                           dict(icon='sparkle', title='Sauna e banho turco', kicker='Bem-estar', text='Sauna seca e banho turco pra fechar o dia de praia, além de academia pros hóspedes.'),
                           dict(icon='heart', title='Só para adultos', kicker='Tranquilidade', text='Um lugar pensado pra casais e amigos que querem silêncio, descanso e boas conversas.')])
    gal = [('g', 28), ('G', 16), ('g', 11), ('G', 14), ('g', 29), ('G', 29), ('g', 7), ('G', 36), ('g', 46), ('G', 20), ('g', 23), ('g', 42)]
    p['gallery'] = dict(title='Um olhar sobre a Sueños', sub='Piscina, jardim florido, quartos novos e o mar de Ponta das Canas.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Sueños de Verano') for k, i in gal])
    google = [
        ('Carolina F.', 'Superou minhas expectativas. O quarto era muito confortável, moderno e funcional. Há cantinhos especiais por toda a pousada. A localização é excelente. A piscina aquecida é nota 10/10.'),
        ('Danilo Z.', 'Excelente lugar para férias relaxantes. Lorena e Miguel foram muito atenciosos, todas as instalações estavam em perfeitas condições, o acesso à praia era espetacular e a piscina fabulosa.'),
        ('Javier P.', 'Excelente pousada, tudo novo e muito bem conservado. A atenção pessoal dos proprietários, Lorena e Miguel, é excepcional. Recomendo pelas instalações e pela localização em frente à praia.'),
        ('Verónica M.', 'Espetacular! A vista do quarto era incrível. A simpatia dos proprietários e da equipe é fantástica. Voltarei com certeza e recomendo muito.'),
        ('Liselotte P.', 'Tudo foi maravilhoso. Um lugar pequeno, mas encantador. Os quartos eram muito limpos e modernos. A localização, bem perto da praia, era ideal. A piscina era muito limpa e agradável.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    rv.insert(1, dict(key='booking', text='Ótima localização em relação à praia. Instalações limpas e espaçosas. Anfitriões atenciosos. Voltaremos.',
                      author='Mougly', source='Booking', stars=5))
    rv.insert(4, dict(key='booking', text='Vista maravilhosa, pousada incrível, aconchegante, com flores, piscina e até chá de boldo pra quem bebe um pouquinho a mais. Adoramos e vamos voltar.',
                      author='Viviani', source='Booking', stars=5))
    p['reviews'] = dict(bg=g(19), headline='9,3 no Booking · 99 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', ''), ('booking', 'Booking', '9,3', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='A pousada aceita crianças?', a='A Sueños é uma pousada só para adultos, pensada pra quem busca tranquilidade.'),
        dict(q='A praia fica longe?', a='Não. A pousada fica de frente pra praia de Ponta das Canas, com uma passarela de madeira que leva direto à areia.'),
        dict(q='Qual o horário de check-in e check-out?', a='Combine o horário de chegada e saída com a gente pelo WhatsApp.'),
        dict(q='Tem estacionamento?', a='Sim, estacionamento coberto e gratuito para os hóspedes.'),
        dict(q='Vocês falam espanhol?', a='Sim. Atendemos em português e espanhol. ¡Hablamos español!'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wave', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
