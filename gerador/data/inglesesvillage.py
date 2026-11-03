"""Ingleses Village (R. Luiz Elias Daux, 38, Ingleses, Florianópolis) — LP no template 'aurelia'.
Fotos: Google Maps (2ª passada, gm2). Sem Instagram ativo (@pousadainglesesvillage sem posts).
Telefone a conferir: (48) 99108-6214. Não confundir com a Pousada Praia dos Ingleses."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('inglesesvillage')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Ingleses+Village+R.+Luiz+Elias+Daux+38+Florian%C3%B3polis'

T = dict(gold='#c98a1c', gold2='#f2c46b', dark='#16465a', darker='#0d2f3d', cream='#fbf7ee', cream2='#f3e9d2',
         sage='#2a8fa6', text='#1b2a30', muted='#5a676b', line='#e3cf9e')

P = dict(
    slug='inglesesvillage', name='Ingleses Village', brand='Ingleses Village', place_short='Ingleses, Norte da Ilha',
    meta_desc='Ingleses Village: pousada com piscina nos Ingleses, Norte de Florianópolis. Apartamentos e sobrados com cozinha, café da manhã, estacionamento e Wi-Fi, a poucos minutos a pé da praia.',
    phone='(48) 99108-6214', wa_number='5548991086214', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Ingleses Village e queria consultar disponibilidade.',
    instagram='',
    address='R. Luiz Elias Daux, 38 - Ingleses do Rio Vermelho, Florianópolis - SC, 88058-510',
    footer_tag='Piscina, café da manhã e a Praia dos Ingleses a poucos minutos a pé.',
    room_word='Apartamento', rooms_label='Acomodações', rooms_eyebrow='Acomodações da Ingleses Village', rooms_title='Espaço de sobra pra família toda',
    rooms_sub='Suítes renovadas e apartamentos tipo sobrado com cozinha equipada, todos com ar-condicionado e café da manhã incluso.',
    tagline='Sobrados amarelos em volta da piscina, no coração dos Ingleses.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar aos Ingleses.',
)


def context(I, wa):
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(3, True), alt='Piscina e sobrados da Ingleses Village', eyebrow='Bem-vindo à Ingleses Village',
                     title='Férias com piscina nos Ingleses',
                     sub='Apartamentos espaçosos com cozinha, café da manhã caprichado e a praia a poucos minutos a pé, no Norte da Ilha.',
                     cta='Ver acomodações')
    p['about'] = dict(eyebrow='Ingleses Village · Florianópolis', title='Um condomínio de férias com cara de casa',
                      text='A Ingleses Village é um conjunto de sobrados amarelos em volta de uma piscina, numa rua tranquila dos Ingleses. São 14 apartamentos, muitos com cozinha completa e dois andares, pensados pra família e grupos de amigos. Tem café da manhã servido todo dia, estacionamento, Wi-Fi e churrasqueira, e dá pra ir a pé até a praia, o centrinho, mercados e restaurantes.',
                      sign='Equipe Ingleses Village', role='Recepção',
                      imgs=[dict(src=s, alt='Pousada Ingleses Village') for s in (G(16), G(7), G(11), G(46))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Ingleses Village.')
    p['rooms'] = [
        dict(name='Suíte renovada', img=G(27), badge='Até 2 hóspedes',
             text='Suíte de casal com marcenaria nova, iluminação indireta, TV, bancada de trabalho, ar-condicionado e banheiro privativo.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Ar-condicionado'), dict(icon='coffee', text='Café incluso')],
             wa=rw('quarto Suíte renovada')),
        dict(name='Apartamento com cozinha', img=G(120), badge='Até 4 hóspedes',
             text='Quarto de casal com sacada, cozinha equipada com geladeira, fogão e micro-ondas, e espaço pra família ou amigos.',
             meta=[dict(icon='kitchen', text='Cozinha'), dict(icon='users', text='Até 4 pessoas'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Apartamento com cozinha')),
        dict(name='Sobrado duplex', img=G(11), badge='Até 6 hóspedes',
             text='Casa de dois andares com sala, cozinha completa, quartos no piso de cima e saída direta pra área da piscina.',
             meta=[dict(icon='home', text='Dois andares'), dict(icon='kitchen', text='Cozinha completa'), dict(icon='pool', text='Ao lado da piscina')],
             wa=rw('Sobrado duplex')),
    ]
    p['exp'] = dict(eyebrow='A experiência Ingleses Village', title='Os dias no Norte da Ilha',
                    sub='Praia de manhã, piscina à tarde e um churrasco com a turma no fim do dia.',
                    cards=[dict(icon='wave', title='Praia dos Ingleses', kicker='A poucos minutos', text='Uma das praias mais procuradas do Norte da Ilha, com mar calmo e as dunas do Santinho ao lado.'),
                           dict(icon='pool', title='Piscina no pátio', kicker='Pra toda a família', text='Piscina cercada pelos sobrados, com cadeiras e espaço pras crianças brincarem.'),
                           dict(icon='coffee', title='Café da manhã', kicker='Incluso', text='Frutas, pães, bolos e café fresquinho servidos todas as manhãs.'),
                           dict(icon='pin', title='Tudo pertinho', kicker='Localização', text='Mercado, farmácia, banco, sorveteria e restaurantes na vizinhança, sem precisar do carro.')])
    gal = [26, 8, 62, 4, 34, 139, 45, 98, 12, 20, 63, 9]
    p['gallery'] = dict(title='Um olhar sobre a Ingleses Village', sub='A piscina, os sobrados, as suítes renovadas e as cozinhas.',
                        imgs=[dict(src=G(i), alt='Ingleses Village') for i in gal])
    google = [
        ('Micaela V.', 'Adoramos a pousada! Fomos muito bem recebidos, o atendimento foi excelente e todos foram muito atenciosos. O café da manhã estava maravilhoso, tudo muito gostoso e feito com carinho.'),
        ('Éderson C.', 'O melhor hotel que fiquei em Florianópolis. Bom atendimento, café com várias opções, silêncio perfeito, excelentes quartos, casas incríveis. Foi tudo perfeito.'),
        ('Carolina M.', 'Amamos a hospedagem, o apartamento é grande e confortável. Agradecimento especial ao João, que fez um excelente atendimento!'),
        ('Filipi F.', 'São extremamente atenciosos, os apartamentos são maravilhosos, espaçosos e bem equipados. Café da manhã delicioso, local super limpo e organizado. Perto de tudo: praia, supermercado, centro.'),
        ('Dionatan D.', 'Super recomendo. Recepção muito boa, os apartamentos são mobiliados e bem espaçosos, banheiros e chuveiros bons, e o café é incrível. Com certeza voltaremos.'),
        ('Carol C.', 'Quartos bem limpos e organizados, a piscina estava limpa. Ótima recepção e localização, bem pertinho da praia e do centro, uns 10 minutos a pé.'),
        ('Davi M.', 'Um sobrado com tudo o que precisa, inclusive piscina. Lugar bem agradável e bem próximo ao mar. Estamos gostando muito e provavelmente voltaremos.'),
        ('Isabella Q.', 'Hospedagem limpa, confortável e espaçosa (é uma casa). Excelente custo-benefício, voltarei mais vezes!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=G(16), headline='4,5 no Google · 284 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='O café da manhã está incluso?', a='Sim. O café da manhã é servido todas as manhãs e está incluso na diária.'),
        dict(q='Qual o horário de check-in e check-out?', a='O check-in é a partir das 14h e o check-out até as 12h. Chegando em outro horário, avise pelo WhatsApp.'),
        dict(q='A praia fica longe?', a='Não. A Praia dos Ingleses fica a poucos minutos a pé, uns 10 minutos de caminhada.'),
        dict(q='Tem estacionamento?', a='Sim, a pousada tem estacionamento no próprio terreno.'),
        dict(q='Os apartamentos têm cozinha?', a='Os apartamentos e sobrados têm cozinha equipada com geladeira, fogão e micro-ondas. As suítes têm frigobar.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wave', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
