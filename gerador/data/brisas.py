"""Pousada Brisas da Lagoa (Ibiraquera, Imbituba) — LP no template 'stayora'.
Obs.: é o mesmo imóvel da antiga Pousada Canto da Lagoa (casa amarela de 3 andares), hoje com outra gestão."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('brisas')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Brisas+da+Lagoa+Ibiraquera+Imbituba'

T = dict(bg='#f6f4ee', alt='#e9ece4', ink='#14201d', ink2='#1b2824', muted='#56625d', dim='#b6bdb5',
         dark='#0f1a17', card='#f6f4ee', accent='#2f6f7e', line='#d9ddd3')

P = dict(
    slug='brisas', name='Pousada Brisas da Lagoa', short='Brisas da Lagoa',
    seo_title='Pousada Brisas da Lagoa | Pet friendly à beira da Lagoa de Ibiraquera',
    meta_desc='Pousada Brisas da Lagoa: suítes com sacada e rede em 4 mil m² de natureza, com píer privativo na Lagoa de Ibiraquera, fogo de chão, sinuca e pet friendly sem restrições. Pertinho da Praia do Rosa. Nota 5,0 no Google.',
    phone='(48) 99130-2610', wa_number='5548991302610', email='',
    wa_text='Olá! Vim pelo site da Pousada Brisas da Lagoa e queria consultar disponibilidade.',
    instagram='pousadabrisasdalagoa', maps_url=MAPS,
    address='Rua Eucalipto, 223 · Ibiraquera, Imbituba/SC · 88780-000', checkin='', checkout='',
    footer_tag='4 mil m² de natureza, deck na lagoa e pet friendly de verdade. Deixe-se levar pelas brisas.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Quartos', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#2f6f7e', '#c0702c', '#4f7a3a', '#7a5c3e', '#a8476b', '#3c5a7a', '#6b5b95', '#5f7f2f']


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(35, True), alt='Varanda com rede e vista para a Lagoa de Ibiraquera',
                     title='Deixe-se levar pelas brisas da lagoa',
                     sub='Suítes com sacada e rede, píer privativo na Lagoa de Ibiraquera e espaço de sobra pro seu pet.',
                     avatars=[('F', '#2f6f7e'), ('M', '#c0702c'), ('V', '#4f7a3a')],
                     proof='Nota 5,0', proof_sub='42 avaliações no Google')
    p['about'] = dict(imgs=[G(23), G(13)], alts=['Casa amarela da pousada no meio da mata', 'Deck de madeira entre as árvores'],
                      stat_num='5.0', stat_dec=1, stat_txt='5,0', stat_label='Nota no Google',
                      kicker='A pousada', title='4 mil m² de natureza, com a lagoa no quintal.',
                      text='A Brisas fica à beira da Lagoa de Ibiraquera, entre árvores, bambus e um deck que leva até a água. São suítes amplas, com entrada e sacada privativas, rede e vista pro verde ou pra lagoa. Quem recebe é a Heloísa, com a ajuda da Brisa, a anfitriã de quatro patas que apresenta a pousada pros pets que chegam.')
    p['amen_title'] = 'Tudo pra desacelerar, com o seu pet junto.'
    p['amenities'] = [('paw', 'Pet friendly sem restrição de porte'), ('lagoon', 'Píer privativo na lagoa'), ('wifi', 'Wi-Fi Starlink'),
                      ('snow', 'Ar-condicionado'), ('kitchen', 'Cozinha coletiva completa'), ('food', 'Churrasqueira'),
                      ('sun', 'Fogo de chão'), ('board', 'Stand up e caiaque'), ('leaf', 'Sacada com rede'),
                      ('car', 'Estacionamento'), ('users', 'Pousada inteira para grupos'), ('tv', 'TV e frigobar')]
    p['spaces_title'] = 'Madeira, mata e a lagoa sempre à vista.'
    p['spaces'] = [dict(img=G(12), title='Fogo de chão', text='Cadeiras em volta da fogueira, pra noite de lua cheia sobre a lagoa.'),
                   dict(img=g(95), title='Salão de sinuca', text='Mesa de sinuca e jogos de tabuleiro num galpão de madeira.'),
                   dict(img=g(98), title='Cozinha coletiva', text='Cozinha completa, com churrasqueira, sempre disponível pros hóspedes.'),
                   dict(img=G(31), title='Caminho pro píer', text='Uma passarela de madeira entre os bambus leva até o deck na lagoa.'),
                   dict(img=g(199), title='Deck externo', text='Sofás e cadeiras de madeira na varanda, de frente pro verde.')]
    p['host'] = dict(img=g(210), alt='Brisa, a cachorra da pousada, olhando a lagoa da varanda', name='Heloísa e Brisa',
                     lines=[('star', '5,0 no Google'), ('paw', 'Pet friendly de verdade'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='A Helô é muito querida e atenciosa, além de a pousada ser pet friendly de verdade.',
                     text='Palavras da Val, que se hospedou na Brisas. A Heloísa recebe cada hóspede de perto, e a Brisa faz o check-in dos pets.')
    p['plan'] = dict(kicker='Acomodações', title='Escolha o seu canto na Brisas.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Suíte Vista Lagoa', note='até 4 hóspedes', img=G(14),
                                 cells=['Vista pra lagoa', 'Sacada privativa com rede', 'Ar-condicionado', 'Frigobar', 'Banheiro privativo']),
                            dict(name='Suíte com Varanda', note='até 3 hóspedes', img=g(120),
                                 cells=['Entrada privativa', 'Varanda com rede', 'Cama de casal', 'Ventilador de teto', 'Banheiro privativo']),
                            dict(name='Suíte com Mini Cozinha', note='até 4 hóspedes', img=G(16),
                                 cells=['Mini cozinha', 'Vista pro verde', 'Ar-condicionado', 'Frigobar', 'Banheiro privativo']),
                            dict(name='Pousada Inteira', note='até 20 pessoas', img=g(76),
                                 cells=['6 quartos', 'Cozinha coletiva', 'Fogo de chão', 'Deck na lagoa', 'Sala de sinuca'])])
    p['exp'] = dict(title='Lagoa, mar e o Rosa por perto.',
                    big=dict(img=G(17, True), title='Lagoa de Ibiraquera', text='Água calma pra stand up, caiaque e kitesurf, e um pôr do sol que reflete no espelho da lagoa.'),
                    wide=dict(img=g(109), title='Praias da região', text='Praia da Luz a 3,3 km, Barra de Ibiraquera a 3,5 km e o centrinho do Rosa a 3 km.'),
                    list_title='Mais pra explorar',
                    list=[('board', 'Stand up paddle na lagoa'), ('kite', 'Kitesurf na Barra'), ('wave', 'Praia do Rosa'), ('fish', 'Pesca artesanal da tainha')],
                    small=dict(img=g(202), title='Noite de fogueira', text='Fogo de chão, céu estrelado e a lua nascendo atrás do morro.'))
    items = [
        ('Marcela B.', 'Google', 'Ficamos no chalé 6 e aproveitamos muito, desde o quarto que tem uma vista incrível pra lagoa, até o deck com acesso para ela. Levamos nosso pet de porte grande que aproveitou cada cantinho.'),
        ('Gabriela F.', 'Google', 'Estivemos um final de semana com nossos dois cachorros de grande porte e nos surpreendemos com a pousada. Lugar de muita paz e natureza maravilhosa! Nossos cães puderam aproveitar o deck da lagoa!'),
        ('Ellen F.', 'Google', 'Fomos muito bem recebidos pela Heloísa, cada cuidado em forma de detalhe. Quartos grandes, com varanda e rede. Dos quartos de cima dá pra ver a lagoa, que conta com um deck até a margem.'),
        ('Val B.', 'Google', 'Linda pousada, quarto espaçoso e lindo, vista para natureza, bem arejado, com uma varanda linda. Nos fundos há um acesso privativo à lagoa de Ibiraquera, lindíssimo!'),
        ('Amanda M.', 'Google', 'Passamos o carnaval na pousada, foram dias ótimos! Utilizamos a cozinha compartilhada, disponível sempre que precisamos. A mesa de sinuca é ótima e o deck externo é impressionante.'),
        ('Thais P.', 'Google', 'Pegamos um final de semana chuvoso, porém aproveitamos demais. O deck da lagoa é sensacional, o apto é bem aconchegante. Fomos muito bem recepcionados.'),
        ('Angelica A.', 'Google', 'Pousada maravilhosa em meio à natureza, muita paz e silêncio. Quartos grandes e confortáveis, cama nova e muito confortável. Tem um deck muito charmoso de frente para a lagoa.'),
        ('Tamiris', 'Google', 'O quarto é aconchegante e tem uma vista linda. Levamos nossos dois cachorros juntos e eles aproveitaram muito! A Heloísa e a Brisa nos recepcionaram com muito carinho!'),
    ]
    p['reviews'] = dict(title='Hóspedes (e pets) que querem voltar.', count=42, rating='5,0',
                        bars=[('Google', '5,0', 100), ('Booking', '9,8', 98), ('Airbnb', '5,0', 100)],
                        note='5,0 no Google · 42 avaliações · notas do Booking e Airbnb divulgadas pela pousada · trechos de avaliações públicas', link=MAPS,
                        headline='5,0 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('A pousada aceita pets de todos os portes?', 'Sim. A Brisas é pet friendly sem restrição de porte ou número de pets por reserva.'),
                ('Tem acesso à lagoa?', 'Sim. Uma passarela leva até o píer privativo da pousada, na beira da Lagoa de Ibiraquera.'),
                ('As praias ficam longe?', 'A Praia da Luz fica a 3,3 km, a Barra de Ibiraquera a 3,5 km e o centrinho do Rosa a 3 km.'),
                ('Dá pra fechar a pousada inteira?', 'Sim. São 6 quartos e a pousada recebe até 20 pessoas, ideal pra família, amigos e comemorações.'),
                ('Tem cozinha?', 'Sim. Há uma cozinha coletiva completa com churrasqueira, e algumas suítes têm mini cozinha.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A Heloísa confirma disponibilidade e valores com você.')]
    p['cta'] = dict(img=g(206, True), title='Reserve seu refúgio na beira da lagoa.',
                    text='Escolha as datas, chame a gente no WhatsApp e traga seu pet junto.')
    return p
