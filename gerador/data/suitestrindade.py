"""Suites Trindade (R. Lauro Linhares, 1526, Trindade, Florianópolis) — site institucional no template 'casa' (home + reservas).
Fotos: Google Maps (sem Instagram). Tipos de apartamento a confirmar com os donos (montados a partir das fotos, das avaliações
e da pesquisa no Booking: suítes de 13 a 15 m² e apartamento de 2 quartos com 28 m² para até 4 pessoas)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Suites+Trindade+R.+Lauro+Linhares+1526+Florian%C3%B3polis'
F = Fotos('suitestrindade')

T = dict(paper='#faf7f2', cream='#efe5d8', espresso='#2e2a26', honey='#a65f3c', olive='#2f6f6a',
         muted='#6e655c', rooms_bg='#f2ebe2', deep='#22302f', gold='#d9a77f')

P = dict(
    slug='suitestrindade', name='Suites Trindade', short='Suites Trindade',
    seo_title='Suites Trindade | Hospedagem perto da UFSC, Florianópolis',
    logo_small='Hospedagem', logo_main='Suites Trindade', logo_img='',
    meta_desc='Suites Trindade: suítes e apartamentos na Rua Lauro Linhares, pertinho da UFSC, com ar-condicionado, frigobar, micro-ondas e Wi-Fi. Nota 4,5 no Google com mais de 300 avaliações.',
    phone='(48) 99663-9441', wa_number='5548996639441', email='',
    wa_text='Olá! Vim pelo site da Suites Trindade e queria consultar disponibilidade.',
    instagram='',
    address='R. Lauro Linhares, 1526 · Trindade, Florianópolis/SC · CEP 88036-003',
    place_line='Trindade · Florianópolis · SC',
    footer_tag='Perto da UFSC, do comércio e de tudo o que você precisa na Ilha.', checkin='14h', checkout='12h',
    rooms_label='Acomodações', lang_gate=False,
)


def context(I, wa):
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(19, True), video='', eyebrow='Trindade · Florianópolis',
                     title='Pertinho da UFSC,<br>com cara de casa',
                     sub='Suítes novas, limpas e silenciosas na Lauro Linhares, com tudo perto: padaria, mercado, shopping e restaurantes.')
    p['intro'] = dict(kicker='A hospedagem', title='Praticidade no coração da Trindade',
                      text='A Suites Trindade é um prédio de suítes e apartamentos na Rua Lauro Linhares, a poucos minutos a pé da UFSC. Cada unidade tem ar-condicionado, TV, frigobar e micro-ondas. A recepção tem parede de tijolinhos, tapetes e móveis de família, e lá em cima um terraço com vista para os morros da Ilha.',
                      badge='Ideal para estudo e trabalho')
    car = [19, 45, 12, 28, 39, 13, 24, 29, 18, 41]
    p['carousel'] = [dict(src=G(i), alt='Suites Trindade') for i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo o que você precisa, sem complicação',
                           text='Seja pra uma prova, um congresso, uma consulta ou uns dias de praia, a Suites Trindade resolve a estadia com conforto e bom preço.')
    cards = [
        (28, 'Suítes novas', 'Cama boa, ar-condicionado, TV e roupa de cama sempre limpinha e cheirosa.', 'Ver acomodações', 'reservas.html'),
        (39, 'Cozinha no quarto', 'Frigobar, micro-ondas e cafeteira pra montar o seu café do jeito que gostar.', 'Ver acomodações', 'reservas.html'),
        (45, 'Recepção aconchegante', 'Salão com parede de tijolinhos, tapetes e poltronas pra esperar com calma.', 'Conhecer', '#pousada'),
        (84, 'Vista do alto', 'Do alto do prédio dá pra ver os morros da Ilha e o campus da UFSC, a poucos minutos a pé.', 'Como chegar', '#contato'),
        (30, 'Banheiros privativos', 'Banheiro em todas as unidades, com chuveiro forte e bancada de granito.', 'Ver acomodações', 'reservas.html'),
        (12, 'Silêncio para descansar', 'Bom isolamento acústico e privacidade, mesmo no centro da Trindade.', 'Conhecer', '#pousada'),
        (24, 'Comércio ao redor', 'Padaria, mercado, farmácia, bancos, restaurantes e shopping a poucos passos.', 'Explorar', '#experiencias'),
        (13, 'Wi-Fi e elevador', 'Wi-Fi gratuito, elevador e entrada com fechadura eletrônica.', 'Reservar', 'reservas.html'),
    ]
    p['cards'] = [dict(img=G(i), title=t, text=x, action=a, href=h) for i, t, x, a, h in cards]
    p['band'] = dict(img=G(24, True), nav='A Trindade', kicker='Suites Trindade',
                     title='A cidade inteira<br>a poucos minutos.',
                     text='Da Trindade você chega rápido ao centro, à Lagoa da Conceição e às praias do leste da Ilha. Na volta, a suíte está pronta pra descansar.',
                     cta='Explorar a região')
    p['exp'] = dict(img=G(41), alt='Vista do campus e dos morros a partir do prédio', badge='Trindade',
                    kicker='Na vizinhança', title='Um bairro que tem de tudo',
                    text='A Lauro Linhares é uma das ruas mais movimentadas da Trindade: dá pra fazer quase tudo a pé, das refeições às compras do dia a dia.',
                    items=['UFSC a poucos minutos a pé', 'Shopping, padarias, mercado e farmácia por perto',
                           'Bares e restaurantes na própria rua', 'Fácil acesso ao centro, à Lagoa e às praias'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Vinícius B.', 'Um hotel maravilhoso. Quartos limpos, com bom tamanho e bastante aconchegantes. Nunca tive uma recepção melhor em um hotel. Extremamente bem localizado e com ótimo preço.'),
        ('William', 'Atendimento sensacional, quartos muito novos, sempre bem limpinhos, chuveiro excelente, cama boa, bom isolamento acústico, recepção aconchegante e muito bem localizado.'),
        ('Marcele C.', 'Muito bem localizado, perto da UFSC, e tem tudo pertinho: padaria, farmácia, restaurantes, shopping. Sem contar a recepção, que é excelente.'),
        ('Tulio C.', 'Pra quem busca um lugar gostoso pra dormir e descansar é perfeito. O quarto é um primor de arrumação e limpeza. Tudo de excelente bom gosto e capricho.'),
        ('Solange M.', 'Limpo, novinho, tranquilo. Para quem gosta de privacidade, é excelente. Meu filho nem queria mais ir embora, achou que era nosso.'),
        ('Gabriela P.', 'Ótimo lugar para hospedagem em família. Apartamentos com móveis novos, banheiro, frigobar, micro-ondas e cafeteira. Preço justo.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,5 no Google · 311 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 311 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=G(15, True), title='Vem pra Trindade?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=G(21, True), kicker='Reserve sua estadia', title='Alguns dias na Ilha.<br>Com tudo pertinho.',
        rooms_kicker='Nossas acomodações', unit_word='Acomodação', prices=False,
        included=['Ar-condicionado', 'TV e frigobar', 'Micro-ondas e cafeteira', 'Banheiro privativo', 'Wi-Fi gratuito', 'Roupa de cama e banho'],
        rooms=[
            dict(name='Suíte Casal', guests=2, price='',
                 detail='Cama de casal, ar-condicionado, TV, frigobar, micro-ondas e banheiro privativo.',
                 imgs=[G(28), G(61), G(44), G(48), G(30)]),
            dict(name='Suíte Twin', guests=2, price='',
                 detail='Duas camas de solteiro, bancada de trabalho, ar-condicionado e banheiro privativo. Boa pra colegas de trabalho ou de estudo.',
                 imgs=[G(18), G(12), G(23), G(14), G(16)]),
            dict(name='Apartamento 2 quartos', guests=4, price='',
                 detail='Dois quartos, sala com TV e minicozinha com frigobar e micro-ondas. Ideal pra família ou pequenos grupos.',
                 imgs=[G(39), G(49), G(32), G(74), G(10)]),
        ])
    return p
