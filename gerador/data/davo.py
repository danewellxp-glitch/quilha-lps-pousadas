"""Pousada Da Vó (Lagoa da Conceição, Florianópolis) — LP no template 'aurelia'.
Antiga Pousada Dutra (renomeada em dez/2021, post do IG). Dona: Simone (reviews). Hospedaria simples:
parte dos quartos usa banheiro compartilhado e a cozinha é de uso dos hóspedes. Nomes dos quartos saíram das placas
nas portas (Armação, Barra da Lagoa) e da legenda "Suíte master": confirmar com a dona."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('davo')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Da+V%C3%B3+Lagoa+da+Concei%C3%A7%C3%A3o+Florian%C3%B3polis'

T = dict(gold='#d0702f', gold2='#f0a66b', dark='#24452f', darker='#16301f', cream='#f9f6ee', cream2='#eef0e2',
         sage='#3f7d5c', text='#1e2a22', muted='#5a675e', line='#d9cdb2')

P = dict(
    slug='davo', name='Pousada Da Vó', brand='Pousada da Vó', place_short='Lagoa da Conceição, Floripa',
    meta_desc='Pousada Da Vó, no centrinho da Lagoa da Conceição, em Florianópolis: quartos simples e limpos, deck com rede, cozinha para os hóspedes e a lagoa a 50 metros. Pet friendly. Nota 4,8 no Google.',
    phone='(48) 99170-3502', wa_number='5548991703502', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Da Vó e queria consultar disponibilidade.',
    instagram='pousada_davo',
    address='R. Afonso Luís Borba, 170 - Lagoa da Conceição, Florianópolis - SC, 88062-040',
    footer_tag='Clima de casa de vó, no coração da Lagoa da Conceição.',
    room_word='Quarto', rooms_label='Quartos', rooms_eyebrow='Quartos da Vó', rooms_title='Onde você vai descansar',
    rooms_sub='Quartos simples, arejados e muito limpos, com roupa de cama e banho. Conte quantas pessoas vêm e a gente indica o melhor.',
    tagline='A 50 metros da Lagoa, perto de bares, restaurantes, mercado e da Avenida das Rendeiras.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar à Lagoa.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=I('/home/claude/fotos/davo/fix/ig38.jpg', big=True)[0], alt='Canoa de madeira nas águas calmas da Lagoa da Conceição', eyebrow='Bem-vindo à Pousada da Vó',
                     title='Seu cantinho na Lagoa da Conceição',
                     sub='Quartos limpos, deck com rede e clima de casa de família, a 50 metros da Lagoa e no meio do centrinho.',
                     cta='Conhecer os quartos')
    p['about'] = dict(eyebrow='Pousada da Vó · Lagoa', title='Recebidos como em casa de vó',
                      text='A Pousada da Vó é uma hospedaria simples e acolhedora no centrinho da Lagoa da Conceição. Tem deck de madeira com rede, jardim, cozinha equipada para os hóspedes e Wi-Fi que pega bem. Quem recebe é a Simone, que, segundo os hóspedes, está sempre disposta a ajudar no que for preciso.',
                      sign='Simone', role='Anfitriã',
                      imgs=[dict(src=s, alt='Pousada da Vó') for s in (g(0), g(80), G(25), g(81))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada da Vó.')
    p['rooms'] = [
        dict(name='Suíte Master', img=g(16), badge='Com banheiro',
             text='Suíte com cama de casal, ar-condicionado, TV e banheiro privativo.',
             meta=[dict(icon='bath', text='Banheiro privativo'), dict(icon='snow', text='Ar-condicionado'), dict(icon='tv', text='TV')],
             wa=rw('Suíte Master')),
        dict(name='Quarto Barra da Lagoa', img=g(8), badge='Casal',
             text='Quarto aconchegante com cama de casal e criado-mudo, pertinho do banheiro e da cozinha dos hóspedes.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='wifi', text='Wi-Fi'), dict(icon='kitchen', text='Cozinha compartilhada')],
             wa=rw('Quarto Barra da Lagoa')),
        dict(name='Quarto Armação', img=g(45), badge='Simples e arejado',
             text='Quarto simples e bem arejado, com roupa de cama e banho, pra quem quer economia sem abrir mão da limpeza.',
             meta=[dict(icon='bed', text='Roupa de cama'), dict(icon='leaf', text='Arejado'), dict(icon='wifi', text='Wi-Fi')],
             wa=rw('Quarto Armação')),
    ]
    p['exp'] = dict(eyebrow='A experiência da Vó', title='Os dias na Lagoa',
                    sub='Lagoa de manhã, praia à tarde e o centrinho à noite, tudo a pé ou pertinho.',
                    cards=[dict(icon='lagoon', title='Lagoa a 50 metros', kicker='Lagoa da Conceição', text='Stand up, vela, caiaque ou só sentar no trapiche e ver o movimento dos barcos.'),
                           dict(icon='food', title='Centrinho e Rendeiras', kicker='Gastronomia', text='Bares, restaurantes, mercado e farmácia ao lado, e a Avenida das Rendeiras a poucos metros.'),
                           dict(icon='wave', title='Praias perto', kicker='Joaquina, Mole e Barra', text='Joaquina, Praia Mole, Galheta e Barra da Lagoa ficam a poucos minutos.'),
                           dict(icon='paw', title='Pet friendly', kicker='Na pousada', text='A pousada aceita animais. Avise na reserva pra combinar tudo.')])
    gal = [('g', 0), ('g', 14), ('G', 17), ('g', 80), ('g', 23), ('g', 2), ('g', 14), ('g', 81), ('g', 57), ('g', 79), ('g', 92), ('g', 87)]
    p['gallery'] = dict(title='Um olhar sobre a Vó', sub='O deck com rede, o jardim e a Lagoa da Conceição logo ali.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada da Vó e Lagoa da Conceição') for k, i in gal])
    google = [
        ('Gisele N.', 'Pousada super aconchegante, a cozinha tem tudo que se precisa. Super bem localizada, fácil acesso a várias praias. A Simone, proprietária, pessoa maravilhosa, sempre disposta a auxiliar em tudo.'),
        ('Karen R.', 'Ótimo local, atendimento top, clima familiar. Super indico para quem quer estar num local tranquilo, seguro e familiar, no coração da Lagoa da Conceição.'),
        ('Celia M.', 'Ótima pousada, tudo muito perfeito, proprietários simpáticos e muito queridos. Tudo muito limpinho, além de estar super bem localizada no centrinho da Lagoa.'),
        ('Juliana K.', 'Localização excelente, anfitriões muito queridos e prestativos, quartos e banheiros extremamente limpos, recomendo!'),
        ('Andre S.', 'Bem localizada, a 50 metros você está na beira da Lagoa, ótimo atendimento. Bem arejado e bem limpo.'),
        ('Stella M.', 'Fiquei simplesmente apaixonada pelo atendimento. Pessoas maravilhosas, atenciosas. Super recomendo, sem falar que é muito limpinha e a ducha é deliciosa.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=I('/home/claude/fotos/davo/fix/ig39.jpg')[0], headline='4,8 no Google · 30 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Qual o horário de check-in e check-out?', a='O check-in é a partir das 14h e o check-out até as 12h. Chegando em outro horário, avise pelo WhatsApp.'),
        dict(q='Os quartos têm banheiro?', a='A Suíte Master tem banheiro privativo. Os outros quartos usam banheiros compartilhados, bem pertinho e sempre limpos.'),
        dict(q='Posso cozinhar?', a='Sim. A cozinha é de uso dos hóspedes e tem tudo que você precisa.'),
        dict(q='Tem café da manhã?', a='O café da manhã é cobrado à parte. Pergunte os detalhes pelo WhatsApp.'),
        dict(q='Aceita pets?', a='Sim, a pousada aceita animais. Avise na hora da reserva.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wave', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
