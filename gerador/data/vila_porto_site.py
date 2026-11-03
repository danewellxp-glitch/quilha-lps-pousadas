"""Pousada Vila Porto da Lagoa — site institucional no template 'casa' (home + reservas), fotos tratadas."""
from common import review_sources
from l3 import pic

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Vila+Porto+da+Lagoa'

T = dict(paper='#fbf7f0', cream='#f5e1e4', espresso='#1f3a5f', honey='#c98f12', olive='#3e7cb1',
         muted='#5f6672', rooms_bg='#f3eee6', deep='#152842', gold='#f4c95d')

P = dict(
    slug='vila_porto_site', name='Pousada Vila Porto da Lagoa', short='Vila Porto da Lagoa',
    seo_title='Pousada Vila Porto da Lagoa | Recanto açoriano na Lagoa da Conceição',
    logo_small='Pousada', logo_main='Vila Porto da Lagoa', logo_img='',
    meta_desc='Pousada Vila Porto da Lagoa: casinhas açorianas coloridas na beira da Lagoa da Conceição, deck sobre a água, caiaque e café da manhã caseiro. Nota 4,5 no Google.',
    phone='(48) 99146-6699', wa_number='5548991466699', email='',
    wa_text='Olá! Vim pelo site da Pousada Vila Porto da Lagoa e queria consultar disponibilidade.',
    instagram='vilaportodalagoa',
    address='Rod. João Gualberto Soares, 9454 (fundos) · São João do Rio Vermelho, Florianópolis/SC',
    place_line='Lagoa da Conceição · Florianópolis · SC',
    footer_tag='Um recanto açoriano na beira da Lagoa da Conceição.', checkin='14h', checkout='12h',
    rooms_label='Suítes', lang_gate=False,
)


def context(I, wa):
    v = lambda i, big=False: I(pic('v', i), big=big)[0]
    iv = lambda i, big=False: I(pic('iv', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=v(42, True), video='', eyebrow='Beira da Lagoa da Conceição',
                     title='Um recanto açoriano<br>na beira da lagoa',
                     sub='Casinhas coloridas, deck sobre a água e café da manhã feito pelos donos.')
    p['intro'] = dict(kicker='A pousada', title='Longe do burburinho, perto de tudo',
                      text='A Vila Porto da Lagoa foi construída como uma pequena vila açoriana: casinhas coloridas em volta de uma praça com fonte, gramado até a beira da Lagoa da Conceição e um deck pra ver o fim de tarde atrás do morro. Reaberta, a pousada é cuidada de perto pelo casal Wagner e Lucélia.',
                      badge='Jeito açoriano de receber')
    car = [39, 12, 75, 27, 70, 24, 16, 74, 58, 26]
    p['carousel'] = [dict(src=v(i), alt='Pousada Vila Porto da Lagoa') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Uma vila inteira pra descansar',
                           text='Da praça com fonte ao deck sobre a água, cada canto foi pensado pra quem procura paz e sossego.')
    cards = [
        (40, 'Casinhas açorianas', 'Fachadas coloridas, janelas de madeira e o charme das vilas do litoral catarinense.', 'Ver suítes', 'reservas.html'),
        (12, 'Deck na lagoa', 'Píer de madeira sobre a água, com espreguiçadeiras e a vista do morro.', 'Conhecer', '#pousada'),
        (76, 'Caiaque na lagoa', 'Caiaques pra remar na Lagoa da Conceição saindo do jardim da pousada.', 'Experiências', '#experiencias'),
        (65, 'Suítes espaçosas', 'Móveis novos, decoração caprichada, ar-condicionado e frigobar.', 'Ver suítes', 'reservas.html'),
        (50, 'Café da manhã', 'Bolos, ovos mexidos e pão de queijo quentinhos, feitos na hora pelos donos.', 'Consultar', '#contato'),
        (20, 'Praça com fonte', 'O coração da vila: gramado, bancos e a fonte iluminada à noite.', 'Conhecer', '#pousada'),
        (55, 'Trilhas e cachoeiras', 'Trilhas pela mata e cachoeiras da região, com as dicas dos anfitriões.', 'Experiências', '#experiencias'),
        (18, 'Espaço para eventos', 'Salão rústico de tijolinho e madeira para almoços, encontros e celebrações.', 'Consultar', '#contato'),
    ]
    p['cards'] = [dict(img=v(i), title=t, text=x, action=a, href=h) for i, t, x, a, h in cards]
    p['band'] = dict(img=v(75, True), nav='A vila', kicker='Vila Porto da Lagoa',
                     title='Paz e sossego<br>na beira d’água.',
                     text='Num canto tranquilo da Ilha, entre o morro e a lagoa. De manhã, café caseiro. À tarde, caiaque e deck. À noite, a praça iluminada e o silêncio.',
                     cta='Explorar a região')
    p['exp'] = dict(img=v(76), alt='Hóspedes remando de caiaque na Lagoa da Conceição', badge='Lagoa da Conceição',
                    kicker='Experiências', title='A lagoa é o quintal',
                    text='Da pousada dá pra sair remando pela Lagoa da Conceição. Pertinho ficam a Costa da Lagoa, a Barra da Lagoa e a Praia do Moçambique.',
                    items=['Caiaque na Lagoa da Conceição', 'Costa da Lagoa e Barra da Lagoa',
                           'Praia do Moçambique e Parque do Rio Vermelho', 'Passeios e trilhas com dicas dos anfitriões'],
                    cta='Pedir dicas pelo WhatsApp')
    items = [
        ('José Antonio F.', 'Excelente escolha para quem quer uma localização próxima da Lagoa da Conceição, da Costa da Lagoa e da Barra da Lagoa porém distante o suficiente de toda a agitação. O casal Wagner e Lucélia são extremamente cuidadosos com seus hóspedes.'),
        ('Debora E.', 'Amei! Lugar lindo, perto da praia, perto de restaurantes, farmácias, padarias. Quartos lindos, espaçosos! Café da manhã excelente! Bolos e ovos mexidos quentinhos, feitos na hora, pelos próprios donos.'),
        ('Moises J. L.', 'Um lugar incrível! Belíssimos quartos bem confortáveis, com todos os móveis novos e funcionais e com vistas inesquecíveis da Lagoa da Conceição. Limpeza impecável e café da manhã bem servido.'),
        ('Cristiane L.', 'Pousada super aconchegante, num canto bem tranquilo da Ilha da Magia. Atendimento personalizado, com passeios e trilhas para conhecer o meio ambiente local, cheio de surpresas maravilhosas!'),
        ('Pedro H. M.', 'O local foi reaberto, quartos são espaçosos, tem uma vista linda da lagoa onde você pode andar de caiaque.'),
        ('Ivan M.', 'Além de muito lindo o local e a vista da lagoa, as instalações são muito boas e agradáveis. Recomendo.'),
    ]
    p['reviews'] = dict(headline='4,5 no Google · 84 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 84 avaliações')]),
                        items=[dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items])
    p['film'] = None
    p['cta'] = dict(img=v(77, True), title='Pronto pra desacelerar na beira da lagoa?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=v(39, True), kicker='Reserve seu refúgio', title='Alguns dias na lagoa.<br>Uma pausa de verdade.',
        rooms_kicker='Nossas suítes', unit_word='Suíte', prices=False,
        included=['Café da manhã caseiro', 'Wi-Fi gratuito', 'Estacionamento', 'Caiaque e deck na lagoa'],
        rooms=[
            dict(name='Suíte Lagoa', guests=2, price='',
                 detail='Suíte ampla na casinha voltada para o jardim e a lagoa, com ar-condicionado, TV e frigobar.',
                 imgs=[v(65), v(64), v(72), v(42), v(12)]),
            dict(name='Suíte Praça', guests=2, price='',
                 detail='De frente para a pracinha com fonte, com cama de casal, ar-condicionado e frigobar.',
                 imgs=[v(70), v(20), v(74), v(40), v(28)]),
            dict(name='Suíte com Banheira', guests=2, price='',
                 detail='Banheira revestida de azulejos e decoração romântica, ideal para casais.',
                 imgs=[v(57), iv(1), v(65), v(58), v(77)]),
        ])
    return p
