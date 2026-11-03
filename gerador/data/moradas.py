import os
from common import review_sources

TEMPLATE = 'doma'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Moradas+do+Mo%C3%A7ambique'
_B = os.path.dirname(os.path.abspath(__file__))
_IG = open(os.path.join(_B, '_moradas_ig_files.txt')).read().split('\n')
_GM = open(os.path.join(_B, '_moradas_gm_files.txt')).read().split('\n')
ig = lambda i: os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'ig3', _IG[i])
gm = lambda i: os.path.join(os.environ.get('QD_LEGACY', '/home/claude'), 'ig3', _GM[i])

T = dict(bg='#f7f5ee', text='#1b2a22', muted_text='#58655d', accent='#2f5d46', accent_ink='#f6f3ea', sage='#b9d3a8',
         label='#b5762a', band='#e7ede0', line='rgba(27,42,34,.14)', card='#eeece3')

P = dict(
    slug='moradas', name='Pousada Moradas do Moçambique', logo_small='Pousada', logo_main='Moradas do Moçambique',
    meta_desc='Pousada Moradas do Moçambique no Rio Vermelho, Florianópolis: flats com cozinha, chalé de madeira, jardim com redes e a Praia do Moçambique pertinho. Nota 4,7 no Google.',
    phone='(48) 98495-1131', wa_number='5548984951131', email='',
    wa_text='Olá! Vim pelo site da Pousada Moradas do Moçambique e queria consultar disponibilidade.',
    instagram='pousadamoradasdomocambique', footer_tag='Natureza, sossego e a Praia do Moçambique logo ali.',
)


def context(I, wa):
    G = lambda i: I(gm(i))[0]
    g = lambda i: I(ig(i))[0]
    Gi = lambda i: I(gm(i))
    gi = lambda i: I(ig(i))
    p = dict(P)
    p['hero'] = dict(img=G(0), alt='Jardim com redes da Pousada Moradas do Moçambique', title='Sossego entre o parque e o mar',
                     sub='Flats e chalé no Rio Vermelho, pertinho da Praia do Moçambique')
    p['intro'] = ['A Moradas do Moçambique fica numa rua tranquila do São João do Rio Vermelho, no norte da Ilha de Florianópolis, entre o Parque Estadual do Rio Vermelho e a Praia do Moçambique.',
                  'Flats completos com cozinha, um chalé de madeira, jardim com redes e o Anderson, que recebe cada hóspede com dicas de trilhas e praias.']
    p['about'] = dict(label='A pousada', title='Um lugar pra descansar de verdade',
                      sub='Jardim grande, muito verde e o barulho do mar ao fundo.',
                      img=G(9), alt='Flats com varanda e redes no jardim',
                      feats=[dict(icon='kitchen', title='Flats com cozinha', text='Cozinha equipada, geladeira, TV e banheiro privativo. Liberdade de casa de praia.'),
                             dict(icon='home', title='Chalé de madeira', text='Chalé aconchegante com cama no mezanino, rede e ducha externa no jardim.'),
                             dict(icon='leaf', title='Natureza em volta', text='Jardim amplo com redes, churrasqueira e o Parque do Rio Vermelho como vizinho.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('car', 'Estacionamento privativo gratuito'), ('kitchen', 'Flats com cozinha completa'), ('snow', 'Ar-condicionado'),
        ('tv', 'TV de tela plana'), ('food', 'Churrasqueira e quiosque'), ('leaf', 'Jardim com redes'), ('paw', 'Aceita pets'),
        ('users', 'Quartos para famílias'), ('plane', 'Transfer do aeroporto (sob consulta)')]]
    gal = [('G', 7), ('i', 22), ('G', 29), ('i', 26), ('G', 13), ('i', 44), ('G', 54), ('i', 28), ('G', 20), ('i', 45), ('G', 15), ('i', 11)]
    imgs = []
    for k, v in gal:
        s, w, h = Gi(v) if k == 'G' else gi(v)
        imgs.append(dict(src=s, w=w, h=h, alt='Pousada Moradas do Moçambique'))
    p['gallery'] = dict(title='Cada canto, sem pressa', sub='Flats, chalé, jardim e o clima de praia do norte da Ilha.', imgs=imgs)
    p['exp'] = dict(title='Além da pousada',
                    sub='O Moçambique é a maior praia da Ilha e ainda tem cara de praia selvagem. Pergunte ao Anderson o melhor caminho.',
                    cards=[dict(img=g(37), alt='Praia do Moçambique', title='Praia do Moçambique',
                                text='Mar aberto, areia sem fim e ondas boas para o surf. Dá pra chegar a pé pelas trilhas do parque.'),
                           dict(img=g(38), alt='Floresta de pinus do Parque do Rio Vermelho', title='Parque do Rio Vermelho',
                                text='Trilhas na sombra da mata e dos pinheirais, a poucos minutos da pousada.'),
                           dict(img=g(51), alt='Canal da Barra da Lagoa', title='Barra da Lagoa',
                                text='O canal, os barcos de pescador e os restaurantes de frutos do mar da Barra ficam pertinho.')])
    p['band'] = G(39)
    p['loc'] = dict(title='Entre o parque e o mar', area='São João do Rio Vermelho · Florianópolis',
                    address='Servidão Altino Manoel Claudino, 634 - São João do Rio Vermelho, Florianópolis - SC, 88060-402',
                    maps_q='Pousada Moradas do Moçambique, Florianópolis', maps_url=MAPS,
                    getting=['Praia do Moçambique: cerca de 1,8 km', 'Barra da Lagoa e Lagoa da Conceição: poucos minutos de carro', 'Aeroporto de Florianópolis: cerca de 32 km'],
                    nearby=['Parque Estadual do Rio Vermelho', 'Supermercado e restaurantes no bairro', 'Praias do Santinho e Ingleses'])
    items = [
        ('google', 'Google', 'Luana S.', 'Lugar incrível, super organizado e limpo! Anderson o dono da pousada super atencioso e prestativo, sempre disposto a ajudar! Nos sentimos em casa! Super recomendo e voltarei com toda certeza!'),
        ('google', 'Google', 'Gislaine D.', 'Passamos dias maravilhosos na pousada. O local é extremamente bem estruturado, possibilita bastante privacidade e conforto devido às ótimas instalações. O preço foi muito acessível e a localidade muito conveniente.'),
        ('booking', 'Booking.com', 'Hóspede verificado', 'Boa localização - próximo a praia do Moçambique e da Barra da Lagoa; o chalé é bem aconchegante e bem equipado. Anderson foi super receptivo e prestativo!'),
        ('google', 'Google', 'Hello Katty', 'O dono da pousada foi super gentil e amável o tempo todo da nossa estadia. Super preocupado da nossa filha de 2 anos. Tentou ajudar e adaptar o nosso quarto e ainda deu dicas super boas sobre o lugar, trilhas e praias. <3'),
        ('google', 'Google', 'Andre M.', 'Pousada legal muito bem localizada no bairro do Rio Vermelho na Praia do Moçambique em Floripa. Os apartamentos possuem cozinha e são limpos e organizados. Recomendo.'),
        ('booking', 'Booking.com', 'Hóspede verificado', 'Gostei de tudo. O Chalé é uma graça. Aconchegante. O anfitrião é super atencioso.'),
        ('google', 'Google', 'Douglas L.', 'Um lugar tranquilo e calmo para trazer paz de espírito. O pessoal da pousada muito atencioso e mantém uma organização impecável. Ótimo para quem busca serenidade.'),
        ('google', 'Google', 'Leabe E.', 'Excelente, o proprietário é muito atencioso e prestativo, ambiente super agradável, os flats e o quiosque são bem estruturados e com um preço muito bom, acessível.'),
    ]
    p['reviews'] = dict(sub='Nota 4,7 no Google e 8,2 no Booking.com.', headline='4,7 no Google · 95 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,7', '4,7 no Google · 95 avaliações'),
                                                ('booking', 'Booking.com', '8,2', '8,2 no Booking.com · 55 avaliações')]),
                        items=[dict(key=k, text=t, author=a, source=s, stars=5) for k, s, a, t in items])
    p['cta'] = dict(title='Pronto pra desacelerar?', sub='Chame o Anderson no WhatsApp e garanta seu flat ou o chalé.')
    return p
