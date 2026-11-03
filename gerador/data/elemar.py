"""Pousada Elemar (Jurerê, Florianópolis) — LP no template 'doma'.
Obs.: a lista dizia Santo Antônio de Lisboa, mas o endereço do Google e do Instagram é em Jurerê."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('elemar')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Elemar+Jurer%C3%AA+Florian%C3%B3polis'

T = dict(bg='#f8f8f3', text='#1b2a22', muted_text='#58665d', accent='#2e7d5b', accent_ink='#fffdf5', sage='#e9b44c',
         label='#c2563a', band='#e4efe7', line='rgba(27,42,34,.14)', card='#eeefe6')

P = dict(
    slug='elemar', name='Pousada Elemar', logo_small='Pousada', logo_main='Elemar',
    meta_desc='Pousada Elemar, em Jurerê, Florianópolis: apartamentos com cozinha equipada e ar-condicionado, churrasqueira, estacionamento e o atendimento da família do seu Elemar, a poucos minutos a pé da praia. Nota 4,8 no Google.',
    phone='(48) 98403-2225', wa_number='5548984032225', email='',
    wa_text='Olá! Vim pelo site da Pousada Elemar e queria consultar disponibilidade.',
    instagram='pousadaelemar', footer_tag='Seu aconchego na Praia de Jurerê.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    gi = lambda src: I(src)
    p = dict(P)
    p['hero'] = dict(img=G(36, True), alt='Mar calmo e azul da Praia de Jurerê',
                     title='Seu aconchego na Praia de Jurerê',
                     sub='Apartamentos completos, ambiente familiar e o mar calmo de Jurerê a uma caminhada')
    p['intro'] = ['A Pousada Elemar é uma pousada de família em Jurerê Tradicional, no norte da Ilha. Os apartamentos têm cozinha equipada, ar-condicionado, TV e roupa de cama, tudo simples, limpo e organizado, com estacionamento dentro da pousada.',
                  'O que os hóspedes mais lembram é o carinho do seu Elemar, da Viviani e de toda a família, que recebem como se fosse em casa.']
    p['about'] = dict(label='A pousada', title='Simples, aconchegante e de família',
                      sub='Uma pousada sem frescura, com tudo o que você precisa pra aproveitar Jurerê.',
                      img=g(0), alt='Fachada da Pousada Elemar com buganvília florida',
                      feats=[dict(icon='kitchen', title='Cozinha em cada apartamento', text='Fogão, geladeira, mesa e utensílios pra fazer as refeições do seu jeito.'),
                             dict(icon='wave', title='Perto da praia', text='Cerca de 800 m do mar calmo de Jurerê, perto de mercados, padaria e restaurantes.'),
                             dict(icon='heart', title='Atendimento de família', text='Quem recebe é a família do seu Elemar, sempre por perto pra ajudar.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi'), ('snow', 'Ar-condicionado'), ('car', 'Estacionamento'), ('kitchen', 'Cozinha equipada'),
        ('tv', 'TV'), ('food', 'Churrasqueira'), ('bed', 'Roupa de cama e banho'), ('users', 'Ideal para famílias e grupos'),
        ('wave', 'Praia a cerca de 800 m'), ('chat', 'Atendimento pelo WhatsApp')]]
    gal = [('g', 16), ('g', 8), ('g', 2), ('G', 31), ('g', 9), ('G', 41), ('g', 4), ('g', 7), ('g', 22), ('g', 23), ('G', 20), ('g', 14)]
    gimgs = []
    for k, i in gal:
        src, w, h = gi(F.gm(i) if k == 'G' else F.ig(i))
        gimgs.append(dict(src=src, w=w, h=h, alt='Pousada Elemar'))
    p['gallery'] = dict(title='Por dentro da Elemar', sub='Apartamentos com cozinha, quartos arejados, área de churrasco e flores por todo lado.', imgs=gimgs)
    p['exp'] = dict(title='Jurerê e o norte da Ilha',
                    sub='A pousada é a base certa pra curtir as praias calmas do norte de Floripa.',
                    cards=[dict(img=g(1), alt='Mar de Jurerê com veleiro ao fundo', title='Praia de Jurerê',
                                text='Mar calmo, areia branca e águas quentinhas, ótimo pra família e pra criança.'),
                           dict(img=G(43), alt='Praia com morro ao fundo', title='Praias do norte',
                                text='Daniela, Forte, Canasvieiras e Ingleses ficam a poucos minutos de carro.'),
                           dict(img=G(39), alt='Churrasco na churrasqueira da pousada', title='Churrasco na pousada',
                                text='Área com churrasqueira pra reunir a turma depois da praia.')])
    p['band'] = G(3, True)
    p['loc'] = dict(title='Em Jurerê Tradicional', area='Jurerê · Florianópolis',
                    address='R. Jurerê Tradicional, 544 - Jurerê, Florianópolis - SC',
                    maps_q='Pousada Elemar, R. Jurerê Tradicional 544, Florianópolis', maps_url=MAPS,
                    getting=['Praia de Jurerê: cerca de 800 m', 'Mercados, padaria e restaurantes: perto', 'Aeroporto de Florianópolis: cerca de 35 km'],
                    nearby=['Praia de Jurerê e Jurerê Internacional', 'Praia do Forte e Daniela', 'Canasvieiras e Ingleses'])
    google = [
        ('Ricardo T.', 'Receptividade que nos surpreendeu! Viviani e toda a família do seu Elemar nos atenderam muito bem! Quartos limpos, organizados. Voltaremos em breve!'),
        ('Marcio R.', 'A melhor pousada de Jurerê, atendimento nota mil, seu Elemar muito simpático, apartamentos bem equipados e tudo muito limpo.'),
        ('Alex C.', 'Uma pousada simples, porém extremamente aconchegante. Ponto máximo? O carinho e atenção dispensados aos hóspedes pelo senhor Elemar e sua família. Super recomendo.'),
        ('Fábio M.', 'Lugar acolhedor, atendimento nota 1000, ambiente familiar, lugar calmo, ideal para quem quer descansar e próximo de mercados, padaria e festas. Recomendo.'),
        ('Helton B.', 'Perfeita pousada para uma excursão, alojamento com ar-condicionado, armário, banheiro, cama, guarda-roupa, TV, próximo ao mar.'),
        ('Rangel M.', 'Com toda certeza voltaremos! Direção super atenciosa, seu Elemar é uma pessoa incrível!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(sub='Hóspedes elogiam o carinho da família, a limpeza e a localização.',
                        headline='4,8 no Google · 62 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', '4,8 no Google · 62 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Vem pra Jurerê?', sub='Fale direto com a família Elemar pelo WhatsApp e garanta seu apartamento.')
    return p
