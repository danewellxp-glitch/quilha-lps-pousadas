"""InnFloripa (Morro das Pedras / Campeche, Florianópolis) — LP no template 'aurelia'."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('innfloripa')
MAPS = 'https://www.google.com/maps/search/?api=1&query=InnFloripa+Morro+das+Pedras+Florian%C3%B3polis'

T = dict(gold='#c2703f', gold2='#eaa877', dark='#1d3a33', darker='#12261f', cream='#faf5ec', cream2='#f1e6d4',
         sage='#4e8a6c', text='#1f2622', muted='#5c6660', line='#dfcaa9')

P = dict(
    slug='innfloripa', name='InnFloripa', brand='InnFloripa', place_short='Campeche, Sul da Ilha',
    meta_desc='InnFloripa: pousada familiar no Morro das Pedras, perto da Praia do Campeche e a 7 minutos do aeroporto de Florianópolis. Suítes privativas e climatizadas, jardim com fontes, terraço e café da manhã caseiro.',
    phone='(48) 98824-0540', wa_number='5548988240540', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da InnFloripa e queria consultar disponibilidade.',
    instagram='innfloripa_campeche',
    address='Servidão Garapuvu do Sul, 439 - Morro das Pedras, Florianópolis - SC, 88066-018',
    footer_tag='Estilo, conforto e economia no Sul da Ilha, pertinho da Praia do Campeche.',
    room_word='Suíte', rooms_label='Suítes', rooms_eyebrow='Suítes da InnFloripa', rooms_title='Onde você vai descansar',
    rooms_sub='Suítes privativas e climatizadas, com banheiro próprio, enxoval caprichado e café da manhã caseiro incluso.',
    tagline='Uma casa de família no Sul da Ilha, entre a Praia do Campeche e o aeroporto.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar ao Campeche.',
)


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=g(33, True), alt='Praia do Campeche com a Ilha do Campeche ao fundo', eyebrow='Bem-vindo à InnFloripa',
                     title='Seu refúgio no Sul da Ilha',
                     sub='Suítes climatizadas, jardim com fontes e café da manhã caseiro, pertinho da Praia do Campeche e a 7 minutos do aeroporto.',
                     cta='Conhecer as suítes')
    p['about'] = dict(eyebrow='InnFloripa · Campeche', title='Uma casa de família pra chamar de sua',
                      text='A InnFloripa é uma pousada familiar no Morro das Pedras, num cantinho silencioso e cheio de verde do Sul da Ilha. A casa tem tijolinho, madeira, jardim com laguinho e fontes, uma estante de livros logo na entrada e um terraço com espreguiçadeiras. Quem recebe é a família da Juliana, com café da manhã fresquinho e as melhores dicas da região.',
                      sign='Juliana e família', role='Anfitriões',
                      imgs=[dict(src=s, alt='Pousada InnFloripa') for s in (g(124), g(45), g(41), g(150))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar a {n} na InnFloripa.')
    p['rooms'] = [
        dict(name='Suíte', img=G(24), badge='Até 2 hóspedes',
             text='Suíte privativa com cama de casal, ar-condicionado, TV e banheiro próprio. Silenciosa e bem ventilada.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Climatizada'), dict(icon='coffee', text='Café incluso')],
             wa=rw('Suíte')),
        dict(name='Suíte com Terraço', img=g(147), badge='Com terraço',
             text='Suíte com cama de casal e acesso a terraço com espreguiçadeiras, sol da manhã e vista dos morros do Sul da Ilha.',
             meta=[dict(icon='sun', text='Terraço'), dict(icon='bed', text='Cama de casal'), dict(icon='snow', text='Climatizada')],
             wa=rw('Suíte com Terraço')),
    ]
    p['exp'] = dict(eyebrow='A experiência InnFloripa', title='Os dias no Sul da Ilha',
                    sub='Praia de manhã, trilha à tarde e o jardim da pousada pra descansar.',
                    cards=[dict(icon='wave', title='Praia do Campeche', kicker='A ~800 m', text='Mar azul, surfe e a Ilha do Campeche no horizonte, dá pra ir a pé.'),
                           dict(icon='hike', title='Trilhas e praias selvagens', kicker='Sul da Ilha', text='Lagoinha do Leste, Matadeiro, Armação e Pântano do Sul a poucos minutos.'),
                           dict(icon='coffee', title='Café caseiro', kicker='Incluso', text='Pães, bolos caseiros, pão de queijo, iogurte e frutas, tudo fresquinho pela manhã.'),
                           dict(icon='plane', title='7 min do aeroporto', kicker='Localização', text='Perfeito pra quem chega ou parte de Florianópolis e quer fugir do trânsito do centro.')])
    gal = [('g', 46), ('g', 35), ('G', 53), ('g', 40), ('g', 9), ('g', 126), ('g', 148), ('G', 50), ('g', 123), ('G', 88), ('g', 201), ('g', 47)]
    p['gallery'] = dict(title='Um olhar sobre a InnFloripa', sub='O jardim, a casa de tijolinho, as suítes e as praias do Sul da Ilha.',
                        imgs=[dict(src=(G(i) if k == 'G' else g(i)), alt='InnFloripa e Sul da Ilha') for k, i in gal])
    google = [
        ('Isabela', 'A pousada é um amor. Logo na entrada tem alguns livros pra ler, o que achei um detalhe bem legal. Nosso quarto era bem silencioso e bem ventilado. A Juliana é super prestativa e atenciosa.'),
        ('Jean S.', 'Lugar muito agradável, familiar e silencioso. Café da manhã bom e saudável. Preço justo. O Felipe, a Juliana e sua família são super prestativos, receptivos e queridos.'),
        ('Anderson W.', 'Ficamos no quarto do 3º andar, a vista dos morros ao redor é linda. O café é simples, mas tudo fresquinho e os bolos são caseiros e muito gostosos!'),
        ('Ana R.', 'Estive hospedada por 5 dias e foram dias maravilhosos. A Juliana e sua família são de um carinho e uma atenção inigualável. Simples, mas aconchegante.'),
        ('Fabricio L.', 'A família proprietária é adorável, muito gentil e prestativa, e realmente se importa em fazer você se sentir em casa. Foram 12 dias maravilhosos.'),
        ('Gabriele S.', 'O ambiente é muito confortável e acolhedor. Os proprietários nos deram dicas maravilhosas. Super pertinho da Praia do Campeche, dá pra ir a pé tranquilamente.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    rv.insert(1, dict(key='booking', text='O espaço é muito lindo, super aconchegante, transmite uma sensação de paz.', author='Isaac', source='Booking', stars=5))
    rv.insert(4, dict(key='booking', text='Pousada é bonita, bem cuidada, com verde e fontes, limpa. Café da manhã satisfatório, localização próxima ao aeroporto.', author='Clarissa', source='Booking', stars=5))
    p['reviews'] = dict(bg=g(46), headline='4,5 no Google · 42 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,5', ''), ('booking', 'Booking', '7,9', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='O café da manhã está incluso?', a='Sim. O café da manhã caseiro está incluso na diária, com pães, bolos, frutas e café fresquinho.'),
        dict(q='Qual o horário de check-in e check-out?', a='O check-in é a partir das 13h30 e o check-out até as 11h. Chegando em outro horário, avise pelo WhatsApp.'),
        dict(q='A praia fica longe?', a='Não. A Praia do Campeche fica a cerca de 800 m, dá pra ir a pé.'),
        dict(q='Fica perto do aeroporto?', a='Sim, a cerca de 7 minutos de carro do Aeroporto Internacional de Florianópolis.'),
        dict(q='Os quartos têm ar-condicionado?', a='Sim. Todas as suítes são privativas e climatizadas, com banheiro próprio.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('hibiscus', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
