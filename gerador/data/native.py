from common import ig2, review_sources
from deco import deco, logo

TEMPLATE = 'aurelia'
U = 'nativepousada'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Native+Lagoa+da+Concei%C3%A7%C3%A3o'

T = dict(gold='#c4a067', gold2='#e2c48e', dark='#1e3a2f', darker='#14261f', cream='#f6f4ee', cream2='#ebe8de',
         sage='#3f6b56', text='#1c2420', muted='#59615c', line='#cbc5b2')

P = dict(
    slug='native', name='Native Pousada', brand='Native', place_short='Lagoa da Conceição, Floripa',
    meta_desc='Native Pousada na Lagoa da Conceição: prédio novo, piscina na cobertura, quartos com ar e frigobar, café com tapioca na hora e nota 4,8 no Google.',
    phone='(47) 99941-3033', wa_number='5547999413033', email='', site='https://linktr.ee/nativepousada', site_label='linktr.ee/nativepousada', facebook='',
    wa_text='Olá! Vim pelo site da Native Pousada e queria consultar disponibilidade.',
    instagram='nativepousada',
    address='R. Afonso Luís Borba, 567 - Lagoa da Conceição, Florianópolis - SC, 88062-040',
    footer_tag='Lagoa da Conceição, Florianópolis.',
    room_word='Quarto', rooms_label='Quartos', rooms_eyebrow='Acomodações', rooms_title='Nossos quartos',
    rooms_sub='Quartos novos, claros e espaçosos, com ar-condicionado, frigobar e arrumação todos os dias.',
    tagline='Piscina na cobertura, a Lagoa aos pés e a Rota Gastronômica a uma caminhada.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar na Lagoa.',
)


def context(I, wa):
    g = lambda i: I(ig2(U, i))[0]
    p = dict(P)
    p['hero'] = dict(img=g(91), alt='Piscina na cobertura da Native Pousada', eyebrow='Bem-vindo à Native',
                     title='Seu canto na Lagoa da Conceição',
                     sub='Pousada nova, moderna e impecável, com piscina na cobertura e a Lagoa a poucos passos.',
                     cta='Ver quartos')
    p['about'] = dict(eyebrow='Native · Lagoa da Conceição', title='Moderna, limpa e acolhedora',
                      text='A Native nasceu pra quem quer a energia da Lagoa da Conceição com conforto de verdade: ambientes modernos, ar-condicionado em todos os espaços, cozinha liberada para os hóspedes e uma equipe que trata todo mundo como família.',
                      sign='Native', role='Pousada na Lagoa',
                      imgs=[dict(src=g(i), alt='Native Pousada') for i in (111, 89, 134, 74)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Native Pousada.')
    p['rooms'] = [
        dict(name='Quarto Casal', img=g(83), badge='Café incluso', text='Cama de casal, banheiro privativo, ar-condicionado, frigobar e janela para o verde da Lagoa.',
             meta=[dict(icon='bed', text='Casal'), dict(icon='users', text='2 hóspedes'), dict(icon='snow', text='Ar')], wa=rw('Quarto Casal')),
        dict(name='Quarto Triplo', img=g(84), badge='Café incluso', text='Cama de casal e cama de solteiro, ideal para amigos ou casal com filho.',
             meta=[dict(icon='bed', text='Casal + solteiro'), dict(icon='users', text='3 hóspedes'), dict(icon='snow', text='Ar')], wa=rw('Quarto Triplo')),
        dict(name='Quarto Família', img=g(85), badge='Café incluso', text='Cama de casal e beliche no mesmo quarto, pra família toda curtir a Lagoa junto.',
             meta=[dict(icon='bed', text='Casal + beliche'), dict(icon='users', text='Família'), dict(icon='snow', text='Ar')], wa=rw('Quarto Família')),
    ]
    p['exp'] = dict(eyebrow='A experiência Native', title='Além da estadia',
                    sub='Do café com tapioca na hora ao pôr do sol na Lagoa, tudo pertinho.',
                    cards=[dict(icon='pool', title='Piscina na cobertura', kicker='Vista para a Lagoa', text='Uma piscina no alto do prédio, com deck de madeira e espreguiçadeiras para o fim de tarde.'),
                           dict(icon='coffee', title='Café da manhã', kicker='Feito na hora', text='Ovos mexidos e tapiocas preparados na hora, frutas, pães e sucos todas as manhãs.'),
                           dict(icon='lagoon', title='Lagoa da Conceição', kicker='A uma caminhada', text='Rota Gastronômica, lojas, mercado e restaurantes a pé. As principais praias ficam a cerca de 15 minutos.')])
    gal = [91, 0, 111, 89, 101, 108, 96, 110, 27, 80, 13, 92]
    p['gallery'] = dict(title='Um olhar sobre a Native', sub='Arquitetura nova, muita luz e a Lagoa logo ali.',
                        imgs=[dict(src=g(i), alt='Native Pousada') for i in gal])
    items = [
        ('Mariel S.', 'Um dos locais mais limpos, organizados, aconchegante e acolhedor que já estivemos. Absolutamente nada a reclamar, só agradecer por tanto cuidado e elogiar. Café da manhã maravilhoso, roupas de cama e banho excelentes, ar condicionado em todos os ambientes.'),
        ('Dandara M.', 'A pousada Native possui uma ótima estrutura, com ambientes modernos, de muito bom gosto e limpeza impecável. Todos os funcionários são bastante atenciosos e prestativos, o que faz diferença na experiência.'),
        ('Manuversieux', 'Tudo incrível, o atendimento excelente, equipe toda muito gentil e pronta para atender a qualquer problema ou solicitação. Estrutura moderna e tudo sempre muito limpinho. Quartos muito espaçosos e fresquinhos.'),
        ('Barbara L.', 'Fiz a reserva via WhatsApp e obtive ótimo atendimento da Marta, proprietária do local. Chegando à pousada fui surpreendida pela limpeza do local, ambiente calmo, familiar, tranquilo, bem arejado.'),
        ('Priscila F.', 'Experiência incrível. A pousada é nova, muitooooo limpa. Café da manhã simples, mas uma delícia. Todos simpáticos e cordiais.'),
        ('Claudinei L.', 'Ótima estrutura com quartos bem confortáveis e limpos, tem serviço de quarto todos os dias e um café da manhã simples mas muito bom.'),
        ('Queiroz', 'A pousada é muito aconchegante, confortável, limpinha e ótima localização. A recepção, funcionários, todos muito educados. Café da manhã delicioso. Eu amei tudo.'),
    ]
    p['reviews'] = dict(bg=g(144), headline='4,8 no Google · 187 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '')]),
                        items=[dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items])
    p['faq'] = [
        dict(q='Os quartos têm ar-condicionado?', a='Sim, ar-condicionado em todos os ambientes e frigobar nos quartos.'),
        dict(q='Como é o café da manhã?', a='Servido todas as manhãs, com ovos mexidos e tapiocas feitos na hora, frutas, pães e sucos.'),
        dict(q='Posso usar a cozinha?', a='Pode. Os hóspedes têm liberdade para usar a cozinha da pousada, seja pra esquentar algo no micro-ondas ou fazer um lanche.'),
        dict(q='Tem estacionamento?', a='Sim, a pousada tem estacionamento para os hóspedes.'),
        dict(q='O que tem por perto?', a='A Rota Gastronômica da Lagoa, lojas, farmácia e supermercado dá pra fazer a pé. As principais praias ficam a cerca de 15 minutos.'),
        dict(q='Como faço a reserva?', a='Pelo WhatsApp (47) 99941-3033 ou pelo Booking.com.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wave', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
