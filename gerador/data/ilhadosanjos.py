"""Pousada Ilha dos Anjos (São João do Rio Vermelho, Florianópolis) — LP no template 'aurelia'."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('ilhadosanjos')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Ilha+dos+Anjos+Rio+Vermelho+Florian%C3%B3polis'

T = dict(gold='#c4843a', gold2='#e6b36b', dark='#1e2a23', darker='#141b16', cream='#f7f1e6', cream2='#efe3cf',
         sage='#617a5a', text='#20241f', muted='#5c6058', line='#d5c2a3')

P = dict(
    slug='ilhadosanjos', name='Pousada Ilha dos Anjos', brand='Ilha dos Anjos', place_short='Rio Vermelho, Florianópolis',
    meta_desc='Pousada Ilha dos Anjos, no São João do Rio Vermelho, em Florianópolis: suítes com varanda e rede, suíte com hidromassagem, café da manhã incluso e a Praia do Moçambique por perto. Nota 4,8 no Google.',
    phone='(48) 99177-0994', wa_number='5548991770994', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada Ilha dos Anjos e queria consultar disponibilidade.',
    instagram='pousadailhadosanjos',
    address='Servidão Ernesto Pereira dos Anjos, 09 - São João do Rio Vermelho, Florianópolis - SC, 88060-236',
    footer_tag='Sossego, natureza e a Praia do Moçambique logo ali.',
    room_word='Suíte', rooms_label='Suítes', rooms_eyebrow='Suítes da Ilha dos Anjos', rooms_title='Nossas acomodações',
    rooms_sub='Quartos amplos e arejados, com ar-condicionado, TV, frigobar e varanda com rede olhando para o verde.',
    tagline='Café da manhã incluso, varanda com rede e o pôr do sol no terraço.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar ao Rio Vermelho.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(16, True), alt='Pousada Ilha dos Anjos vista do alto, cercada de verde', eyebrow='Bem-vindo à Ilha dos Anjos',
                     title='Seu refúgio no norte da Ilha',
                     sub='Uma pousada cercada de natureza no Rio Vermelho, com café da manhã incluso e a Praia do Moçambique a poucos minutos.',
                     cta='Conhecer as suítes')
    p['about'] = dict(eyebrow='Ilha dos Anjos · Rio Vermelho', title='Longe da badalação, perto do mar',
                      text='Num bairro residencial e tranquilo, ao lado da reserva ambiental do Parque do Rio Vermelho, a Ilha dos Anjos é feita pra quem quer descansar de verdade. Suítes amplas com varanda e rede, jardim florido, café da manhã reforçado e a atenção da Sheila, que recebe cada hóspede com dicas de praias, trilhas e passeios.',
                      sign='Ilha dos Anjos', role='Pousada · Florianópolis',
                      imgs=[dict(src=G(i), alt='Pousada Ilha dos Anjos') for i in (6, 7, 20, 13)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar a {n} na Pousada Ilha dos Anjos.')
    p['rooms'] = [
        dict(name='Suíte com Hidromassagem', img=G(8), badge='Café incluso',
             text='Cama queen, banheira de hidromassagem e vista para as montanhas da reserva ambiental. A escolha dos casais.',
             meta=[dict(icon='bed', text='Cama queen'), dict(icon='bath', text='Hidromassagem'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Suíte com Hidromassagem')),
        dict(name='Suíte com Varanda', img=g(36), badge='Café incluso',
             text='Cama de casal ou duas de solteiro, varanda com rede, TV, frigobar e ar-condicionado.',
             meta=[dict(icon='bed', text='Casal ou solteiro'), dict(icon='users', text='2 hóspedes'), dict(icon='leaf', text='Varanda com rede')],
             wa=rw('Suíte com Varanda')),
        dict(name='Quarto Quádruplo', img=G(5), badge='Café incluso',
             text='Espaço para a família ou a turma de amigos, com cama de casal e camas de solteiro.',
             meta=[dict(icon='users', text='Até 4 hóspedes'), dict(icon='tv', text='TV e frigobar'), dict(icon='snow', text='Ar-condicionado')],
             wa=rw('Quarto Quádruplo')),
    ]
    p['exp'] = dict(eyebrow='A experiência Ilha dos Anjos', title='Além da estadia',
                    sub='Do café da manhã ao pôr do sol no terraço, cada momento é cuidado de perto.',
                    cards=[dict(icon='coffee', title='Café da manhã', kicker='Incluso na diária', text='Café da manhã fresquinho, variado e bem servido, todas as manhãs.'),
                           dict(icon='sun', title='Pôr do sol no terraço', kicker='Fim de tarde', text='O terraço da pousada é o lugar pra ver o céu mudar de cor e, à noite, as estrelas.'),
                           dict(icon='hike', title='Trilha até o Moçambique', kicker='Natureza', text='A Praia do Moçambique fica a cerca de 2 km, pela reserva ambiental do Parque do Rio Vermelho.'),
                           dict(icon='heart', title='Clima de romance', kicker='Para casais', text='Suíte com banheira de hidromassagem, vinho e pétalas: o cenário certo pra uma escapada a dois.')])
    gal = [('G', 9), ('g', 40), ('G', 31), ('g', 29), ('G', 33), ('g', 24), ('G', 27), ('g', 39), ('G', 10), ('g', 34), ('G', 12), ('g', 17)]
    p['gallery'] = dict(title='Um olhar sobre a Ilha dos Anjos', sub='Jardim, suítes, terraço e o mar do norte da Ilha por perto.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='Pousada Ilha dos Anjos') for k, i in gal])
    google = [
        ('Sandra B.', 'Nossa estadia foi excelente! A pousada é um encanto, muito bem cuidada e tudo de muito bom gosto. Camas confortáveis, roupas de cama e banho cheirosas, uma super tranquilidade. Ótimo café da manhã!'),
        ('Kamila K.', 'Pousada maravilhosa, perfeito pra ficar em off. Roupa de cama impecável, limpeza nota 10, café da manhã fresquinho, o terraço na suíte Premium é lindo para curtir o céu estrelado.'),
        ('Veejay', 'Pousada maravilhosa, aconchegante e tudo muito limpo. Café da manhã reforçado! Lugar calmo para descansar. A Sheila nos recepcionou muito bem e deu ótimas dicas de locais e passeios. Nota 10!'),
        ('Marcelo B.', 'Atendimento impecável. Quarto muito confortável, amplo e arejado. Sacada com rede, mesa e varal. Localização perfeita para quem busca tranquilidade em meio à badalação de Florianópolis.'),
        ('Rodrigo C.', 'Localizada em uma vizinhança tranquila, a pousada é aconchegante, com ótimas instalações, café da manhã de qualidade e os quartos, com varanda, são limpos e espaçosos.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    rv.insert(2, dict(key='booking', text='Pousada deliciosa e muito confortável. O quarto tem uma linda vista pro pôr do sol, além de ser confortável e aconchegante. O atendimento é ímpar.',
                      author='Pedro', source='Booking', stars=5))
    rv.insert(5, dict(key='booking', text='Quarto excelente, café da manhã delicioso, estacionamento tranquilo, atendimento excepcional.',
                      author='José', source='Booking', stars=5))
    p['reviews'] = dict(bg=g(17), headline='4,8 no Google · 80 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,8', ''), ('booking', 'Booking', '8,3', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Qual o horário de check-in e check-out?', a='Check-in a partir das 14h e check-out até as 11h. Se precisar de outro horário, fale com a gente pelo WhatsApp.'),
        dict(q='O café da manhã está incluso?', a='Sim, o café da manhã está incluso na diária.'),
        dict(q='A praia fica longe?', a='A Praia do Moçambique fica a cerca de 2 km. A pousada fica num bairro residencial e tranquilo, então o ideal é estar de carro ou usar aplicativo.'),
        dict(q='Tem estacionamento?', a='Sim, estacionamento gratuito para os hóspedes.'),
        dict(q='Vocês fazem traslado do aeroporto?', a='Sim, a pousada oferece traslado do aeroporto. Consulte valores e horários pelo WhatsApp.'),
        dict(q='Tem acomodação para família?', a='Sim. Além das suítes de casal, temos quarto quádruplo e estúdio. Conte quantas pessoas vêm e a gente indica a melhor opção.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('wing', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
