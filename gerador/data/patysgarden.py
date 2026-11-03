"""Paty's Garden hospedagem & Bistrô (Jurerê Tradicional, Florianópolis) — site institucional no template 'casa' (home + reservas).
Suítes numeradas (1, 2, 5, 6) vêm das legendas do Instagram; tipos e capacidades a confirmar com a Paty/Bira."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Paty%27s+Garden+hospedagem+%26+Bistr%C3%B4+Jurer%C3%AA'
F = Fotos('patysgarden')

T = dict(paper='#fbf6f1', cream='#f1e3d8', espresso='#3a2620', honey='#b8674a', olive='#6f7a52',
         muted='#76625a', rooms_bg='#f3e6dc', deep='#3b2a26', gold='#e8b9a0')

P = dict(
    slug='patysgarden', name="Paty's Garden hospedagem & Bistrô", short="Paty's Garden",
    seo_title="Paty's Garden | Pousada de charme e bistrô em Jurerê Tradicional",
    logo_small='Hospedagem & Bistrô', logo_main="Paty's Garden", logo_img='',
    meta_desc="Paty's Garden: pousada de charme com bistrô em Jurerê Tradicional, a um quarteirão e meio da praia. Suítes com decoração vintage, jacuzzi aquecida, café da manhã personalizado, pet friendly. Nota 4,7 no Google.",
    phone='(48) 99162-5854', wa_number='5548991625854', email='',
    wa_text="Olá! Vim pelo site do Paty's Garden e queria consultar disponibilidade.",
    instagram='patysgardenbistro',
    address='R. Jorge Cherem, 95 · Jurerê, Florianópolis/SC · CEP 88053-620',
    place_line='Jurerê Tradicional · Florianópolis · SC',
    footer_tag='Mais que uma hospedagem e um bistrô: uma casa para bons momentos.', checkin='14h', checkout='11h',
    rooms_label='Suítes', lang_gate=False,
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(9, True), video='', eyebrow='Jurerê Tradicional · Florianópolis',
                     title="Paty's Garden,<br>uma casa para bons momentos",
                     sub='Suítes com decoração vintage, jacuzzi aquecida e um bistrô de cozinha autoral, a um quarteirão e meio da praia.')
    p['intro'] = dict(kicker='A pousada', title='Cuidada pelos próprios donos',
                      text="O Paty's Garden é uma pousada familiar com bistrô em Jurerê Tradicional. Cada canto tem uma história: os pratos pintados na parede, o telefone antigo, os quadros da família. Quem recebe são a Patrícia (a Paty) e o Bira, com café da manhã montado do jeito de cada hóspede e jantar no bistrô a poucos passos da suíte.",
                      badge='Pet friendly')
    car = [('g', 97), ('g', 59), ('g', 39), ('g', 101), ('g', 61), ('g', 95), ('g', 18), ('g', 124), ('g', 64), ('g', 89)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt="Paty's Garden") for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Pousada de charme com bistrô em casa',
                           text='Da jacuzzi aquecida ao jantar à luz de velas, tudo é pensado pra você não precisar sair de Jurerê.')
    cards = [
        ('g', 89, 'Suítes vintage', 'Cama de casal, ar-condicionado, TV, frigobar e uma decoração que parece de conto de fadas.', 'Ver suítes', 'reservas.html'),
        ('g', 96, 'Jacuzzi aquecida', 'Jacuzzi externa aquecida no deck, com vinho geladinho esperando quem quiser relaxar.', 'Conhecer', '#pousada'),
        ('g', 114, 'Bistrô no térreo', 'Cozinha mediterrânea e massas artesanais, com o chef Thiago no comando.', 'Reservar mesa', '#contato'),
        ('g', 18, 'Café personalizado', 'O café da manhã é montado do jeito que cada hóspede gosta: ovos, frutas, bolos e pães.', 'Conhecer', '#pousada'),
        ('g', 39, 'Noite romântica', 'Cama com pétalas, vinho e jantar no bistrô para celebrar datas especiais.', 'Consultar', '#contato'),
        ('g', 54, 'Home office', 'Suíte com escrivaninha e Wi-Fi rápido, pra trabalhar com calma perto da praia.', 'Consultar', '#contato'),
        ('g', 19, 'Pet friendly', 'Seu amigo de quatro patas é bem-vindo, e recebido com o mesmo carinho que você.', 'Consultar', '#contato'),
        ('g', 97, 'Varanda do bistrô', 'Deck de madeira, venezianas antigas e mesas pra um café da tarde sem pressa.', 'Conhecer', '#pousada'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=g(131, True), nav='Jurerê', kicker="Paty's Garden",
                     title='A praia a um quarteirão e meio,<br>o jantar no térreo.',
                     text='A pousada fica em Jurerê Tradicional, perto da praia, de restaurantes, mercados e cafés. Dá pra fazer tudo a pé e voltar pra jantar em casa.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(180), alt="Salmão ao molho de laranja do Paty's Garden Bistrô", badge='Bistrô',
                    kicker='Experiências', title='Hospedagem com gastronomia',
                    text="O bistrô do Paty's Garden é um dos motivos pra voltar: pratos de inspiração mediterrânea, massas feitas à mão e o famoso sorvete de queijo com goiabada da casa.",
                    items=['Jantar no bistrô a poucos passos da suíte', 'Massas artesanais e menu degustação',
                           'Pacotes com jantar e pernoite em datas especiais', 'Praia de Jurerê a um quarteirão e meio'],
                    cta='Pedir o cardápio pelo WhatsApp')
    google = [
        ('Nahir S.', 'Incrível! O serviço é excelente e os quartos são lindos. Os proprietários fazem você se sentir em casa. O café da manhã é delicioso e farto. Os quartos parecem saídos de um conto de fadas.'),
        ('Andrea A.', 'Uma estadia maravilhosa. Decoração vintage linda e de bom gosto! Os quartos são confortáveis e espaçosos. Apenas a um quarteirão e meio da praia de Jurerê.'),
        ('Pamela F.', 'A pousada é muito aconchegante e os espaços são lindos e charmosos. O atendimento é diferenciado e familiar. As refeições servidas no Bistrô da própria pousada são uma delícia!'),
        ('Eliana T.', 'Muito bom gosto e aconchego. Tudo impecável! E tem o diferencial de ser muito bem atendida pelos donos com carinho e atenção máxima!'),
        ('Lucas', 'Meus pais sempre se hospedam aqui pelo atendimento íntimo e amigável. Todo o hotel e a cozinha são cuidados pela família. A grande estrela é o sorvete de queijo com goiabada, feito na casa.'),
        ('Daniel X.', "O Paty's Garden é um lugar incrível, seja para se hospedar ou para uma boa refeição. Cada detalhe do ambiente transmite acolhimento e cuidado."),
        ('Carmen L.', 'Surpreendente! Excelente! Localização, atendimento, estrutura! Tudo pensado para acolher bem! Muito capricho e carinho envolvidos!'),
        ('Irene M.', 'Pense num restaurante aconchegante, silêncio, só música clássica ao fundo e uma ótima comida. Um achado. Recomendo muito.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,7 no Google · 38 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,7', '4,7 no Google · 38 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=g(98, True), title='Vem pra Jurerê?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=g(124, True), kicker='Reserve sua estadia', title='Alguns dias em Jurerê.<br>Entre a jacuzzi e o bistrô.',
        rooms_kicker='Nossas suítes', unit_word='Suíte', prices=False,
        included=['Café da manhã personalizado', 'Ar-condicionado', 'TV e frigobar', 'Wi-Fi gratuito', 'Jacuzzi externa aquecida', 'Pet friendly'],
        rooms=[
            dict(name='Suíte 1', guests=2, price='',
                 detail='Suíte de casal com vista para a jacuzzi externa, ar-condicionado, TV e frigobar.',
                 imgs=[g(122), g(124), g(119), g(121), g(120)]),
            dict(name='Suíte 2', guests=2, price='',
                 detail='Suíte de casal com cantinho de home office, pra conciliar trabalho e descanso perto da praia.',
                 imgs=[g(101), g(100), g(102), g(104), g(103)]),
            dict(name='Suíte 5', guests=2, price='',
                 detail='Cama de casal, ar-condicionado, banheiro com bancada de madeira, TV e frigobar, com vista para a jacuzzi e a alameda que leva à praia.',
                 imgs=[g(28), g(30), g(26), g(34), g(66)]),
            dict(name='Suíte 6', guests=2, price='',
                 detail='Suíte espaçosa e aconchegante, com lustre, cama de casal e decoração encantadora.',
                 imgs=[g(89), g(90), g(92), g(91)]),
        ])
    return p
