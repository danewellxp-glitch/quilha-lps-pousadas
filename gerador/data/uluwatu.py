from common import ig2, review_sources

TEMPLATE = 'doma'
U = 'pousadauluwatu'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Uluwatu+Praia+do+Rosa'

T = dict(bg='#faf6f0', text='#1b2226', muted_text='#5a6267', accent='#0f4c5c', accent_ink='#fbf6ee', sage='#f2b880',
         label='#d9691f', band='#f3e7d6', line='rgba(27,34,38,.14)', card='#f1ebe2')

P = dict(
    slug='uluwatu', name='Pousada Uluwatu', logo_small='Pousada', logo_main='Uluwatu',
    meta_desc='Pousada Uluwatu, cabanas e suítes no centrinho da Praia do Rosa: piscina, café da manhã, estacionamento e nota 4,6 no Google.',
    phone='(48) 9206-6200', wa_number='554892066200', email='',
    wa_text='Olá! Vim pelo site da Pousada Uluwatu e queria consultar disponibilidade.',
    instagram='pousadauluwatu', footer_tag='Cabanas e suítes. Surf, sol e serenidade na Praia do Rosa.',
)


def context(I, wa):
    g = lambda i: I(ig2(U, i))[0]
    gi = lambda i: I(ig2(U, i))
    p = dict(P)
    p['hero'] = dict(img=g(28), alt='Piscina e jardim da Pousada Uluwatu', title='Surf, sol e serenidade',
                     sub='Cabanas e suítes no centrinho da Praia do Rosa')
    p['intro'] = ['A Uluwatu é um refúgio de paz no coração da Praia do Rosa. Cabanas e suítes cercadas de jardim, piscina para o fim de tarde e redes espalhadas pelas varandas.',
                  'Daqui você vai a pé até o centrinho, pega as trilhas para as praias e volta pra um café da manhã caprichado no dia seguinte.']
    p['about'] = dict(label='A pousada', title='Um refúgio no centrinho do Rosa',
                      sub='Tijolinho, madeira, muito verde e o cuidado de quem conhece cada canto da praia.',
                      img=g(117), alt='Piscina e cabanas da Uluwatu no fim de tarde',
                      feats=[dict(icon='bed', title='Cabanas e suítes', text='Quartos com ar-condicionado, cama confortável, roupa de cama cheirosa e chuveiro bem quentinho.'),
                             dict(icon='pool', title='Piscina e jardim', text='Piscina no meio do jardim, deck com redes e muito verde para descansar.'),
                             dict(icon='wave', title='Praia a pé', text='Centrinho do Rosa ao lado e o Rosa Norte a uma caminhada de 15 a 20 minutos.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('coffee', 'Café da manhã incluído'), ('car', 'Estacionamento incluído'), ('pool', 'Piscina'),
        ('snow', 'Ar-condicionado'), ('paw', 'Aceita pets'), ('kitchen', 'Cozinha em algumas cabanas'), ('leaf', 'Varandas com rede'),
        ('check', 'Água filtrada nos quartos'), ('home', 'Área com varal e tanque')]]
    gal = [21, 10, 16, 27, 38, 19, 36, 24, 97, 60, 91, 69]
    p['gallery'] = dict(title='Cada canto, sem pressa', sub='Jardim, piscina, cabanas e o café da manhã da Uluwatu.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Pousada Uluwatu') for i in gal])
    p['exp'] = dict(title='Além da pousada',
                    sub='A Praia do Rosa tem onda, trilha, lagoa e pôr do sol. A gente indica o melhor programa pro seu dia.',
                    cards=[dict(img=g(1), alt='Surfista na Praia do Rosa', title='Surf', text='Ondas para todos os níveis na Praia do Rosa, com escolas e aluguel de prancha pertinho.'),
                           dict(img=g(114), alt='Mirante da Praia do Rosa', title='Trilhas e mirantes', text='Trilhas que saem do centrinho para o Rosa Norte, o Rosa Sul e os mirantes da praia.'),
                           dict(img=g(46), alt='Pôr do sol na lagoa', title='Lagoa de Ibiraquera', text='O pôr do sol mais bonito da região, com stand up e kitesurf na lagoa.')])
    p['band'] = g(54)
    p['loc'] = dict(title='No centrinho da Praia do Rosa', area='Praia do Rosa · Imbituba',
                    address='Estrada Geral Praia do Rosa - Ibiraquera, Imbituba - SC, 88780-000',
                    maps_q='Pousada Uluwatu, Praia do Rosa, Imbituba', maps_url=MAPS,
                    getting=['Praia do Rosa: cerca de 900 m', 'Rosa Norte: 15 a 20 min a pé', 'Aeroporto de Florianópolis: cerca de 1h30 de carro'],
                    nearby=['Centrinho do Rosa, restaurantes e lojas', 'Trilhas para as praias', 'Lagoa de Ibiraquera'])
    items = [
        ('Luciana P.', 'Ótima localização na Praia do Rosa, pertinho do centrinho! Espaço muito aconchegante e com ótimo serviço! Espaço bom nos quartos, varanda com rede, piscina. Se voltar no Rosa, volto na Uluwatu.'),
        ('Alessandra A.', 'Experiência simplesmente incrível! A pousada é charmosa, acolhedora e muito bem cuidada, perfeita para relaxar e curtir a Praia do Rosa.'),
        ('Marcela M.', 'As camas são muito confortáveis e a roupa de cama é muito cheirosa, o quarto muito limpo, até água filtrada tem! Um luxo só, a piscina muito limpinha e o café da manhã é muito gostoso e aconchegante.'),
        ('Guilherme L.', 'Ficamos 5 dias em família, eu, minha esposa e nossos dois filhos (sendo um pequeno), e desde o primeiro momento nos sentimos acolhidos. O ambiente é extremamente aconchegante, organizado e muito bem cuidado.'),
        ('Vanessa K.', 'Localização excelente, perto de restaurantes e uma caminhadinha de 15-20 minutos até o Rosa Norte. O quarto é confortável e limpo. Chuveiro super quentinho!'),
        ('Ana Claudia C.', 'Quartos incríveis, tudo limpo e organizado. Os anfitriões são muito queridos e atenciosos. Além do local ser perto de tudo. Centrinho, trilhas para as praias. Com certeza irei voltar.'),
        ('Robertablee', 'Pousada agradável, ótima localização com estacionamento incluído e um café da manhã gostoso.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    rv.insert(3, dict(key='tripadvisor', text='Uma experiência incrível! pousada é muito bem localizada, perfeita para fazer as trilhas para a praia e a região com facilidade. As acomodações são extremamente confortáveis e aconchegantes.',
                      author='andr_dK2635OT', source='Tripadvisor', stars=5))
    p['reviews'] = dict(sub='Nota 4,6 no Google, com quase 190 avaliações de hóspedes.', headline='4,6 no Google · 189 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,6', '4,6 no Google · 189 avaliações'),
                                                ('tripadvisor', 'Tripadvisor', '4,5', '4,5 no Tripadvisor')]),
                        items=rv)
    p['cta'] = dict(title='Pronto pra pegar onda?', sub='Fale com a gente pelo WhatsApp e garanta sua cabana na Praia do Rosa.')
    return p
