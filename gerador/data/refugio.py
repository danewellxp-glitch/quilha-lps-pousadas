from common import ig, gm, review_sources

TEMPLATE = 'doma'
U = 'pousada.refugiodalagoa'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Ref%C3%BAgio+da+Lagoa+Rio+Tavares+Florian%C3%B3polis'

T = dict(bg='#f8f4ee', text='#231a14', muted_text='#62574e', accent='#6b3b22', accent_ink='#f8f1e8', sage='#d9b48c',
         label='#a0522d', band='#ece2d3', line='rgba(35,26,20,.14)', card='#efe7dc')

P = dict(
    slug='refugio', name='Pousada Refúgio da Lagoa', logo_small='Pousada', logo_main='Refúgio da Lagoa',
    meta_desc='Pousada Refúgio da Lagoa no Rio Tavares, sul da Ilha de Florianópolis: chalés de madeira, jardim, aceita pets e praia a poucos minutos a pé.',
    phone='(48) 99668-7794', wa_number='5548996687794', email='',
    wa_text='Olá! Vim pelo site da Refúgio da Lagoa e queria consultar disponibilidade.',
    instagram='pousada.refugiodalagoa', footer_tag='Chalés de madeira no sul da Ilha de Florianópolis.',
)


def context(I, wa):
    g = lambda i: I(ig(U, i))[0]
    G = lambda n: I(gm('refugio/' + n))[0]
    Gi = lambda n: I(gm('refugio/' + n))
    gi = lambda i: I(ig(U, i))
    p = dict(P)
    p['hero'] = dict(img=G('gm2_029_4032x2268.jpg'), alt='Chalés de madeira e jardim da Pousada Refúgio da Lagoa',
                     title='Um refúgio de madeira no sul da Ilha',
                     sub='Chalés rústicos, jardim tropical e a praia a poucos minutos a pé')
    p['intro'] = ['A Refúgio da Lagoa é uma pousada de madeira escondida numa rua tranquila do Rio Tavares, entre a Lagoa da Conceição e o Campeche.',
                  'Aqui o dia começa na rede da varanda e termina no pôr do sol da praia. Seu cachorro também é bem-vindo.']
    p['about'] = dict(label='A pousada', title='Rústica, aconchegante e cheia de verde',
                      sub='Arquitetura toda em madeira, muitas janelas e um jardim que abraça os chalés.',
                      img=G('gm2_008_2880x1920.jpg'), alt='Jardim com mesa e os chalés de madeira',
                      feats=[dict(icon='bed', title='Suítes e lofts', text='Quartos coloridos com ar-condicionado e lofts com cozinha para estadias mais longas.'),
                             dict(icon='paw', title='Pet friendly', text='Hóspedes podem trazer o cachorro, sem cobranças absurdas por isso.'),
                             dict(icon='wave', title='Praia a pé', text='Um caminho bonito e tranquilo leva até a praia em 5 a 10 minutos.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('coffee', 'Café da manhã'), ('car', 'Estacionamento'), ('snow', 'Ar-condicionado'),
        ('paw', 'Aceita pets'), ('food', 'Churrasqueira'), ('kitchen', 'Lofts com cozinha'), ('clock', 'Check-in 14h · check-out 11h')]]
    gal = [('G', 'gm2_007_3024x4032.jpg'), ('I', 11), ('G', 'gm2_006_3820x2866.jpg'), ('G', 'gm2_020_4032x3024.jpg'),
           ('I', 2), ('G', 'gm2_019_3959x2969.jpg'), ('G', 'gm2_013_3024x4032.jpg'), ('I', 27), ('G', 'gm2_010_4032x3024.jpg'), ('I', 26)]
    imgs = []
    for k, v in gal:
        s, w, h = Gi(v) if k == 'G' else gi(v)
        imgs.append(dict(src=s, w=w, h=h, alt='Refúgio da Lagoa'))
    p['gallery'] = dict(title='Cada canto, feito à mão', sub='Madeira, cores e plantas em cada detalhe da pousada.', imgs=imgs)
    p['exp'] = dict(title='Além da pousada',
                    sub='No sul da Ilha tem praia, lagoa e trilha pra todo gosto. A gente manda as dicas de onde ir e onde comer pelo WhatsApp.',
                    cards=[dict(img=g(27), alt='Pôr do sol na praia', title='Praias do sul da Ilha',
                                text='Campeche, Morro das Pedras e Joaquina ficam a poucos minutos. A mais perto dá pra ir a pé.'),
                           dict(img=g(26), alt='Stand up paddle entre a mata', title='Lagoa e stand up',
                                text='Remar entre o mangue e a mata, ou passar a tarde na Lagoa da Conceição.'),
                           dict(img=g(2), alt='Leitura na rede da varanda', title='Rede e descanso',
                                text='Tem dia que o melhor programa é a rede da varanda e um bom livro.')])
    p['band'] = G('gm2_030_4608x3072.jpg')
    p['loc'] = dict(title='No coração do sul da Ilha', area='Rio Tavares · Campeche',
                    address='Servidão Vilmar Sotero de Farias, 160 - Rio Tavares, Florianópolis - SC, 88048-417',
                    maps_q='Pousada Refúgio da Lagoa, Servidão Vilmar Sotero de Farias 160, Florianópolis', maps_url=MAPS,
                    getting=['Aeroporto de Florianópolis: cerca de 15 min de carro', 'Centro de Florianópolis: cerca de 30 min de carro'],
                    nearby=['Praia a 5–10 min a pé', 'Lagoa da Conceição', 'Campeche e Joaquina'])
    items = [
        ('Mariana A.', 'Incrível! Atendimento impecável, super atencioso! Tudo muito limpo e charmoso! Energia incrível, a praia tá a uns 5-10 minutos a pé, um caminho muito delicioso e lindo pra chegar lá!'),
        ('Thaina C.', 'Eu amei demais o lugar, a Renata é muito atensiosa (…) top demais tudo de madeira, amo ❤️'),
        ('Villefort', 'Pousada linda! Bairro tranquilo, bonito, pertinho de uma praia linda. Fui a pé. Destaque para a qualidade do chuveiro.'),
        ('Viviane B.', 'O melhor de tudo é q vc pode levar o seu cão desde que seja comportado, é claro! Eu levei a minha Golden Retriever Maya e foi super tranquilo.'),
        ('Bianca J.', 'Lugar muito aconchegante, tranquilo, instalações confortáveis, limpas e funcionais, com decoração rústica encantadora.'),
    ]
    p['reviews'] = dict(sub='Nota 4,6 no Google, com mais de 200 avaliações de hóspedes.', headline='4,6 no Google · 212 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,6', '4,6 no Google · 212 avaliações')]),
                        items=[dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items])
    p['cta'] = dict(title='Pronto pra se refugiar?', sub='Chame a gente no WhatsApp e reserve seu chalé no sul da Ilha.')
    return p
