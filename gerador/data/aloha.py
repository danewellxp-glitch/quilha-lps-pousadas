from common import ig, review_sources
from deco import deco, logo

TEMPLATE = 'aurelia'
U = 'pousadaalohapraiadorosa'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+ALOHA+BEACH+HOUSE+Praia+do+Rosa'

T = dict(gold='#c0915a', gold2='#e2b67a', dark='#1d2b26', darker='#151a17', cream='#f6f2ea', cream2='#ede5d8',
         sage='#5f7a6c', text='#1f2421', muted='#5b605a', line='#cdbfa9')

P = dict(
    slug='aloha', name='Pousada Aloha Beach House', brand='Aloha', place_short='Praia do Rosa, SC',
    meta_desc='Pousada Aloha Beach House na Praia do Rosa: piscina com deck, hidromassagem, café da manhã na sua suíte e nota 4,7 no Google.',
    phone='(48) 99180-1910', wa_number='5548991801910', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Aloha Beach House e queria consultar disponibilidade.',
    instagram='pousadaalohapraiadorosa',
    address='Av. Porto Novo, 860 - Praia do Rosa, Imbituba - SC, 88780-000', footer_tag='Praia do Rosa, Santa Catarina.',
    room_word='Suíte', rooms_label='Suítes', rooms_eyebrow='Suítes da Aloha', rooms_title='Nossas suítes',
    rooms_sub='Suítes completas, com ar-condicionado e roupa de cama de hotel, cercadas pelo jardim tropical da casa.',
    tagline='Piscina, hidromassagem e o centrinho do Rosa a uma caminhada.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar na Praia do Rosa.',
)


def context(I, wa):
    g = lambda i: I(ig(U, i))[0]
    p = dict(P)
    p['hero'] = dict(img=g(27), alt='Lounge com hidromassagem da Aloha Beach House', eyebrow='Bem-vindo à Aloha',
                     title='Seu refúgio na Praia do Rosa',
                     sub='Uma beach house cercada de palmeiras, com piscina, hidromassagem e café da manhã entregue na sua suíte.',
                     cta='Conhecer as suítes')
    p['about'] = dict(eyebrow='Aloha Beach House · Praia do Rosa', title='Mais que um lugar pra dormir',
                      text='Escadas de pedra, muito verde, deck de madeira em volta da piscina e um silêncio que deixa descansar de verdade. Na Aloha você é recebido pelo anfitrião, ganha as melhores dicas do Rosa e começa o dia com uma cesta de café caprichada.',
                      sign='Aloha', role='Beach House · desde a primeira onda',
                      imgs=[dict(src=g(i), alt='Aloha Beach House') for i in (73, 111, 18, 14)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar a {n} na Aloha Beach House.')
    p['rooms'] = [
        dict(name='Suíte Casal', img=g(13), badge='Café incluso', text='Cama de casal, banheiro privativo com chuveiro quentinho e enxoval de hotel.',
             meta=[dict(icon='bed', text='Cama casal'), dict(icon='users', text='2 hóspedes'), dict(icon='snow', text='Ar-condicionado')], wa=rw('Suíte Casal')),
        dict(name='Suíte com Cozinha', img=g(0), badge='Café incluso', text='Geladeira, pia, fogão e utensílios para ter a liberdade de uma casa de praia.',
             meta=[dict(icon='kitchen', text='Cozinha'), dict(icon='users', text='Casal ou família'), dict(icon='snow', text='Ar-condicionado')], wa=rw('Suíte com Cozinha')),
        dict(name='Suíte Família', img=g(10), badge='Café incluso', text='Para quem vem com as crianças ou com a turma de amigos curtir o Rosa junto.',
             meta=[dict(icon='bed', text='Casal + solteiro'), dict(icon='users', text='Família'), dict(icon='paw', text='Pet friendly')], wa=rw('Suíte Família')),
    ]
    p['exp'] = dict(eyebrow='A experiência Aloha', title='Além da estadia',
                    sub='Da piscina ao centrinho do Rosa, cada detalhe é pensado para você aproveitar sem pressa.',
                    cards=[dict(icon='pool', title='Piscina & Hidromassagem', kicker='Sem taxa extra', text='Piscina com deck de madeira, espreguiçadeiras, redes e hidromassagem liberada para os hóspedes.'),
                           dict(icon='coffee', title='Café na sua suíte', kicker='Todas as manhãs', text='Cesta com frutas, pães, ovos mexidos, pão de queijo e bolo caseiro, entregue na porta do quarto.'),
                           dict(icon='wave', title='Praia do Rosa', kicker='Dicas do anfitrião', text='Centrinho a pé, praia a uma caminhada e as melhores dicas de passeio, surf, trilha e restaurante.')])
    gal = [27, 18, 85, 109, 23, 36, 83, 72, 79, 111, 14, 57, 9, 20]
    p['gallery'] = dict(title='Um olhar sobre a Aloha', sub='Deck, piscina, jardim e o mar da Praia do Rosa logo ali.',
                        imgs=[dict(src=g(i), alt='Aloha Beach House') for i in gal])
    items = [
        ('Alessandra C.', 'Se forem vir pro Rosa, a melhor pousada é essa. Lugar rodeado de natureza e o mais importante: silenciosa.'),
        ('Claiton C.', 'E a cereja do bolo é o café da manhã servido na porta do quarto com produtos mineiros. Recomendo totalmente.'),
        ('Tatiana O.', 'Excelente atendimento, o anfitrião é super cordial, passou várias dicas de passeio e onde comer. (…) Agora o café da manhã ele simplesmente arrasa!'),
        ('Camila F.', 'Com certeza foi a melhor estadia onde já estivemos. (…) Não voltaremos como clientes e sim como amigos que tiveram o melhor que o Rosa pode oferecer.'),
        ('Isabelli N.', 'Ótima localização, café da manhã impecável, todos da pousada muito queridos e solícitos (…). Nota 10, nada a reclamar!'),
        ('Amanda C.', 'Achei linda a pousada, aconchegante e com estilo rústico! Café da manhã cheio de detalhes e delicioso!'),
        ('Daniel V.', 'Lugar incrível. Não vejo a hora de voltar. Tudo impecável. Meu pet foi super bem recebido.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    rv.insert(3, dict(key='tripadvisor', text='A estadia foi excelente! A Carla e o André são muito queridos e de uma atenção ímpar aos pequenos detalhes.',
                      author='milkalr', source='Tripadvisor', stars=5))
    p['reviews'] = dict(bg=g(86), headline='4,7 no Google · 259 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,7', ''), ('tripadvisor', 'Tripadvisor', '4,2', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Qual o horário de check-in e check-out?', a='Check-in a partir das 14h e check-out até as 11h. Se precisar de outro horário, fale com a gente pelo WhatsApp.'),
        dict(q='O café da manhã está incluso?', a='Sim. Todas as manhãs uma cesta caprichada é entregue na sua suíte, com frutas, pães, bolos e quitutes quentinhos.'),
        dict(q='A hidromassagem é cobrada à parte?', a='Não. Piscina e hidromassagem ficam liberadas para os hóspedes, sem taxa extra.'),
        dict(q='A pousada aceita pets?', a='Seu pet é bem-vindo. Avise na reserva para prepararmos tudo.'),
        dict(q='Tem estacionamento?', a='Sim, a pousada tem estacionamento para os hóspedes.'),
        dict(q='Fica longe da praia?', a='A Aloha fica na Av. Porto Novo, perto do centrinho do Rosa, que dá pra fazer a pé, e a uma caminhada da praia.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('hibiscus', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
