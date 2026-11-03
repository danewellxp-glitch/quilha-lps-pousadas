"""Pousada Goulin (São João do Rio Vermelho, Florianópolis) — LP no template 'stayora'."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('goulin')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+Goulin+Rio+Vermelho+Florian%C3%B3polis'

T = dict(bg='#f5f7f6', alt='#e6eeee', ink='#10201f', ink2='#172826', muted='#566664', dim='#b4c0bf',
         dark='#0c1918', card='#f5f7f6', accent='#1f7fa3', line='#d6dfde')

P = dict(
    slug='goulin', name='Pousada Goulin', short='Goulin',
    seo_title='Pousada Goulin | Apartamentos perto da Praia do Moçambique',
    meta_desc='Pousada Goulin, no São João do Rio Vermelho, em Florianópolis: apartamentos e studios completos, com cozinha, ar-condicionado e garagem, pertinho da Praia do Moçambique. Nota 5,0 no Google.',
    phone='(48) 98416-0465', wa_number='5548984160465', email='',
    wa_text='Olá! Vim pelo site da Pousada Goulin e queria consultar disponibilidade.',
    instagram='pousadagoulin', maps_url=MAPS,
    address='Servidão Manoel Cesário Coelho, 779 · São João do Rio Vermelho, Florianópolis/SC · 88060-421', checkin='', checkout='',
    footer_tag='A vida fica melhor na praia. Apartamentos completos perto da Praia do Moçambique.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Acomodações', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#1f7fa3', '#c0702c', '#3f7d3a', '#7a5c3e', '#a8476b', '#3c5a7a', '#6b5b95', '#5f7f2f']


def context(I, wa):
    g = lambda i, big=False: I(F.ig(i), big=big)[0]
    G = lambda i, big=False: I(F.gm(i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(9, True), alt='Mar azul e costão no norte da Ilha de Santa Catarina',
                     title='A vida fica melhor perto da praia',
                     sub='Apartamentos completos e tranquilos no Rio Vermelho, pertinho da Praia do Moçambique.',
                     avatars=[('L', '#1f7fa3'), ('S', '#c0702c'), ('T', '#3f7d3a')],
                     proof='Nota 5,0', proof_sub='52 avaliações no Google')
    p['about'] = dict(imgs=[g(60), g(66)], alts=['Fachada da pousada com cerca branca e palmeira', 'Studio com cozinha americana e cama de casal'],
                      stat_num='5.0', stat_dec=1, stat_txt='5,0', stat_label='Nota no Google',
                      kicker='A pousada', title='Simples, completa e com cara de casa.',
                      text='A Goulin fica numa servidão tranquila do São João do Rio Vermelho, perto da Praia do Moçambique e das dunas do norte da Ilha. São apartamentos e studios com cozinha, ar-condicionado e TV, tudo limpinho e organizado, e uma casa para grupos maiores. Quem recebe é o Felipe, o proprietário, que atende cada hóspede de perto.')
    p['amen_title'] = 'O que você precisa pra curtir a praia sem complicação.'
    p['amenities'] = [('kitchen', 'Cozinha equipada'), ('snow', 'Ar-condicionado'), ('tv', 'TV'),
                      ('car', 'Garagem'), ('food', 'Churrasqueira'), ('broom', 'Tudo limpo e organizado'),
                      ('wave', 'Praia do Moçambique por perto'), ('hike', 'Trilhas e dunas'), ('leaf', 'Parque do Rio Vermelho'),
                      ('users', 'Casa para até 8 pessoas'), ('shield', 'Rua tranquila'), ('chat', 'Atendimento direto pelo WhatsApp')]
    p['spaces_title'] = 'Apartamentos novos e espaço pra reunir a turma.'
    p['spaces'] = [dict(img=g(66), title='Studio', text='Cozinha americana, cama de casal e acabamento novo.'),
                   dict(img=g(59), title='Cozinha completa', text='Fogão, geladeira, micro-ondas e utensílios pra cozinhar como em casa.'),
                   dict(img=g(67), title='Quarto', text='Cama de casal, ar-condicionado, TV e roupa de cama.'),
                   dict(img=g(1), title='Área coberta', text='Mesa grande e bancos pra refeição em grupo, ao lado da churrasqueira.'),
                   dict(img=g(53), title='À noite', text='Fachada iluminada e garagem pro carro ficar em segurança.')]
    p['plan'] = dict(kicker='Acomodações', title='Escolha o seu espaço na Goulin.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Studio', note='até 2 hóspedes', img=g(36),
                                 cells=['Cozinha americana', 'Cama de casal', 'Ar-condicionado', 'TV', 'Banheiro privativo']),
                            dict(name='Apartamento', note='até 4 hóspedes', img=g(68),
                                 cells=['Quarto de casal', 'Cozinha completa', 'Ar-condicionado', 'TV', 'Banheiro privativo']),
                            dict(name='Casa', note='até 8 hóspedes', img=g(0),
                                 cells=['Para até 8 pessoas', 'Área com mesa grande', 'Churrasqueira', 'Cozinha', 'Estacionamento'])])
    p['exp'] = dict(title='O norte da Ilha começa aqui.',
                    big=dict(img=G(4, True), title='Dunas e Praia do Moçambique', text='Uma das praias mais selvagens de Floripa, com mar aberto, dunas e restinga.'),
                    wide=dict(img=G(8), title='Lagoa da Conceição', text='A lagoa, o centrinho e as praias do leste ficam a poucos minutos de carro.'),
                    list_title='Mais pra explorar',
                    list=[('wave', 'Praia do Moçambique'), ('board', 'Surf no Moçambique'), ('hike', 'Trilhas do norte da Ilha'), ('lagoon', 'Barra da Lagoa')],
                    small=dict(img=G(13), title='Parque do Rio Vermelho', text='Bosque de pinus e trilhas na reserva ao lado da pousada.'))
    items = [
        ('Lais J.', 'Google', 'Lugar maravilhoso, já fui por duas vezes e recomendo sempre. É muito limpo, confortável e uma ótima localização. E o proprietário muito querido e acessível.'),
        ('Simone N.', 'Google', 'Pousada com tudo que precisamos para passar as férias, limpa e muito organizada, lugar tranquilo, mercado, farmácia, restaurante perto, boa localização.'),
        ('Samuel L.', 'Google', 'Uma ótima alternativa de estadia na ilha. Começando pelo anfitrião, que é muito atencioso e prestativo. A localização é perfeita, próxima do norte da ilha e da lagoa.'),
        ('Larissa A.', 'Google', 'Lugar aconchegante, silencioso, ótimo para descansar. Quando chegamos estava tudo limpinho e cheiroso! A praia é muito linda e a trilha é show!'),
        ('Cristieli S.', 'Google', 'Lugar maravilhoso. Limpo, organizado, preço bom. Felipe muito atencioso e prestativo. Já faz uns 5 anos que vamos sempre.'),
        ('Maykon S.', 'Google', 'Excelente! Flat bem estruturado, limpinho, organizado, atendimento nota 10, recomendo e pretendo voltar.'),
        ('Tania P.', 'Google', 'Estadia muito agradável, lugar tranquilo, anfitrião muito atencioso, vale muito a pena pra quem quer descansar e aproveitar as maravilhas da ilha!'),
        ('Debora N.', 'Google', 'Ótimo lugar, ambiente super limpo, Felipe muito atencioso, show de bola, fiquei 5 dias e deu pra conhecer outras praias.'),
    ]
    p['reviews'] = dict(title='Quem vem uma vez, volta.', count=52, rating='5,0',
                        bars=[('Google', '5,0', 100)],
                        note='5,0 no Google · 52 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='5,0 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('A praia fica longe?', 'A pousada fica no São João do Rio Vermelho, pertinho da Praia do Moçambique.'),
                ('Os apartamentos têm cozinha?', 'Sim. Studios e apartamentos têm cozinha equipada, geladeira e utensílios.'),
                ('Tem garagem?', 'Sim, há garagem para os hóspedes.'),
                ('Tem opção para grupos?', 'Sim. Temos uma casa para até 8 pessoas, com área coberta e churrasqueira.'),
                ('Qual o horário de check-in e check-out?', 'Combine o horário de chegada e saída com o Felipe pelo WhatsApp.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A gente confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=G(14, True), title='Reserve seu canto no norte da Ilha.',
                    text='Escolha as datas, chame a gente no WhatsApp e venha curtir a praia.')
    return p
