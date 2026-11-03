"""Pousada Gendra's (Praia do Rosa, Imbituba) — LP no template 'doma'.
7 casas completas (2, 4, 6 e 8 pessoas) segundo a bio do IG. Anfitrião: Germán (reviews). Público muito argentino:
parte das reviews do Google foi escrita em espanhol e aparece aqui na tradução do próprio Google (hl=pt-BR)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('gendras')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Gendra%27s+Praia+do+Rosa+Imbituba'

T = dict(bg='#fbf6ee', text='#2a1d16', muted_text='#6a5a4f', accent='#b8542f', accent_ink='#fff8ef', sage='#3f7a5a',
         label='#b8542f', band='#f2e4d2', line='rgba(42,29,22,.14)', card='#f4ead9')

P = dict(
    slug='gendras', name="Pousada Gendra's", logo_small='Pousada', logo_main="Gendra's",
    meta_desc="Pousada Gendra's, na Praia do Rosa: 7 casas completas para 2, 4, 6 e 8 pessoas, com cozinha, piscina, deck e aulas de yoga, perto do centrinho e das praias. Nota 4,9 no Google.",
    phone='(48) 99135-1435', wa_number='5548991351435', email='',
    wa_text="Olá! Vim pelo site da Pousada Gendra's e queria consultar disponibilidade.",
    instagram='pousada_gendras', footer_tag='Casas completas no coração da Praia do Rosa.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    gi = lambda src: I(src)
    p = dict(P)
    p['hero'] = dict(img=G(0, True), alt="Deck, piscina e casas de tijolinho da Pousada Gendra's no fim de tarde",
                     title='Sua casa no coração da Praia do Rosa',
                     sub='Casas completas pra 2 a 8 pessoas, com piscina, deck e o centrinho a poucos passos')
    p['intro'] = ['A Gendra\'s é uma pousada de casas completas na Praia do Rosa, perto do centrinho, dos bares, restaurantes e praias. São 7 casas de tijolinho e madeira, com vitrais coloridos, cozinha equipada e espaço pra 2, 4, 6 ou 8 pessoas.',
                  'Quem recebe é o Germán, que segundo os hóspedes está sempre por perto pra ajudar, indicar passeios e preparar um menu caseiro no fim do dia.']
    p['about'] = dict(label='A pousada', title='Tijolinho, vitral e cheiro de praia',
                      sub='Um jeito simples e caloroso de viver o Rosa, com a casa inteira pra você e sua turma.',
                      img=g(2), alt="Pátio da Pousada Gendra's com casas de tijolinho e vitrais",
                      feats=[dict(icon='home', title='Casas completas', text='Quarto, sala e cozinha equipada, pra família ou grupo de amigos.'),
                             dict(icon='pool', title='Piscina e deck', text='Piscina no deck de madeira, com guarda-sóis e cadeiras pra depois da praia.'),
                             dict(icon='sun', title='Yoga e boa energia', text='Aulas de yoga na pousada e um clima leve, de casa cheia de amigos.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('home', '7 casas completas'), ('users', 'Casas para 2, 4, 6 e 8 pessoas'), ('kitchen', 'Cozinha equipada'), ('pool', 'Piscina com deck'),
        ('sun', 'Aulas de yoga'), ('food', 'Menus caseiros e cervejinha gelada'), ('wifi', 'Wi-Fi'), ('heart', 'Acolhe a comunidade LGBTQ+'),
        ('wave', 'Perto do centrinho e das praias'), ('clock', 'Check-out até 11h')]]
    gal = [('g', 0), ('g', 43), ('g', 11), ('g', 1), ('g', 18), ('G', 16), ('g', 12), ('g', 47), ('g', 31), ('g', 45), ('g', 21), ('g', 3)]
    gimgs = []
    for k, i in gal:
        src, w, h = gi(F.gm(i) if k == 'G' else F.ig(i))
        gimgs.append(dict(src=src, w=w, h=h, alt="Pousada Gendra's"))
    p['gallery'] = dict(title="Por dentro da Gendra's", sub='Casas com vitrais e tijolinho, cozinhas completas, deck, piscina e muito verde.', imgs=gimgs)
    p['exp'] = dict(title='O Rosa a pé',
                    sub='A pousada fica perto do centrinho, então dá pra fazer quase tudo sem carro.',
                    cards=[dict(img=g(19), alt='Pôr do sol na Praia do Rosa', title='Praia do Rosa',
                                text='Uma das baías mais bonitas do Brasil, com surf, trilhas e pores do sol de cinema.'),
                           dict(img=g(20), alt='Piscina natural entre as pedras do costão', title='Piscina natural',
                                text='Água verde e calma entre as pedras do costão, pra quem gosta de uma trilha curta.'),
                           dict(img=g(44), alt='Pátio arborizado da pousada', title='Fim de tarde na pousada',
                                text='Menu caseiro, cerveja gelada e conversa boa no pátio depois da praia.')])
    p['band'] = G(25, True)
    p['loc'] = dict(title='No coração da Praia do Rosa', area='Praia do Rosa · Imbituba/SC',
                    address='Praia do Rosa, Imbituba - SC, 88780-000',
                    maps_q="Pousada Gendra's, Praia do Rosa, Imbituba", maps_url=MAPS,
                    getting=['Centrinho do Rosa: a poucos passos', 'Praia mais próxima: a poucas quadras', 'Aeroporto de Florianópolis: cerca de 90 km'],
                    nearby=['Praia do Rosa e Rosa Norte', 'Lagoa de Ibiraquera', 'Trilhas e piscinas naturais do costão'])
    google = [
        ('Camila S.', 'Pousada incrível, muito bem localizada, muito bem equipada e a simpatia do German é sem igual, está sempre disposto a ajudar. Lá vende cervejinhas e comidinhas, vale muito a pena!'),
        ('Ana Claudia G.', 'Nossa estadia na Pousada foi maravilhosa, nos sentimos em casa! Super limpa, bem equipada, perto de tudo, segura e o atendimento foi perfeito!'),
        ('KRB A.', 'A pousada é nota 10! Muito bem localizada, próxima do centrinho onde há restaurantes e mercado 24 horas. Muito aconchegante, e o atendimento do Sr. German é nota 1000.'),
        ('Jennifer P.', 'Pousada encantadora. Excelente localização. Ambiente familiar e muito tranquilo. Administrada pelos proprietários, muito simpáticos e atenciosos a cada detalhe.'),
        ('Macarena M.', 'Perfeito para famílias e grupos de amigos, a poucos passos do centro e a poucos quarteirões da praia. Oferecem uma variedade de menus deliciosos e acessíveis.'),
        ('Federico S.', 'O lugar era incrível, de fácil acesso e seguro. Os pores do sol eram maravilhosos e o Germán recomendou ótimas atividades. Voltaremos com certeza!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(sub='Hóspedes elogiam o Germán, a localização e o clima de casa.',
                        headline='4,9 no Google · 27 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,9', '4,9 no Google · 27 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Bora pro Rosa?', sub="Chame a Gendra's no WhatsApp e escolha a casa do tamanho da sua turma.")
    return p
