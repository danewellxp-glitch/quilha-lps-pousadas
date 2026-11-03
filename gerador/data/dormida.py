from common import ig, review_sources

TEMPLATE = 'doma'
U = 'dormidadopeixe'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Dormida+do+Peixe+Rua+Central+do+Rosa+Imbituba'

T = dict(bg='#f8f6f1', text='#16211f', muted_text='#56615e', accent='#1f4d55', accent_ink='#f4f1ea', sage='#9cc3bf',
         label='#2a7f79', band='#e1ebe7', line='rgba(22,33,31,.14)', card='#efede6')

P = dict(
    slug='dormida', name='Pousada Dormida do Peixe', logo_small='Pousada', logo_main='Dormida do Peixe',
    meta_desc='Pousada Dormida do Peixe, entre a Lagoa de Ibiraquera e a Praia do Rosa: apartamentos amplos, piscina e nota 5,0 no Google.',
    phone='(48) 99107-1011', wa_number='5548991071011', email='',
    wa_text='Olá! Vim pelo site da Dormida do Peixe e queria consultar disponibilidade.',
    instagram='dormidadopeixe', footer_tag='Tranquilidade e conforto entre a lagoa e o mar.',
)


def context(I, wa):
    g = lambda i: I(ig(U, i))[0]
    gi = lambda i: I(ig(U, i))
    p = dict(P)
    p['hero'] = dict(img=g(29), alt='Caminho de deck pelo jardim até a piscina da Dormida do Peixe',
                     title='Desacelere entre a lagoa e o mar',
                     sub='Apartamentos amplos com vista para as montanhas, a 10 minutos a pé do centrinho do Rosa')
    p['intro'] = ['A Dormida do Peixe foi feita pra quem quer acordar sem pressa. Os apartamentos são novos e amplos, com sala, suíte e varanda com rede olhando para as montanhas, a lagoa e o mar lá no fundo.',
                  'Daqui você vai a pé até o centrinho do Rosa, pega a trilha para o Rosa Norte ou passa a tarde na piscina sem ver o tempo passar.']
    p['about'] = dict(label='A pousada', title='Um cantinho de paz no Rosa',
                      sub='Tudo novo, limpo e espaçoso, com o cuidado de quem recebe cada hóspede pessoalmente.',
                      img=g(30), alt='Piscina com deck de madeira no jardim',
                      feats=[dict(icon='bed', title='Apartamentos amplos', text='Sala, lavabo e suíte com cama grande, ar-condicionado e enxoval de qualidade.'),
                             dict(icon='leaf', title='Varandas com rede', text='Vista para as montanhas e a Lagoa de Ibiraquera, com o mar ao fundo.'),
                             dict(icon='pool', title='Piscina e churrasqueira', text='Área externa com piscina, pátio, churrasqueira e cozinha compartilhada.')])
    p['amenities'] = [dict(icon=i, text=t) for i, t in [
        ('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('pool', 'Piscina'), ('car', 'Estacionamento interno gratuito'),
        ('coffee', 'Café da manhã opcional, das 7h às 10h'), ('kitchen', 'Cozinha compartilhada e churrasqueira'),
        ('paw', 'Aceita pets'), ('key', 'Portão eletrônico e entrada monitorada'), ('clock', 'Check-in 14h · check-out 12h'),
        ('leaf', 'Varandas com rede e vista')]]
    gal = [29, 8, 17, 12, 20, 23, 44, 3, 13, 25]
    p['gallery'] = dict(title='Cada canto, sem pressa', sub='Um olhar de perto na pousada, no jardim e na lagoa logo abaixo.',
                        imgs=[dict(src=gi(i)[0], w=gi(i)[1], h=gi(i)[2], alt='Dormida do Peixe') for i in gal])
    p['exp'] = dict(title='Além da pousada',
                    sub='A gente conhece cada trilha e cada praia da região. Pergunte e a gente indica o melhor programa pro seu dia.',
                    cards=[dict(img=g(26), alt='Faixa de areia da Praia do Rosa', title='Praia do Rosa',
                                text='Uma das praias mais procuradas de Santa Catarina, com o centrinho a cerca de 10 minutos a pé da pousada.'),
                           dict(img=g(21), alt='Placa da trilha Rosa Norte e Lagoa', title='Trilhas',
                                text='A trilha Rosa Norte e Lagoa passa pertinho. Dá pra emendar mar, morro e lagoa no mesmo dia.'),
                           dict(img=g(25), alt='Lagoa de Ibiraquera', title='Lagoa de Ibiraquera',
                                text='Kitesurf, stand up paddle e o pôr do sol mais bonito da região, na beira da lagoa.')])
    p['band'] = g(11)
    p['loc'] = dict(title='Entre a lagoa e o mar', area='Ibiraquera · Praia do Rosa',
                    address='Rua Central do Rosa, s/n - Ibiraquera, Imbituba - SC, 88780-000',
                    maps_q='Dormida do Peixe, Rua Central do Rosa, Imbituba', maps_url=MAPS,
                    getting=['Centrinho do Rosa: cerca de 10 min a pé', 'Garopaba: cerca de 20 min de carro', 'Aeroporto de Florianópolis: cerca de 1h30 de carro'],
                    nearby=['Praia do Rosa e Rosa Norte', 'Lagoa de Ibiraquera', 'Praia da Barra de Ibiraquera e Praia do Luz'])
    G = 'Google'
    items = [
        ('Suian Q.', 'Minha estadia foi maravilhosa! A pousada é extremamente aconchegante, confortável e transmite uma sensação de paz desde o momento em que cheguei.'),
        ('Elmo L.', 'O grande destaque foi o atendimento do anfitrião, Pedro. Sempre cordial, simpático e prestativo, ele nos ajudou em tudo o que precisamos.'),
        ('Nathália C.', 'O quarto (peguei o mais barato, hein) é muito melhor do que o anunciado. É uma kitnet praticamente, com paisagem linda e dá pra ver o mar ao fundo.'),
        ('Juliana S.', 'Quando cheguei à pousada que percebi o porque ser 5 estrelas no Google. É um apartamento muito bom! Com sala, lavabo + uma suíte!'),
        ('Erika B.', 'Excelente atendimento, os quartos modernos e bem claros, além da decoração ser linda ❤️'),
        ('Elvis F.', 'Local agradável, quartos muito confortáveis e amplos, tem uma sala além do cômodo principal, com redes para descanso e uma bela vista das montanhas.'),
        ('Suellen C.', 'Fomos muito bem recebidos pelos donos. Eles esquentaram a janta do meu bebê e ofereceram tudo que precisava. Super indico o lugar.'),
        ('Claudio M.', 'Pousada simplesmente maravilhosa, anfitriões demais agradáveis, tudo muito limpo, organizado, linda decoração dos quartos.'),
    ]
    rv = [dict(key='google', text=t, author=a, source=G, stars=5) for a, t in items]
    rv.insert(2, dict(key='tripadvisor', text='A pousada é MARAVILHOSA. Super novinha, quartos gigantes com ar condicionado e ventilador, com uma sacadona e vista para as montanhas/lagoa.',
                      author='viagensdacami', source='Tripadvisor', stars=5))
    p['reviews'] = dict(sub='Nota máxima no Google, com mais de 230 avaliações de hóspedes.', headline='5,0 no Google · 235 avaliações',
                        link=MAPS,
                        sources=review_sources([('google', 'Google', '5,0', '5,0 no Google · 235 avaliações'),
                                                ('tripadvisor', 'Tripadvisor', '5/5', '5/5 no Tripadvisor')]),
                        items=rv)
    p['cta'] = dict(title='Pronto pra desacelerar?', sub='Fale direto com a gente pelo WhatsApp e garanta sua data no Rosa.')
    return p
