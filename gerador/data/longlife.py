"""Long Life Campeche Pousada (Campeche, Florianópolis) — LP no template 'stayora'."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('longlife')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Long+Life+Campeche+Pousada+Florian%C3%B3polis'

T = dict(bg='#f7f6f2', alt='#eceae3', ink='#121411', ink2='#1b1d19', muted='#5a5c55', dim='#babbb4',
         dark='#0e100d', card='#f7f6f2', accent='#3f7d3a', line='#dddcd4')

P = dict(
    slug='longlife', name='Long Life Campeche Pousada', short='Long Life',
    seo_title='Long Life Campeche Pousada | Pousada pequena e tranquila no Campeche',
    meta_desc='Long Life Campeche Pousada: chalés de madeira numa rua tranquila do Campeche, em Florianópolis, café da manhã na cesta e as dicas do Rafa, o anfitrião. Nota 9,6 no Booking e 4,7 no Google.',
    phone='(48) 99993-3135', wa_number='5548999933135', email='',
    wa_text='Olá! Vim pelo site da Long Life Campeche e queria consultar disponibilidade.',
    instagram='longlifecampeche', maps_url=MAPS,
    address='Servidão dos Açorianos · Campeche, Florianópolis/SC · 88063-462', checkin='', checkout='11h',
    footer_tag='Pousada pequena e tranquila na Praia do Campeche. O nosso maior luxo é o calor humano.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Quartos', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#3f7d3a', '#c0702c', '#2a6f97', '#7a5c3e', '#a8476b', '#3c5a7a', '#6b5b95', '#5f7f2f']


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(11, True), alt='Pôr do sol na Praia do Campeche, com a Ilha do Campeche ao fundo',
                     title='Seu canto de paz na Praia do Campeche',
                     sub='Chalés de madeira numa rua tranquila, café da manhã na cesta e a praia a uma caminhada.',
                     avatars=[('G', '#3f7d3a'), ('A', '#c0702c'), ('J', '#2a6f97')],
                     proof='Nota 9,6', proof_sub='129 avaliações no Booking')
    p['about'] = dict(imgs=[G(8), G(20)], alts=['Chalé de madeira com escada e plantas', 'Porta de um chalé com flores no deck'],
                      stat_num='9.6', stat_dec=1, stat_txt='9,6', stat_label='Nota no Booking',
                      kicker='A pousada', title='Uma pousada pequena, feita com calor humano.',
                      text='A Long Life fica numa servidão calma do Campeche, onde dá pra acordar com o som dos passarinhos. São chalés de madeira com varanda pro jardim, ar-condicionado e tudo muito limpo. Quem recebe é o Rafa, que conhece cada trilha, onda e restaurante do sul da Ilha.')
    p['amen_title'] = 'O essencial pra descansar, sem complicação.'
    p['amenities'] = [('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('coffee', 'Café da manhã incluso'),
                      ('car', 'Estacionamento'), ('leaf', 'Varanda com vista pro jardim'), ('kitchen', 'Cozinha em alguns quartos'),
                      ('tv', 'TV e frigobar'), ('wave', 'Praia do Campeche a pé'), ('hike', 'Dicas de trilhas e passeios'),
                      ('heart', 'Acolhe a comunidade LGBTQ+'), ('shield', 'Rua tranquila e segura'), ('clock', 'Check-out até 11h')]
    p['spaces_title'] = 'Madeira, jardim e aquele clima de casa de praia.'
    p['spaces'] = [dict(img=G(15), title='Quarto', text='Cama confortável, roupa de cama de qualidade, ar-condicionado e frigobar.'),
                   dict(img=G(35), title='Varanda com pergolado', text='Cadeiras de madeira, plantas e sombra pra ler ou tomar um café.'),
                   dict(img=G(12), title='Chalés à noite', text='Luz quente, silêncio e o céu do Campeche depois da praia.'),
                   dict(img=G(21), title='Quarto com clima de surf', text='Prancha na parede, madeira e iluminação aconchegante.'),
                   dict(img=G(14), title='Deck do jardim', text='O cantinho do violão, com a prancha One Love pintada pela casa.')]
    p['host'] = dict(img=g(88), alt='Rafa, o anfitrião, com a prancha One Love', name='Rafa, anfitrião',
                     lines=[('star', '10 em atendimento no Booking'), ('wave', 'Surfista e trilheiro'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='O Rafa é sensacional, anfitrião de milhões, cara gente boa, simpático, dá altas dicas de passeios e lugares pra conhecer na ilha.',
                     text='Palavras da Gabriela, que já se hospedou três vezes na Long Life. Surfista e trilheiro, o Rafa recebe cada hóspede com as melhores dicas do sul da Ilha.')
    p['plan'] = dict(kicker='Quartos', title='Escolha o seu cantinho na Long Life.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Quarto Queen com Varanda', note='até 2 hóspedes', img=G(29),
                                 cells=['Cama queen-size', 'Varanda térrea', 'Vista pro jardim', 'Ar-condicionado', 'Banheiro privativo']),
                            dict(name='Quarto Duplo Deluxe', note='até 2 hóspedes', img=g(153),
                                 cells=['Cama de casal', 'Ar-condicionado', 'Frigobar', 'TV', 'Banheiro privativo']),
                            dict(name='Suíte Vista Montanha', note='até 2 hóspedes', img=g(155),
                                 cells=['Cama queen-size', 'Vista pro morro', 'Ar-condicionado', 'Mesa de apoio', 'Banheiro privativo'])])
    p['exp'] = dict(title='O sul da Ilha começa na porta.',
                    big=dict(img=g(83, True), title='Praia do Campeche', text='Surf, caminhada na areia e o pôr do sol com a Ilha do Campeche no horizonte.'),
                    wide=dict(img=g(36), title='Lagoinha do Leste', text='Uma das trilhas mais bonitas de Floripa, entre o mar e a mata.'),
                    list_title='Mais pra explorar',
                    list=[('boat', 'Ilha do Campeche'), ('hike', 'Morro do Lampião'), ('board', 'Surf no Campeche'), ('lagoon', 'Lagoa do Peri')],
                    small=dict(img=G(7), title='Café na cesta', text='O café da manhã chega numa cesta, pra tomar no seu ritmo.'))
    items = [
        ('Gabriela C.', 'Google', 'Já me hospedei 3 vezes na pousada, o Rafa é sensacional, anfitrião de milhões, dá altas dicas de passeios e lugares pra conhecer na ilha, é super solícito!'),
        ('Andrei R.', 'Google', 'A pousada fica em uma rua bem calma, super silenciosa, você escuta apenas os passarinhos ao acordar. Os chalés são bem novinhos, ar condicionado muito bom e tudo super limpo.'),
        ('Francisco', 'Booking', 'O Rafa (anfitrião) é muito gente boa e prestativo. Os quartos são bem limpos, com bom ar condicionado e frigobar.'),
        ('Ivonete C.', 'Google', 'Super limpinho, cheirosinho, e os proprietários são muito atenciosos com os hóspedes, sem tirar a privacidade. O café da manhã vem em uma cesta no quarto, é bem gostoso.'),
        ('Joyce F.', 'Google', 'A pousada nos surpreendeu, principalmente por toda atenção do Rafa. O quarto é super confortável e o café da manhã, que vem numa cesta, também é ótimo.'),
        ('Camargo', 'Booking', 'Uma ótima oportunidade para se hospedar num ambiente familiar, confortável e tranquilo. O café da manhã é gostoso, cama confortável.'),
        ('Thâmara S.', 'Google', 'Fomos muito bem recepcionados pelo Rafa, super simpático e atencioso. O quarto é aconchegante e limpo, numa rua silenciosa mas com fácil acesso à praia.'),
        ('Moreira', 'Booking', 'A gente não conseguia ficar para o café da manhã porque iríamos viajar, e eles nos deixaram um sanduíche, fruta e um iogurte à noite.'),
    ]
    p['reviews'] = dict(title='O tipo de estadia que faz voltar.', count=129, rating='9,6',
                        bars=[('Booking', '9,6', 96), ('Google', '4,7', 94), ('Atendimento', '10', 100)],
                        note='9,6 no Booking · 129 avaliações · 4,7 no Google · 64 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='9,6 no Booking', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-out?', 'O check-out é até as 11h. Para horário de chegada, combine com a gente pelo WhatsApp.'),
                ('O café da manhã está incluso?', 'Sim. O café da manhã vem numa cesta, com tudo embalado, pra você tomar no seu ritmo.'),
                ('A praia fica longe?', 'A Praia do Campeche fica a cerca de 15 minutos a pé, por uma rua tranquila.'),
                ('Tem estacionamento?', 'Sim, a pousada tem estacionamento para os hóspedes.'),
                ('A pousada aceita pets?', 'Não recebemos pets no momento. Chame a gente se tiver dúvidas.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. O Rafa confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=g(2, True), title='Reserve seu canto de paz no Campeche.',
                    text='Escolha as datas, chame a gente no WhatsApp e venha descansar perto do mar.')
    return p
