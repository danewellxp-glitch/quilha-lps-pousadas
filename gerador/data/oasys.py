"""OASYS - Floripa (Praia Mole / Lagoa da Conceição) — LP no template 'stayora'.
Hospedagem + centro holístico + eventos. As acomodações são reservadas hoje pelo Airbnb (links no linktr.ee)."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('oasys')
MAPS = 'https://www.google.com/maps/search/?api=1&query=OASYS+-+Floripa+Praia+Mole+Florianopolis'

T = dict(bg='#f6f3ee', alt='#ebe6dc', ink='#14211f', ink2='#1b2a28', muted='#56625f', dim='#b8bdb6',
         dark='#0e1b1a', card='#f6f3ee', accent='#1f8a83', line='#dcd8ce')

P = dict(
    slug='oasys', name='OASYS - Floripa', short='OASYS Floripa',
    seo_title='OASYS Floripa | Hospedagem e santuário com vista para a Lagoa da Conceição',
    meta_desc='OASYS Floripa: casas, lofts e chalés no morro entre a Praia Mole e a Lagoa da Conceição, com piscina, pôr do sol sobre a lagoa, yoga e terapias integrativas. Nota 4,8 no Google.',
    phone='(48) 98864-2588', wa_number='5548988642588', email='',
    wa_text='Olá! Vim pelo site do OASYS Floripa e queria consultar disponibilidade.',
    instagram='oasys.floripa', maps_url=MAPS,
    address='Rod. Jorn. Manoel de Menezes, 631 · Praia Mole, Florianópolis/SC · 88061-700', checkin='14h', checkout='11h',
    footer_tag='Um santuário de experiências na Ilha da Magia: hospedagem, centro holístico e eventos.',
    nav=[('O santuário', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Acomodações', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#1f8a83', '#c0702c', '#4f7a3a', '#7a5c3e', '#a8476b', '#3c5a7a', '#6b5b95', '#b5762a']


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(16, True), alt='Varanda com rede e o pôr do sol sobre a Lagoa da Conceição',
                     title='Um oásis entre a Praia Mole e a Lagoa',
                     sub='Casas, lofts e chalés no meio da mata, com piscina, o pôr do sol mais bonito da ilha e vivências pra corpo e alma.',
                     avatars=[('V', '#1f8a83'), ('L', '#c0702c'), ('T', '#4f7a3a')],
                     proof='Nota 4,8', proof_sub='42 avaliações no Google')
    p['about'] = dict(imgs=[g(48), g(36)], alts=['Piscina e casas do OASYS entre as palmeiras', 'Casa em torre no meio da mata'],
                      stat_num='4.8', stat_dec=1, stat_txt='4,8', stat_label='Nota no Google',
                      kicker='O santuário', title='Hospedagem, centro holístico e eventos num só lugar.',
                      text='O OASYS fica no morro entre a Praia Mole e a Lagoa da Conceição, cercado de mata atlântica. São seis acomodações independentes, de loft pra casal a casa pra grupos, com piscina de frente pra lagoa e espaços pra yoga, terapias integrativas, retiros e celebrações.')
    p['amen_title'] = 'Natureza, conforto e tempo pra você.'
    p['amenities'] = [('pool', 'Piscina com vista'), ('lagoon', 'Vista da Lagoa da Conceição'), ('leaf', 'Varandas com rede'),
                      ('kitchen', 'Cozinha nas acomodações'), ('snow', 'Ar-condicionado'), ('sparkle', 'Terapias integrativas'),
                      ('sun', 'Aulas de yoga'), ('bath', 'Banheira (Morada dos Manacás)'), ('food', 'Churrasqueira'),
                      ('users', 'Espaço para eventos e retiros'), ('wave', 'Praia Mole a ~500 m'), ('clock', 'Check-in 14h · check-out 11h')]
    p['spaces_title'] = 'Cada canto com a lagoa no horizonte.'
    p['spaces'] = [dict(img=g(34), title='Sala com rede', text='Pé-direito alto, rede na janela e a lagoa inteira emoldurada.'),
                   dict(img=G(12), title='Piscina e deck', text='Espreguiçadeiras, guarda-sóis e a vista do pôr do sol sobre a Lagoa da Conceição.'),
                   dict(img=g(22), title='Suítes', text='Cama de casal, ar-condicionado e janelas abertas pro verde.'),
                   dict(img=g(56), title='Salão holístico', text='Arcos de tijolo, luz natural e espaço pra yoga, vivências e encontros.'),
                   dict(img=g(39), title='Roda de fogo', text='Círculo de pedras na mata para cerimônias e rodas de conversa.')]
    p['host'] = dict(img=g(32), alt='Hóspede meditando à beira da piscina com vista para a lagoa', name='Equipe OASYS',
                     lines=[('sparkle', 'Terapias integrativas e massagem'), ('sun', 'Yoga e vivências'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='O pôr do sol mais lindo que já vi! Um verdadeiro refúgio, um Oásis!',
                     text='Palavras da Valéria, uma das hóspedes. No OASYS a equipe recebe de perto, ajuda com tudo e oferece terapias holísticas pra quem quer desacelerar de verdade.')
    p['plan'] = dict(kicker='Acomodações', title='Seis casas, lofts e chalés, do casal ao grupo.',
                     foot='Capacidades conforme os anúncios atuais no Airbnb · fotos ilustrativas, confirme os detalhes com a pousada',
                     rooms=[dict(name='Morada dos Manacás', note='até 10 hóspedes', img=G(94),
                                 cells=['4 quartos', '6 camas', '3 banheiros', 'Banheira', 'Casa inteira pra grupos']),
                            dict(name='Casa Lírio da Paz', note='até 6 hóspedes', img=G(104),
                                 cells=['1 quarto', '4 camas', '1 banheiro', 'Casa de hóspedes', 'Vista da lagoa']),
                            dict(name='Loft Girassol', note='até 5 hóspedes', img=g(8),
                                 cells=['1 quarto', '3 camas', '1 banheiro', 'Loft com cozinha', 'Janelas pra lagoa']),
                            dict(name='Loft Beija-Flor', note='até 4 hóspedes', img=g(12),
                                 cells=['1 quarto', '2 camas', '1 banheiro', 'Loft', 'Vista pro verde']),
                            dict(name='Chalé Jasmim', note='até 4 hóspedes', img=g(22),
                                 cells=['1 quarto', '1 cama', '1 banheiro', 'Chalé', 'Vista da lagoa']),
                            dict(name='Recanto Margarida', note='até 2 hóspedes', img=g(17),
                                 cells=['1 quarto', 'Cama de casal', '1 banheiro', 'Loft para casal', 'Meio da mata'])])
    p['exp'] = dict(title='Vivências, trilhas e o pôr do sol da lagoa.',
                    big=dict(img=g(38, True), title='Cerimônias e vivências', text='Rodas de fogo, cacau, sound healing e encontros com facilitadores convidados.'),
                    wide=dict(img=g(52), title='Pôr do sol na Lagoa', text='Todo fim de tarde o sol se põe atrás da lagoa, bem na frente das varandas.'),
                    list_title='Pertinho daqui',
                    list=[('wave', 'Praia Mole a ~500 m'), ('hike', 'Trilha do Gravatá'), ('hike', 'Trilha da Galheta'), ('food', 'Centrinho da Lagoa')],
                    small=dict(img=g(92), title='Eventos e celebrações', text='Casamentos, retiros e jantares com a lagoa ao fundo.'))
    items = [
        ('Valéria R.', 'Google', 'O pôr do sol mais lindo que já vi! Lugar extremamente tranquilo, com ótimas opções de terapias holísticas. Um verdadeiro refúgio, um Oásis!'),
        ('Matheus C.', 'Google', 'Uma das melhores estadias, sempre recebendo muita atenção e sendo bem acolhido. Um lugar muito energético que também conta com opções de massagem e aulas de yoga.'),
        ('Carolina M.', 'Google', 'Nos hospedamos na Lírio da Paz, uma casinha encantadora para nós quatro. Acordar de manhã com a vista da lagoa é maravilhoso.'),
        ('Lucas N.', 'Google', 'Lugar incrível com uma vista sensacional para a Lagoa da Conceição. Extremamente limpo e organizado por uma equipe muito presente e prestativa!'),
        ('Tamy L.', 'Google', 'Lugar maravilhoso no meio da natureza, perto de uma das praias mais lindas e da trilha do Gravatá. Acomodações confortáveis e com muito estilo.'),
        ('Leti G.', 'Google', 'Fui com um grupo de 12 pessoas e nos deram a casa maior. Ficamos muito confortáveis, com muitos banheiros, tudo perfeito. Recomendo 100%!'),
        ('Luana P.', 'Google', 'O Oasys é um espaço incrível, com uma energia surreal! As acomodações foram muito bem planejadas, super aconchegantes e espaçosas!'),
        ('Roseli S.', 'Google', 'Oasys é um pedaço de paraíso, lugar aonde não se tem vontade de deixar. Excelente atendimento, limpo, organizado e uma atmosfera mágica.'),
    ]
    p['reviews'] = dict(title='O que os hóspedes levam do OASYS.', count=42, rating='4,8',
                        bars=[('Google', '4,8', 96), ('Airbnb · Manacás', '4,85', 97)],
                        note='4,8 no Google · 42 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='4,8 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 14h e o check-out até as 11h. Se precisar de outro horário, combine pelo WhatsApp.'),
                ('Que tipos de acomodação vocês têm?', 'São seis: a Morada dos Manacás (casa pra até 10 pessoas), a Casa Lírio da Paz, os lofts Girassol e Beija-Flor, o Chalé Jasmim e o Recanto Margarida, pra casal.'),
                ('Dá pra ir à praia a pé?', 'Sim. A Praia Mole fica a cerca de 500 m, e a trilha do Gravatá e o centrinho da Lagoa também ficam pertinho.'),
                ('Tem estacionamento?', 'As vagas são poucas, porque o terreno é no morro. Consulte a disponibilidade de vaga antes de chegar.'),
                ('Vocês oferecem terapias e yoga?', 'Sim. O OASYS também é um centro holístico, com terapias integrativas, massagem, aulas de yoga e vivências. Pergunte a agenda.'),
                ('Posso fazer um evento ou retiro aí?', 'Sim. O espaço recebe retiros, workshops, casamentos e celebrações. Chame no WhatsApp para montar a proposta.')]
    p['cta'] = dict(img=G(55, True), title='Reserve seu refúgio de frente pra lagoa.',
                    text='Escolha as datas, chame a gente no WhatsApp e venha viver o OASYS de perto.')
    return p
