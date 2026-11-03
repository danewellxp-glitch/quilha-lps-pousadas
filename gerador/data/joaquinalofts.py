"""Joaquina Lofts (Servidão Mata Atlântica, 62, Joaquina, Florianópolis) — site no template 'stayora'.
Fotos: Google Maps 2ª passada (gm2). Nota 5,0 no Google (263). Anfitrião: Stewson e família. 4 lofts com cozinha,
piscina aquecida, sauna úmida e churrasqueira. Hoje usa Linktree + Airbnb (Loft 03/04) no lugar de site."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('joaquinalofts')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Joaquina+Lofts+Servid%C3%A3o+Mata+Atl%C3%A2ntica+62+Florian%C3%B3polis'

T = dict(bg='#f5f4ef', alt='#e9e8e0', ink='#101412', ink2='#18201c', muted='#56605a', dim='#b6bcb6',
         dark='#0b100d', card='#f5f4ef', accent='#2e7a57', line='#dcded6')

P = dict(
    slug='joaquinalofts', name='Joaquina Lofts', short='Joaquina Lofts',
    seo_title='Joaquina Lofts | Lofts com piscina aquecida na Joaquina, Florianópolis',
    meta_desc='Joaquina Lofts: lofts com cozinha em meio à mata, piscina aquecida, sauna e churrasqueira, a poucos minutos da Praia da Joaquina e da Lagoa da Conceição. Nota 5,0 no Google.',
    phone='(48) 99600-5926', wa_number='5548996005926', email='',
    wa_text='Olá! Vim pelo site da Joaquina Lofts e queria consultar disponibilidade.', instagram='', maps_url=MAPS,
    address='Servidão Mata Atlântica, 62 · Joaquina, Florianópolis/SC', checkin='15h', checkout='11h',
    footer_tag='Lofts em meio à mata, com piscina aquecida e sauna, entre a Joaquina e a Lagoa da Conceição.',
    nav=[('Os lofts', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Acomodações', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#2e7a57', '#b5762a', '#3f6b5c', '#14313a', '#8a5a44', '#2a6f97', '#6b5b95', '#c06c84']


def context(I, wa):
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(98, True), alt='Piscina e lofts da Joaquina Lofts em meio às palmeiras',
                     title='Um refúgio tropical a passos da Joaquina',
                     sub='Lofts com cozinha, piscina aquecida e sauna no meio da mata, entre a praia e a Lagoa da Conceição.',
                     avatars=[('C', '#2e7a57'), ('L', '#b5762a'), ('J', '#3f6b5c')],
                     proof='Nota 5,0', proof_sub='263 avaliações no Google')
    p['about'] = dict(imgs=[G(26), G(4)], alts=['Piscina com pufes e prancha de surfe', 'Loft com cama king e sala'],
                      stat_num='5.0', stat_dec=1, stat_txt='5,0', stat_label='Nota no Google',
                      kicker='Os lofts', title='Um lugar com alma, no meio do verde.',
                      text='A Joaquina Lofts são quatro lofts cercados de palmeiras, samambaias e bambus, a poucos minutos da Praia da Joaquina. Cada loft tem quarto, sala e cozinha, decoração com madeira, tijolinho e peças garimpadas, e cama de hotel. Lá embaixo, a piscina aquecida, a sauna e a área de churrasco, com jazz e MPB tocando baixinho.')
    p['amen_title'] = 'Tudo pra desligar sem abrir mão do conforto.'
    p['amenities'] = [('pool', 'Piscina aquecida'), ('sparkle', 'Sauna úmida'), ('kitchen', 'Cozinha em todos os lofts'),
                      ('snow', 'Ar-condicionado'), ('wifi', 'Wi-Fi pra videochamada'), ('food', 'Churrasqueira'),
                      ('leaf', 'Jardim tropical'), ('bed', 'Cama king e enxoval de hotel'), ('wave', 'Praia da Joaquina pertinho'),
                      ('lagoon', 'Lagoa da Conceição a poucos minutos'), ('tv', 'TV nos lofts'), ('clock', 'Check-in 15h · check-out 11h')]
    p['spaces_title'] = 'Cada canto pensado pra desacelerar.'
    p['spaces'] = [dict(img=G(25), title='O loft', text='Quarto, sala e decoração com peças de madeira esculpida, tijolinho e luz baixa.'),
                   dict(img=G(37), title='Varanda com rede', text='Rede, gramado e a vista dos morros da Lagoa no fim de tarde.'),
                   dict(img=G(95), title='Cozinha equipada', text='Geladeira, cooktop, utensílios e bancada pra preparar o café sem pressa.'),
                   dict(img=G(27), title='Piscina à noite', text='Água aquecida, pufes e a mata iluminada em volta.'),
                   dict(img=G(55), title='Área de churrasco', text='Mesa comprida, churrasqueira e espaço pra receber os amigos.')]
    p['host'] = dict(img=G(6), alt='Lofts e piscina da Joaquina Lofts', name='Stewson e família',
                     lines=[('star', 'Nota 5,0 no Google'), ('pin', 'Entre a Joaquina e a Lagoa'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='Experiência incrível, um dos melhores lugares que já me hospedei em Florianópolis. Me senti na Indonésia e em casa.',
                     text='Palavras do Bruno, um dos hóspedes. Quem recebe é o próprio Stewson, com a família e os gatos da casa, e as melhores dicas da Ilha.')
    p['plan'] = dict(kicker='Acomodações', title='Escolha o seu loft.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Loft Jardim', note='até 2 hóspedes', img=G(17),
                                 cells=['Cama king', 'Sala com sofá', 'Cozinha equipada', 'Ar-condicionado', 'Vista do jardim']),
                            dict(name='Loft Varanda', note='até 2 hóspedes', img=G(84),
                                 cells=['Cama king', 'Sala de estar', 'Varanda com rede', 'Cozinha equipada', 'Banheiro privativo']),
                            dict(name='Loft Família', note='até 4 hóspedes', img=G(76),
                                 cells=['Duas camas de casal', 'Cozinha equipada', 'Ar-condicionado', 'Espaço pra família', 'Banheiro privativo'])])
    p['exp'] = dict(title='A Joaquina e a Lagoa, logo ali.',
                    big=dict(img=G(115, True), title='Praia da Joaquina', text='Dunas, surfe e mar aberto a poucos minutos dos lofts.'),
                    wide=dict(img=G(128), title='Lagoa da Conceição', text='Bares, restaurantes e o pôr do sol na beira da lagoa, a poucos minutos.'),
                    list_title='Mais pra explorar',
                    list=[('board', 'Sandboard nas dunas'), ('hike', 'Trilhas da Costa da Lagoa'), ('wave', 'Praia Mole e Galheta'), ('food', 'Gastronomia da Lagoa')],
                    small=dict(img=G(69), title='Café sem pressa', text='Monte seu café na cozinha do loft e tome na varanda.'))
    items = [
        ('Camilla S.', 'Google', 'Lugar incrível em meio à natureza, com piscina quentinha, sauna úmida e espaço para o churrasco. Além de um pôr do sol para ficar na memória.'),
        ('Leom G.', 'Google', 'Um lugar simplesmente incrível! O loft é espaçoso, aconchegante e muito funcional, com cozinha, sala e quarto muito bem organizados.'),
        ('Cristel T.', 'Google', 'Um lugar com alma. Encontrei um ambiente de extremo bom gosto, verde em abundância e uma recepção calorosa e impecável.'),
        ('Jeneffer T.', 'Google', 'Minha pousada preferida em Florianópolis, já nos hospedamos várias vezes e sempre voltamos. Fica a poucos metros da famosa praia da Joaquina.'),
        ('Juno O.', 'Google', 'Loft muito confortável, cama espetacular, piscina aquecida, sauna, música ambiente e área de churrasco. Vale cada real.'),
        ('Jeremy J.', 'Google', 'Best accommodation I have had since arriving in Brazil. Beautiful rooms, WiFi good enough for video calls and a lovely pool with sauna inside what feels like a jungle.'),
        ('Francisco A.', 'Google', 'O local é um verdadeiro paraíso, decoração com muito verde e cheia de estilo. O loft é muito bem equipado, com enxoval caprichado.'),
        ('Alessandro R.', 'Google', 'Lugar maravilhoso, muito seguro, tranquilo e aconchegante. Já me hospedei 4 vezes com minha esposa: nossa pousada favorita em Floripa.'),
    ]
    p['reviews'] = dict(title='O tipo de estadia que os hóspedes comentam.', count=263, rating='5,0',
                        bars=[('Google', '5,0', 100)],
                        note='5,0 no Google · 263 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='5,0 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 15h e o check-out até as 11h. Se precisar de outro horário, combine com a gente pelo WhatsApp.'),
                ('A piscina é aquecida?', 'Sim. A piscina é aquecida e tem sauna úmida ao lado, pra aproveitar mesmo nos dias mais frescos.'),
                ('Os lofts têm cozinha?', 'Sim, todos os lofts têm cozinha equipada, com geladeira, cooktop e utensílios.'),
                ('A que distância fica a praia?', 'A Praia da Joaquina fica a poucos minutos, e o centrinho da Lagoa da Conceição também.'),
                ('Dá pra trabalhar de lá?', 'Sim. O Wi-Fi aguenta videochamadas e os lofts têm espaço de apoio pra notebook.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A gente confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=G(11, True), title='Reserve seu loft no meio da mata.',
                    text='Escolha as datas, chame a gente no WhatsApp e garanta piscina aquecida, sauna e a Joaquina logo ali.')
    return p
