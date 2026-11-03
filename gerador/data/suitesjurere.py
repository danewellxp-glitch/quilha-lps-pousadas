"""Suites Jurerê Internacional (Av. dos Búzios, 2021, Jurerê Internacional, Florianópolis) — site no template 'casa' (home + reservas).
Fotos: Google Maps (gm2, poucas) + fotos de parceiros mostradas no Maps (px, 640px, origem worldota/Ostrovok). Dono: Oliver.
Tipos de acomodação montados a partir das fotos: confirmar com o dono."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Suites+Jurere+Internacional+Av.+dos+B%C3%BAzios+2021'
F = Fotos('suitesjurere')

T = dict(paper='#fbf8f3', cream='#f1e7da', espresso='#2b2724', honey='#b0603c', olive='#3d6b5e',
         muted='#6c635a', rooms_bg='#f4ece2', deep='#1f2f2c', gold='#e0a77c')

P = dict(
    slug='suitesjurere', name='Suites Jurerê Internacional', short='Suites Jurerê',
    seo_title='Suites Jurerê | Hospedagem em Jurerê Internacional, Florianópolis',
    logo_small='Suites', logo_main='Jurerê', logo_img='',
    meta_desc='Suites Jurerê: suítes e apartamentos com cozinha em Jurerê Internacional, perto da praia e do Jurerê Open Shopping. Deck com jardim, ar-condicionado e Wi-Fi.',
    phone='(48) 98804-8466', wa_number='5548988048466', email='',
    wa_text='Olá! Vim pelo site da Suites Jurerê e queria consultar disponibilidade.',
    instagram='',
    address='Av. dos Búzios, 2021 · Jurerê Internacional, Florianópolis/SC · CEP 88053-301',
    place_line='Jurerê Internacional · Florianópolis · SC',
    footer_tag='Perto da praia, do Open Shopping e de tudo o que Jurerê tem de melhor.', checkin='14h', checkout='11h',
    rooms_label='Acomodações', lang_gate=False,
)


def context(I, wa):
    X = lambda i, big=False: I(F._get('px', i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=X(18, True), video='', eyebrow='Jurerê Internacional · Florianópolis',
                     title='Jurerê do jeito<br>mais tranquilo',
                     sub='Suítes e apartamentos com cozinha, deck com jardim e a praia de Jurerê a poucos minutos a pé.')
    p['intro'] = dict(kicker='A hospedagem', title='Um cantinho verde no meio de Jurerê',
                      text='A Suites Jurerê fica na Av. dos Búzios, em Jurerê Internacional, pertinho da praia e do Jurerê Open Shopping. São suítes e apartamentos com ar-condicionado, Wi-Fi e cozinha, em volta de um deck de madeira com jardim, pergolado e cantinhos pra descansar. Quem recebe é o Oliver e a equipe, sempre por perto pra ajudar.',
                      badge='Pertinho da praia')
    car = [0, 19, 3, 9, 14, 10, 16, 34, 7, 12]
    p['carousel'] = [dict(src=X(i), alt='Suites Jurerê') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Conforto de casa, com cara de férias',
                           text='Pra um fim de semana na praia, um evento ou uns dias de trabalho, a Suites Jurerê tem o que você precisa.')
    cards = [
        ('X', 19, 'Deck com jardim', 'Mesa ao ar livre, guarda-sol e flores pra tomar um café com calma.', 'Conhecer', '#pousada'),
        ('X', 3, 'Ofurô no deck', 'Banheira de hidromassagem ao ar livre, entre tijolinho e madeira.', 'Conhecer', '#pousada'),
        ('X', 10, 'Cozinha equipada', 'Cooktop, micro-ondas, geladeira e bancada de granito nas unidades com cozinha.', 'Ver acomodações', 'reservas.html'),
        ('X', 8, 'Suítes confortáveis', 'Cama de casal, ar-condicionado, TV e roupa de cama sempre limpinha.', 'Ver acomodações', 'reservas.html'),
        ('X', 16, 'Corredor florido', 'Vasos, flores e pergolado de madeira por todo o caminho.', 'Conhecer', '#pousada'),
        ('X', 36, 'Jurerê a pé', 'O Jurerê Open Shopping, restaurantes e beach clubs a poucos passos.', 'Explorar', '#experiencias'),
        ('X', 14, 'Sala de jantar', 'Mesa pra quatro, TV e espaço pra receber a família nos apartamentos maiores.', 'Ver acomodações', 'reservas.html'),
        ('G', 9, 'Praia pertinho', 'Areia fofa, mar calmo e água de coco a poucos minutos de caminhada.', 'Como chegar', '#contato'),
    ]
    p['cards'] = [dict(img=(X(i) if k == 'X' else G(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=X(34, True), nav='Jurerê', kicker='Suites Jurerê',
                     title='O melhor de Jurerê<br>a poucos passos.',
                     text='Praia de mar calmo, beach clubs, o Open Shopping e as ruas arborizadas do bairro. Na volta, o deck com jardim espera por você.',
                     cta='Explorar a região')
    p['exp'] = dict(img=X(22), alt='Jurerê Open Shopping', badge='Jurerê',
                    kicker='Na vizinhança', title='Um bairro pra curtir a pé',
                    text='Jurerê Internacional é um dos bairros mais charmosos da Ilha, com ruas arborizadas, praia de mar calmo e muita coisa pra fazer perto da pousada.',
                    items=['Praia de Jurerê a poucos minutos a pé', 'Jurerê Open Shopping, restaurantes e cafés',
                           'Beach clubs e a Fortaleza de São José da Ponta Grossa', 'Fácil acesso a Canasvieiras e Daniela'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Luis Fernando', 'Oliver é um ótimo e prestativo anfitrião. A localização é ótima em Jurerê, muito tranquilo e agradável. As suítes são bem agradáveis, têm tudo o que precisamos. Nota 10.'),
        ('Carlos Henrique B.', 'Ótima localização, acomodações que atendem perfeitamente, limpeza, todos os equipamentos e Wi-Fi funcionando e um excelente atendimento.'),
        ('Lucena S.', 'Experiência muito boa, todos os colaboradores super atenciosos e rápidos, e o dono Oliver principalmente. Tem tudo o que precisa, além da ótima localização.'),
        ('Marcela D.', 'Adorei! Limpo, seguro, tranquilo e acolhedor. O Oliver foi muito atencioso, os funcionários foram simpáticos e fica perto da praia. Recomendo muito!'),
        ('Claudio D.', 'O lugar e a localização são ótimos. O atendimento do proprietário é de longe o melhor. É o lugar que escolho sempre que volto a Florianópolis.'),
        ('Marcio Gabriel R.', 'O local é excelente. Perto da praia e do comércio. Os quartos são muito agradáveis e confortáveis. O proprietário é muito simpático e gentil.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,3 no Google · 38 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,3', '4,3 no Google · 38 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=X(0, True), title='Bora pra Jurerê?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=X(4, True), kicker='Reserve sua estadia', title='Uns dias em Jurerê.<br>Sem complicação.',
        rooms_kicker='Nossas acomodações', unit_word='Acomodação', prices=False,
        included=['Ar-condicionado', 'Wi-Fi gratuito', 'TV', 'Cozinha ou kitchenette', 'Banheiro privativo', 'Roupa de cama e banho'],
        rooms=[
            dict(name='Suíte', guests=2, price='',
                 detail='Cama de casal, ar-condicionado, TV, frigobar e banheiro privativo. Prática pra um casal.',
                 imgs=[X(8), X(30), X(38), X(9), G(3)]),
            dict(name='Apartamento com Cozinha', guests=4, price='',
                 detail='Quarto, sala com sofá e cozinha equipada com bancada de granito. Ideal pra família ou amigos.',
                 imgs=[X(42), X(39), X(41), X(37), X(10)]),
            dict(name='Loft Duplex', guests=4, price='',
                 detail='Dois andares, sala com TV, escada de madeira e quarto no mezanino. Saída pro deck com jardim.',
                 imgs=[X(15), X(12), X(7), X(14), X(33)]),
        ])
    return p
