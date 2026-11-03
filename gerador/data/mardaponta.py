from common import ig2, review_sources

TEMPLATE = 'doma'
U = 'mardaponta'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Residencial+Mar+da+Ponta+Ponta+das+Canas'

T = dict(bg='#f8f7f3', text='#17213a', muted_text='#56607a', accent='#1d3f7a', accent_ink='#f7f5ef', sage='#a9c1e6',
         label='#c2562c', band='#e5ecf5', line='rgba(23,33,58,.14)', card='#eeeee8')

P = dict(
    slug='mardaponta', name='Residencial Mar da Ponta', logo_small='Residencial', logo_main='Mar da Ponta',
    meta_desc='Residencial Mar da Ponta, hospedagem familiar em Ponta das Canas, Florianópolis: chalés e apartamentos com cozinha, pertinho do mar, nota 4,9 no Google.',
    phone='(48) 99828-7939', wa_number='5548998287939', email='',
    wa_text='Olá! Vim pelo site do Residencial Mar da Ponta e queria consultar disponibilidade.',
    instagram='mardaponta', footer_tag='Seu lar na praia com clima de férias.',
)


def context(I, wa):
    g = lambda i: I(ig2(U, i))[0]
    gi = lambda i: I(ig2(U, i))
    p = dict(P)
    p['hero'] = dict(img=g(12), alt='Praia de Ponta das Canas', title='Seu lar na praia',
                     sub='Hospedagem familiar em Ponta das Canas, pertinho do mar')
    p['intro'] = ['O Mar da Ponta é uma hospedagem de família no norte da Ilha de Florianópolis, a poucos passos da praia de Ponta das Canas.',
                  'Chalés e apartamentos completos, com cozinha e churrasqueira, decoração rústica e anfitriões que recebem você como se fosse da casa.']
    p['about'] = dict(label='O residencial', title='Clima de férias, jeito de casa',
                      sub='Varandas de madeira, arcos e muita calma, num bairro tranquilo e cheio de comércio.',
                      img=g(25), alt='Varandas de madeira do Mar da Ponta',
                      feats=[dict(icon='home', title='Chalés e apartamentos', text='Chalé com dois quartos, sala, cozinha e área com churrasqueira. Ótimo para a família toda.'),
                             dict(icon='wave', title='Pertinho do mar', text='A praia de Ponta das Canas fica a poucos passos. Tem quarto com vista para o mar.'),
                             dict(icon='heart', title='Atendimento de família', text='Anfitriões presentes, atenciosos e cheios de dicas sobre o norte da Ilha.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('kitchen', 'Cozinha completa nos chalés e apartamentos'), ('food', 'Churrasqueira'),
        ('car', 'Estacionamento'), ('users', 'Ideal para crianças'), ('clock', 'Check-in 14h · check-out 12h'), ('wave', 'Praia a poucos passos')]]
    gal = [19, 65, 11, 76, 78, 28, 30, 80, 64, 69, 79, 21]
    p['gallery'] = dict(title='Cada canto, com cara de férias', sub='Quartos, apartamentos e o mar de Ponta das Canas.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Residencial Mar da Ponta') for i in gal])
    p['exp'] = dict(title='Além do residencial',
                    sub='O norte da Ilha tem mar calmo, praia de água clara e pôr do sol na areia. A gente indica o melhor pra cada dia.',
                    cards=[dict(img=g(50), alt='Barco na praia de água clara', title='Praias do norte',
                                text='Ponta das Canas, Lagoinha, Brava e Cachoeira do Bom Jesus, todas pertinho.'),
                           dict(img=g(54), alt='Pessoas nas pedras do mar', title='Mar calmo', text='Água tranquila e transparente, perfeita para quem viaja com crianças.'),
                           dict(img=g(47), alt='Pôr do sol na praia', title='Pôr do sol', text='Fim de tarde na areia de Ponta das Canas, com o céu pegando fogo.')])
    p['band'] = g(39)
    p['loc'] = dict(title='No norte da Ilha, pertinho do mar', area='Ponta das Canas · Florianópolis',
                    address='Rua Associação Atlética - Ponta das Canas, Florianópolis - SC, 88056-830',
                    maps_q='Residencial Mar da Ponta, Ponta das Canas, Florianópolis', maps_url=MAPS,
                    getting=['Praia de Ponta das Canas a poucos passos', 'Canasvieiras e Jurerê: poucos minutos de carro', 'Aeroporto de Florianópolis: cerca de 50 min de carro'],
                    nearby=['Praia da Lagoinha', 'Restaurantes, mercado, farmácia e sorveteria a pé'])
    items = [
        ('Mônica T.', 'Simplesmente excelente nossa estadia! O anfitrião Luís e sua esposa, são extremamente atenciosos com tudo. A pousada é mimosa, toda decoração é rústica. Fica bem pertinho da praia em Ponta das Canas.'),
        ('Tiago R.', 'Excelente ambiente, muito tranquilo e aconchegante, dona Aurora muito simpática, quarto ótimo com vista para o mar, bem pertinho da praia.'),
        ('Poliane', 'Local acolhedor, bom custo benefício, próximo da praia e de mercados, com estrutura para que você possa fazer seu almoço, no chalé 2 quartos sendo uma suíte, sala, cozinha, banheiro social e área no fundo com churrasqueira.'),
        ('Cris B.', 'Lugar lindo, ambiente acolhedor, muito organizado e limpo!!! Muito próxima a praia, calmaria literalmente pra descanso. Os anfitriões Talita & Luis muito queridos. Super recomendo!'),
        ('Ezequiel A.', 'Adorei o lugar e o chalé é ótimo, lugar bem tranquilo, atendimento nem se fala, me senti como se fosse da família.'),
        ('Mayara A.', 'Pra quem quer ficar pertinho do mar, essa pousada é a ideal. Anfitriões mega simpáticos e acessíveis. Cozinha compartilhada, mas limpa e organizada. Recomendo.'),
        ('Gabriel G.', 'Eu adorei a pousada, muito bonita e aconchegante. O bairro na qual ela se encontra possui diversos comércios e é pertinho da praia, sendo bem tranquila e segura.'),
    ]
    p['reviews'] = dict(sub='Nota 4,9 no Google, com quase 140 avaliações de hóspedes.', headline='4,9 no Google · 139 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,9', '4,9 no Google · 139 avaliações')]),
                        items=[dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items])
    p['cta'] = dict(title='Bora pra praia?', sub='Chame a gente no WhatsApp e reserve seu chalé em Ponta das Canas.')
    return p
