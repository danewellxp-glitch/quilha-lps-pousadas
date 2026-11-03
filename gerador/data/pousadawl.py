"""Pousada WL - Alojamento para Atletas (R. Ten. Calandrini, 452, Carianos, Florianópolis) — LP no template 'stayora'.
@pousadawl (1.718 seg., ~60 posts, quase tudo reel/arte com atletas) · Google 4,9 (94). Não está no Booking nem no Airbnb; o Facebook
(facebook.com/pousadawl, 43 seg.) não tem recomendações. Sem site próprio: o perfil do Google aponta pro Instagram (argumento de venda).
Hospedagem para jovens atletas em frente ao Estádio da Ressacada (Avaí), a 10 min do Campeche e perto do aeroporto. Também recebe pais
e visitantes por poucas noites (reviews). Fundador/anfitrião: Willians (@willianswl), citado como "Will" nas avaliações.
Telefone: (48) 99995-8971 no Google; o Facebook mostra (48) 9995-8971 (falta um dígito) — usado o do Google.
Fotos: Google Maps (gm, idx 0 e 6-12 são da WL; 1-5 e 13-15 são de outros lugares) + Instagram (ig, 11 fotos escolhidas de 87).
Fotos de atletas: só cenas de grupo, sem close de menor. Sem preço e sem horário de check-in publicados (não inventar)."""
from fotos import Fotos

TEMPLATE = 'stayora'
ENHANCE = True
F = Fotos('pousadawl')
MAPS = 'https://www.google.com/maps/search/?api=1&query=Pousada+WL+Carianos+Florian%C3%B3polis'

# azul-marinho das artes do IG (azul do Avaí) + preto/branco do logo
T = dict(bg='#f5f6f8', alt='#e8ebf1', ink='#0c1220', ink2='#141c2e', muted='#566075', dim='#b2bac9',
         dark='#0a1120', card='#f5f6f8', accent='#1d4fa0', line='#d7dce6')

P = dict(
    slug='pousadawl', name='Pousada WL', short='Pousada WL',
    seo_title='Pousada WL | Alojamento para atletas em frente à Ressacada, Carianos, Florianópolis',
    meta_desc='Pousada WL: hospedagem para jovens atletas e suas famílias em frente ao Estádio da Ressacada (Avaí), em Carianos, Florianópolis. Alimentação, piscina, ambiente seguro e acompanhamento de perto. Nota 4,9 no Google.',
    phone='(48) 99995-8971', wa_number='5548999958971', email='',
    wa_text='Olá, Willians! Vim pelo site da Pousada WL e queria informações sobre hospedagem.', instagram='pousadawl', maps_url=MAPS,
    address='R. Ten. Calandrini, 452 · Carianos, Florianópolis/SC · 88047-600', checkin='', checkout='',
    footer_tag='Hospedagem para jovens atletas, em frente à Ressacada. Evolução dentro e fora de campo.',
    nav=[('A pousada', '#sobre'), ('Estrutura', '#comodidades'), ('Espaços', '#espacos'),
         ('Hospedagem', '#acomodacoes'), ('Rotina', '#experiencias'), ('Dúvidas', '#faq')],
)

COLORS = ['#1d4fa0', '#c08a1e', '#2f6b4f', '#14213d', '#8a3b3b', '#2a6f97', '#5b4b8a', '#a0603a', '#3d5a80']


def context(I, wa):
    G = lambda i, big=False, crop=None: I(F.gm(i), big=big, crop=crop)[0]
    S = lambda i, big=False, crop=None: I(F.ig(i), big=big, crop=crop)[0]
    p = dict(P)
    p['hero'] = dict(img=G(9, True, (0.12, 0.12, 1, 0.82)), alt='Piscina da Pousada WL com coqueiros e a rede do campinho ao fundo',
                     title='Sua casa em Floripa, em frente à Ressacada',
                     sub='Hospedagem para jovens atletas e suas famílias em Carianos, com alimentação, piscina, ambiente seguro e o acompanhamento de perto do Willians.',
                     avatars=[('J', '#1d4fa0'), ('A', '#c08a1e'), ('T', '#2f6b4f')],
                     proof='4,9 no Google', proof_sub='94 avaliações de atletas e pais')
    p['about'] = dict(imgs=[G(0), S(6)], alts=['Fachada da Pousada WL com o logo na parede', 'Atletas reunidos na área da piscina'],
                      stat_num='4.9', stat_dec=1, stat_txt='4,9', stat_label='Nota no Google · 94 avaliações',
                      kicker='A pousada', title='Um lar pra quem está correndo atrás do sonho.',
                      text='A Pousada WL fica em Carianos, bem em frente ao Estádio da Ressacada, casa do Avaí, a poucos minutos do aeroporto e a 10 minutos da praia do Campeche. Recebe jovens atletas que vêm para avaliações ou para passar a temporada no clube, e também os pais e visitantes que querem ficar por perto. Comida boa, casa limpa, regras claras e alguém de confiança cuidando de tudo: é isso que deixa as famílias tranquilas.')
    p['amen_title'] = 'Estrutura pensada pra rotina de quem treina.'
    p['amenities'] = [('pin', 'Em frente à Ressacada'), ('food', 'Alimentação na pousada'), ('pool', 'Piscina'),
                      ('shield', 'Ambiente seguro e familiar'), ('users', 'Acompanhamento dos atletas'), ('star', 'Sala de jogos'),
                      ('wifi', 'Wi-Fi'), ('tv', 'TV'), ('broom', 'Casa sempre limpa'),
                      ('plane', 'Pertinho do aeroporto'), ('wave', 'Campeche a 10 min'), ('chat', 'Suporte 24 horas')]
    p['spaces_title'] = 'Simples, limpo e do jeito que o atleta precisa.'
    p['spaces'] = [dict(img=G(9), title='Piscina', text='Pra relaxar depois do treino ou de uma viagem longa, com o campinho logo ao lado.'),
                   dict(img=G(7), title='Quartos compartilhados', text='Beliches, ventilador e espaço organizado pra dividir com os colegas de time.'),
                   dict(img=G(11), title='Quartos', text='Ambientes arejados, com ventilador de teto, TV e roupa de cama.'),
                   dict(img=G(8), title='Área externa', text='Mesas ao ar livre pra refeição, conversa e aquele tempo de folga.'),
                   dict(img=G(10), title='Entrada e pátio', text='Casa murada, pátio com coqueiro e entrada direta pela Ten. Calandrini.')]
    p['host'] = dict(img=G(0), alt='Fachada da Pousada WL com o logo', name='Willians, fundador',
                     lines=[('users', 'Acompanha os atletas de perto'), ('chat', 'Suporte 24 horas'), ('pin', 'Carianos, em frente à Ressacada')],
                     quote='Willians hospedou meu filho por uma semana, período em que esteve em avaliação no Avaí. Acolhimento, cuidado e segurança.',
                     text='Palavras da Marilene O., mãe de atleta. A atenção do Willians com os meninos é o que mais aparece nas avaliações dos pais.')
    p['plan'] = dict(kicker='Hospedagem', title='Do período de avaliação à temporada inteira.',
                     foot='Formatos citados por hóspedes nas avaliações · condições e valores direto com a pousada',
                     rooms=[dict(name='Atleta em avaliação', note='alguns dias ou semanas', img=G(7),
                                 cells=['Estadia durante a avaliação no clube', 'Em frente à Ressacada', 'Quarto compartilhado',
                                        'Alimentação na pousada', 'Acompanhamento e segurança']),
                            dict(name='Temporada', note='meses no clube', img=S(9),
                                 cells=['Pra quem já joga no clube', 'Rotina organizada e disciplina', 'Convivência com o grupo',
                                        'Refeições e casa limpa', 'Os pais acompanham de longe, tranquilos']),
                            dict(name='Pais e visitantes', note='poucas noites', img=G(11),
                                 cells=['Pra quem vem acompanhar o atleta', 'Pertinho do aeroporto', 'Quarto com TV e Wi-Fi',
                                        'Piscina e área externa', 'Dicas de restaurantes e mercados'])])
    p['exp'] = dict(title='A rotina na WL vai além do quarto.',
                    big=dict(img=S(1, True), title='Noites em família', text='Confraternizações na beira da piscina, com atletas, pais e a equipe da casa.'),
                    wide=dict(img=S(10), title='Comida boa todo dia', text='A alimentação é um dos pontos mais elogiados por atletas e pais.'),
                    list_title='Tudo pertinho',
                    list=[('pin', 'Estádio da Ressacada em frente'), ('plane', 'Aeroporto a poucos minutos'),
                          ('wave', 'Praia do Campeche a 10 min'), ('home', 'Mercados, padarias e restaurantes no bairro')],
                    small=dict(img=S(7), title='Mesa cheia', text='Jantar ao ar livre na área da piscina.'))
    items = [
        ('Telma M.', 'Google', 'Local extremamente agradável para atletas e familiares. Ambiente seguro e acolhedor; o proprietário é extremamente responsável e atencioso.'),
        ('Émerson G.', 'Google', 'Morei um tempo na pousada enquanto jogava no Avaí e recomendo muito. Lugar limpo, aconchegante, com o melhor preço da região, e donos muito atenciosos.'),
        ('Andrea C.', 'Google', 'Me senti segura e satisfeita com o ambiente e com as pessoas. Gostei muito da atenção do proprietário, o Will, bastante prestativo.'),
        ('João Vitor M.', 'Google', 'Lugar bem localizado, perto do clube, alimentação muito boa! Recomendo para todos os atletas e pais.'),
        ('Jefferson S.', 'Google', 'Fui muito bem recebido, cuidaram por 5 meses do meu filho, ganhei amigos. Super recomendo.'),
        ('Crislaine V.', 'Google', 'Ótimo pra quem procura um lugar perto do estádio do Avaí. Seguro, limpo e organizado, com alimentação, sala de jogos e piscina.'),
        ('Edson C.', 'Google', 'Fomos bem recebidos depois de 9h de viagem e ainda ganhamos dicas de restaurantes. Bem perto do aeroporto. Na próxima vez, já sei onde ficar.'),
        ('Bruno D.', 'Google', 'Pousada limpa, organizada, ambiente seguro e o proprietário dá toda atenção. Indico para atletas que vão jogar no Avaí.'),
        ('Mariana T.', 'Google', 'Ambiente familiar, atenção adequada aos atletas, disciplina e respeito.'),
        ('Luiciano A.', 'Google', 'Muito atencioso e receptivo. Fiquei bem tranquilo em mandar meu filho para lá.'),
        ('Mateus F.', 'Google', 'Ambiente bom e acolhedor para a família, excelente localização e próximo de tudo. Excelente alimentação.'),
        ('Janaina V.', 'Google', 'Super acolhedor! Tudo limpinho, e nos ajudaram informando restaurantes, padarias e mercados.'),
    ]
    p['reviews'] = dict(title='Os pais confiam. Os atletas recomendam.', count=94, rating='4,9',
                        bars=[('Google', '4,9', 98)],
                        note='4,9 no Google (94 avaliações) · trechos resumidos de avaliações públicas',
                        link=MAPS, headline='4,9 no Google', sources=[],
                        items=[dict(author=a, source=s, text=t, stars=5, color=COLORS[i % len(COLORS)]) for i, (a, s, t) in enumerate(items)])
    p['faq'] = [('Para quem é a Pousada WL?', 'Para jovens atletas que vêm a Florianópolis para avaliações ou para jogar uma temporada no clube, e também para os pais e visitantes que querem ficar perto do estádio.'),
                ('Fica perto do Avaí?', 'Fica em frente ao Estádio da Ressacada, em Carianos. Dá pra ir a pé.'),
                ('Tem alimentação?', 'Sim, a pousada oferece alimentação. É um dos pontos mais elogiados pelos atletas e pelos pais nas avaliações.'),
                ('Os pais podem acompanhar e se hospedar?', 'Podem. Muitos pais ficam alguns dias na pousada e outros acompanham de longe, com o Willians mantendo contato.'),
                ('Por quanto tempo dá pra ficar?', 'De uma noite até meses. Tem atleta que fica só o período de avaliação e quem mora na pousada a temporada inteira. Combine direto com a gente.'),
                ('Recebe atletas do futebol feminino?', 'Sim, a WL também recebe meninas. Chame no WhatsApp para saber como funciona a hospedagem.'),
                ('Fica longe do aeroporto?', 'Não, Carianos é o bairro do aeroporto de Florianópolis. Em poucos minutos você está na pousada.'),
                ('Como faço pra reservar?', 'Escolha as datas no calendário e envie pelo WhatsApp. O Willians confirma a disponibilidade e as condições com você.')]
    p['cta'] = dict(img=G(12, True), title='Fale direto com o Willians.',
                    text='Conte quem é o atleta, o clube e o período, e tire suas dúvidas pelo WhatsApp.')
    return p
