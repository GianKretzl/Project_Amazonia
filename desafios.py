"""
Sistema de Desafios Educacionais - Projeto Sombra Roxa
Desafios organizados por personagem e disciplina:
- Dr. Arnaldo Silva (Ciências)
- Valdemar (Geografia)
- Pajé Yakamu (História)
- Deputado Venturi (Matemática + Português)
"""

DESAFIOS = {
    # ============================================
    # DR. ARNALDO SILVA - CIÊNCIAS
    # ============================================
    'ciencias_1': {
        'id': 'ciencias_1',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'O que é bioacumulação e por que é perigosa para comunidades que vivem perto de rios contaminados?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) É quando animais acumulam músculos e ficam mais fortes',
            'B) É quando substâncias tóxicas se concentram progressivamente nos organismos através da cadeia alimentar',
            'C) É quando plantas acumulam água em suas raízes',
            'D) É quando o solo acumula nutrientes naturalmente'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Bioacumulação é o processo onde substâncias tóxicas (como mercúrio) se acumulam nos organismos. Peixes pequenos contaminados são comidos por peixes maiores, que concentram ainda mais o veneno. Comunidades ribeirinhas que dependem da pesca podem sofrer envenenamento grave.',
        'recompensa': 'dica_coltan',
        'dica_texto': '💡 DICA DESBLOQUEADA: Pergunte ao Dr. Arnaldo "Que químicos são usados para processar Coltan?"'
    },
    
    'ciencias_2': {
        'id': 'ciencias_2',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'Como a poluição química em rios pode causar eutrofização e proliferação de algas tóxicas?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) As algas se alimentam diretamente dos químicos tóxicos',
            'B) Os químicos matam predadores das algas, permitindo crescimento descontrolado',
            'C) Excesso de nutrientes (nitrogênio e fósforo) causa crescimento explosivo de algas que consomem oxigênio',
            'D) As algas mutam geneticamente e se tornam tóxicas'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Exato! Químicos industriais frequentemente contêm nutrientes como nitrogênio e fósforo. O excesso causa eutrofização - crescimento explosivo de algas que consomem todo oxigênio da água e podem produzir toxinas, criando "zonas mortas" e matando peixes.',
        'recompensa': 'pergunta_chave_1',
        'dica_texto': '🔓 PERGUNTA DESBLOQUEADA: "Por que a mancha no rio é roxa e não de outra cor?"'
    },
    
    'ciencias_3': {
        'id': 'ciencias_3',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'Qual é o impacto da contaminação por metais pesados na saúde humana a longo prazo?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Apenas problemas estomacais temporários',
            'B) Danos permanentes ao sistema nervoso, rins e desenvolvimento infantil',
            'C) Fortalecimento do sistema imunológico',
            'D) Nenhum efeito significativo em baixas doses'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Metais pesados como mercúrio, chumbo e cádmio causam danos neurológicos permanentes, afetam os rins, causam problemas cardiovasculares e são especialmente perigosos para crianças e gestantes, podendo causar deficiências no desenvolvimento.',
        'recompensa': 'dica_saude',
        'dica_texto': '💡 DICA: Pergunte "Que sintomas a população local está apresentando?"'
    },
    
    # ============================================
    # VALDEMAR - GEOGRAFIA
    # ============================================
    'geografia_1': {
        'id': 'geografia_1',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'Qual fator é essencial para a viabilidade econômica de uma fazenda na Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Apenas a vontade do fazendeiro de trabalhar duro',
            'B) Solo fértil, acesso a estradas e proximidade de mercados consumidores',
            'C) Quantidade de chuva na região',
            'D) Apoio dos povos indígenas locais'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Uma fazenda precisa de: solo fértil (raro na Amazônia após desmatamento), logística para escoar produção (estradas) e proximidade de mercados. Sem isso, os custos superam o lucro. Quando uma fazenda não tem essas condições mas existe mesmo assim... há algo suspeito!',
        'recompensa': 'dica_economia',
        'dica_texto': '💡 DICA: Pergunte ao Valdemar "Como a fazenda se mantém lucrativa com solo ruim e logística cara?"'
    },
    
    'geografia_2': {
        'id': 'geografia_2',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'O que é grilagem de terras e como ela afeta territórios indígenas na Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) É a criação legal de fazendas em áreas desmatadas',
            'B) É a apropriação ilegal de terras públicas através de documentos falsos',
            'C) É um método sustentável de agricultura',
            'D) É a proteção de áreas de preservação ambiental'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Grilagem é a falsificação de documentos para roubar terras públicas ou indígenas. Grileiros usam fazendas como "fachada" para legitimar presença ilegal, pressionam fronteiras de reservas indígenas e frequentemente estão ligados a crimes ambientais e violência.',
        'recompensa': 'dica_grilagem',
        'dica_texto': '🔓 PERGUNTA: "Quem realmente é dono da documentação da fazenda?"'
    },
    
    'geografia_3': {
        'id': 'geografia_3',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'Qual é a relação entre desmatamento e degradação do solo na Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Desmatamento melhora o solo para agricultura',
            'B) Não há relação entre desmatamento e qualidade do solo',
            'C) Sem a cobertura florestal, o solo amazônico perde nutrientes rapidamente devido à erosão e lixiviação',
            'D) O solo fica mais fértil após o desmatamento'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Correto! O solo amazônico é naturalmente pobre - os nutrientes estão nas plantas, não no solo. Sem a floresta, a chuva intensa lava (lixivia) os poucos nutrientes restantes e causa erosão. Por isso fazendas amazônicas frequentemente fracassam economicamente.',
        'recompensa': 'dica_solo',
        'dica_texto': '💡 DICA: "Se o solo é ruim, por que Valdemar mantém a fazenda?"'
    },
    
    # ============================================
    # PAJÉ YAKAMU - HISTÓRIA
    # ============================================
    'historia_1': {
        'id': 'historia_1',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'A Constituição de 1988 garante direitos aos povos indígenas no Brasil. Qual é o principal direito territorial assegurado?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Direito de comprar terras com desconto',
            'B) Direito originário sobre as terras que tradicionalmente ocupam',
            'C) Direito de alugar terras do governo',
            'D) Direito de escolher qualquer terra disponível'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! A Constituição reconhece o direito ORIGINÁRIO dos povos indígenas sobre suas terras tradicionais - ou seja, um direito anterior ao próprio Estado brasileiro. Essas terras são inalienáveis e indisponíveis, não podem ser vendidas ou invadidas.',
        'recompensa': 'dica_direitos',
        'dica_texto': '💡 DICA: Pergunte "Como invasões de terra indígena são permitidas se há proteção constitucional?"'
    },
    
    'historia_2': {
        'id': 'historia_2',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'O conhecimento tradicional indígena sobre a floresta é transmitido por gerações. Por que esse conhecimento é valioso?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Apenas por valor cultural e histórico',
            'B) Contém informações sobre plantas medicinais, manejo sustentável e localização de recursos naturais',
            'C) Não tem valor prático no mundo moderno',
            'D) Serve apenas para atrair turistas'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exatamente! O conhecimento tradicional inclui: localização de recursos (como minerais), propriedades medicinais de plantas (várias descobertas científicas vieram desse conhecimento), técnicas de manejo sustentável e mapeamento detalhado da floresta. É por isso que esse conhecimento é cobiçado!',
        'recompensa': 'dica_conhecimento',
        'dica_texto': '🔓 PERGUNTA: "Que tipo de mapa ou conhecimento ancestral vocês guardam?"'
    },
    
    'historia_3': {
        'id': 'historia_3',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'Ao longo da história do Brasil, como povos indígenas foram afetados por ciclos econômicos de exploração?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Sempre foram beneficiados economicamente',
            'B) Sofreram expulsão de terras, violência e doenças durante ciclos da borracha, ouro, madeira',
            'C) Não foram afetados pois viviam isolados',
            'D) Receberam compensação justa em todos os casos'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Durante o Ciclo da Borracha, Ciclo do Ouro, extração de madeira e agropecuária, povos indígenas foram sistematicamente expulsos, escravizados ou mortos. Esse padrão se repete: interesse econômico → invasão de terras → violência. O Coltan é apenas o mais novo ciclo dessa história trágica.',
        'recompensa': 'dica_historia',
        'dica_texto': '💡 DICA: "Quem se beneficia economicamente da invasão da terra indígena hoje?"'
    },
    
    # ============================================
    # DEPUTADO VENTURI - MATEMÁTICA + PORTUGUÊS
    # ============================================
    'matematica_1': {
        'id': 'matematica_1',
        'disciplina': 'Matemática',
        'entity_id': 'politico',
        'pergunta': 'Se 1kg de Coltan vale R$ 500 no mercado ilegal, e uma operação extrai 200kg por mês durante 2 anos, qual o lucro total estimado?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) R$ 100.000',
            'B) R$ 1.200.000',
            'C) R$ 2.400.000',
            'D) R$ 12.000.000'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Correto! Cálculo: 200kg/mês × R$500 = R$100.000/mês. Em 2 anos (24 meses): R$100.000 × 24 = R$2.400.000. Isso mostra porque vale a pena montar uma operação ilegal complexa - o lucro é milionário!',
        'recompensa': 'dica_lucro',
        'dica_texto': '💡 DICA: Pergunte "Quanto dinheiro você ganhou com a operação de Coltan?"'
    },
    
    'matematica_2': {
        'id': 'matematica_2',
        'disciplina': 'Matemática',
        'entity_id': 'politico',
        'pergunta': 'Uma área de floresta com 10.000 hectares é desmatada a uma taxa de 5% ao ano. Em quantos anos restará menos de 5.000 hectares?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) 10 anos',
            'B) Aproximadamente 14 anos',
            'C) 20 anos',
            'D) 50 anos'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Com decaimento exponencial de 5% ao ano, usamos a fórmula: Área_final = Área_inicial × (0.95)^anos. Para chegar a 5.000 hectares (metade): 10.000 × (0.95)^anos = 5.000. Resolvendo: anos ≈ 13.9 anos. Isso mostra como o desmatamento pode destruir rapidamente uma floresta inteira!',
        'recompensa': 'dica_desmatamento',
        'dica_texto': '🔓 PERGUNTA: "Quanto da reserva já foi desmatada ilegalmente?"'
    },
    
    'portugues_1': {
        'id': 'portugues_1',
        'disciplina': 'Português',
        'entity_id': 'politico',
        'pergunta': 'Analise a frase: "O deputado alega que a exploração é para o desenvolvimento sustentável da região." Qual figura de linguagem está presente?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Metáfora',
            'B) Eufemismo (suavizar algo negativo)',
            'C) Hipérbole',
            'D) Ironia'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! "Desenvolvimento sustentável" é um EUFEMISMO - palavra bonita para disfarçar "exploração ilegal e destruição ambiental". Políticos corruptos usam linguagem técnica e positiva para esconder crimes. Sempre desconfie quando alguém usa muitas palavras bonitas sem explicar os detalhes!',
        'recompensa': 'dica_discurso',
        'dica_texto': '💡 DICA: "Confronte o deputado com evidências diretas, sem aceitar evasivas"'
    },
    
    'portugues_2': {
        'id': 'portugues_2',
        'disciplina': 'Português',
        'entity_id': 'politico',
        'pergunta': 'Em um discurso político, qual estratégia retórica é usada para desviar atenção de acusações?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Responder diretamente às acusações',
            'B) Atacar o acusador ou mudar de assunto (falácia ad hominem)',
            'C) Apresentar dados e provas',
            'D) Admitir erros e pedir desculpas'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Quando políticos corruptos são confrontados, usam falácias: atacam quem acusa ("você é comunista/radical"), mudam de assunto ("e o outro partido?") ou usam whataboutism. Reconhecer essas táticas ajuda a não cair em manipulação e manter o foco nas evidências!',
        'recompensa': 'dica_retorica',
        'dica_texto': '🔓 ESTRATÉGIA: Ignore ataques pessoais e mantenha pressão com fatos e pistas coletadas'
    },
    
    'interdisciplinar_1': {
        'id': 'interdisciplinar_1',
        'disciplina': 'Interdisciplinar',
        'entity_id': 'politico',
        'pergunta': 'Conectando Geografia + História + Ciências: Como uma operação de mineração ilegal pode afetar simultaneamente o meio ambiente, povos indígenas e a economia local?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Apenas polui o rio, sem outros impactos',
            'B) Contamina água (Ciências), invade terras tradicionais (História/Direitos), cria economia ilegal (Geografia)',
            'C) Beneficia todos através de empregos',
            'D) Não há conexão entre esses aspectos'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Perfeito! É um problema SISTÊMICO: (1) Poluição química mata peixes e envenena pessoas; (2) Invasão viola direitos históricos indígenas; (3) Economia ilegal concentra riqueza em criminosos, não beneficia comunidade; (4) Desmatamento muda clima local. Tudo está conectado - por isso se chama Sombra Roxa Conspiracy!',
        'recompensa': 'visao_completa',
        'dica_texto': '🎯 VISÃO COMPLETA: Você entende toda a conspiração. Confronte o deputado com TODAS as evidências!'
    }
}

def verificar_resposta(desafio_id, resposta_usuario):
    """Verifica se a resposta do desafio está correta"""
    desafio = DESAFIOS.get(desafio_id)
    if not desafio:
        return {'sucesso': False, 'erro': 'Desafio não encontrado'}
    
    resposta_correta = desafio['resposta_correta']
    sucesso = resposta_usuario.upper() == resposta_correta
    
    return {
        'sucesso': sucesso,
        'explicacao': desafio['explicacao'] if sucesso else 'Resposta incorreta. Reflita sobre o contexto da investigação e tente novamente.',
        'recompensa': desafio['recompensa'] if sucesso else None,
        'dica_texto': desafio['dica_texto'] if sucesso else None
    }

def get_desafios_por_entidade(entity_id):
    """Retorna desafios de uma entidade específica"""
    return [
        {
            'id': d['id'],
            'disciplina': d['disciplina'],
            'pergunta': d['pergunta'],
            'opcoes': d['opcoes'],
            'tipo': d['tipo']
        }
        for d in DESAFIOS.values() 
        if d.get('entity_id') == entity_id
    ]

def get_resumo_desafios():
    """Retorna resumo de todos os desafios (sem respostas)"""
    return [{
        'id': d['id'],
        'disciplina': d['disciplina'],
        'entity_id': d['entity_id'],
        'tipo': d['tipo']
    } for d in DESAFIOS.values()]
