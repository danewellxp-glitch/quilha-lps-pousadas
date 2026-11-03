from common import ig, review_sources
from deco import deco, logo

TEMPLATE = 'aurelia'
U = 'pousada_aeropouso'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Aeropouso+Pousada+Carianos+Florian%C3%B3polis'

T = dict(gold='#c9773f', gold2='#f0a86a', dark='#22303a', darker='#161e24', cream='#f7f2eb', cream2='#eee4d7',
         sage='#3f6170', text='#1d2328', muted='#5a6066', line='#d4c2ad')

P = dict(
    slug='aeropouso', name='Aeropouso Pousada', brand='Aeropouso', place_short='Carianos, Florianópolis',
    meta_desc='Aeropouso Pousada em Carianos, a 5 minutos do Aeroporto de Florianópolis: quartos com ar-condicionado, café da manhã a qualquer hora e nota 4,6 no Google.',
    phone='(48) 98426-7440', wa_number='5548984267440', email='', site='', site_label='', facebook='',
    wa_text='Olá! Vim pelo site da Aeropouso e queria consultar disponibilidade.',
    instagram='pousada_aeropouso',
    address='R. João Jorge Mussi, 406 - Carianos, Florianópolis - SC, 88047-510',
    footer_tag='Seu pouso pertinho do aeroporto.',
    room_word='Quarto', rooms_label='Quartos', rooms_eyebrow='Acomodações', rooms_title='Nossos quartos',
    rooms_sub='Quartos limpos e silenciosos, com ar-condicionado, chuveiro forte e roupa de cama de qualidade.',
    tagline='A 5 minutos do aeroporto, com café da manhã esperando por você a qualquer hora.',
    faq_sub='Tudo o que você precisa saber antes do seu voo.',
)


def context(I, wa):
    g = lambda i: I(ig(U, i))[0]
    p = dict(P)
    p['hero'] = dict(img=g(11), alt='Praia do sul da Ilha de Florianópolis', eyebrow='Bem-vindo à Aeropouso',
                     title='Pouse tranquilo antes do próximo voo',
                     sub='Pousada a 5 minutos do Aeroporto de Florianópolis, com chegada no seu horário e as praias do sul da Ilha logo ali.',
                     cta='Ver quartos')
    p['about'] = dict(eyebrow='Aeropouso · Carianos', title='Feita pra quem está de passagem',
                      text='Voo cedo, conexão longa ou chegada de madrugada: a Aeropouso foi pensada pra isso. Você chega e sai no seu horário, e o café da manhã fica pronto numa cestinha com o número do seu quarto, disponível desde a madrugada.',
                      sign='Aeropouso', role='Pousada executiva',
                      imgs=[dict(src=g(i), alt='Aeropouso Pousada') for i in (1, 3, 9, 15)])
    rw = lambda n: wa(P['wa_number'], f'Olá! Quero consultar o {n} na Aeropouso.')
    p['rooms'] = [
        dict(name='Quarto Casal', img=g(17), badge='Café incluso', text='Cama de casal, banheiro privativo, ar-condicionado e enxoval sempre limpinho.',
             meta=[dict(icon='bed', text='Casal'), dict(icon='users', text='2 hóspedes'), dict(icon='snow', text='Ar-condicionado')], wa=rw('Quarto Casal')),
        dict(name='Quarto Triplo', img=g(7), badge='Café incluso', text='Uma cama de casal e camas de solteiro para viajar em família ou com amigos.',
             meta=[dict(icon='bed', text='Casal + solteiro'), dict(icon='users', text='3 hóspedes'), dict(icon='snow', text='Ar-condicionado')], wa=rw('Quarto Triplo')),
        dict(name='Quarto Standard', img=g(3), badge='Café incluso', text='Iluminado e silencioso, perfeito pra descansar entre um voo e outro.',
             meta=[dict(icon='bed', text='Casal'), dict(icon='users', text='2 hóspedes'), dict(icon='wifi', text='Wi-Fi')], wa=rw('Quarto Standard')),
    ]
    p['exp'] = dict(eyebrow='A experiência Aeropouso', title='Pensada pro seu voo',
                    sub='Praticidade de hotel de aeroporto com o carinho de uma pousada de família.',
                    cards=[dict(icon='plane', title='5 min do aeroporto', kicker='Sem correria', text='Perto do Aeroporto Internacional de Florianópolis, de supermercado, farmácias e lojas.'),
                           dict(icon='coffee', title='Café a qualquer hora', kicker='Desde a madrugada', text='Cestinha identificada com o número do quarto, na geladeira, pra você tomar café no seu ritmo.'),
                           dict(icon='wave', title='Praias do sul da Ilha', kicker='Entre um voo e outro', text='Campeche, Armação e Pântano do Sul ficam perto pra dar aquela escapadinha.')])
    gal = [1, 12, 3, 9, 13, 7, 2, 17, 15, 4]
    p['gallery'] = dict(title='Um olhar sobre a Aeropouso', sub='Quartos, área de café e o sul da Ilha logo ali.',
                        imgs=[dict(src=g(i), alt='Aeropouso Pousada') for i in gal])
    items = [
        ('Luiz H.', 'Posso afirmar que essa pousada próxima a aeroportos é a melhor que já fiquei, mesmo em Guarulhos não temos nada próximo ao que a Aeropouso oferece.'),
        ('Jhessica G.', 'O café da manhã foi um diferencial encantador: tudo organizado com muito carinho dentro de uma geladeira, em uma cesta identificada com o número do quarto.'),
        ('Elton L.', 'Excelente! Tudo muito limpo, organizado e aconchegante. Os donos são pessoas de um coração muito bom. Perto do aeroporto e pontos de referência.'),
        ('Alexsander', 'Tudo muito bem aconchegante e organizado, com uma ótima área externa. Está salvo nos meus favoritos pois planejo voltar!'),
        ('Talita D.', 'Pousada simples, mas com ar caseiro. Perto do aeroporto é voltada exatamente para estadia no aguardo de voo. Recepção acolhedora.'),
        ('Marcelo S.', 'Lugar limpo, agradável.. um silêncio... super recomendo.'),
    ]
    rv = [dict(key='google', text=t, author=a, source='Google', stars=5) for a, t in items]
    rv.insert(2, dict(key='tripadvisor', text='Pousada muito aconchegante, localizada próxima ao aeroporto, uma ótima opção para pernoitar. O atendimento é diferenciado, você é bem tratado e se sente acolhido.',
                      author='suh_and28', source='Tripadvisor', stars=5))
    p['reviews'] = dict(bg=g(13), headline='4,6 no Google · 416 avaliações', link=MAPS,
                        sources=review_sources([('google', 'Google', '4,6', ''), ('tripadvisor', 'Tripadvisor', '4,5', '')]),
                        items=rv)
    p['faq'] = [
        dict(q='Qual a distância até o aeroporto?', a='Cerca de 5 minutos de carro até o Aeroporto Internacional de Florianópolis.'),
        dict(q='Posso chegar de madrugada?', a='Pode. A pousada foi pensada pra quem está em trânsito, com liberdade pra chegar e sair no horário do seu voo. Combine a chegada pelo WhatsApp.'),
        dict(q='Como funciona o café da manhã?', a='Fica numa cestinha na geladeira, identificada com o número do seu quarto, disponível desde a madrugada.'),
        dict(q='Os quartos têm ar-condicionado?', a='Sim, todos os quartos têm ar-condicionado e banheiro privativo.'),
        dict(q='O que tem por perto?', a='Supermercado, farmácias e lojas no bairro, e as praias do sul da Ilha a poucos minutos de carro.'),
    ]
    p['loc'] = dict(maps_url=MAPS)
    return p


def extra():
    return dict(logo_svg=logo('plane', 30), deco_svg=deco('a'), deco_svg2=deco('b'))
