from common import ig2, review_sources

TEMPLATE = 'doma'
U = 'pousadalosamigoscampeche'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Los+Amigos+Campeche+Florian%C3%B3polis'

T = dict(bg='#faf6f1', text='#2a1d17', muted_text='#66574e', accent='#8a3b23', accent_ink='#fbf4ec', sage='#f1b48d',
         label='#c8702c', band='#f5e5d6', line='rgba(42,29,23,.14)', card='#f1e9df'

)

P = dict(
    slug='losamigos', name='Pousada Los Amigos', logo_small='Pousada', logo_main='Los Amigos',
    meta_desc='Pousada Los Amigos no Campeche, Florianópolis: piscina, café da manhã, suítes com ar e smart TV, a poucos minutos a pé da praia.',
    phone='(48) 99638-9917', wa_number='5548996389917', email='',
    wa_text='Olá! Vim pelo site da Pousada Los Amigos e queria consultar disponibilidade.',
    instagram='pousadalosamigoscampeche', footer_tag='No Campeche, a poucos minutos da praia.',
)


def context(I, wa):
    g = lambda i: I(ig2(U, i))[0]
    gi = lambda i: I(ig2(U, i))
    p = dict(P)
    p['hero'] = dict(img=g(95), alt='Praia do Campeche com a Ilha do Campeche ao fundo', title='Entre amigos, no Campeche',
                     sub='Pousada com piscina e café da manhã, a poucos minutos a pé da praia')
    p['intro'] = ['A Los Amigos fica numa rua tranquila do Campeche, perto da praia, das pizzarias, cafés e sorveterias do bairro.',
                  'Suítes confortáveis, piscina no jardim e um café da manhã caprichado, com o atendimento de quem recebe hóspede como amigo.']
    p['about'] = dict(label='A pousada', title='Simples, limpa e acolhedora',
                      sub='Jardim com piscina, quiosque coberto e suítes pensadas para descansar depois da praia.',
                      img=g(57), alt='Piscina da Pousada Los Amigos',
                      feats=[dict(icon='bed', title='Suítes', text='Banheiro privativo, ar-condicionado, ventilador de teto, frigobar e smart TV.'),
                             dict(icon='pool', title='Piscina e quiosque', text='Piscina no jardim e quiosque coberto com mesas para o café e o fim de tarde.'),
                             dict(icon='wave', title='Praia a pé', text='A praia do Campeche fica a poucos minutos de caminhada, de frente para a Ilha do Campeche.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('coffee', 'Café da manhã incluído'), ('car', 'Estacionamento'), ('pool', 'Piscina'),
        ('snow', 'Ar-condicionado e ventilador de teto'), ('tv', 'Smart TV'), ('kitchen', 'Frigobar'), ('paw', 'Aceita pets'),
        ('key', 'Serviço de camareira'), ('plane', 'Traslado do aeroporto (sob consulta)')]]
    gal = [11, 10, 65, 0, 24, 37, 15, 8, 79, 66]
    p['gallery'] = dict(title='Cada canto, entre amigos', sub='Piscina, quiosque, café e o Campeche logo ali.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Pousada Los Amigos') for i in gal])
    p['exp'] = dict(title='Além da pousada',
                    sub='O Campeche tem praia, ilha, trilha e vida de bairro. A gente indica o melhor programa pro seu dia.',
                    cards=[dict(img=g(67), alt='Ilha do Campeche vista da praia', title='Ilha do Campeche',
                                text='Água cristalina e trilhas arqueológicas. Os barcos saem da praia, pertinho da pousada.'),
                           dict(img=g(80), alt='Barco de pescador no Campeche', title='Vila de pescadores',
                                text='Os barcos coloridos e a pesca artesanal fazem parte da paisagem do Campeche.'),
                           dict(img=g(84), alt='Trilha e praia no sul da Ilha', title='Trilhas do sul da Ilha',
                                text='Morro das Pedras, Armação, Matadeiro e Lagoinha do Leste a poucos minutos de carro.')])
    p['band'] = g(86)
    p['loc'] = dict(title='No coração do Campeche', area='Campeche · Florianópolis',
                    address='Serv. Arvoredo, 61 - Campeche, Florianópolis - SC, 88063-120',
                    maps_q='Pousada Los Amigos, Servidão Arvoredo 61, Campeche, Florianópolis', maps_url=MAPS,
                    getting=['Praia do Campeche: poucos minutos a pé', 'Aeroporto de Florianópolis: cerca de 15 min de carro'],
                    nearby=['Pizzarias, bares, cafés e sorveterias', 'Supermercado e padaria', 'Ilha do Campeche'])
    items = [
        ('Neide M.', 'Nossa estadia foi muito boa, a pousada fica bem próxima à praia do Campeche, na altura da ilha do Campeche, com restaurantes, mercados, padaria bem próximos. Café da manhã delicioso, os anfitriões foram muito atenciosos e flexíveis com nosso check-in.'),
        ('Rafaela F.', 'Ótima localização, próximo às pizzarias/bares/cafés e supermercado. A praia fica uns 10 minutos a pé. Pousada limpa e organizada. Café da manhã com bastante variedade. A Elisângela foi super atenciosa!'),
        ('Valeria R.', 'Um lugar incrível, desde a recepção, estadia e último dia, tudo incrível e super indico! Ficamos super à vontade e recebemos todo o cuidado. Voltarei com certeza!'),
        ('Cida S.', 'Lugar maravilhoso, muito calmo e aconchegante, café da manhã muito bom, quarto com tv, ar condicionado e ventilador, piscina. Atendimento nota 10 🥰'),
        ('Tamyris F.', 'Atendimento ótimo! Sr. Francisco foi muito prestativo desde o primeiro contato por telefone! (…) achei a pousada muito limpa e o café da manhã maravilhoso.'),
        ('Sara L.', 'Boa localização, poucos minutos para a praia. Tem um bom café da manhã. (…) Lugar familiar, a anfitriã é bastante atenciosa e prestativa. Meus pequenos foram bem recebidos.'),
        ('Ivan', 'Destaco a localização excelente com muita proximidade de comércio de diversos tipos: sorveteria, cafeteria, lojas, supermercados. (…) Café da manhã muito bom. Camas, travesseiros, toalhas, chuveiros ótimos.'),
    ]
    p['reviews'] = dict(sub='Nota 4,7 no Google, com mais de 130 avaliações de hóspedes.', headline='4,7 no Google · 138 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,7', '4,7 no Google · 138 avaliações')]),
                        items=[dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items])
    p['cta'] = dict(title='Bora pro Campeche?', sub='Chame a gente no WhatsApp e garanta sua suíte.')
    return p
