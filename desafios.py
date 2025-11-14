"""
Sistema de Desafios Educacionais - Projeto Sombra Roxa
Desafios organizados por personagem (5 por entidade):
- Dr. Arnaldo Silva (Ciências)
- Valdemar (Geografia)
- Pajé Yakamu (História)

⚠️ ATENÇÃO: Algumas dicas são FALSAS para desafiar pensamento crítico!
"""

DESAFIOS = {
    # ============================================
    # DR. ARNALDO SILVA - CIÊNCIAS (5 desafios)
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte ao Dr. Arnaldo sobre químicos específicos usados no processamento de minerais.',
        'dica_falsa': False
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
            'C) O excesso de nutrientes (nitrogênio e fósforo) causa crescimento explosivo de algas que consomem oxigênio',
            'D) As algas mutam geneticamente e se tornam tóxicas'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Exato! Químicos industriais frequentemente contêm nutrientes como nitrogênio e fósforo. O excesso causa eutrofização - crescimento explosivo de algas que consomem todo oxigênio da água e podem produzir toxinas, criando "zonas mortas" e matando peixes.',
        'recompensa': 'pergunta_chave_1',
        'dica_texto': '🚨 DICA FALSA: Pergunte se a cor roxa vem de refluxo de petróleo subterrâneo.',
        'dica_falsa': True
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte sobre a conexão entre o gado de Valdemar e a fonte de água.',
        'dica_falsa': False
    },
    
    'ciencias_4': {
        'id': 'ciencias_4',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'O que são cianobactérias e por que sua proliferação em rios é perigosa?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) São peixes azuis que limpam a água',
            'B) São bactérias fotossintetizantes que podem produzir toxinas mortais quando proliferam descontroladamente',
            'C) São algas marinhas inofensivas',
            'D) São plantas aquáticas que filtram poluentes'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Cianobactérias (ou algas azuis) fazem fotossíntese mas são bactérias. Quando há excesso de nutrientes poluentes, proliferam e produzem cianotoxinas que causam danos ao fígado, sistema nervoso e podem ser fatais para humanos e animais que bebem água contaminada.',
        'recompensa': 'dica_toxinas',
        'dica_texto': '🚨 DICA FALSA: Pergunte se a NASA está escondendo dados sobre meteoros na Amazônia.',
        'dica_falsa': True
    },
    
    'ciencias_5': {
        'id': 'ciencias_5',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'Por que a análise de satélite é importante para detectar anomalias ambientais em regiões remotas?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) É mais barato que outros métodos',
            'B) Permite monitorar grandes áreas de difícil acesso e detectar mudanças que não seriam visíveis no solo',
            'C) Satélites podem limpar a poluição automaticamente',
            'D) Não é importante, basta observação local'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Imagens de satélite permitem monitorar milhares de km² simultaneamente, detectar padrões invisíveis ao nível do solo (como a Sombra Roxa) e acompanhar mudanças ao longo do tempo. Na Amazônia, onde o acesso é difícil, satélites são essenciais para flagrar crimes ambientais.',
        'recompensa': 'dica_satelite',
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte como Gian descobriu a anomalia e qual foi sua teoria inicial.',
        'dica_falsa': False
    },
    
    # ============================================
    # VALDEMAR - GEOGRAFIA (5 desafios)
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte a Valdemar sobre os custos operacionais e o lucro real da fazenda.',
        'dica_falsa': False
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
        'dica_texto': '🚨 DICA FALSA: Pergunte se Valdemar tem contrato oficial com a FUNAI para usar a terra.',
        'dica_falsa': True
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte por que Valdemar mantém a fazenda se o solo não é bom para agricultura.',
        'dica_falsa': False
    },
    
    'geografia_4': {
        'id': 'geografia_4',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'O que são corredores logísticos e por que são estratégicos na Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) São trilhas para turismo ecológico',
            'B) São rotas de transporte (estradas, rios) que permitem escoamento de produção e acesso a áreas remotas',
            'C) São áreas de preservação ambiental',
            'D) São caminhos para animais selvagens'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Corredores logísticos (BR-163, hidrovias) são cruciais para viabilizar atividades econômicas em regiões remotas. Quem controla a logística, controla o acesso e a exploração. A Fazenda Nova Fronteira está posicionada ESTRATEGICAMENTE para ser um ponto de apoio logístico!',
        'recompensa': 'dica_logistica',
        'dica_texto': '🚨 DICA FALSA: Pergunte se a fazenda exporta soja orgânica certificada para a Europa.',
        'dica_falsa': True
    },
    
    'geografia_5': {
        'id': 'geografia_5',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'Como a especulação fundiária funciona na prática da Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Comprar terra barata, valorizar com infraestrutura real, revender com lucro',
            'B) Invadir/grilar terra, fingir produção, aguardar valorização por obras públicas próximas, revender ou usar como garantia',
            'C) Apenas comprar terras legalmente e esperar',
            'D) Alugar terras indígenas com permissão'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Especuladores GRILAM terras públicas/indígenas com documentos falsos, fazem desmatamento mínimo para "comprovar posse", aguardam obras públicas (estradas, hidrovias) que valorizam a região, e revendem ou usam como garantia bancária. É um esquema lucrativo baseado em crime!',
        'recompensa': 'dica_especulacao',
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte sobre quem prometeu a hidrovia e por que passaria exatamente ali.',
        'dica_falsa': False
    },
    
    # ============================================
    # PAJÉ YAKAMU - HISTÓRIA (5 desafios)
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte ao Pajé sobre tentativas políticas de reverter a demarcação.',
        'dica_falsa': False
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
        'dica_texto': '🚨 DICA FALSA: Pergunte se a Trilha dos Ancestrais leva a um templo atlante com ouro.',
        'dica_falsa': True
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
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte sobre o homem de terno que visitou a aldeia antes de Gian desaparecer.',
        'dica_falsa': False
    },
    
    'historia_4': {
        'id': 'historia_4',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'O que foi o Estatuto do Índio (Lei 6.001/1973) e qual sua importância antes da Constituição de 1988?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Lei que permitia escravização indígena',
            'B) Primeira lei que tentou proteger direitos indígenas, mas com visão integracionista (assimilar índios à sociedade)',
            'C) Lei que proibia indígenas de ter terras',
            'D) Lei criada apenas para turismo'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! O Estatuto de 1973 foi um avanço, mas tinha visão INTEGRACIONISTA - queria que índios se "integrassem" e deixassem de ser índios. Só com a Constituição de 1988 reconheceu-se o direito de manter cultura e identidade próprias. Foi uma mudança histórica fundamental!',
        'recompensa': 'dica_estatuto',
        'dica_texto': '🚨 DICA FALSA: Pergunte se o governo federal ofereceu compensação financeira justa pela invasão.',
        'dica_falsa': True
    },
    
    'historia_5': {
        'id': 'historia_5',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'Qual foi o papel da Fundação Nacional do Índio (FUNAI) ao longo da história?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Sempre protegeu indígenas eficientemente',
            'B) Criada em 1967, teve períodos de proteção mas também foi usada para facilitar invasões durante ditadura militar',
            'C) Nunca teve poder real',
            'D) Foi criada por povos indígenas'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! A FUNAI nasceu com missão protetora, mas durante a Ditadura Militar (1964-1985) foi USADA para abrir terras indígenas para grandes projetos (rodovias, mineração). Até hoje sofre interferência política. Quando há interesse econômico, a proteção "desaparece". Igual ao caso do Coltan!',
        'recompensa': 'dica_funai',
        'dica_texto': '💡 DICA VERDADEIRA: Pergunte sobre a "Pedra Preta Pesada que Brilha" mencionada pelos ancestrais.',
        'dica_falsa': False
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
        'resposta_correta': resposta_correta,
        'explicacao': desafio['explicacao'] if sucesso else 'Resposta incorreta. Reflita sobre o contexto da investigação e tente novamente.',
        'recompensa': desafio['recompensa'] if sucesso else None,
        'dica_texto': desafio['dica_texto'] if sucesso else None,
        'dica_falsa': desafio.get('dica_falsa', False) if sucesso else None
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
