"""Pousada Casa De Mar (R. Heitor Bitencourt, 90, Canasvieiras, Florianópolis) — LP no template 'aurelia'.
Fotos: Instagram @pousada_casademar (ig) + Google Maps 2ª passada (gm2). Sócios Juan Leonardo Alvarez Albero / Juan Pablo
Vacatello; recepção com o Hermes. Telefones: (48) 99615-2544 (WhatsApp, usado aqui) ou (11) 4393-0281 (Maps)."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('casademar')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Casa+De+Mar+R.+Heitor+Bitencourt+90+Canasvieiras'

T = dict(gold='#b5643c', gold2='#e9a57c', dark='#1f3d4a', darker='#132a33', cream='#fbf8f3', cream2='#f0e6da',
         sage='#3f8fa0', text='#1d2528', muted='#5d686b', line='#e2cdb6')

P = dict(
    slug='casademar', name='Pousada Casa De Mar', brand='Casa De Mar', place_short='Canasvieiras, Norte da Ilha',
    meta_desc='Pousada Casa De Mar em Canasvieiras, Florianópolis: suítes climatizadas, piscina com deck, café da manhã caseiro e a praia a 3 minutos a pé.',
    phone='(48) 99615-2544', wa_number='5548996152544', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Casa De Mar e queria consultar disponibilidade.',
    instagram='pousada_casademar',
    address='R. Heitor Bitencourt, 90 - Canasvieiras, Florianópolis - SC, 88054-450',
    footer_tag='Uma casa aconchegante numa rua arborizada de Canasvieiras, a 3 minutos da praia.',
    room_word='Suíte', rooms_label='Suítes', rooms_eyebrow='Suítes da Casa De Mar', rooms_title='Onde você vai descansar',
    rooms_sub='Suítes climatizadas, com TV, banheiro privativo, cama confortável e café da manhã incluso.',
    tagline='Uma casa de praia em Canasvieiras, com piscina e a areia a 3 minutos a pé.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar a Canasvieiras.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(5, True), alt='Piscina com deck e a casa da Pousada Casa De Mar', eyebrow='Bem-vindo à Casa De Mar',
                     title='Sua casa de praia em Canasvieiras',
                     sub='Suítes climatizadas, piscina com deck e café da manhã caprichado, numa rua tranquila a 3 minutos a pé do mar.',
                     cta='Conhecer as suítes')
    p['about'] = dict(eyebrow='Casa De Mar · Canasvieiras', title='Pequena, aconchegante e pertinho do mar',
                      text='A Casa De Mar é uma pousada intimista numa rua arborizada de Canasvieiras. São poucas suítes, todas com ar-condicionado e TV, em volta de uma piscina com deck de madeira, varanda e jardim. Tem mercado na quadra, bares e restaurantes por perto e a praia a uns 3 minutos de caminhada. Na recepção, o Hermes e a equipe recebem cada hóspede com as melhores dicas da Ilha.',
                      sign='Juan e equipe', role='Anfitriões',
                      imgs=[dict(src=s, alt='Pousada Casa De Mar') for s in (G(54), g(12), g(22), g(7))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar a {n} na Casa De Mar.')
    p['rooms'] = [
        dict(name='Suíte Casal', img=g(8), badge='Até 2 hóspedes',
             text='Cama de casal, ar-condicionado, TV, roupa de cama caprichada e banheiro privativo com chuveiro forte.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Ar-condicionado'), dict(icon='coffee', text='Café incluso')],
             wa=rw('Suíte Casal')),
        dict(name='Suíte com Varanda', img=g(5), badge='Até 3 hóspedes',
             text='Teto de madeira, cama de casal e de solteiro e porta pra varanda, com luz natural e vista das árvores.',
             meta=[dict(icon='sun', text='Varanda'), dict(icon='users', text='Até 3 pessoas'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Suíte com Varanda')),
        dict(name='Suíte Família', img=g(9), badge='Até 4 hóspedes',
             text='Cama de casal e camas de solteiro, TV e ar-condicionado. Boa pra famílias e grupos de amigos.',
             meta=[dict(icon='users', text='Até 4 pessoas'), dict(icon='tv', text='TV'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Suíte Família')),
    ]
    p['exp'] = dict(eyebrow='A experiência Casa De Mar', title='Os dias em Canasvieiras',
                    sub='Mar calmo de manhã, piscina à tarde e o agito do centrinho à noite.',
                    cards=[dict(icon='wave', title='Praia de Canasvieiras', kicker='A 3 min a pé', text='Mar calmo e morno, ótimo pra crianças, com passeios de escuna saindo da praia.'),
                           dict(icon='pool', title='Piscina com deck', kicker='Na pousada', text='Deck de madeira, espreguiçadeiras e mesa pra tomar um chimarrão ao sol.'),
                           dict(icon='coffee', title='Café da manhã', kicker='Incluso', text='Pães, frutas, ovos, bolo e suco, servido todas as manhãs.'),
                           dict(icon='pin', title='Tudo por perto', kicker='Localização', text='Mercados na quadra e bares e restaurantes a poucos passos, numa rua arborizada e tranquila.')])
    gal = [('G', 37), ('g', 20), ('G', 17), ('g', 15), ('G', 28), ('g', 3), ('G', 36), ('g', 21), ('G', 52), ('g', 14), ('G', 55), ('g', 4)]
    p['gallery'] = dict(title='Um olhar sobre a Casa De Mar', sub='A piscina, as suítes, o café e o mar de Canasvieiras.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Casa De Mar') for k, i in gal])
    google = [
        ('Ana Luísa R.', 'Uma experiência aconchegante e cheia de acolhimento! O Hermes é um ótimo anfitrião, faz a gente se sentir muito bem recebido, além de dar ótimas dicas sobre o que fazer na região.'),
        ('Camilla N.', 'Ambiente super aconchegante, ar-condicionado ótimo, banheiro e chuveiro excelentes e um café da manhã delicioso. A praia fica a apenas 3 minutos a pé.'),
        ('Flávia', 'Fica super próxima da praia, em rua arborizada e tranquila, com supermercados a uma quadra. Tudo bem novinho, café da manhã muito gostoso e pessoal super simpático.'),
        ('Rafael Z.', 'O quarto é maravilhoso, muito limpo e aconchegante. O ar-condicionado funciona perfeitamente e o café é ótimo. Voltarei muito em breve.'),
        ('Matheus N.', 'Lugar fantástico, bem localizado, café fenomenal, tudo climatizado. Os funcionários parecem sempre estar querendo fazer algo a mais. Super recomendo.'),
        ('Taise', 'A pousada é excelente e com ótimo atendimento! Pertinho da praia, de mercado e restaurantes. Ideal para quem busca tranquilidade.'),
        ('Daniela S.', 'Fomos bem recepcionados, bons quartos com TV e ar-condicionado, piscina, varanda com cadeiras, café da manhã simples porém muito gostoso. Bom custo-benefício.'),
        ('Augusto C.', 'Hospedagem acolhedora e atendimento excelente do gerente Juan e de toda a equipe.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=G(36), headline='4,5 no Google · 232 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='O café da manhã está incluso?', a='Sim. O café da manhã está incluso na diária e é servido todas as manhãs.'),
        dict(q='Qual o horário de check-in e check-out?', a='O check-in é a partir das 14h e o check-out até as 10h. Chegando em outro horário, avise pelo WhatsApp.'),
        dict(q='A praia fica longe?', a='Não. A Praia de Canasvieiras fica a cerca de 3 minutos a pé.'),
        dict(q='Os quartos têm ar-condicionado?', a='Sim. Todas as suítes têm ar-condicionado, TV e banheiro privativo.'),
        dict(q='Tem estacionamento?', a='Sim, a pousada tem estacionamento para hóspedes.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('anchor', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
