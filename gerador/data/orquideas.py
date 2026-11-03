"""Pousada Recanto das Orquídeas (São João do Rio Vermelho, perto da Praia do Moçambique) — LP no template 'stayora'.
Anfitrião: Alejo (argentino, segundo as reviews). Os tipos de suíte foram montados a partir das fotos do Maps
(suíte com hidro, suíte família com beliche, suíte casal): confirmar com o dono. Os posts do IG trazem promoções com
preço e outro WhatsApp (48 99153-6854); usado o do Google (48 98416-6288) e nenhum preço."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('orquideas')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Recanto+das+Orqu%C3%ADdeas+S%C3%A3o+Jo%C3%A3o+do+Rio+Vermelho+Florian%C3%B3polis'

T = dict(bg='#f8f6f3', alt='#efe9ee', ink='#1d1420', ink2='#2a1d2d', muted='#655a68', dim='#bdb4bf',
         dark='#1c1320', card='#f8f6f3', accent='#a8407a', line='#e2dae2')

P = dict(
    slug='orquideas', name='Pousada Recanto das Orquídeas', short='Recanto das Orquídeas',
    seo_title='Pousada Recanto das Orquídeas | Ao lado da trilha da Praia do Moçambique',
    meta_desc='Pousada Recanto das Orquídeas, em São João do Rio Vermelho, Florianópolis: suítes com ar-condicionado, piscina, hidromassagem, churrasqueira e pet friendly, ao lado da trilha para a Praia do Moçambique. Nota 5,0 no Google.',
    phone='(48) 98416-6288', wa_number='5548984166288', email='',
    wa_text='Olá! Vim pelo site da Pousada Recanto das Orquídeas e queria consultar disponibilidade.',
    instagram='pousrecantodasorquideas', maps_url=MAPS,
    address='Servidão Caminho das Orquídeas, 293 · São João do Rio Vermelho, Florianópolis/SC · 88060-280', checkin='14h', checkout='11h',
    footer_tag='Natureza, conforto e a Praia do Moçambique ao lado.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Suítes', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#a8407a', '#2f7d6d', '#c0702c', '#3c5a7a', '#6b5b95', '#7a5c3e', '#4f7a3a', '#c06c84']


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(12, True), alt='Piscina da pousada com um cachorrinho no deck',
                     title='Seu refúgio ao lado da Praia do Moçambique',
                     sub='Suítes confortáveis, piscina e hidromassagem, num cantinho tranquilo no meio da natureza do Rio Vermelho.',
                     avatars=[('M', '#a8407a'), ('J', '#2f7d6d'), ('B', '#c0702c')],
                     proof='Nota 5,0', proof_sub='27 avaliações no Google')
    p['about'] = dict(imgs=[g(8), G(26)], alts=['Piscina com deck de madeira', 'Suíte com cama de casal e TV'],
                      stat_num='5.0', stat_dec=1, stat_txt='5,0', stat_label='Nota no Google',
                      kicker='A pousada', title='Tranquilidade, natureza e tudo impecável.',
                      text='O Recanto das Orquídeas fica em São João do Rio Vermelho, colado na trilha que leva à Praia do Moçambique, a maior e uma das mais preservadas da Ilha. Tem suítes com ar-condicionado, piscina, hidromassagem, churrasqueira e cozinha em algumas acomodações, tudo cuidado de perto pelo proprietário.')
    p['amen_title'] = 'Conforto pra descansar de verdade.'
    p['amenities'] = [('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('pool', 'Piscina externa'),
                      ('bath', 'Hidromassagem'), ('car', 'Estacionamento'), ('kitchen', 'Cozinha em algumas suítes'),
                      ('food', 'Churrasqueira'), ('paw', 'Aceita pets'), ('tv', 'TV nas suítes'),
                      ('hike', 'Trilha para o Moçambique ao lado'), ('leaf', 'Cercado de natureza'), ('clock', 'Check-in 14h · check-out 11h')]
    p['spaces_title'] = 'Cada canto pensado pra você relaxar.'
    p['spaces'] = [dict(img=G(29), title='Piscina e deck', text='Piscina com deck, espreguiçadeiras e muito sol no meio do verde.'),
                   dict(img=G(24), title='Hidromassagem', text='Banheira de hidro com iluminação suave, perfeita pra uma noite a dois.'),
                   dict(img=G(16), title='Cozinha equipada', text='Cozinha completa, com cooktop, micro-ondas, geladeira e balcão.'),
                   dict(img=G(19), title='Varanda com mesinha', text='Cantinho de janela pra um café da manhã sem pressa.'),
                   dict(img=G(31), title='Sala de jantar', text='Mesa de madeira maciça, TV e espaço pra família toda.')]
    p['host'] = dict(img=G(0), alt='Casa da pousada com a piscina em frente', name='Alejo e equipe',
                     lines=[('star', 'Nota 5,0 no Google'), ('pin', 'Ao lado da trilha do Moçambique'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='As instalações são excelentes e exatamente como aparecem nas fotos.',
                     text='Palavras do Heber, um dos hóspedes. No Recanto das Orquídeas quem recebe é o próprio dono, com atendimento atencioso a cada detalhe.')
    p['plan'] = dict(kicker='Suítes', title='Escolha a suíte do seu jeito.', foot='Tipos montados a partir das fotos · confirme os detalhes com a pousada',
                     rooms=[dict(name='Suíte com Hidro', note='para casais', img=G(24),
                                 cells=['Cama de casal', 'Hidromassagem', 'Ar-condicionado', 'TV', 'Ideal pra datas especiais']),
                            dict(name='Suíte Casal', note='até 2 hóspedes', img=G(26),
                                 cells=['Cama de casal', 'Ar-condicionado', 'Smart TV', 'Banheiro privativo', 'Janela pro verde']),
                            dict(name='Suíte Família', note='para famílias', img=G(18),
                                 cells=['Cama de casal', 'Beliche', 'Ar-condicionado', 'TV', 'Espaço pras crianças'])])
    p['exp'] = dict(title='A Praia do Moçambique logo ali.',
                    big=dict(img=G(35, True), title='Trilha pela floresta', text='Pela reserva florestal do Rio Vermelho são cerca de 1,5 km até a areia do Moçambique.'),
                    wide=dict(img=G(25), title='Dunas do Moçambique', text='As dunas ficam a uns 200 metros da pousada.'),
                    list_title='Mais pra explorar',
                    list=[('wave', 'Praia do Moçambique'), ('hike', 'Reserva do Rio Vermelho'), ('lagoon', 'Lagoa da Conceição'), ('wave', 'Barra da Lagoa')],
                    small=dict(img=G(12), title='Pet friendly', text='Seu bichinho é bem-vindo como parte da família.'))
    items = [
        ('Michelle A.', 'Google', 'Fui atendida com muita atenção, cordialidade e carinho. O ambiente é acolhedor, tranquilo e cercado por uma natureza encantadora, perfeito para descansar.'),
        ('Saliza O.', 'Google', 'Pousada incrível em cada detalhe, muito limpa, organizada e super bem localizada, ao lado da trilha do Moçambique, uma das praias mais lindas de Florianópolis.'),
        ('Heber T.', 'Google', 'O primeiro ponto que gostaria de destacar é a fidelidade das instalações: são excelentes e exatamente como aparecem nas fotos.'),
        ('Yanina V.', 'Google', 'Lugar lindo, muito seguro, impecavelmente limpo, atendimento personalizado e, o melhor de tudo, aceitaram nosso animal de estimação como parte da família.'),
        ('Ailen P.', 'Google', 'Excelente lugar para relaxar longe das multidões. A Praia do Moçambique é a mais bonita de todas. A hospitalidade do Alejo foi espetacular!'),
        ('Leandro P.', 'Google', 'Pessoas maravilhosas, muito gentis. O lugar é lindo, limpo e muito tranquilo, ideal para relaxar, aproveitar a piscina e fazer um ótimo churrasco!'),
        ('Betty H.', 'Google', 'Lugar lindo, super tranquilo e perfeito para famílias. O Alejo é muito atencioso, sempre disposto a ajudar.'),
        ('Flor D.', 'Google', 'Adoramos nossa estadia, muito agradável, confortável, com ar-condicionado e perfeita para relaxar. A piscina foi um dos nossos lugares favoritos.'),
    ]
    p['reviews'] = dict(title='Hospedagem nota 5 em cada detalhe.', count=27, rating='5,0',
                        bars=[('Google', '5,0', 100)],
                        note='5,0 no Google · 27 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='5,0 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 14h e o check-out até as 11h. Precisa de outro horário? Combine pelo WhatsApp.'),
                ('A praia fica longe?', 'A trilha para a Praia do Moçambique começa ao lado da pousada. São cerca de 1,5 km pela floresta, ou dá pra ir de carro.'),
                ('Aceita pets?', 'Sim! Seu pet é bem-vindo. Avise na reserva.'),
                ('Tem estacionamento?', 'Sim, a pousada tem estacionamento.'),
                ('As suítes têm cozinha?', 'Algumas acomodações têm cozinha equipada. Pergunte qual é a melhor opção pro seu grupo.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A pousada confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=g(8, True), title='Reserve seu cantinho perto do Moçambique.',
                    text='Escolha as datas, chame no WhatsApp e venha descansar no meio da natureza.')
    return p
