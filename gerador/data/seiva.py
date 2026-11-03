"""SEIVA Pousada da Lagoa (R. Ver. Osni Ortiga, 397, Dunas da Lagoa, Florianópolis) — site no template 'stayora'.
Fotos: Google Maps 2ª passada (gm2, quase todas verticais). No Booking aparece como 'Pousada da Lagoa' (8,6).
Donos atuais citados nas avaliações recentes: Juliano e Giovanna (antes: Fernando; Rodrigo e Isabel). 6 quartos, café da manhã."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('seiva')
MAPS = 'https://www.google.com/maps/search/?api=1&query=SEIVA+Pousada+da+Lagoa+R.+Ver.+Osni+Ortiga+397+Florian%C3%B3polis'

T = dict(bg='#f6f5f0', alt='#e8ebe6', ink='#111614', ink2='#19211e', muted='#56615c', dim='#b6bdb9',
         dark='#0c1311', card='#f6f5f0', accent='#2a6f8f', line='#dde0da')

P = dict(
    slug='seiva', name='SEIVA Pousada da Lagoa', short='SEIVA',
    seo_title='SEIVA Pousada da Lagoa | Lagoa da Conceição, Florianópolis',
    meta_desc='SEIVA Pousada da Lagoa: pousada familiar de frente para a Lagoa da Conceição, a poucos minutos da Rua das Rendeiras e das dunas da Joaquina. Café da manhã caseiro e quartos limpinhos.',
    phone='(48) 99151-9979', wa_number='5548991519979', email='',
    wa_text='Olá! Vim pelo site da SEIVA Pousada da Lagoa e queria consultar disponibilidade.', instagram='', maps_url=MAPS,
    address='R. Ver. Osni Ortiga, 397 · Dunas da Lagoa, Florianópolis/SC', checkin='14h', checkout='12h',
    footer_tag='Pousada familiar de frente pra Lagoa da Conceição, com café caseiro e as dunas logo ali.',
    nav=[('A pousada', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Quartos', '#acomodacoes'), ('Experiências', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#2a6f8f', '#b5762a', '#3f6b5c', '#14313a', '#8a5a44', '#2e7a57', '#6b5b95', '#c06c84']


def context(I, wa):
    G = lambda i, big=False: I(F._get('gm2', i), big=big)[0]
    p = dict(P)
    p['hero'] = dict(img=G(53, True), alt='Trapiche na Lagoa da Conceição em frente à pousada',
                     title='A Lagoa da Conceição na porta de casa',
                     sub='Pousada familiar com café da manhã caseiro, a poucos passos da beira da lagoa e da Rua das Rendeiras.',
                     avatars=[('E', '#2a6f8f'), ('A', '#b5762a'), ('G', '#3f6b5c')],
                     proof='Nota 4,6', proof_sub='189 avaliações no Google')
    p['about'] = dict(imgs=[G(0), G(25)], alts=['Fachada da pousada com o mural da lagoa', 'Suíte com quadro e cama de casal'],
                      stat_num='4.6', stat_dec=1, stat_txt='4,6', stat_label='Nota no Google',
                      kicker='A pousada', title='Uma casa de família de frente pra lagoa.',
                      text='A SEIVA é uma pousada pequena e familiar nas Dunas da Lagoa, do outro lado da rua da Lagoa da Conceição. São poucos quartos, todos limpos e cheirosos, com cama gostosa e chuveiro bom. De manhã tem café caseiro com bolos feitos na casa, e o centrinho da Lagoa, a Rua das Rendeiras e as dunas da Joaquina ficam a poucos minutos.')
    p['amen_title'] = 'O essencial, feito com carinho.'
    p['amenities'] = [('coffee', 'Café da manhã caseiro'), ('wifi', 'Wi-Fi gratuito'), ('tv', 'Smart TV com Netflix'),
                      ('bed', 'Cama confortável'), ('bath', 'Chuveiro forte'), ('lagoon', 'Lagoa em frente'),
                      ('board', 'Empréstimo de caiaque e sandboard'), ('sun', 'Cadeira e guarda-sol de praia'), ('kitchen', 'Cozinha em alguns quartos'),
                      ('plane', 'Traslado do aeroporto'), ('users', 'Ideal pra famílias'), ('clock', 'Check-in 14h · check-out 12h')]
    p['spaces_title'] = 'Pequena, aconchegante e cheia de detalhes.'
    p['spaces'] = [dict(img=G(26), title='Suítes', text='Cama de casal, roupa de cama impecável, quadros de praia e janela pro verde.'),
                   dict(img=G(21), title='Café da manhã', text='Bolos caseiros, frutas, pães e omelete feito na hora.'),
                   dict(img=G(12), title='Recepção', text='Parede pintada à mão, banco de madeira e as dicas de quem conhece a Lagoa.'),
                   dict(img=G(29), title='Varanda', text='Deck de madeira com vasos de flores pra tomar um café ao ar livre.'),
                   dict(img=G(55), title='Visitas no telhado', text='Os saguis da Lagoa aparecem quase todo dia pra dar bom-dia.')]
    p['host'] = dict(img=G(16), alt='Recepção da Pousada da Lagoa', name='Juliano e Giovanna',
                     lines=[('star', 'Nota 4,6 no Google'), ('pin', 'De frente pra Lagoa da Conceição'), ('chat', 'Atendimento direto pelo WhatsApp')],
                     quote='Pensa num casal gente boa. A pousada reflete a energia deles. Limpa, cheirosa, cama gostosa e chuveiro bom.',
                     text='Palavras da Elaine, uma das hóspedes. Na SEIVA quem recebe é o próprio casal, com os bolos da Giovanna no café e as dicas do Juliano pra aproveitar a Ilha.')
    p['plan'] = dict(kicker='Quartos', title='Escolha o seu quarto.', foot='Distribuição ilustrativa · confirme os detalhes com a pousada',
                     rooms=[dict(name='Suíte Casal', note='até 2 hóspedes', img=G(25),
                                 cells=['Cama de casal', 'Banheiro privativo', 'Smart TV', 'Ventilador de teto', 'Café da manhã']),
                            dict(name='Suíte Família', note='até 4 hóspedes', img=G(4),
                                 cells=['Cama de casal', 'Beliche', 'Banheiro privativo', 'Ventilador de teto', 'Café da manhã']),
                            dict(name='Quarto com Varanda', note='até 2 hóspedes', img=G(35),
                                 cells=['Cama de casal', 'Porta pra varanda', 'Vista pro verde', 'Smart TV', 'Café da manhã'])])
    p['exp'] = dict(title='A Lagoa, as dunas e a Joaquina, logo ali.',
                    big=dict(img=G(24, True), title='Dunas da Joaquina', text='Sandboard e pôr do sol nas dunas, a poucos minutos da pousada.'),
                    wide=dict(img=G(65), title='Beira da Lagoa', text='Caminhada, stand up e caiaque na Lagoa da Conceição, do outro lado da rua.'),
                    list_title='Mais pra explorar',
                    list=[('food', 'Restaurantes da Rua das Rendeiras'), ('board', 'Sandboard nas dunas'), ('wave', 'Joaquina e Praia Mole'), ('hike', 'Trilha da Costa da Lagoa')],
                    small=dict(img=G(44), title='Café caseiro', text='Servido toda manhã, com bolo de laranja que os hóspedes não esquecem.'))
    items = [
        ('Edina S.', 'Google', 'Atendimento excelente desde o online até a chegada. O Juliano é um cara da vibe muito boa, a pousada fica próxima das melhores praias da ilha, da lagoa e do centrinho.'),
        ('Elaine Z.', 'Google', 'Pensa num casal gente boa. Limpa, cheirosa, cama gostosa e chuveiro bom. O café da manhã bem servido e os bolos da Giovanna são uma delícia.'),
        ('Gábriele T.', 'Google', 'Ficamos uma semana na pousada. A Giovanna e o Juliano foram super atenciosos, simpáticos e prestativos. Bem limpa e organizada.'),
        ('Aline', 'Google', 'Ótima pousada familiar. Suíte sempre limpa, roupas de cama e toalhas impecáveis, chuveiro bom. Café da manhã excelente, com bolos (o de laranja foi o melhor que já comi).'),
        ('Nathalia G.', 'Google', 'Ótima localização, a uns 2 minutos andando da Rua das Rendeiras, em frente à Lagoa, com bares, restaurantes, passeios, mercado e farmácia.'),
        ('Jamir M.', 'Google', 'Atendimento perfeito desde o contato telefônico. Funcionários educados e prestativos. Limpeza e café da manhã excelentes.'),
        ('Fabiana C.', 'Google', 'Ótima pousada, perto da Lagoa. Empresta caiaque, cadeiras, barraca de praia e sandboard. Tem café da manhã e a televisão tem Netflix.'),
        ('Alejandro M.', 'Google', 'Um ótimo lugar para aproveitar a Lagoa da Conceição. Confortável, tranquilo, sem luxos, mas com esse gosto de se sentir em casa.'),
    ]
    p['reviews'] = dict(title='O tipo de estadia que os hóspedes comentam.', count=189, rating='4,6',
                        bars=[('Google', '4,6', 92), ('Booking', '8,6', 86)],
                        note='4,6 no Google · 189 avaliações · trechos de avaliações públicas', link=MAPS,
                        headline='4,6 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 14h e o check-out até as 12h. Se precisar de outro horário, combine com a gente pelo WhatsApp.'),
                ('O café da manhã está incluso?', 'Sim. O café da manhã caseiro é servido todas as manhãs, com bolos feitos na casa.'),
                ('Tem estacionamento?', 'As vagas são poucas, então avise na reserva se vier de carro pra gente reservar a sua.'),
                ('A lagoa fica perto?', 'A beira da Lagoa da Conceição fica do outro lado da rua, e a Rua das Rendeiras a poucos minutos a pé.'),
                ('Vocês emprestam equipamento de praia?', 'Sim: caiaque, cadeiras, guarda-sol e prancha de sandboard pra curtir a lagoa e as dunas.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. A gente confirma disponibilidade e valor com você.')]
    p['cta'] = dict(img=G(69, True), title='Reserve seus dias na Lagoa.',
                    text='Escolha as datas, chame a gente no WhatsApp e garanta seu quarto com café caseiro e a lagoa em frente.')
    return p
