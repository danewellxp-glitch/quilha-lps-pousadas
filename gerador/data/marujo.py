from common import ig, review_sources
from deco import deco, logo

TEMPLATE = 'aurelia'
U = 'pousada.marujo'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Marujo+Barra+da+Lagoa+Florian%C3%B3polis'

T = dict(gold='#d0904f', gold2='#f0b679', dark='#173045', darker='#0f1e2b', cream='#f5f1ea', cream2='#e9e3d8',
         sage='#2f6b8a', text='#1b232b', muted='#56606a', line='#c9bba6')

P = dict(
    slug='marujo', name='Pousada Marujo', brand='Marujo', place_short='Barra da Lagoa, Floripa',
    meta_desc='Pousada Marujo na Barra da Lagoa, Florianópolis: apartamentos com cozinha, varanda com rede, piscina e pet friendly.',
    phone='(48) 99107-4878', wa_number='5548991074878', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Marujo e queria consultar disponibilidade.',
    instagram='pousada.marujo',
    address='Rod. João Gualberto Soares, 17.421 - Barra da Lagoa, Florianópolis - SC, 88061-500',
    footer_tag='O pouso do marujo na Barra da Lagoa.',
    room_word='Apartamento', rooms_label='Acomodações', rooms_eyebrow='Acomodações', rooms_title='Seu cantinho na Barra',
    rooms_sub='Apartamentos com cozinha, banheiro privativo e varandinha com rede, pra se sentir em casa na ilha.',
    tagline='Piscina no jardim, rede na varanda e a praia da Barra pertinho.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar na Barra da Lagoa.',
)


def context(I, wa):
    g = lambda i: I(ig(U, i))[0]
    p = dict(P)
    p['hero'] = dict(img=g(10), alt='Piscina e jardim da Pousada Marujo', eyebrow='Bem-vindo ao Marujo',
                     title='Seu pouso na Barra da Lagoa',
                     sub='Apartamentos com cozinha, piscina no jardim e a vila de pescadores mais charmosa de Floripa a poucos passos.',
                     cta='Ver acomodações')
    p['about'] = dict(eyebrow='O Pouso do Marujo · Barra da Lagoa', title='Simples, acolhedora e perto de tudo',
                      text='Casinhas de tijolinho, buganvílias floridas, redes nas varandas e um anfitrião que recebe todo mundo pelo nome. Mercado, padaria e lanchonete ficam a um minuto, e a praia da Barra a uma caminhada.',
                      sign='Marujo', role='Pousada na Barra da Lagoa',
                      imgs=[dict(src=g(i), alt='Pousada Marujo') for i in (3, 28, 36, 47)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada Marujo.')
    p['rooms'] = [
        dict(name='Apartamento Casal', img=g(48), badge='Com cozinha', text='Cama de casal, banheiro privativo, cozinha equipada e varandinha com rede.',
             meta=[dict(icon='bed', text='Casal'), dict(icon='users', text='2 hóspedes'), dict(icon='kitchen', text='Cozinha')], wa=rw('Apartamento Casal')),
        dict(name='Apartamento Família', img=g(30), badge='Com cozinha', text='Quarto com casal e solteiro e sala/cozinha com camas extras para a família toda.',
             meta=[dict(icon='bed', text='Casal + solteiros'), dict(icon='users', text='Até 5 hóspedes'), dict(icon='kitchen', text='Cozinha')], wa=rw('Apartamento Família')),
        dict(name='Cozinha de Apoio', img=g(49), badge='Em todos', text='Geladeira, fogão, micro-ondas, chaleira e louças: dá pra fazer a sua comida sem sair da pousada.',
             meta=[dict(icon='kitchen', text='Fogão e geladeira'), dict(icon='tv', text='TV'), dict(icon='wifi', text='Wi-Fi')], wa=rw('apartamento com cozinha')),
    ]
    p['exp'] = dict(eyebrow='A experiência Marujo', title='Além da estadia',
                    sub='A Barra é vila de pescador, canal, praia e lagoa num lugar só. A gente indica o melhor de cada um.',
                    cards=[dict(icon='pool', title='Piscina no jardim', kicker='Depois da praia', text='Pra relaxar quando volta da praia, cercada de verde e com mesinhas ao redor.'),
                           dict(icon='wave', title='Praia da Barra', kicker='Pertinho', text='A praia da Barra da Lagoa, o canal e a Prainha ficam a poucos minutos.'),
                           dict(icon='paw', title='Pet friendly', kicker='Família toda', text='Seu cachorro é bem-vindo e as crianças têm espaço de sobra no jardim.')])
    gal = [45, 34, 3, 0, 2, 50, 5, 25, 40, 47, 36, 10]
    p['gallery'] = dict(title='Um olhar sobre o Marujo', sub='Jardim, piscina e o jeitinho de vila de pescador da Barra.',
                        imgs=[dict(src=g(i), alt='Pousada Marujo') for i in gal])
    items = [
        ('Elias S.', 'Excelente pousada aqui Florianópolis, recomendo, localização ótima, acomodação muito legal, bem aconchegante, tudo incluso geladeira, fogão top.'),
        ('Gustavo B.', 'Fiquei em um quarto com uma cama de casal + uma de solteiro e banheiro, também com uma área privada na frente com mesa e rede! O local tem piscina.'),
        ('Flavia S.', 'Os quartos são limpos, camas macias. Cada quarto tem banheiro privativo e cozinha. E uma pequena varanda com uma rede, ideal para um descanso.'),
        ('Sandra B.', 'Tivemos uma grata surpresa com nossa estadia, o anfitrião é nota 10, sempre solícito e muito atento a tudo.'),
        ('Claudete S.', 'Fiquei uma semana com minha família. O lugar é simples, tem de tudo, gostei bastante e recomendo. (…) O local é próximo de tudo e isso facilita bastante.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    rv.insert(1, dict(key='tripadvisor', text='Excelentes acomodações, excelente atendimento, excelente café da manhã, marcou minha vida, recomendo a todos os viajantes que irão à Florianópolis.',
                      author='monalisag228', source='Tripadvisor', stars=5))
    p['reviews'] = dict(bg=g(5), headline='4,5 no Google · 243 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', ''), ('tripadvisor', 'Tripadvisor', '4,7', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Os apartamentos têm cozinha?', a='Sim. Todos têm geladeira, fogão, micro-ondas e louças, além de banheiro privativo.'),
        dict(q='Tem café da manhã?', a='O café da manhã é servido na alta temporada, de dezembro a março. No resto do ano tem mercado e padaria a um minuto da pousada.'),
        dict(q='Posso levar meu pet?', a='Pode! A pousada aceita animais. Avise na reserva.'),
        dict(q='Tem estacionamento?', a='Sim, estacionamento gratuito dentro da pousada.'),
        dict(q='Os quartos têm ar-condicionado?', a='Os apartamentos são ventilados, com ventilador. Pergunte pelo WhatsApp qual acomodação atende melhor o seu grupo.'),
        dict(q='Como funciona a chegada?', a='Você recebe a chave do apartamento e do portão na chegada. Combine o horário com o anfitrião pelo WhatsApp.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('anchor', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
