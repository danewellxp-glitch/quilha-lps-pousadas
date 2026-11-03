from common import ig2, review_sources
from deco import deco, logo

TEMPLATE = 'aurelia'
U = 'pousadatalisma'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Talism%C3%A3+Porto+da+Lagoa+Florian%C3%B3polis'

T = dict(gold='#cf8f55', gold2='#f2b57a', dark='#143247', darker='#0d2232', cream='#f4f6f6', cream2='#e6eef0',
         sage='#2a7896', text='#1a2730', muted='#55636c', line='#bfcfd4')

P = dict(
    slug='talisma', name='Pousada Talismã', brand='Talismã', place_short='Porto da Lagoa, Floripa',
    meta_desc='Pousada Talismã no Porto da Lagoa, Florianópolis: piscina, café da manhã na cesta, quartos com ar e micro-ondas, perto da Lagoa e do Campeche.',
    phone='(48) 98838-5880', wa_number='5548988385880', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Talismã e queria consultar disponibilidade.',
    instagram='pousadatalisma',
    address='R. Ver. Osni Ortiga, 2720 - Porto da Lagoa, Florianópolis - SC, 88062-450',
    footer_tag='Conforto e tranquilidade perto das praias mais bonitas de Floripa.',
    room_word='Quarto', rooms_label='Acomodações', rooms_eyebrow='Acomodações', rooms_title='Quartos e apartamentos',
    rooms_sub='Quartos limpinhos, com ar-condicionado, frigobar, micro-ondas e TV por assinatura. Tem opção com cozinha completa.',
    tagline='Piscina, café da manhã na cesta e a Lagoa da Conceição a poucos minutos.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar no Porto da Lagoa.',
)


def context(I, wa):
    g = lambda i: I(ig2(U, i))[0]
    p = dict(P)
    p['hero'] = dict(img=g(27), alt='Piscina da Pousada Talismã', eyebrow='Bem-vindo à Talismã',
                     title='Viva bons momentos em Floripa',
                     sub='Pousada familiar no Porto da Lagoa, entre a Lagoa da Conceição e as praias do sul da Ilha.',
                     cta='Ver acomodações')
    p['about'] = dict(eyebrow='Pousada Talismã · Porto da Lagoa', title='Conforto com jeito de casa',
                      text='Uma pousada de família, com piscina no meio do jardim, flores por todo lado e estacionamento amplo com portão automático. Daqui você chega fácil na Lagoa da Conceição, no Campeche e em todas as praias do sul da Ilha.',
                      sign='Talismã', role='Pousada de família',
                      imgs=[dict(src=g(i), alt='Pousada Talismã') for i in (17, 48, 72, 15)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada Talismã.')
    p['rooms'] = [
        dict(name='Quarto Casal', img=g(21), badge='Ar-condicionado', text='Cama de casal, banheiro privativo, frigobar, micro-ondas e TV por assinatura.',
             meta=[dict(icon='bed', text='Casal'), dict(icon='users', text='2 hóspedes'), dict(icon='snow', text='Ar')], wa=rw('Quarto Casal')),
        dict(name='Quarto Família', img=g(29), badge='Ar-condicionado', text='Camas extras para quem vem com as crianças. Espaço, silêncio e limpeza diária.',
             meta=[dict(icon='bed', text='Casal + solteiro'), dict(icon='users', text='Família'), dict(icon='tv', text='TV a cabo')], wa=rw('Quarto Família')),
        dict(name='Apartamento com Cozinha', img=g(30), badge='Cozinha completa', text='Sala, cozinha equipada e quarto separado, para estadias mais longas na Ilha.',
             meta=[dict(icon='kitchen', text='Cozinha'), dict(icon='users', text='Família'), dict(icon='snow', text='Ar')], wa=rw('Apartamento com Cozinha')),
    ]
    p['exp'] = dict(eyebrow='A experiência Talismã', title='Além da estadia',
                    sub='Piscina pra relaxar, café caprichado e as praias mais bonitas da Ilha por perto.',
                    cards=[dict(icon='pool', title='Piscina e jardim', kicker='Pra família toda', text='Piscina cercada de flores e palmeiras, com área externa e churrasqueira.'),
                           dict(icon='coffee', title='Café na cesta', kicker='Feito com carinho', text='Cesta montada com frutas, bolo, pães e sucos, entregue com todo o capricho.'),
                           dict(icon='lagoon', title='Lagoa e praias', kicker='Tudo pertinho', text='Lagoa da Conceição, Campeche e Joaquina a poucos minutos de carro. Mercado e padaria no bairro.')])
    gal = [27, 5, 47, 21, 71, 62, 16, 53, 86, 9, 34, 40]
    p['gallery'] = dict(title='Um olhar sobre a Talismã', sub='Piscina, jardim, café e o pôr do sol da Lagoa.',
                        imgs=[dict(src=g(i), alt='Pousada Talismã') for i in gal])
    items = [
        ('Giovanna P.', 'O lugar é bonito e extremamente tranquilo, possui uma ótima piscina, flores, área externa com churrasqueira e a limpeza dos quartos é frequente e satisfatória. (…) o café da manhã é servido em uma cesta, com tudo delicioso e com muito capricho.'),
        ('Simone M.', 'Pousada bem localizada, extremamente limpa, completa, wi fi, ar condicionado, silenciosa, com estacionamento, próxima a super, praias, lagoa. Uma piscina maravilhosa!'),
        ('Bruna T.', 'Fomos super bem recepcionados, Diogo nos esperou na madrugada, voltaremos com certeza, nosso novo lugar preferido. Muito capricho o AP, ótima localização e ambiente familiar.'),
        ('Alexandre B.', 'Pousada super aconchegante, pousada familiar com excelente atendimento, todos da família muito atenciosos, a limpeza e organização sem reclamações, café da manhã preparado com muito carinho, tudo fresquinho.'),
        ('Rafael R.', 'Localizada em um ponto estratégico da ilha, bem próxima a parte sul da Lagoa da Conceição, permite acesso a todas as praias com facilidade (especialmente a praia de Campeche).'),
        ('Raquel F.', 'Pousada aconchegante, recepção Sr. Avelino e família muito atenciosos, educados... acomodação confortável, café da manhã ótimo, saí de lá querendo voltar.'),
        ('Sabrina R.', 'Maravilhoso lugar, dono foi super hospitaleiro, lugar limpo perto de muitos locais mercado praia farmácia restaurante etc... ganharam uma cliente 👏'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    rv.insert(2, dict(key='booking', text='Ótimas acomodações, ótima cama, banheiro limpo, quartos bem arejados e ótimo serviço de quarto, além disso os funcionários são excelentes e o café da manhã é perfeito.',
                      author='Hóspede verificado', source='Booking.com', stars=5))
    p['reviews'] = dict(bg=g(34), headline='4,5 no Google · 191 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', ''), ('booking', 'Booking.com', '', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='O café da manhã está incluso?', a='Na temporada o café é servido numa cesta caprichada. Fora da temporada, confirme pelo WhatsApp: tem padaria e mercado pertinho da pousada.'),
        dict(q='Os quartos têm ar-condicionado?', a='Sim. Os quartos têm ar-condicionado, frigobar, micro-ondas, louça e TV por assinatura.'),
        dict(q='Tem estacionamento?', a='Sim, estacionamento amplo dentro da pousada, com portão automático. Você recebe o controle na chegada.'),
        dict(q='Posso levar meu pet?', a='A pousada aceita animais. Avise na reserva.'),
        dict(q='Chego de madrugada, tem problema?', a='Combine o horário pelo WhatsApp que a família recebe você.'),
        dict(q='A pousada fica perto da praia?', a='Fica no Porto da Lagoa, a poucos minutos de carro da Lagoa da Conceição, do Campeche e da Joaquina.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wave', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
