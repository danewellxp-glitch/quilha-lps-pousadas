"""Pousada Duas Irmãs 2 (Servidão José Felisberto de Oliveira, 70, Lagoa da Conceição, Florianópolis) — LP no template 'doma'.
Fotos: Google Maps (gm, só 34 e simples). Apartamentos simples com ar, TV, frigobar e banheiro; estacionamento; sem café da manhã.
Administrada pelas irmãs donas. Nota 4,3 (107)."""
from common import review_sources
from fotos import Fotos

TEMPLATE = 'doma'
ENHANCE = True
F = Fotos('duasirmas2')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Duas+Irm%C3%A3s+2+Lagoa+da+Concei%C3%A7%C3%A3o'

T = dict(bg='#f9f7f0', text='#1b2422', muted_text='#5a6461', accent='#2c6e6a', accent_ink='#fbf8ef', sage='#e9c23f',
         label='#b0832a', band='#e6efe9', line='rgba(27,36,34,.14)', card='#f1eee3')

P = dict(
    slug='duasirmas2', name='Pousada Duas Irmãs 2', logo_small='Pousada', logo_main='Duas Irmãs',
    meta_desc='Pousada Duas Irmãs 2, na Lagoa da Conceição, Florianópolis: apartamentos com ar-condicionado, TV, frigobar e estacionamento, pertinho da lagoa e dos restaurantes.',
    phone='(48) 3232-5131', wa_number='554832325131', email='',
    wa_text='Olá! Vim pelo site da Pousada Duas Irmãs e queria consultar disponibilidade.',
    instagram='', footer_tag='Simples, limpa e com preço justo, de frente pra Lagoa da Conceição.',
)


def context(I, wa):
    g = lambda i: I(F.gm(i))[0]
    gi = lambda i: I(F.gm(i))
    p = dict(P)
    p['hero'] = dict(img=g(21), alt='Lagoa da Conceição com o sol entre as nuvens',
                     title='Sua base na Lagoa da Conceição',
                     sub='Apartamentos práticos com ar-condicionado e estacionamento, pertinho da lagoa, dos restaurantes e das praias do leste')
    p['intro'] = ['A Pousada Duas Irmãs fica numa servidão tranquila da Lagoa da Conceição, a poucos passos da beira da lagoa. É uma hospedagem simples e bem cuidada, tocada pelas próprias irmãs que dão nome à casa.',
                  'Daqui você chega rápido à Joaquina, à Praia Mole e ao centrinho da Lagoa, cheio de bares e restaurantes. Na volta, o apartamento está limpo, gelado e pronto pra descansar.']
    p['about'] = dict(label='A pousada', title='Praticidade com preço justo',
                      sub='Muitos hóspedes voltam sempre, pela localização, pela limpeza e pelo atendimento das donas.',
                      img=g(7), alt='Varanda dos apartamentos',
                      feats=[dict(icon='bed', title='Apartamentos completos', text='Cama de casal e de solteiro, ar-condicionado, TV, frigobar e banheiro privativo.'),
                             dict(icon='car', title='Estacionamento incluso', text='Vaga pro carro no próprio terreno, sem custo extra.'),
                             dict(icon='lagoon', title='De frente pra Lagoa', text='A beira da Lagoa da Conceição fica a poucos passos da pousada.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('snow', 'Ar-condicionado'), ('tv', 'TV'), ('kitchen', 'Frigobar'), ('bath', 'Banheiro privativo'),
        ('car', 'Estacionamento incluso'), ('bed', 'Roupa de cama e banho'), ('lagoon', 'Lagoa a poucos passos'),
        ('food', 'Restaurantes por perto'), ('wave', 'Joaquina a 6 min de carro'), ('users', 'Atendimento das donas')]]
    gal = [31, 8, 5, 15, 4, 6]
    p['gallery'] = dict(title='Conheça a pousada', sub='Os apartamentos, a varanda e a Lagoa da Conceição logo ali.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Pousada Duas Irmãs 2') for i in gal])
    p['exp'] = dict(title='Além da pousada',
                    sub='A Lagoa é o ponto de partida perfeito pra conhecer o leste da Ilha. Pergunte que a gente indica.',
                    cards=[dict(img=g(29), alt='Beira da Lagoa da Conceição', title='Lagoa da Conceição',
                                text='Stand up, caiaque, passeio de barco até a Costa da Lagoa e o pôr do sol na beira da água.'),
                           dict(img=g(24), alt='Centrinho da Lagoa à noite', title='Centrinho da Lagoa',
                                text='Bares, restaurantes de frutos do mar e vida noturna a poucos minutos.'),
                           dict(img=g(22), alt='Pôr do sol na Lagoa', title='Joaquina e Praia Mole',
                                text='Dunas, surfe e mar aberto a cerca de 6 minutos de carro.')])
    p['band'] = g(29)
    p['loc'] = dict(title='Na Lagoa da Conceição', area='Lagoa da Conceição · Leste da Ilha',
                    address='Servidão José Felisberto de Oliveira, 70 - Lagoa da Conceição, Florianópolis - SC, 88062-430',
                    maps_q='Pousada Duas Irmãs 2, Servidão José Felisberto de Oliveira 70, Florianópolis', maps_url=MAPS,
                    getting=['Praia da Joaquina: cerca de 6 min de carro', 'Centro de Florianópolis: cerca de 20 min de carro', 'Aeroporto de Florianópolis: cerca de 30 min de carro'],
                    nearby=['Centrinho da Lagoa', 'Praia Mole e Joaquina', 'Costa da Lagoa'])
    items = [
        ('Sheila G.', 'Um lugar maravilhoso. Tranquilo! Acolhedor! Ótima opção de estadia e a vista direto para a Lagoa da Conceição. Super recomendo.'),
        ('Paula F.', 'Amei a estadia, os quartos são bem amplos, tudo muito limpo e organizado, ótima localização e preço justo. A proprietária é um amor de pessoa.'),
        ('José Guilherme I.', 'Apartamento com cama de casal e uma de solteiro, ar-condicionado, banheiro privativo e estacionamento incluído, de frente para a Lagoa da Conceição. Muitos restaurantes perto.'),
        ('Magaiver P.', 'Ótima localização e apartamentos bem limpos. Ficamos felizes com a escolha. Recomendo.'),
        ('J. Comarú', 'Ótimo atendimento, quarto confortável, ar gelando e ótima localização, bem pertinho da lagoa!'),
        ('Jei R.', 'Experiência excelente. Limpeza, segurança, tranquilidade, conforto. E atendimento com excelência de todos.'),
        ('Márcio M.', 'Excelente localização. As donas são extremamente simpáticas e prestativas.'),
        ('Núbia M.', 'Amamos a recepção das duas irmãs, muito simpáticas e muito alegres.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    p['reviews'] = dict(sub='Mais de 100 avaliações de hóspedes no Google.', headline='4,3 no Google · 107 avaliações',
                        link=MAPS, sources=review_sources([('google', 'Google', '4,3', '4,3 no Google · 107 avaliações')]),
                        items=rv)
    p['cta'] = dict(title='Bora pra Lagoa?', sub='Ligue ou chame a gente pelo WhatsApp e garanta seu apartamento perto da lagoa.')
    return p
