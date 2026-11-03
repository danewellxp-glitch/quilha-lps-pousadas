"""Pousada Praia da Armação (Armação do Pântano do Sul, Florianópolis) — site institucional no template 'casa' (home + reservas).
Sem Instagram. Fotos 100% do Google Maps, tiradas com câmera grande-angular (olho de peixe leve): as usadas passam por
correção de distorção (cv2.undistort) antes do tratamento. Tipos de apartamento montados a partir das reviews
("quartos para 2 ou 3 pessoas", "apartamento de 2 quartos") e das fotos: confirmar com os donos (seu Dauri e esposa)."""
import os
from common import review_sources
from fotos import Fotos

TEMPLATE = 'casa'
ENHANCE = True
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Praia+da+Arma%C3%A7%C3%A3o+Servid%C3%A3o+Tom%C3%A1s+Pires+64+Florian%C3%B3polis'
F = Fotos('armacao')


def U(i):
    """Foto do Maps com a distorção de grande-angular corrigida (cache em <slug>/undist/)."""
    src = F.gm(i)
    out = os.path.join(F.base, 'undist', os.path.basename(src))
    if not os.path.exists(out):
        import cv2
        import numpy as np
        im = cv2.imread(src)
        h, w = im.shape[:2]
        K = np.array([[w * .55, 0, w / 2], [0, w * .55, h / 2], [0, 0, 1]], float)
        D = np.array([-.28, .06, 0, 0, 0], float)
        nK, _ = cv2.getOptimalNewCameraMatrix(K, D, (w, h), 0.0)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        cv2.imwrite(out, cv2.undistort(im, K, D, None, nK), [cv2.IMWRITE_JPEG_QUALITY, 95])
    return out


T = dict(paper='#f6faf7', cream='#e3efe6', espresso='#1f3b2c', honey='#1f7a5a', olive='#3d6b8c',
         muted='#58685e', rooms_bg='#e8f1ea', deep='#173126', gold='#f2c66d')

P = dict(
    slug='armacao', name='Pousada Praia da Armação', short='Praia da Armação',
    seo_title='Pousada Praia da Armação | Apartamentos a 50 m da praia, no Sul da Ilha',
    logo_small='Pousada', logo_main='Praia da Armação', logo_img='',
    meta_desc='Pousada Praia da Armação, no Sul da Ilha de Florianópolis: apartamentos com cozinha, varanda com vista pro mar e a Praia da Armação a uns 50 metros. Pet friendly. Nota 4,5 no Google.',
    phone='(48) 98837-4350', wa_number='5548988374350', email='',
    wa_text='Olá! Vim pelo site da Pousada Praia da Armação e queria consultar disponibilidade.',
    instagram='',
    address='Servidão Tomás Pires, 64 · Armação do Pântano do Sul, Florianópolis/SC · CEP 88066-355',
    place_line='Armação · Sul da Ilha · Florianópolis',
    footer_tag='Apartamentos simples e completos, com o mar da Armação na porta.', checkin='', checkout='',
    rooms_label='Apartamentos', lang_gate=False,
)


def context(I, wa):
    u = lambda i, big=False: I(U(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=u(18, True), video='', eyebrow='Armação · Sul da Ilha',
                     title='O mar da Armação<br>na porta de casa',
                     sub='Apartamentos completos, com cozinha e varanda, a uns 50 metros da praia.')
    p['intro'] = dict(kicker='A pousada', title='Simples, limpa e pertinho do mar',
                      text='A Pousada Praia da Armação fica numa servidão tranquila da Armação do Pântano do Sul, a poucos passos da areia. São apartamentos com cozinha equipada, roupa de cama e banho e varanda olhando pro mar, ótimos pra casal, família ou um grupo pequeno. Quem recebe são os donos, com atendimento atencioso e o jeito acolhedor de casa de praia.',
                      badge='Pet friendly')
    car = [('u', 0), ('u', 9), ('u', 12), ('u', 33), ('u', 24), ('u', 17), ('u', 25), ('u', 19), ('u', 14), ('u', 35)]
    p['carousel'] = [dict(src=(u(i) if k == 'u' else G(i)), alt='Pousada Praia da Armação') for k, i in car]
    p['cards_head'] = dict(kicker='Cada canto', title='Tudo pra uma temporada no Sul da Ilha',
                           text='Apartamentos completos, vista pro mar e a praia a poucos passos.')
    cards = [
        ('u', 9, 'Quartos arejados', 'Cama de casal, ventilador de teto, armário e janela pro céu do Sul da Ilha.', 'Ver apartamentos', 'reservas.html'),
        ('u', 12, 'Cozinha equipada', 'Geladeira, fogão e utensílios, com mesa pra família toda.', 'Ver apartamentos', 'reservas.html'),
        ('u', 33, 'Varanda com vista', 'Do corredor do andar de cima dá pra ver o mar da Armação.', 'Conhecer', '#pousada'),
        ('u', 20, 'Praia a 50 m', 'A Praia da Armação fica a uns 50 metros, logo no fim da rua.', 'Conhecer', '#pousada'),
        ('u', 56, 'Churrasqueira', 'Espaço com churrasqueira pra reunir a turma depois da praia.', 'Conhecer', '#pousada'),
        ('u', 23, 'Para 2 ou 3 pessoas', 'Quartos com cama de casal ou de solteiro, pra casal, família ou amigos.', 'Ver apartamentos', 'reservas.html'),
        ('u', 14, 'Estacionamento', 'Garagem coberta no térreo do prédio.', 'Consultar', '#contato'),
        ('G', 62, 'Trilhas do Sul da Ilha', 'Lagoinha do Leste, Matadeiro e Pântano do Sul a poucos minutos.', 'Explorar', '#experiencias'),
    ]
    p['cards'] = [dict(img=(u(i) if k == 'u' else G(i)), title=t, text=x, action=a, href=h) for k, i, t, x, a, h in cards]
    p['band'] = dict(img=u(15, True), nav='A região', kicker='Praia da Armação',
                     title='Pé na areia,<br>sem pressa.',
                     text='Mercado, farmácia e o comércio da Armação ficam pertinho, dá pra ir a pé ou de bike. E de lá saem as trilhas e os barcos pras praias mais bonitas do Sul da Ilha.',
                     cta='Explorar a região')
    p['exp'] = dict(img=G(70), alt='Passarela de madeira na Armação', badge='Sul da Ilha',
                    kicker='Experiências', title='Trilhas, barcos e praias selvagens',
                    text='A Armação é ponto de partida pra viver o Sul da Ilha: a trilha da Lagoinha do Leste, a praia do Matadeiro, o costão e os barcos de pescadores na beira da areia.',
                    items=['Praia da Armação a uns 50 metros', 'Trilha para o Matadeiro e a Lagoinha do Leste',
                           'Pântano do Sul e seus restaurantes de frutos do mar', 'Comércio local a poucos minutos de bike'],
                    cta='Pedir dicas pelo WhatsApp')
    google = [
        ('Diego F.', 'Os quartos são ótimos para duas ou três pessoas. O local é simples porém muito limpo, organizado. Fica muito próximo da praia da Armação, uns 50 metros. Para casais é perfeito!'),
        ('Ana', 'É perto da praia e de bike acessível para ir no mercado, farmácia, etc. Acomodação simples e com vista para o mar. E o melhor é que aceitam pets!'),
        ('Liza B.', 'Na beira da praia, apartamento de 2 quartos com toda a infraestrutura. A dona do estabelecimento muito gentil. Recomendo.'),
        ('Marília B.', 'Tem tudo que se precisa, utensílios de cozinha, toalha, roupas de cama, e tem vista pro mar.'),
        ('Bandeira21', 'Casa simples, mas acolhedora. Um apoio básico de produtos para casa, cama e banho. Vale a pena. Gratidão pela recepção.'),
        ('Walter M.', 'Praia linda, água cristalina.'),
    ]
    items = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(headline='4,5 no Google · 26 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', '4,5 no Google · 26 avaliações')]),
                        items=items)
    p['film'] = None
    p['cta'] = dict(img=u(17, True), title='Bora pro Sul da Ilha?')
    p['loc'] = dict(maps_url=MAPS)
    p['res'] = dict(
        hero=u(29, True), kicker='Reserve sua estadia', title='Alguns dias na Armação.<br>Com o mar logo ali.',
        rooms_kicker='Nossos apartamentos', unit_word='Apartamento', prices=False,
        included=['Cozinha equipada', 'Roupa de cama e banho', 'Ventilador de teto', 'TV', 'Estacionamento', 'Pet friendly'],
        rooms=[
            dict(name='Apartamento 1 Quarto', guests=3, price='',
                 detail='Quarto com cama de casal, cozinha com mesa e sofá, banheiro e varanda. Ideal pra casal ou casal com filho.',
                 imgs=[u(9), u(12), u(13), u(33), u(41)]),
            dict(name='Apartamento 2 Quartos', guests=5, price='',
                 detail='Dois quartos (casal e solteiros), sala com cozinha completa e varanda com vista pro mar.',
                 imgs=[u(24), u(23), u(25), u(44), u(10)]),
        ])
    return p
