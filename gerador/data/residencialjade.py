"""Residencial Jade (Servidão Maria Serafina de Oliveira, 140, Cachoeira do Bom Jesus, Florianópolis) — LP no template 'stayora'.
Fotos: Airbnb (ab, 32 fotos em 1920px, anúncios AP1 54355642 e AP5 14251772). Instagram @residencialjade é pequeno (323 seg., 27 posts, muito reel).
Notas: Google 4,8 (185) · Airbnb perfil do anfitrião 4,91 (430), AP1 4,95 (19), AP5 4,96 (107) · Booking 8,9 (53, só pelo snippet do Google).
Anfitrião: José (Superhost há 11 anos, responde em até 1h) e a esposa. Apartamentos completos de 1 quarto (3 camas, até 4 pessoas).
Sem café da manhã e sem piscina. Site atual residencialjade.com.br é um motor de reserva com seções vazias; o perfil do Google não aponta pra ele.
Fotos ab 22, 23 e 26 têm o rótulo 'Residencial Jade' gravado (drone): 23 descartada; 22 recortada (0,0.5,1,1) e 26 recortada (0.30,0,1,1), ambas sem o rótulo. A 21 tem o rótulo no telhado: descartada."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('residencialjade')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Residencial+Jade+Cachoeira+do+Bom+Jesus+Florian%C3%B3polis'

# verde-jade do azulejo da fachada + madeira
T = dict(bg='#f6f4ee', alt='#e7ece8', ink='#0f1615', ink2='#172220', muted='#55615d', dim='#b3bdb9',
         dark='#0b1413', card='#f6f4ee', accent='#1d7366', line='#d8dfdb')

P = dict(
    slug='residencialjade', name='Residencial Jade', short='Residencial Jade',
    seo_title='Residencial Jade | Apartamentos a 150 m do mar na Cachoeira do Bom Jesus, Florianópolis',
    meta_desc='Residencial Jade: apartamentos completos para até 4 pessoas, com cozinha, varanda, ar-condicionado e estacionamento, a 150 m da praia da Cachoeira do Bom Jesus. Pet friendly. Nota 4,8 no Google.',
    phone='(48) 98404-6503', wa_number='5548984046503', email='',
    wa_text='Olá, José! Vim pelo site do Residencial Jade e queria consultar disponibilidade.', instagram='residencialjade', maps_url=MAPS,
    address='Servidão Maria Serafina de Oliveira, 140 · Cachoeira do Bom Jesus, Florianópolis/SC', checkin='14h', checkout='10h',
    footer_tag='Apartamentos completos a 150 m do mar, num bairro tranquilo do norte da Ilha.',
    nav=[('O residencial', '#sobre'), ('Comodidades', '#comodidades'), ('Espaços', '#espacos'),
         ('Apartamento', '#acomodacoes'), ('Arredores', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#1d7366', '#a0603a', '#3f6b5c', '#14313a', '#8a5a44', '#2a6f97', '#6b5b95', '#c06c84', '#5b7f3a']


def context(I, wa):
    A = lambda i, big=False, crop=None: I(F._get('ab', i), big=big, crop=crop)[0]
    p = dict(P)
    p['hero'] = dict(img=A(6, True), alt='Vista aérea da Cachoeira do Bom Jesus com o mar e as ilhas ao fundo',
                     title='Seu apartamento a 150 m do mar, no norte da Ilha',
                     sub='Apartamentos completos para até 4 pessoas na Cachoeira do Bom Jesus, com cozinha, varanda e o atendimento do Sr. José, Superhost há 11 anos.',
                     avatars=[('A', '#1d7366'), ('M', '#a0603a'), ('R', '#3f6b5c')],
                     proof='4,8 no Google', proof_sub='185 avaliações · 4,91 no Airbnb')
    p['about'] = dict(imgs=[A(14), A(5)], alts=['Varanda com mesa, azulejo verde-jade e porta de madeira', 'Vista aérea do Residencial Jade'],
                      stat_num='4.91', stat_dec=2, stat_txt='4,91', stat_label='Média no Airbnb · 430 avaliações',
                      kicker='O residencial', title='Casa de praia, com cara de casa mesmo.',
                      text='O Residencial Jade fica numa servidão tranquila da Cachoeira do Bom Jesus, a uns 150 m do mar. São apartamentos completos, com quarto, sala e cozinha equipada, para até 4 pessoas, com varanda, ar-condicionado, Wi-Fi por fibra e estacionamento privativo. Quem recebe é o próprio José, com a esposa, há mais de 11 anos.')
    p['amen_title'] = 'O que você precisa pra ficar à vontade, como em casa.'
    p['amenities'] = [('wave', 'Praia a 150 m'), ('kitchen', 'Cozinha completa'), ('snow', 'Ar-condicionado'),
                      ('wifi', 'Wi-Fi por fibra óptica'), ('parking', 'Estacionamento privativo'), ('paw', 'Pet friendly'),
                      ('tv', 'TV a cabo e Chromecast'), ('users', 'Ideal pra famílias'), ('food', 'Churrasqueira'),
                      ('broom', 'Serviço de lavanderia'), ('plane', 'Traslado do aeroporto'), ('clock', 'Check-in 14h · check-out 10h')]
    p['spaces_title'] = 'Tudo no lugar, limpinho e pronto pra chegar.'
    p['spaces'] = [dict(img=A(11), title='O quarto', text='Cama de casal, enxoval trocado, ar-condicionado e ventilador de teto.'),
                   dict(img=A(32), title='Sala e cozinha', text='Ambiente integrado, com sofá, mesa pra quatro e cozinha completa.'),
                   dict(img=A(9), title='Cozinha equipada', text='Fogão, geladeira, micro-ondas, cafeteira, torradeira e louça completa.'),
                   dict(img=A(25), title='Varanda', text='Mesinha na varanda pra tomar o café olhando a rua tranquila.'),
                   dict(img=A(2), title='Pátio e churrasqueira', text='Área comum com churrasqueira e estacionamento dentro do residencial.')]
    p['host'] = dict(img=A(1), alt='Fachada do Residencial Jade com azulejo verde-jade e madeira', name='Sr. José e esposa',
                     lines=[('star', 'Superhost no Airbnb há 11 anos'), ('chat', 'Responde em até 1 hora'), ('pin', 'Cachoeira do Bom Jesus, a 150 m do mar')],
                     quote='O diferencial é o nível de atendimento do proprietário, o Sr. José, e sua esposa, sempre simpáticos e prestativos.',
                     text='Palavras do Andre, de Porto Alegre, que já voltou pela segunda vez. O atendimento do José é o que mais aparece nos comentários dos hóspedes.')
    p['plan'] = dict(kicker='Acomodação', title='Um apartamento completo, do jeito que a família precisa.',
                     foot='Distribuição ilustrativa · confirme os detalhes de cada apartamento com o residencial',
                     rooms=[dict(name='Apartamento completo', note='até 4 hóspedes', img=A(12),
                                 cells=['1 quarto + sala', '3 camas · até 4 pessoas', 'Quarto com cama de casal',
                                        'Cozinha completa', 'Ar, Wi-Fi e TV a cabo'])])
    p['exp'] = dict(title='A praia na porta, o norte da Ilha inteiro por perto.',
                    big=dict(img=A(26, True, (0.30, 0, 1, 1)), title='Cachoeira do Bom Jesus', text='Mar calmo e areia clara a uns 150 m do residencial, com o comércio do bairro ao lado.'),
                    wide=dict(img=A(22, False, (0, 0.5, 1, 1)), title='Pé na areia', text='Mar calmo e bairro tranquilo, ótimo pra descansar e caminhar na beira da praia.'),
                    list_title='Tudo pertinho',
                    list=[('home', 'Mercado, farmácia e padaria a pé'), ('food', 'Centrinho de Canasvieiras a 5 min de carro'),
                          ('wave', 'Ponta das Canas e Lagoinha'), ('car', 'Fácil de estacionar e de sair pra passear')],
                    small=dict(img=A(30), title='A orla à noite', text='Calçadão iluminado pra caminhar depois do jantar.'))
    items = [
        ('Andre L.', 'Google', 'Excelente lugar para passar as férias e descansar. O apartamento é muito aconchegante e bem equipado. Já é a segunda vez que nos hospedamos.'),
        ('Robson F.', 'Airbnb', 'Fiquei com minha esposa e meu filho de 8 meses: conforto e praticidade. Seu José muito educado e prestativo. Perto de farmácia, mercado, padaria e praia.'),
        ('Michelle C.', 'Google', 'Lugar aconchegante, tudo limpo e organizado. Sr. José e a esposa muito atenciosos. Wi-Fi muito bom e colchão muito confortável.'),
        ('Cristian', 'Airbnb', 'Localização muito boa, lugar confortável e silencioso. O José foi muito atencioso e nosso pet foi bem-vindo. 100% recomendado.'),
        ('Fernanda M.', 'Google', 'Local super agradável, bem equipado e pertinho da praia. Cozinha, ar-condicionado, chuveiro muito bom e TV. Preço justo e um excelente anfitrião.'),
        ('Fabio A.', 'Airbnb', 'Tudo estava em ordem e limpo. José foi muito simpático e sempre disponível para qualquer dúvida.'),
        ('Yasmim J.', 'Google', 'Ambiente calmo e localização ótima, perto de tudo. Quando voltamos, o apartamento estava cheiroso, organizado e com as toalhas trocadas.'),
        ('Cassilda R.', 'Google', 'O Sr. José é um excelente anfitrião, sempre atento no WhatsApp. Amamos a estadia: quarto confortável com ar e cozinha com o necessário.'),
        ('Hyojeong', 'Airbnb', 'A cinco minutos a pé da praia e do supermercado, ruas tranquilas e estacionamento fácil. O apartamento era exatamente como nas fotos.'),
    ]
    p['reviews'] = dict(title='Os hóspedes voltam, e contam por quê.', count=668, rating='4,8',
                        bars=[('Google', '4,8', 96), ('Airbnb', '4,91', 98), ('Booking', '8,9', 89)],
                        note='4,8 no Google (185) · 4,91 no Airbnb (430, perfil do anfitrião) · 8,9 no Booking (53) · trechos de avaliações públicas',
                        link=MAPS, headline='4,8 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Qual o horário de check-in e check-out?', 'O check-in é a partir das 14h e o check-out até as 10h. Se precisar de outro horário, é só combinar com o José pelo WhatsApp.'),
                ('A que distância fica a praia?', 'A praia da Cachoeira do Bom Jesus fica a uns 150 m, poucos minutos a pé. Mercado, farmácia e padaria também ficam pertinho.'),
                ('Tem café da manhã?', 'Não servimos café da manhã, mas todos os apartamentos têm cozinha completa, com cafeteira, torradeira, micro-ondas, fogão e louça.'),
                ('Quantas pessoas cabem no apartamento?', 'Os apartamentos têm 1 quarto e sala, com 3 camas, para até 4 pessoas.'),
                ('Posso levar meu pet?', 'Sim, o Residencial Jade é pet friendly. Avise na hora da reserva.'),
                ('Tem estacionamento?', 'Sim, estacionamento privativo e gratuito dentro do residencial.'),
                ('Como faço a reserva?', 'Escolha as datas no calendário e envie pelo WhatsApp. O José confirma a disponibilidade e o valor com você.')]
    p['cta'] = dict(img=A(28, True), title='Reserve direto com o José.',
                    text='Escolha as datas, chame no WhatsApp e garanta seu apartamento a 150 m da praia da Cachoeira do Bom Jesus.')
    return p
