"""Pousada 4 Estações Campeche — site institucional no template 'casa' (home + reservas), fotos tratadas."""
from common import review_sources
from l3 import pic

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+4+Esta%C3%A7%C3%B5es+Campeche'

T = dict(paper='#fbf8f2', cream='#f1e7d6', espresso='#1d3557', honey='#d9733a', olive='#2a9d8f',
         muted='#5d6670', rooms_bg='#f4efe6', deep='#13233a', gold='#f2b880')

P = dict(
    slug='quatro_estacoes_site', name='Pousada 4 Estações Campeche', short='4 Estações',
    seo_title='Pousada 4 Estações | Apartamentos no Campeche, Florianópolis',
    logo_small='Pousada', logo_main='4 Estações', logo_img='',
    meta_desc='Pousada 4 Estações no Campeche, Florianópolis: apartamentos e estúdios com cozinha, piscina com cascata, a 5 minutos a pé da praia. Nota 9,1 no Booking e 4,7 no Google.',
    phone='(48) 99624-7686', wa_number='5548996247686', email='',
    wa_text='Olá! Vim pelo site da Pousada 4 Estações e queria consultar disponibilidade.',
    instagram='pousada4estacoescampeche',
    address='Rua Tereza Lopes, 83 · Campeche, Florianópolis/SC', place_line='Campeche · Florianópolis · SC',
    footer_tag='Apartamentos aconchegantes perto da Praia do Campeche.',
    rooms_label='Apartamentos', lang_gate=False,
)


def context(I, wa):
    e = lambda i, big=False: I(pic('e', i), big=big)[0]
    ie = lambda i, big=False: I(pic('ie', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=e(16, True), video='', eyebrow='Campeche · Florianópolis',
                     title='Seu apartamento<br>perto do mar',
                     sub='Apartamentos e estúdios com cozinha, piscina com cascata e a Praia do Campeche a 5 minutos a pé.')
    p['intro'] = dict(kicker='A pousada', title='Em casa no Campeche',
                      text='A 4 Estações é uma pousada de família no Campeche: apartamentos e estúdios com cozinha, piscina com cascata, espaço zen no jardim e área de churrasco. Quem recebe são o Jairdo e a Dona Lúcia, que conhecem cada trilha, praia e passeio do sul da ilha.',
                      badge='9,1 no Booking.com')
    car = [20, 21, 15, 45, 14, 39, 30, 22, 57, 13]
    p['carousel'] = [dict(src=e(i), alt='Pousada 4 Estações Campeche') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Conforto de casa, clima de praia',
                           text='Apartamentos completos pra ficar uns dias ou umas semanas, com tudo que a ilha tem de bom a poucos passos.')
    cards = [
        ('e', 45, 'Apartamentos com cozinha', 'Fogão, geladeira, utensílios, mesa e sofá-cama. Liberdade de casa perto da praia.', 'Ver apartamentos', 'reservas.html'),
        ('e', 21, 'Quartos confortáveis', 'Cama de casal, ar-condicionado, TV e roupa de cama e banho inclusas.', 'Ver apartamentos', 'reservas.html'),
        ('e', 14, 'Piscina com cascata', 'Piscina no jardim cercado de palmeiras, com cascata e espreguiçadeiras.', 'Conhecer', '#pousada'),
        ('e', 39, 'Espaço Zen', 'Deck de madeira no meio do verde, pra relaxar depois de um dia de passeio.', 'Conhecer', '#pousada'),
        ('e', 40, 'Churrasqueira', 'Área coberta com churrasqueira e mesa comprida pra reunir a turma.', 'Conhecer', '#pousada'),
        ('ie', 87, 'Passeios de caiaque', 'Remadas com a pousada pela costa, pela Ilha do Campeche e pelas lagoas.', 'Experiências', '#experiencias'),
        ('e', 56, 'Passeio de bugue', 'O bugue azul da pousada leva você às praias e mirantes do sul da ilha.', 'Experiências', '#experiencias'),
        ('ie', 97, 'Trilhas guiadas', 'Lagoinha do Leste, Naufragados, Saquinho: trilhas saindo da pousada.', 'Experiências', '#experiencias'),
    ]
    p['cards'] = [dict(img=(e(i) if k == 'e' else ie(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=ie(254, True), nav='O Campeche', kicker='Pousada 4 Estações',
                     title='O sul da ilha<br>no seu ritmo.',
                     text='Do nascer do sol na Praia do Campeche ao fim de tarde no Pântano do Sul: a pousada fica entre o mar, as lagoas e as trilhas mais bonitas de Floripa.',
                     cta='Ver os passeios')
    p['exp'] = dict(img=ie(97), alt='Vista da Lagoinha do Leste do alto da trilha', badge='Lagoinha do Leste',
                    kicker='Passeios com a pousada', title='Aventura com quem conhece a ilha',
                    text='O Jairdo organiza trilhas, remadas de caiaque e passeios de bugue com os hóspedes. É só perguntar a programação da semana.',
                    items=['Praia do Campeche a cerca de 5 min a pé', 'Caiaque até a Ilha do Campeche',
                           'Trilhas da Lagoinha do Leste, Naufragados e Saquinho', 'Aeroporto de Florianópolis a cerca de 6 km'],
                    cta='Perguntar a programação')
    items = [
        ('google', 'Google', 'Kalinca T.', 'Pousada incrível, linda, limpíssima, aconchegante, muito bem localizada... mercado no mesmo quarteirão, farmácia, barzinhos, fica entre as praias do Campeche e Morro das Pedras. Anfitriões maravilhosos.'),
        ('google', 'Google', 'Betth C.', 'Acomodação tipo apartamento, com uma suíte maravilhosa no segundo andar e no primeiro andar uma cozinha com geladeira, fogão e uma sala com TV e sofá bicama. Excelente localização, perto do comércio e da praia.'),
        ('booking', 'Booking.com', 'Claudia', 'Fomos super bem atendidos, equipe muito prestativa e educada, adoramos! Quarto grande e com uma pequena cozinha! Localização muito boa.'),
        ('google', 'Google', 'Eli D.', 'Obrigado de coração a Jairdo e sua família pela recepção, conselhos, passeios... pousada aconchegante, limpinha, me sentindo em casa, calmo e perto da praia.'),
        ('google', 'Google', 'Rogério S.', 'Proprietário é muito gente boa e hospitaleiro. A pousada é top, tudo limpo e organizado. Recomendo sempre!'),
        ('booking', 'Booking.com', 'André', 'Tudo perfeito, muito pertinho da praia, restaurantes, mercados... Super indico. Comunicação perfeita.'),
    ]
    p['reviews'] = dict(headline='4,7 no Google · 95 avaliações · 9,1 no Booking.com · 211 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,7', '4,7 no Google'), ('booking', 'Booking.com', '9,1', '9,1 no Booking.com')]),
                        items=[dict(key=k, text=t, author=a, source=s, stars=5) for k, s, a, t in items])
    p['film'] = None
    p['cta'] = dict(img=ie(190, True), title='Pronto pra viver o Campeche?')
    p['loc'] = dict(maps_url=MAPS)
    room = lambda *ids: [e(i) for i in ids]
    p['res'] = dict(
        hero=e(20, True), kicker='Reserve seu apartamento', title='Alguns dias no Campeche.<br>Com cara de casa.',
        rooms_kicker='Nossos apartamentos', unit_word='Apartamento', prices=False,
        included=['Wi-Fi gratuito', 'Estacionamento privativo', 'Piscina com cascata', 'Roupa de cama e banho'],
        rooms=[
            dict(name='Estúdio Vista Piscina', guests=2, price='',
                 detail='Cama de casal, cozinha compacta, ar-condicionado e vista para a piscina.',
                 imgs=room(21, 49, 51, 15, 22)),
            dict(name='Apartamento Standard', guests=4, price='',
                 detail='Cama de casal e sofás-cama, sala com TV e cozinha completa com fogão e geladeira.',
                 imgs=room(45, 24, 30, 12, 54)),
            dict(name='Apartamento Superior', guests=4, price='',
                 detail='Duplex: suíte no andar de cima, sala com sofá-cama e cozinha embaixo.',
                 imgs=room(55, 50, 19, 48, 27)),
        ])
    return p
