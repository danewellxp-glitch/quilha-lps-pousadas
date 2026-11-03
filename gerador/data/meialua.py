"""Pousada Meia Lua (Praia do Rosa, Imbituba) — site institucional no template 'casa' (home + reservas)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Meia+Lua+Praia+do+Rosa+Imbituba'
F = Fotos('meialua')

T = dict(paper='#f8f4ec', cream='#ece2cf', espresso='#2f2418', honey='#c4692b', olive='#3f6b45',
         muted='#6b5e50', rooms_bg='#efe6d6', deep='#1f3326', gold='#e8b866')

P = dict(
    slug='meialua', name='Pousada Meia Lua', short='Meia Lua',
    seo_title='Pousada Meia Lua | Chalés e suítes no centrinho da Praia do Rosa',
    logo_small='Pousada', logo_main='Meia Lua', logo_img='',
    meta_desc='Pousada Meia Lua, na Praia do Rosa: chalés de madeira e suítes em meio a um jardim tropical, piscina, área verde, pet friendly e o centrinho do Rosa a uma caminhada. Nota 4,5 no Google.',
    phone='(48) 99998-0268', wa_number='5548999980268', email='',
    wa_text='Olá! Vim pelo site da Pousada Meia Lua e queria consultar disponibilidade.',
    instagram='meialuapousadaoficial',
    address='R. John Lennon, s/n · Praia do Rosa, Imbituba/SC · CEP 88780-000',
    place_line='Praia do Rosa · Imbituba · SC',
    footer_tag='Chalés, jardim e piscina pertinho do centrinho do Rosa.', checkin='14h', checkout='11h',
    rooms_label='Acomodações', lang_gate=False,
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(125, True), video='', eyebrow='Praia do Rosa · Imbituba',
                     title='Meia Lua,<br>o seu canto no Rosa',
                     sub='Chalés de madeira e suítes num jardim tropical, com piscina e o centrinho a uma caminhada.')
    p['intro'] = dict(kicker='A pousada', title='Madeira, jardim e o Rosa logo ali',
                      text='A Meia Lua fica numa área verde ampla, cheia de palmeiras, flores e caminhos de pedra, a poucos passos do centrinho da Praia do Rosa. São chalés de madeira e suítes de tijolinho, com varanda e rede, em volta de uma piscina. Quem recebe são a Adriana e o Márcio, que estão sempre por perto pra ajudar no que for preciso.',
                      badge='Aberta o ano inteiro')
    car = [('g', 4), ('g', 2), ('g', 5), ('g', 110), ('g', 72), ('g', 119), ('g', 18), ('g', 61), ('g', 113), ('g', 145)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Meia Lua') for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Uma pousada pra viver o Rosa',
                           text='Da rede na varanda à piscina no meio do jardim, tudo foi pensado pra quem quer descansar perto do mar.')
    cards = [
        ('g', 11, 'Chalés de madeira', 'Chalés com varanda, rede e cozinha, cercados de verde. Cada um com nome e jeito próprio.', 'Ver acomodações', 'reservas.html'),
        ('g', 110, 'Suítes aconchegantes', 'Suítes de tijolinho com ar-condicionado, frigobar e janelas pro jardim.', 'Ver suítes', 'reservas.html'),
        ('g', 122, 'Piscina', 'Piscina cercada de palmeiras e espreguiçadeiras, pra voltar da praia e cair na água.', 'Conhecer', '#pousada'),
        ('g', 119, 'Varanda com rede', 'A rede na varanda é o lugar oficial do fim de tarde na Meia Lua.', 'Conhecer', '#pousada'),
        ('g', 16, 'Jardim tropical', 'Palmeiras, flores e caminhos de pedra numa área verde ampla.', 'Conhecer', '#pousada'),
        ('g', 17, 'Pet friendly', 'Seu pet é bem-vindo. Quem recebe junto é o Aslan, o labrador da casa.', 'Consultar', '#contato'),
        ('G', 21, 'Sinuca e pebolim', 'Área de jogos coberta pra noite em família ou com a turma.', 'Conhecer', '#pousada'),
        ('g', 99, 'Lareira no inverno', 'Tem chalé com lareira, pra quem vem ver as baleias na temporada de inverno.', 'Consultar', '#contato'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=g(161, True), nav='A região', kicker='Meia Lua',
                     title='O centrinho a pé,<br>a praia logo ali.',
                     text='A pousada fica perto da feirinha, dos bares, restaurantes e mercados do Rosa. Dá pra fazer quase tudo a pé, inclusive as trilhas até a praia.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(7), alt='Costão e mar azul da Praia do Rosa', badge='Praia do Rosa',
                    kicker='Experiências', title='Trilhas, mar e baleias',
                    text='A Praia do Rosa é uma das baías mais bonitas do Brasil: mar de surf, dunas, lagoas e trilhas entre o verde e o costão. No inverno, as baleias-francas aparecem bem pertinho da areia.',
                    items=['Centrinho do Rosa, feirinha, bares e restaurantes', 'Trilhas para a Praia do Rosa e o Rosa Norte',
                           'Dunas e Lagoa de Ibiraquera', 'Observação de baleias-francas (temporada de inverno)'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Isabella A.', 'O lugar é perfeito, além de ser super bem posicionado perto da feirinha e da praia. O quarto é lindo e aconchegante. A pousada toda em si é nota 10, pretendo voltar muitas vezes!'),
        ('Evellyn B.', 'Pousada muito aconchegante, tranquila e extremamente organizada e limpa. A recepção é excelente, os donos são muito receptivos e queridos. A localização é ótima, perto de tudo.'),
        ('Carolina B.', 'A pousada é linda e bem aconchegante! Fomos muito bem recepcionados e estava pertinho de tudo, podendo fazer a pé praticamente todas as trilhas e o centrinho.'),
        ('Cristiane S.', 'Fui recebida com extrema cordialidade e simpatia, fazendo-me sentir em casa durante os 20 dias que estive hospedada na cabana Bangalô. Um refúgio encantador, cercado de beleza natural e tranquilidade.'),
        ('Bruna E.', 'Minha estadia na Pousada Meia Lua foi simplesmente excelente! Desde antes da chegada, fomos muito bem recebidos com muita simpatia e cordialidade pela Adriana.'),
        ('Rivana B.', 'Uma delícia de lugar, tudo maravilhoso, recepção impecável, quartos aconchegantes, limpinhos e tudo isso bem pertinho do centro. Adoramos e super recomendamos.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,5 no Google · 52 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 52 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=g(84, True), title='Bora pro Rosa?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=g(45, True), kicker='Reserve sua estadia', title='Alguns dias no Rosa.<br>Entre a rede e a piscina.',
        rooms_kicker='Nossas acomodações', unit_word='Acomodação', prices=False,
        included=['Ar-condicionado', 'Wi-Fi gratuito', 'Estacionamento interno', 'Piscina', 'Área verde e jardim', 'Pet friendly'],
        rooms=[
            dict(name='Suíte com Vista para a Piscina', guests=2, price='',
                 detail='Suíte de tijolinho com cama de casal, ar-condicionado e frigobar, de frente pra piscina.',
                 imgs=[g(110), g(164), g(94), g(166), G(3)]),
            dict(name='Suíte com Vista do Jardim', guests=3, price='',
                 detail='Cama de casal e cama de solteiro, ar-condicionado e janelas pro jardim tropical.',
                 imgs=[g(116), g(118), g(12), g(59), G(7)]),
            dict(name='Bangalô Deluxe', guests=3, price='',
                 detail='Bangalô de madeira com cama de casal grande e cama de solteiro, cercado de verde.',
                 imgs=[g(114), g(6), g(38), G(6), G(43)]),
            dict(name='Chalé', guests=5, price='',
                 detail='Chalé de madeira com mezanino, cozinha e varanda com rede. Cama de casal, solteiro e beliche.',
                 imgs=[g(111), g(113), g(120), g(112), G(9)]),
            dict(name='Casa de 2 Quartos', guests=6, price='',
                 detail='Dois quartos, sala e cozinha completa, pra família ou turma de amigos.',
                 imgs=[g(179), g(180), g(181), G(27), G(32)]),
        ])
    return p
