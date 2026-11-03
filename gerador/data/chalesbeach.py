"""Pousada Chalés Beach (Ibiraquera / Praia do Rosa) — site institucional no template 'casa' (home + reservas)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Chal%C3%A9s+Beach+Praia+do+Rosa+Imbituba'
F = Fotos('chalesbeach')

T = dict(paper='#fbf7ef', cream='#efe5d3', espresso='#3a2516', honey='#c06f2c', olive='#4c7a4b',
         muted='#6a5d4f', rooms_bg='#f3eadb', deep='#22311f', gold='#ecbd6e')

P = dict(
    slug='chalesbeach', name='Pousada Chalés Beach', short='Chalés Beach',
    seo_title='Pousada Chalés Beach | Chalés completos na Praia do Rosa',
    logo_small='Pousada', logo_main='Chalés Beach', logo_img='',
    meta_desc='Pousada Chalés Beach, em Ibiraquera, na Praia do Rosa: chalés de madeira com cozinha completa, varanda com rede, área de jogos, churrasqueiras e pet friendly. Nota 5,0 no Google e 9,7 no Booking.',
    phone='(48) 99204-6267', wa_number='5548992046267', email='',
    wa_text='Olá! Vim pelo site da Pousada Chalés Beach e queria consultar disponibilidade.',
    instagram='pousadachalesbeach',
    address='R. Peixe Espada · Ibiraquera, Imbituba/SC · CEP 88780-000',
    place_line='Praia do Rosa · Imbituba · SC',
    footer_tag='Chalés completos, jardim e a Praia do Rosa logo ali.', checkin='', checkout='12h',
    rooms_label='Chalés', lang_gate=False,
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gmfix(i), big=big)[0]  # fotos HDR do Maps vêm arroxeadas
    p = dict(P)
    p['hero'] = dict(img=G(26, True), video='', eyebrow='Ibiraquera · Praia do Rosa',
                     title='Seu chalé<br>na Praia do Rosa',
                     sub='Chalés de madeira completos, varanda com rede e um jardim inteiro pra família curtir.')
    p['intro'] = dict(kicker='A pousada', title='Casa de praia, com jeito de pousada',
                      text='A Chalés Beach fica numa rua tranquila de Ibiraquera, pertinho do centrinho do Rosa. Os chalés de madeira têm cozinha equipada, ar-condicionado e varanda com rede, em volta de um jardim com área de jogos, churrasqueiras e parquinho. Quem recebe são os próprios donos, que cuidam de cada detalhe.',
                      badge='Abertos o ano todo')
    car = [('g', 8), ('G', 38), ('g', 18), ('g', 6), ('G', 41), ('g', 58), ('g', 62), ('G', 37), ('g', 76), ('g', 46)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Chalés Beach') for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo o que a família precisa',
                           text='Do chalé com cozinha completa à área de jogos no jardim, a pousada foi pensada pra você se sentir em casa perto do mar.')
    cards = [
        ('g', 32, 'Chalés de madeira', 'Chalés aconchegantes, com ar-condicionado, TV e banheiro privativo.', 'Ver chalés', 'reservas.html'),
        ('g', 48, 'Varanda com rede', 'Todo chalé tem varanda com rede olhando pro jardim. Pra ler, cochilar e ver o fim de tarde.', 'Conhecer', '#pousada'),
        ('g', 40, 'Cozinha completa', 'Fogão, geladeira, micro-ondas e utensílios: dá pra cozinhar como em casa.', 'Ver chalés', 'reservas.html'),
        ('G', 11, 'Área de jogos', 'Sinuca e pingue-pongue no espaço coberto, ao lado da área gourmet.', 'Conhecer', '#pousada'),
        ('g', 64, 'Churrasqueiras', 'Churrasqueiras pra reunir a família e os amigos depois da praia.', 'Consultar', '#contato'),
        ('G', 19, 'Parquinho', 'Parquinho e caixa de areia pras crianças, com o jardim todo à vista.', 'Conhecer', '#pousada'),
        ('G', 49, 'Pet friendly', 'Seu cachorro é bem-vindo: o espaço é cercado e seguro pra ele também.', 'Consultar', '#contato'),
        ('G', 37, 'Jardim florido', 'Gramado, plantas e as plaquinhas coloridas que dão o clima da pousada.', 'Conhecer', '#pousada'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=G(41, True), nav='A região', kicker='Chalés Beach',
                     title='O Rosa a uma<br>caminhada de distância.',
                     text='Dá pra fazer quase tudo a pé: o centrinho, os bares, os restaurantes e até a trilha pro Rosa Norte. Na volta, rede na varanda e churrasco no jardim.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(0), alt='Vista da Praia do Rosa do alto do costão', badge='Praia do Rosa',
                    kicker='Experiências', title='Mar, trilha e lagoa por perto',
                    text='A pousada fica entre a Lagoa de Ibiraquera e a Praia do Rosa, uma das praias mais bonitas de Santa Catarina. No inverno, Imbituba recebe as baleias-francas.',
                    items=['Centrinho do Rosa, bares e restaurantes a pé', 'Trilha para o Rosa Norte', 'Lagoa de Ibiraquera',
                           'Observação de baleias-francas (temporada de inverno)'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Hanna D.', 'Eu me surpreendi. Muito melhor que as fotos! Seri, a anfitriã atenciosa, chalé lindo, completíssimo! Tem garagem, fácil de chegar. Com certeza voltarei.'),
        ('Mary P.', 'Esse lugar é mágico. Ambiente maravilhoso. A higienização do local perfeita. O atendimento foi perfeito. Silêncio à noite encanta a alma.'),
        ('Beatriz F.', 'A localização é ótima, dá para fazer tudo a pé (centrinho, bares, até ir para o Rosa Norte por uma trilha). O local é super aconchegante e mais uma vez fomos super bem recebidos.'),
        ('Natália M.', 'Estadia maravilhosa! Chalés completos, com mobília, eletros e utensílios de cozinha… limpíssimo! Proprietários educados, atenciosos e preocupados com o bem-estar dos hóspedes!'),
        ('Kahuana H.', 'A pousada é linda! A cabana possui todos os itens necessários para uma boa estadia, além da área gourmet com mesa de sinuca, um lindo jardim e parquinho infantil.'),
        ('Lívia P.', 'Chalé vem equipado, anfitriões educados e agradáveis! Aproveitamos a parte externa para um churrasco em família e levamos nosso cachorrinho, local seguro para ele também.'),
    ]
    booking = [
        ('Andreia', 'Anfitriã muito receptiva, atenciosa e prestativa. A acomodação é fantástica, tudo muito limpo e organizado.'),
        ('Airton', 'Pousada excelente. Lugar sossegado e pertinho das praias e do centrinho do Rosa.'),
        ('Luiz', 'Lugar com ótima localização. Perto da SurfLand. Bem limpo, com ótimo custo-benefício. Pessoal bem atencioso e solícito. Voltaremos.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    for k, (a, t) in enumerate(booking):
        items.insert(1 + 2 * k, dict(key='booking', text=t, author=a, source='Booking', stars=5))
    p['reviews'] = dict(headline='5,0 no Google · 81 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '5,0', '5,0 no Google · 81 avaliações'),
                                                ('booking', 'Booking', '9,7', '9,7 no Booking · 35 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=g(68, True), title='Bora reservar seu chalé no Rosa?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=g(18, True), kicker='Reserve seu chalé', title='Alguns dias no Rosa.<br>Com cara de casa.',
        rooms_kicker='Nossos chalés', unit_word='Chalé', prices=False,
        included=['Cozinha completa', 'Ar-condicionado e TV', 'Wi-Fi gratuito', 'Estacionamento', 'Varanda com rede', 'Pet friendly'],
        rooms=[
            dict(name='Chalé de 1 Quarto', guests=4, price='',
                 detail='Cama de casal e sofá-cama, cozinha equipada, ar-condicionado e varanda com rede. Ideal pra casal com filhos.',
                 imgs=[g(9), g(12), g(11), g(13), g(6)]),
            dict(name='Chalé', guests=6, price='',
                 detail='Duas camas de casal e sofá-cama, cozinha completa e varanda com rede, pra família ou turma de amigos.',
                 imgs=[G(25), G(27), G(28), G(21), g(40)]),
            dict(name='Chalé Superior', guests=2, price='',
                 detail='Cama de casal, ar-condicionado e TV, com a varanda e a rede de frente pro jardim.',
                 imgs=[g(44), g(74), g(75), g(46), g(42)]),
            dict(name='Casa de 2 Quartos', guests=8, price='',
                 detail='Dois quartos com cama de casal, sala com sofá-cama e cozinha completa, pra grupos maiores.',
                 imgs=[g(78), g(79), g(80), g(81), g(82)]),
        ])
    return p
