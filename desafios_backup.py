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
            'C) O excesso de nutrientes (nitrogênio e fósforo) causa crescimento explosivo de algas que consomem oxigênio',
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
        'dica_texto': '💡 DICA: Pergunte "Como a cor roxa indica presença de cianobactérias específicas?"'
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
        'dica_texto': '💡 DICA: "Como o Dr. Arnaldo descobriu a anomalia? Pergunte sobre o monitoramento."'
    },
    
    'ciencias_6': {
        'id': 'ciencias_6',
        'disciplina': 'Ciências',
        'entity_id': 'biologo',
        'pergunta': 'O que é lixiviação e como ela relaciona-se com a mineração de Coltan?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) É um método de plantio sustentável',
            'B) É o processo onde água da chuva dissolve e arrasta substâncias químicas do solo para rios',
            'C) É a limpeza natural de rios',
            'D) É quando animais bebem água contaminada'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Perfeito! Lixiviação é quando água (chuva) percola pelo solo e arrasta substâncias dissolvidas. Na mineração de Coltan, os químicos usados no processamento são lixiviados para os rios, causando contaminação massiva e persistente. É por isso que a Sombra Roxa continua crescendo!',
        'recompensa': 'dica_lixiviacao',
        'dica_texto': '💡 DICA: "Por que a contaminação está se espalhando? Pergunte sobre lixiviação."'
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
        'dica_texto': '💡 DICA: "Pergunte ao Valdemar sobre a hidrovia prometida pelo deputado."'
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
        'dica_texto': '💡 DICA: "A fazenda é realmente sobre soja? Pergunte sobre o REAL negócio."'
    },
    
    'geografia_6': {
        'id': 'geografia_6',
        'disciplina': 'Geografia',
        'entity_id': 'fazendeiro',
        'pergunta': 'Qual é o papel de latifundiários e empresas no processo de desmatamento ilegal?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Sempre operam dentro da lei',
            'B) Usam "laranjas", documentos falsos e pressão política para legalizar invasões e desmatamento',
            'C) Apenas compram terras de pequenos produtores',
            'D) Não têm relação com desmatamento'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Grandes operações ilegais usam "laranjas" (nomes falsos), documentos forjados, grilagem, e LOBBY POLÍTICO para "legalizar" invasões a posteriori. Valdemar é um "laranja" - um nome de fachada para proteger o verdadeiro dono (Deputado Venturi)!',
        'recompensa': 'dica_laranja',
        'dica_texto': '💡 DICA: "Valdemar é o verdadeiro dono? Ou só um empregado?"'
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
        'dica_texto': '💡 DICA: "Como a lei mudou entre 1973 e 1988? Pergunte sobre direitos históricos."'
    },
    
    'historia_5': {
        'id': 'historia_5',
        'disciplina': 'História',
        'entity_id': 'lider_indigena',
        'pergunta': 'Como funcionava o sistema de aldeamento durante a colonização portuguesa?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Sistema de proteção voluntária de indígenas',
            'B) Reunir indígenas de diferentes povos em aldeias controladas por jesuítas/colonizadores para facilitar conversão e trabalho forçado',
            'C) Sistema de ensino gratuito',
            'D) Programa de preservação cultural'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Aldeamentos eram campos de concentração disfarçados: retiravam indígenas de suas terras, misturavam povos diferentes (destruindo culturas), forçavam conversão religiosa e trabalho. Muitos morreram de doenças e maus-tratos. É a origem histórica da invasão de terras indígenas!',
        'recompensa': 'dica_aldea mento',
        'dica_texto': '💡 DICA: "O passado se repete? Pergunte sobre paralelos históricos."'
    },
    
    'historia_6': {
        'id': 'historia_6',
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
        'dica_texto': '💡 DICA: "Por que a fiscalização falhou? Há interferência política?"'
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
    
    'matematica_3': {
        'id': 'matematica_3',
        'disciplina': 'Matemática',
        'entity_id': 'politico',
        'pergunta': 'Se um político recebe 10% de propina sobre R$ 2.400.000 em Coltan por ano, quanto ele lucra em 5 anos?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) R$ 240.000',
            'B) R$ 1.200.000',
            'C) R$ 2.400.000',
            'D) R$ 12.000.000'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! 10% de R$ 2.400.000 = R$ 240.000/ano. Em 5 anos: R$ 240.000 × 5 = R$ 1.200.000. Mais de um milhão em propinas! Isso explica porque políticos corruptos protegem operações ilegais - o lucro é astronômico e vale o risco.',
        'recompensa': 'dica_propina',
        'dica_texto': '💡 DICA: "Quanto Venturi realmente ganha? Pergunte sobre a parte dele."'
    },
    
    'portugues_3': {
        'id': 'portugues_3',
        'disciplina': 'Português',
        'entity_id': 'politico',
        'pergunta': 'Analise: "Estamos trazendo progresso e desenvolvimento para a região." Qual recurso linguístico está presente?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Uso de primeira pessoa do plural (nós) para incluir ouvinte e diluir responsabilidade pessoal',
            'B) Uso honesto de linguagem clara',
            'C) Metáfora poética',
            'D) Ironia'
        ],
        'resposta_correta': 'A',
        'explicacao': 'Perfeito! "Estamos/Nós" cria FALSA INCLUSÃO (você não está trazendo nada!) e DILUI RESPONSABILIDADE (quem exatamente? ninguém específico). Políticos usam isso para parecer que "todos" concordam e evitar assumir responsabilidade pessoal por decisões criminosas!',
        'recompensa': 'dica_primeira_pessoa',
        'dica_texto': '💡 DICA: "Quem é WE? Pergunte: VOCÊ especificamente fez o quê?"'
    },
    
    'matematica_4': {
        'id': 'matematica_4',
        'disciplina': 'Matemática',
        'entity_id': 'politico',
        'pergunta': 'Uma empresa de mineração ilegal quer processar 500kg de Coltan/mês. Se cada kg usa 2 litros de solvente tóxico que depois vai pro rio, quantos litros de veneno são despejados por ano?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) 1.000 litros',
            'B) 6.000 litros',
            'C) 12.000 litros',
            'D) 24.000 litros'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Correto! 500kg × 2 litros = 1.000 litros/mês. Em 1 ano (12 meses): 1.000 × 12 = 12.000 litros de solvente tóxico despejados no Rio Dourado! Isso mata peixes, envenena pessoas e cria a Sombra Roxa. O lucro vale 12 MIL LITROS DE VENENO por ano!',
        'recompensa': 'dica_veneno',
        'dica_texto': '💡 DICA: "Quantos litros de químico já foram despejados? Pergunte sobre o impacto total."'
    },
    
    'portugues_4': {
        'id': 'portugues_4',
        'disciplina': 'Português',
        'entity_id': 'politico',
        'pergunta': 'O que é "greenwashing" (lavagem verde) no contexto de discurso político-empresarial?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Limpeza real de áreas poluídas',
            'B) Usar imagens e discurso "sustentável" para esconder práticas destrutivas',
            'C) Programa de reflorestamento efetivo',
            'D) Certificação ambiental séria'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Greenwashing é propaganda enganosa: empresas/políticos usam termos como "sustentável", "eco-friendly", "desenvolvimento consciente" enquanto destroem o meio ambiente. Venturi usa "desenvolvimento sustentável" para esconder mineração ilegal assassina. É MARKETING, não realidade!',
        'recompensa': 'dica_greenwashing',
        'dica_texto': '💡 DICA: "Ignore as palavras bonitas. Pergunte sobre AÇÕES CONCRETAS."'
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
    },
    
    'interdisciplinar_2': {
        'id': 'interdisciplinar_2',
        'disciplina': 'Interdisciplinar',
        'entity_id': 'biologo',
        'pergunta': 'Conectando Ciências + Matemática + Geografia: Se 80% da biodiversidade amazônica está em 20% da floresta (áreas de alta concentração), qual o impacto de desmatar 1.200 hectares de floresta primária?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Baixo impacto, floresta se recupera sozinha',
            'B) Altíssimo impacto: perda desproporcional de espécies, quebra de corredor ecológico, erosão do solo',
            'C) Médio impacto, apenas algumas espécies afetadas',
            'D) Sem impacto se replantar depois'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! Desmatamento de floresta primária causa: (1) PERDA IRREVERSÍVEL de espécies (80% da biodiversidade em pontos críticos); (2) EROSÃO por chuvas intensas sem proteção da vegetação; (3) QUEBRA DE CORREDORES ECOLÓGICOS impedindo migração de animais; (4) MUDANÇA CLIMÁTICA local (menos evapotranspiração = menos chuva). Não dá pra "replantar" 200 anos de evolução!',
        'recompensa': 'impacto_total',
        'dica_texto': '🌳 IMPACTO TOTAL: Pergunte ao Dr. Arnaldo sobre a escala real da destruição ecológica'
    },
    
    'interdisciplinar_3': {
        'id': 'interdisciplinar_3',
        'disciplina': 'Interdisciplinar',
        'entity_id': 'fazendeiro',
        'pergunta': 'Conectando Geografia + Matemática + História: Se Valdemar comprou 5.000 hectares a R$ 500/hectare em terras "griladas" (documentos falsos), quanto ele economizou comparado ao preço legal de R$ 3.000/hectare?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) R$ 2,5 milhões',
            'B) R$ 12,5 milhões',
            'C) R$ 15 milhões',
            'D) R$ 25 milhões'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exato! Preço legal: 5.000 × R$ 3.000 = R$ 15 milhões. Preço grilado: 5.000 × R$ 500 = R$ 2,5 milhões. DIFERENÇA: R$ 12,5 milhões economizados! Grilagem (roubo de terras com documentos falsos) é CRIME e é base da exploração ilegal. Historicamente, 80% da Amazônia desmatada é em terras griladas!',
        'recompensa': 'grilagem_revelada',
        'dica_texto': '📜 GRILAGEM: Confronte Valdemar sobre a legalidade dos seus documentos de propriedade'
    },
    
    'interdisciplinar_4': {
        'id': 'interdisciplinar_4',
        'disciplina': 'Interdisciplinar',
        'entity_id': 'lider_indigena',
        'pergunta': 'Conectando História + Ciências + Português: Qual a relação entre conhecimento tradicional indígena e ciência moderna na conservação da Amazônia?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Conhecimento tradicional é inferior e deve ser ignorado',
            'B) São complementares: povos indígenas têm milênios de observação empírica validada pela ciência moderna',
            'C) Apenas ciência moderna importa',
            'D) São incompatíveis e contraditórios'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Perfeito! Povos indígenas têm MILÊNIOS de conhecimento sobre: plantas medicinais (70% dos medicamentos vêm de conhecimento tradicional), padrões climáticos, manejo sustentável, sinais de desequilíbrio ecológico. A ciência moderna VALIDA esse conhecimento com método científico. Juntos são MAIS FORTES! A Sombra Roxa foi detectada por Yakamu antes de qualquer cientista!',
        'recompensa': 'conhecimento_ancestral',
        'dica_texto': '🪶 SABEDORIA ANCESTRAL: Ouça o Pajé sobre sinais que a ciência ainda não detectou'
    },
    
    'interdisciplinar_5': {
        'id': 'interdisciplinar_5',
        'disciplina': 'Interdisciplinar',
        'entity_id': 'politico',
        'pergunta': 'Conectando Matemática + Geografia + Português: Se um político usa "desenvolvimento sustentável" para aprovar mineração que gera R$ 50 milhões/ano mas causa R$ 200 milhões em danos ambientais, qual o termo técnico correto?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Investimento produtivo',
            'B) Externalidade negativa não contabilizada (custo social oculto)',
            'C) Progresso econômico',
            'D) Desenvolvimento regional'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Correto! EXTERNALIDADE NEGATIVA = custos que empresa/político não paga, mas a sociedade sim (água poluída, saúde, desmatamento). R$ 50 milhões de lucro privado vs R$ 200 milhões de prejuízo público = BALANÇO NEGATIVO! "Desenvolvimento sustentável" é GREENWASHING para esconder esse roubo. O político embolsa lucro e sociedade paga a conta!',
        'recompensa': 'custo_real',
        'dica_texto': '💰 CUSTO REAL: Pergunte ao Venturi: Quem paga pela limpeza? Quem paga pelos doentes?'
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
