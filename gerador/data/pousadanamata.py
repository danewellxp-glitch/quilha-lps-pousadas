"""Pousada na Mata (Servidão Amantino Cameu, 768, Rio Tavares, Florianópolis) — LP no template 'aurelia'.
Fotos: Google Maps (gm; quase só área externa, natureza e praias). Proprietário citado: Diego. Chalés/apartamentos para 2 a 4
pessoas com minicozinha; sem café da manhã. Site antigo pousadanamata.com.br fora do ar. NÃO citar possível venda."""
from common import review_sources
from deco import deco, logo
from fotos import Fotos

TEMPLATE = 'aurelia'
ENHANCE = True
F = Fotos('pousadanamata')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+na+Mata+Servid%C3%A3o+Amantino+Cameu+768+Florian%C3%B3polis'

T = dict(gold='#b5502f', gold2='#e59b6f', dark='#1f3b2c', darker='#12261b', cream='#f8f6ee', cream2='#ece6d3',
         sage='#4f8a5b', text='#1c2420', muted='#5b665f', line='#dccfae')

P = dict(
    slug='pousadanamata', name='Pousada na Mata', brand='Pousada na Mata', place_short='Rio Tavares, Florianópolis',
    meta_desc='Pousada na Mata: chalés com cozinha em meio à natureza no Rio Tavares, Florianópolis, entre a Joaquina e o Campeche. Silêncio, varandas com rede, saguis e tucanos no jardim.',
    phone='(48) 3334-4348', wa_number='554833344348', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Pousada na Mata e queria consultar disponibilidade.',
    instagram='',
    address='Servidão Amantino Cameu, 768 - Rio Tavares, Florianópolis - SC, 88048-413',
    footer_tag='Chalés com cozinha no meio do verde, entre as praias do leste e do sul da Ilha.',
    room_word='Chalé', rooms_label='Chalés', rooms_eyebrow='Chalés da Pousada na Mata', rooms_title='Sua casinha no meio do verde',
    rooms_sub='Chalés para 2 a 4 pessoas, com quarto, banheiro e cozinha equipada. Varandas com rede e vista pro morro.',
    tagline='Silêncio, mata e passarinho, a poucos minutos das praias mais bonitas da Ilha.',
    faq_sub='O que os hóspedes mais perguntam antes de chegar.',
)


def context(I, wa):
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(24, True), alt='Chalés verdes com redes na varanda e palmeiras', eyebrow='Bem-vindo à Pousada na Mata',
                     title='Descanse no meio da mata',
                     sub='Chalés com cozinha, varanda com rede e muito silêncio, a poucos minutos da Joaquina e do Campeche.',
                     cta='Conhecer os chalés')
    p['about'] = dict(eyebrow='Pousada na Mata · Rio Tavares', title='Uma pousada ecológica, feita pra desacelerar',
                      text='A Pousada na Mata fica numa área preservada do Rio Tavares, bem no centro da Ilha. Os chalés verdes ficam espalhados por um jardim cheio de palmeiras, com varandas com rede olhando pro morro. Saguis, tucanos e aracuãs aparecem todo dia. Cada chalé tem cozinha equipada, e as praias da Joaquina, do Campeche e do Morro das Pedras ficam a poucos minutos.',
                      sign='Diego e família', role='Anfitriões',
                      imgs=[dict(src=s, alt='Pousada na Mata') for s in (G(37), G(90), G(95), G(2))])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Pousada na Mata.')
    p['rooms'] = [
        dict(name='Chalé Casal', img=G(95), badge='Até 2 hóspedes',
             text='Quarto de casal, banheiro privativo e minicozinha com geladeira, fogão e utensílios. Janelas com tela e cortinas.',
             meta=[dict(icon='bed', text='Cama de casal'), dict(icon='kitchen', text='Minicozinha'), dict(icon='leaf', text='Vista do jardim')],
             wa=rw('Chalé Casal')),
        dict(name='Chalé com Varanda', img=G(21), badge='Até 3 hóspedes',
             text='Chalé no andar de cima, com sacada e rede olhando pro morro. Perfeito pra quem quer sossego.',
             meta=[dict(icon='sun', text='Varanda com rede'), dict(icon='users', text='Até 3 pessoas'), dict(icon='kitchen', text='Cozinha')],
             wa=rw('Chalé com Varanda')),
        dict(name='Chalé Família', img=G(37), badge='Até 4 hóspedes',
             text='Espaço pra família ou amigos, com cozinha completa pra preparar as refeições sem sair de casa.',
             meta=[dict(icon='users', text='Até 4 pessoas'), dict(icon='kitchen', text='Cozinha completa'), dict(icon='car', text='Estacionamento')],
             wa=rw('Chalé Família')),
    ]
    p['exp'] = dict(eyebrow='A experiência na Mata', title='Natureza de um lado, praia do outro',
                    sub='O centro da Ilha é o ponto de partida perfeito pras praias do leste e do sul.',
                    cards=[dict(icon='leaf', title='Bichos no jardim', kicker='Todo dia', text='Saguis, tucanos, aracuãs e muitas aves visitam a pousada de manhã cedo.'),
                           dict(icon='wave', title='Campeche e Morro das Pedras', kicker='Pertinho', text='Praias de mar aberto e areia branca a poucos minutos de carro.'),
                           dict(icon='board', title='Joaquina e Lagoa', kicker='A poucos minutos', text='Dunas, surfe e os restaurantes da Lagoa da Conceição logo ali.'),
                           dict(icon='kitchen', title='Cozinha no chalé', kicker='Mais economia', text='Cozinha equipada e mercados por perto pra preparar suas refeições.')])
    gal = [60, 14, 90, 17, 38, 107, 115, 6, 78, 108, 79, 121]
    p['gallery'] = dict(title='Um olhar sobre a Pousada na Mata', sub='Os chalés, o jardim, os bichos e as praias da região.',
                        imgs=[dict(src=G(i), alt='Pousada na Mata') for i in gal])
    google = [
        ('Céu E.', 'Lugar bonito, aconchegante, limpo, agradável, tranquilo, jardim bonito e bem cuidado, detalhes que fazem a diferença como cortinas que dão privacidade, telas na janela e camareira. Muito verde e silêncio.'),
        ('Mirella K.', 'A estrutura da pousada é ótima, charmosa e meio rústica. Ficamos em um quarto que tinha sacada com rede, perfeita para quem quer sossego. O proprietário Diego está sempre por perto.'),
        ('Marjorie', 'O preço é muito acessível e a pousada é bem acolhedora. Tem pequenos chalés para 2, 3 ou 4 pessoas com cozinhas equipadas, banheiro e quarto. Tudo de boa qualidade.'),
        ('Dyego', 'Por ser bem no meio da mata, a pousada é rústica e muito tranquila, o que a torna bem especial. Quando você acorda e abre a janela, dá de cara com um visual sensacional.'),
        ('Roberto B.', 'Uma pousada ecológica numa ilha fantástica, numa área preservada, com bom atendimento e bom custo-benefício. Proprietário Diego muito atencioso.'),
        ('Paulo T.', 'Irada a pousada, literalmente no meio da mata. Vários bichos: tucanos, aracuã, macacos e várias aves.'),
        ('Everaldo W.', 'Pousada muito bonita e bem localizada, no centro da ilha, bom para explorar tanto o sul como o norte, com atendimento excelente.'),
        ('Gustavo H.', 'Atendimento excepcional! Pessoas de paz e bem. Pousada bem estruturada, em meio à natureza. Recomendo!'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in google]
    p['reviews'] = dict(bg=G(120), headline='4,6 no Google · 126 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,6', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Os chalés têm cozinha?', a='Sim. Todos têm cozinha equipada com geladeira, fogão e utensílios, ótimo pra quem quer economizar.'),
        dict(q='Tem café da manhã?', a='A pousada não serve café da manhã, mas tem mercados e padarias por perto.'),
        dict(q='A praia fica longe?', a='As praias do Campeche, Morro das Pedras e Joaquina ficam a poucos minutos de carro.'),
        dict(q='Como é o acesso?', a='Fica numa servidão tranquila do Rio Tavares, com um trecho curto de estrada de terra no final.'),
        dict(q='Tem estacionamento?', a='Sim, a pousada tem estacionamento para hóspedes.'),
        dict(q='Como faço a reserva?', a='Escolha as datas na barra de reserva e envie pelo WhatsApp. A gente confirma disponibilidade e valores com você.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('palm', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
