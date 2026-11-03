"""Pousada Dormida do Peixe — site institucional no template 'casa' (home + reservas), fotos tratadas."""
import os
from common import ig
from data.dormida import MAPS, P as LP, context as _lp_context

TEMPLATE = 'casa'
ENHANCE = True
U = 'dormidadopeixe'
_GMD = os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'gm4', 'dormida')
_GMIDX = {int(l.split('\t')[0]): l.split('\t')[1] for l in open(os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'ig', 'sheets', 'gmdorm_idx.txt')).read().strip().split('\n')}
gm = lambda i: os.path.join(_GMD, _GMIDX[i])

T = dict(paper='#f8f6f1', cream='#e3ece8', espresso='#14313a', honey='#23807a', olive='#3f6b5c',
         muted='#56615e', rooms_bg='#edf2ef', deep='#0e2329', gold='#9fd6cf')

P = dict(
    slug='dormida_site', name='Pousada Dormida do Peixe', short='Dormida do Peixe',
    seo_title='Pousada Dormida do Peixe | Praia do Rosa e Lagoa de Ibiraquera',
    logo_small='Pousada', logo_main='Dormida do Peixe', logo_img='',
    meta_desc=LP['meta_desc'], phone=LP['phone'], wa_number=LP['wa_number'], email='',
    wa_text=LP['wa_text'], instagram=LP['instagram'],
    address='Rua Central do Rosa, s/n · Ibiraquera, Imbituba/SC', place_line='Praia do Rosa · Imbituba · SC',
    footer_tag='Tranquilidade e conforto entre a lagoa e o mar.', checkin='14h', checkout='12h',
    rooms_label='Apartamentos', lang_gate=False,
)


def context(I, wa):
    g = lambda i, big=False: I(ig(U, i), big=big)[0]
    G = lambda i, big=False: I(gm(i), big=big)[0]
    base = _lp_context(lambda *a, **k: ('', 0, 0), wa)
    p = dict(P)
    p['hero'] = dict(img=g(29, True), video='', eyebrow='Praia do Rosa · Ibiraquera',
                     title='Desacelere entre<br>a lagoa e o mar',
                     sub='Apartamentos amplos com varanda e vista, a 10 minutos a pé do centrinho do Rosa.')
    p['intro'] = dict(kicker='A pousada', title='Um cantinho de paz no Rosa',
                      text='A Dormida do Peixe foi feita pra quem quer acordar sem pressa. Os apartamentos são novos e amplos, com sala, suíte e varanda com rede olhando para as montanhas, a Lagoa de Ibiraquera e o mar lá no fundo. Quem recebe é a própria família, com as melhores dicas da região.',
                      badge='Nota 5,0 no Google')
    car = [('G', 4), ('g', 17), ('G', 12), ('g', 30), ('G', 0), ('g', 19), ('G', 42), ('g', 8), ('G', 59), ('g', 11)]
    p['carousel'] = [dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Dormida do Peixe') for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo pensado pra você descansar',
                           text='Apartamentos completos, varandas com rede, piscina no jardim e a natureza do Rosa em volta.')
    cards = [
        ('G', 12, 'Apartamentos amplos', 'Sala com sofá, mesa, frigobar e lavabo, além da suíte. Espaço de sobra pra família.', 'Ver apartamentos', 'reservas.html'),
        ('G', 4, 'Suítes confortáveis', 'Cama grande, ar-condicionado, ventilador e enxoval de qualidade.', 'Ver apartamentos', 'reservas.html'),
        ('g', 17, 'Varandas com rede', 'Rede, poltronas e a vista das montanhas e da lagoa para o fim de tarde.', 'Conhecer', '#pousada'),
        ('g', 30, 'Piscina e jardim', 'Piscina com deck de madeira, espreguiçadeiras e muito verde em volta.', 'Conhecer', '#pousada'),
        ('g', 44, 'Café da manhã', 'Bandeja caprichada com frutas, pães, frios e sucos, das 7h às 10h (opcional).', 'Consultar', '#contato'),
        ('g', 11, 'Vista da lagoa', 'Do alto, a Lagoa de Ibiraquera, as montanhas e o mar no horizonte.', 'Explorar', '#regiao'),
        ('g', 26, 'Praia do Rosa', 'O centrinho fica a cerca de 10 minutos a pé e a praia logo depois.', 'Como chegar', '#experiencias'),
        ('g', 42, 'Trilhas e praias', 'Rosa Norte, Ibiraquera e Praia do Luz pertinho. A gente indica o roteiro.', 'Experiências', '#experiencias'),
    ]
    p['cards'] = [dict(img=(G(i) if k == 'G' else g(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=G(5, True), nav='A região', kicker='Dormida do Peixe',
                     title='Entre a lagoa<br>e o mar.',
                     text='Do jardim você vê as montanhas. Da varanda, a Lagoa de Ibiraquera. Lá no fundo, o mar do Rosa. Aqui o dia passa devagar, do café na varanda ao pôr do sol na beira da piscina.',
                     cta='Explorar a região')
    p['exp'] = dict(img=g(23), alt='Trilha com vista para a lagoa e o mar', badge='Rosa Norte e Lagoa',
                    kicker='Experiências', title='O melhor do Rosa a pé',
                    text='A trilha Rosa Norte e Lagoa passa pertinho da pousada. Dá pra emendar mar, morro e lagoa no mesmo dia, e voltar pra um mergulho na piscina.',
                    items=['Centrinho do Rosa a cerca de 10 min a pé', 'Trilha Rosa Norte e Lagoa', 'Lagoa de Ibiraquera: kitesurf, SUP e pôr do sol',
                           'Praia do Luz, Barra de Ibiraquera e Garopaba'],
                    cta='Pedir dicas pelo WhatsApp')
    rv = base['reviews']
    keep = ['Suian Q.', 'Elmo L.', 'viagensdacami', 'Juliana S.', 'Elvis F.', 'Suellen C.']
    rv['items'] = [r for r in rv['items'] if r['author'] in keep]
    p['reviews'] = rv
    p['film'] = None
    p['cta'] = dict(img=G(38, True), title='Pronto pra desacelerar no Rosa?')
    p['loc'] = dict(maps_url=MAPS)
    room = lambda *ids: [(G(i) if k == 'G' else g(i)) for k, i in ids]
    p['res'] = dict(
        hero=G(0, True), kicker='Reserve seu refúgio', title='Alguns dias no Rosa.<br>Uma pausa de verdade.',
        rooms_kicker='Nossos apartamentos', unit_word='Apartamento', prices=False,
        included=['Wi-Fi gratuito', 'Estacionamento interno', 'Piscina e jardim', 'Roupa de cama e banho'],
        rooms=[
            dict(name='Apartamento com Sala', guests=4, price='',
                 detail='Sala com sofá, mesa e frigobar, lavabo e suíte com cama de casal, ar-condicionado e varanda com rede.',
                 imgs=room(('G', 12), ('G', 4), ('g', 13), ('g', 19), ('G', 42))),
            dict(name='Apartamento Vista Montanha', guests=2, price='',
                 detail='Suíte ampla e clara, com cama de casal, frigobar e vista para as montanhas e a lagoa.',
                 imgs=room(('G', 17), ('G', 59), ('g', 12), ('g', 17), ('g', 11))),
            dict(name='Apartamento Família', guests=4, price='',
                 detail='Duas camas, sala integrada e espaço de sobra para quem viaja com as crianças.',
                 imgs=room(('G', 8), ('G', 23), ('G', 35), ('g', 50), ('g', 18))),
        ])
    return p
