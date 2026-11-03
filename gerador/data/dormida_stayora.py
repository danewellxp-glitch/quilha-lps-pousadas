"""Demo do template 'stayora' com a Pousada Dormida do Peixe (fotos tratadas)."""
from common import ig
from data.dormida import MAPS, P as LP
from data.dormida_site import gm, U

TEMPLATE = 'stayora'
ENHANCE = True

T = dict(bg='#f7f7f7', alt='#ebecef', ink='#111214', ink2='#1a1a1a', muted='#595959', dim='#b9babd',
         dark='#0b0c0e', card='#f7f7f7', accent='#23807a', line='#dddde4')

P = dict(
    slug='dormida_stayora', name='Pousada Dormida do Peixe', short='Dormida do Peixe',
    seo_title='Pousada Dormida do Peixe | Praia do Rosa e Lagoa de Ibiraquera',
    meta_desc=LP['meta_desc'], phone=LP['phone'], wa_number=LP['wa_number'], email='',
    wa_text=LP['wa_text'], instagram=LP['instagram'], maps_url=MAPS,
    address='Rua Central do Rosa, s/n · Ibiraquera, Imbituba/SC', checkin='14h', checkout='12h',
    footer_tag='Apartamentos amplos com varanda e vista, entre a Lagoa de Ibiraquera e a Praia do Rosa.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Apartamentos', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#23807a', '#b5762a', '#3f6b5c', '#14313a', '#8a5a44', '#2a6f97', '#6b5b95', '#c06c84']


def context(I, wa):
    g = lambda i, big=False: I(ig(U, i), big=big)[0]
    G = lambda i, big=False: I(gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(5, True), alt='Piscina e jardim da Dormida do Peixe vistos do alto',
                     title='Seu refúgio entre a lagoa e o mar',
                     sub='Apartamentos amplos com varanda, piscina no jardim e o centrinho do Rosa a 10 minutos a pé.',
                     avatars=[('S', '#23807a'), ('E', '#b5762a'), ('J', '#3f6b5c')],
                     proof='Nota 5,0', proof_sub='235 avaliações no Google')
    p['about'] = dict(imgs=[G(27), G(12)], alts=['Fachada com palmeiras', 'Sala de um apartamento'],
                      stat_num='5.0', stat_dec=1, stat_txt='5,0', stat_label='Nota no Google',
                      kicker='A pousada', title='Um cantinho de paz feito pra desacelerar.',
                      text='A Dormida do Peixe tem apartamentos novos e amplos, com sala, suíte e varanda com rede olhando para as montanhas, a Lagoa de Ibiraquera e o mar lá no fundo. Tudo limpo, claro e cuidado de perto pela família que recebe cada hóspede.')
    p['amen_title'] = 'Tudo pensado pra uma estadia tranquila.'
    p['amenities'] = [('wifi', 'Wi-Fi gratuito'), ('snow', 'Ar-condicionado'), ('pool', 'Piscina com deck'),
                      ('car', 'Estacionamento interno'), ('coffee', 'Café da manhã opcional'), ('leaf', 'Varandas com rede'),
                      ('paw', 'Aceita pets'), ('key', 'Portão eletrônico'), ('kitchen', 'Cozinha compartilhada'),
                      ('food', 'Churrasqueira'), ('tv', 'TV nos apartamentos'), ('clock', 'Check-in 14h · check-out 12h')]
    p['spaces_title'] = 'Espaço de sobra pra viver o Rosa sem pressa.'
    p['spaces'] = [dict(img=G(12), title='Sala do apartamento', text='Sofá, mesa, frigobar e lavabo: espaço de casa, com cara de pousada.'),
                   dict(img=g(17), title='Varanda com rede', text='Rede, poltronas e a vista das montanhas e da lagoa no fim de tarde.'),
                   dict(img=g(30), title='Piscina e deck', text='Piscina com deck de madeira, espreguiçadeiras e muito verde em volta.'),
                   dict(img=G(4), title='Suíte', text='Cama grande, ar-condicionado, ventilador e enxoval de qualidade.'),
                   dict(img=g(29), title='Jardim', text='O caminho de deck pelo gramado até a piscina, com a serra ao fundo.')]
    p['host'] = dict(img=G(0), alt='Fachada da Pousada Dormida do Peixe', name='Pedro e família',
                     lines=[('star', 'Nota 5,0 no Google'), ('pin', 'Entre a Lagoa de Ibiraquera e o Rosa'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='O grande destaque foi o atendimento do anfitrião, Pedro. Sempre cordial, simpático e prestativo.',
                     text='Palavras do Elmo, um dos hóspedes. Na Dormida do Peixe quem recebe é a própria família, com as melhores dicas de praia, trilha e restaurante da região.')
    p['plan'] = dict(kicker='Apartamentos', title='Conheça cada apartamento antes de chegar.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Apartamento com Sala', note='até 4 hóspedes', img=g(19),
                                 cells=['Suíte com cama de casal', 'Sala com sofá', 'Varanda com rede', 'Lavabo', 'Frigobar e mesa']),
                            dict(name='Apartamento Vista Montanha', note='até 2 hóspedes', img=g(11),
                                 cells=['Cama de casal', 'Ar-condicionado', 'Vista da lagoa', 'Frigobar', 'Banheiro privativo']),
                            dict(name='Apartamento Família', note='até 4 hóspedes', img=G(8),
                                 cells=['Duas camas', 'Sala integrada', 'Espaço pra família', 'Ar-condicionado', 'Varanda'])])
    p['exp'] = dict(title='O melhor do Rosa, a poucos passos.',
                    big=dict(img=g(26, True), title='Praia do Rosa', text='O centrinho fica a cerca de 10 minutos a pé e a praia logo depois.'),
                    wide=dict(img=g(25), title='Lagoa de Ibiraquera', text='Kitesurf, stand up paddle e o pôr do sol mais bonito da região.'),
                    list_title='Mais pra explorar',
                    list=[('hike', 'Trilha Rosa Norte e Lagoa'), ('kite', 'Kitesurf na lagoa'), ('board', 'Stand up paddle'), ('wave', 'Praia do Luz e Barra')],
                    small=dict(img=g(44), title='Café na bandeja', text='Opcional, das 7h às 10h, servido no apartamento.'))
    items = [
        ('Suian Q.', 'Google', 'Minha estadia foi maravilhosa! A pousada é extremamente aconchegante, confortável e transmite uma sensação de paz desde o momento em que cheguei.'),
        ('Elmo L.', 'Google', 'O grande destaque foi o atendimento do anfitrião, Pedro. Sempre cordial, simpático e prestativo, ele nos ajudou em tudo o que precisamos.'),
        ('viagensdacami', 'Tripadvisor', 'A pousada é MARAVILHOSA. Super novinha, quartos gigantes com ar condicionado e ventilador, com uma sacadona e vista para as montanhas/lagoa.'),
        ('Juliana S.', 'Google', 'Quando cheguei à pousada que percebi o porque ser 5 estrelas no Google. É um apartamento muito bom! Com sala, lavabo + uma suíte!'),
        ('Elvis F.', 'Google', 'Local agradável, quartos muito confortáveis e amplos, tem uma sala além do cômodo principal, com redes para descanso e uma bela vista das montanhas.'),
        ('Suellen C.', 'Google', 'Fomos muito bem recebidos pelos donos. Eles esquentaram a janta do meu bebê e ofereceram tudo que precisava. Super indico o lugar.'),
        ('Erika B.', 'Google', 'Excelente atendimento, os quartos modernos e bem claros, além da decoração ser linda.'),
        ('Claudio M.', 'Google', 'Pousada simplesmente maravilhosa, anfitriões demais agradáveis, tudo muito limpo, organizado, linda decoração dos quartos.'),
    ]
    p['reviews'] = dict(title='O tipo de estadia que os hóspedes comentam.', count=235, rating='5,0',
                        bars=[('Google', '5,0', 100), ('Tripadvisor', '5/5', 100), ('Limpeza', '5,0', 100)],
                        note='5,0 no Google · 235 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='5,0 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 14h e o check-out até as 12h. Se precisar de outro horário, combine com a gente pelo WhatsApp.'),
                ('O café da manhã está incluso?', 'O café da manhã é opcional, servido das 7h às 10h. Pergunte o valor na hora da reserva.'),
                ('Posso levar meu pet?', 'Sim, a pousada aceita pets. Avise na reserva para prepararmos tudo.'),
                ('Tem estacionamento?', 'Sim, estacionamento interno gratuito, com portão eletrônico.'),
                ('A que distância fica a praia?', 'O centrinho do Rosa fica a cerca de 10 minutos a pé, e a trilha Rosa Norte e Lagoa passa pertinho.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A pousada confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=g(29, True), title='Reserve seu refúgio entre a lagoa e o mar.',
                    text='Escolha as datas, chame a gente no WhatsApp e garanta seu apartamento com varanda, piscina e o Rosa logo ali.')
    return p
