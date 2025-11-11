"""
Sistema de IA simulada inteligente para respostas sem OpenAI
"""
import random

def simulated_reply_improved(ent, message, chat_history=None):
    """Resposta inteligente e contextual quando OpenAI não está disponível"""
    msg = message.lower().strip()
    entity_id = ent['id']
    nome = ent['nome']
    
    # Detectar saudações simples
    saudacoes = ['oi', 'olá', 'ola', 'hey', 'hi', 'hello', 'bom dia', 'boa tarde', 'boa noite', 'e ai', 'eai']
    eh_saudacao_simples = msg in saudacoes or len(msg) < 4
    
    # Se for saudação simples, retornar introdução sem pistas
    if eh_saudacao_simples:
        introducoes = {
            'biologo': """*Dr. Arnaldo olha para você com expressão preocupada*

Olá... você deve estar aqui pela investigação, não é? Sou Dr. Arnaldo Silva, biólogo de campo do INPA.

*ajusta os óculos nervosamente*

Há algo muito estranho acontecendo nesta região. Mas antes de contar, preciso saber se posso confiar em você.

O que você gostaria de saber especificamente? Pode perguntar sobre minha pesquisa, sobre o rio, ou sobre... eventos recentes.""",
            
            'fazendeiro': """*Valdemar olha desconfiado*

Olá. E você é...? Mais um jornalista bisbilhoteiro? Ou do IBAMA?

*cruza os braços*

Sou Valdemar, dono da Fazenda Nova Fronteira. Produção de soja e gado. Tudo legal, tudo certificado.

O que você quer saber? Faça perguntas diretas que eu decido se respondo.""",
            
            'lider_indigena': """*Yakamu observa você em silêncio por um momento*

...Olá, visitante.

*tom cauteloso*

Sou Yakamu, guardião das histórias do meu povo. Você vem com perguntas, imagino.

Muitos vêm aqui. Poucos ouvem de verdade. Prove que você é diferente. Pergunte com respeito, e talvez eu compartilhe o que sei.""",
            
            'politico': """*Deputado Venturi oferece um sorriso político calculado*

Olá! Sempre um prazer receber visitantes interessados no desenvolvimento da Amazônia.

*aperto de mão firme demais*

Deputado Venturi, três mandatos na Comissão de Desenvolvimento Regional. Como posso ajudá-lo?

Temos grandes planos para esta região. Progresso sustentável, sabe como é. Em que posso ser útil?"""
        }
        
        return introducoes.get(entity_id, f"Olá! Sou {nome}. O que você gostaria de saber?")
    
    # Verificar histórico para evitar respostas idênticas
    chat_history = chat_history or []
    recent_replies = [h.get('content', '') for h in chat_history if h.get('role') == 'assistant'][-3:]
    
    # Função auxiliar para detectar palavras-chave com mais flexibilidade
    def contains_any(text, keywords):
        return any(kw in text for kw in keywords)
    
    # Função para escolher resposta variada
    def choose_varied_response(options):
        """Escolhe uma resposta que não foi usada recentemente"""
        for option in options:
            if option not in recent_replies:
                return option
        # Se todas já foram usadas, escolhe aleatoriamente
        return random.choice(options)
    
    # Respostas específicas por entidade com MUITO mais inteligência
    if entity_id == 'biologo':
        # Perguntas sobre a Sombra Roxa
        if contains_any(msg, ['sombra', 'roxa', 'mancha', 'anomalia', 'rio', 'poluição', 'roxo', 'violeta', 'púrpura', 'o que', 'que é', 'aconteceu']):
            return choose_varied_response([
                """*Dr. Arnaldo ajusta os óculos nervosamente*

Ah... isso que chamam de sombra roxa... É por isso que eu mal durmo à noite. Nas imagens de satélite, eu vi uma mancha roxa anormal no rio, logo acima da Fazenda Nova Fronteira.

Não é mercúrio comum de garimpo. É uma proliferação de algas tóxicas causada por uma anomalia química coltan - um coquetel químico muito específico, o tipo usado para processar esse mineral raro de celulares e eletrônicos.

O problema? NÃO HÁ MINAS OFICIAIS desse mineral na região! Então... de onde vem esse químico? Foi isso que o Gian foi investigar.""",

                """*transpira e olha ao redor*

A tal sombra roxa... *suspiro profundo* É uma contaminação química gravíssima. Coletei amostras do rio e o que encontrei me apavorou.

O padrão de toxicidade é único - corresponde exatamente aos químicos que causam uma anomalia química coltan, usados para processar esse mineral. As algas estão se alimentando desses compostos e liberando toxinas mortais.

Mas o mais assustador? Não existe nenhuma operação legal desse tipo de mineração aqui. Alguém está extraindo isso ilegalmente, e em grande escala!""",

                """*voz baixa, como se alguém pudesse ouvir*

Você pergunta sobre essa sombra roxa? É o pesadelo que me persegue.

Depois de anos estudando a Amazônia, nunca vi nada assim. A anomalia química coltan no rio não é acidental - é industrial, massiva, deliberada.

Quem está fazendo isso tem muito dinheiro e poder. E não quer ser descoberto. *pausa* O Gian entendeu isso... e pagou o preço."""
            ])
        
        
        # Perguntas sobre Coltan
        elif contains_any(msg, ['coltan', 'mineral', 'químico', 'metal', 'celular', 'eletrônico', 'coquetel']):
            return choose_varied_response([
                """O Coltan é um mineral crítico para a indústria de tecnologia. Extremamente valioso e raro.

O químico que detectei no rio - essa anomalia química coltan - só é usado para processar esse mineral. Mas oficialmente não há extração dele aqui. Quando contei isso para o Gian sobre essa sombra roxa, ele ficou obcecado em descobrir a verdade.

Ele foi atrás do Valdemar, dono da Fazenda Nova Fronteira. E depois... ele desapareceu.""",

                """*gesticula com entusiasmo científico misturado com medo*

Coltan - Columbita-Tantalita. É o que faz seu celular funcionar, seus laptops, drones, tudo! Vale mais que ouro no mercado internacional.

A sombra roxa que encontrei tem a assinatura química exata do processamento desse mineral - uma anomalia química coltan pura! Alguém está minerando isso aqui, ilegalmente, em escala industrial.

O Gian entendeu a gravidade quando expliquei. Foi investigar... e nunca mais voltou."""
            ])
        
        
        # Perguntas sobre Gian
        elif contains_any(msg, ['gian', 'jornalista', 'desapareceu', 'desaparecido', 'sumiu', 'aconteceu']):
            return choose_varied_response([
                """*voz trêmula*

O Gian era diferente. Ele realmente se importava. Quando mostrei os dados para ele, ele entendeu a gravidade.

Ele disse que ia confrontar o Valdemar da fazenda. Disse que algo não batia - uma fazenda em local tão ruim economicamente... 

Foi a última vez que falei com ele. Depois recebi... ameaças. Para parar a pesquisa.""",

                """*limpa lágrimas dos olhos*

Gian Kretzl... ele foi a única pessoa que levou minha pesquisa a sério. Outros me chamaram de paranóico, de alarmista.

Mas Gian viu os dados da SOMBRA ROXA e entendeu: isso é uma conspiração gigante. Ele foi atrás do Valdemar para investigar a fazenda.

*voz quebra* Três dias depois, ele sumiu. E eu comecei a receber ameaças de morte."""
            ])
        
        
        # Perguntas sobre Valdemar/Fazenda
        elif contains_any(msg, ['valdemar', 'fazenda', 'fronteira', 'fazendeiro', 'dono']):
            return """*olha ao redor nervoso*

Valdemar... o dono da Fazenda Nova Fronteira. Algo muito estranho naquele lugar.

A fazenda fica em um local horrível para agricultura - solo pobre, logística ruim. Como ele mantém aquilo funcionando?

O Gian foi investigar ele. Nunca mais voltou. *sussurra* Você deveria falar com o Valdemar, mas... tome cuidado."""
        
        # Perguntas sobre ameaças/medo
        elif contains_any(msg, ['ameaça', 'medo', 'perigo', 'quem', 'perseguindo', 'assustado']):
            return """*transpira visivelmente*

Desde que contei ao Gian sobre a anomalia química, coisas estranhas começaram a acontecer.

Telefones estranhos. Carros me seguindo. Uma vez encontraram meu carro com os pneus furados e um recado: "Pare de fazer perguntas."

Não sei quem são, mas são poderosos. O Gian mencionou ter visto um helicóptero perto da fazenda..."""
        
        # Pergunta genérica ou sobre ele mesmo
        else:
            return """Sou Dr. Arnaldo Silva, biólogo de campo do INPA - Instituto Nacional de Pesquisas da Amazônia.

Descobri uma anomalia química coltan no rio - a tal sombra roxa. Um coquetel usado para processar esse mineral raro, mas não há minas oficiais na região!

Pergunte-me sobre a mancha roxa, o Coltan, o Gian ou o Valdemar. Preciso da sua ajuda para descobrir a verdade!"""
        
    elif entity_id == 'fazendeiro':
        # Perguntas sobre Sombra Roxa
        if contains_any(msg, ['sombra', 'roxa', 'rio', 'poluição', 'químico', 'veneno', 'mancha', 'que', 'qual']):
            return """*Valdemar cruza os braços defensivamente*

Essa história de "sombra roxa"? Propaganda! Os índios que ficam jogando lixo no rio, fazendo sei lá o quê por lá.

Minha fazenda é legal, tem toda documentação. Produzo soja e gado, só isso. Se tem alguma coisa estranha no rio, não é problema meu."""
        
        # Perguntas sobre Coltan/garimpo
        elif contains_any(msg, ['coltan', 'mineral', 'garimpo', 'extração', 'minério', 'metal']):
            return """*fica visivelmente nervoso*

Coltan?! Onde você ouviu isso? Olha aqui, isso é difamação! Minha fazenda produz SOJA e GADO, entendeu?

*transpira* 

Quem mandou você aqui? Foi aquele biólogo metido? Ou... você está trabalhando com o jornalista?"""
        
        # Perguntas sobre lucro/economia
        elif contains_any(msg, ['lucro', 'dinheiro', 'prejuízo', 'econom', 'ganha', 'paga', 'caro', 'viável', 'produz', 'vale']):
            return """*irritado*

Escuta aqui, nem toda fazenda é sobre lucro imediato! Isso é um INVESTIMENTO ESTRATÉGICO, entende?

*nervoso* Tá, vou ser sincero... essa fazenda é uma fachada mesmo. A terra é ruim, logística péssima. Mas serve ao propósito.

O meu interesse na reserva ao lado... ISSO sim vale milhões. A terra tem valor estratégico...

*murmura* Além disso, eu não respondo só a mim mesmo..."""
        
        # Perguntas sobre terra indígena/expansão
        elif contains_any(msg, ['terra indígena', 'reserva', 'índios', 'indígena', 'expansão', 'território', 'quer', 'deseja']):
            return """*olhos brilham com ganância*

Ah, então é isso que te interessa? A reserva vizinha?

Olha, aquela terra está sendo DESPERDIÇADA. Vou ser franco... essa fazenda é só uma fachada. O verdadeiro interesse está na reserva ao lado.

Milhões em recursos, sem uso produtivo! Eventualmente, com as pessoas certas em Brasília, essa terra vai ser liberada para o desenvolvimento.

É progresso. É inevitável."""
        
        # Perguntas sobre Gian
        elif contains_any(msg, ['gian', 'jornalista', 'desapareceu', 'sumiu', 'visitou']):
            return """*expressão sombria*

Esse jornalista... ele veio aqui fazendo um monte de perguntas inconvenientes.

Falando de Coltan, de poluição, de coisas que ele não entendia. Eu avisei ele para não meter o nariz onde não era chamado.

*olhar frio* Não sei onde ele está agora. E não é problema meu."""
        
        # Perguntas sobre quem manda/chefe
        elif contains_any(msg, ['quem', 'chefe', 'manda', 'ordem', 'patrão', 'brasília', 'político']):
            return """*fica defensivo*

Eu sou o dono da fazenda! Eu que mando aqui!

*pausa, percebe que falou demais*

Quer dizer... eu tenho investidores, parceiros de negócio. Gente importante. Mas isso é assunto privado."""
        
        # Pergunta genérica
        else:
            return """Sou Valdemar, dono da Fazenda Nova Fronteira. Produtora de soja e gado.

*defensivo* Tudo legal, tudo documentado. Embora entre nós... é uma fazenda fachada para meu interesse na reserva vizinha.

Pergunte sobre a fazenda, a produção, ou por que todos ficam me incomodando!"""
    
    elif entity_id == 'lider_indigena':
        # Perguntas sobre rio/poluição
        if contains_any(msg, ['sombra', 'roxa', 'rio', 'poluição', 'veneno', 'água', 'doente', 'que', 'qual']):
            return """*olhar sombrio*

O rio chora. Nossos avós nadavam nessas águas. Nossos filhos bebiam dele.

Agora? Peixes mortos. Crianças doentes. A "Sombra Roxa" que você fala... é sangue da floresta envenenado.

O homem da fazenda diz que é nossa culpa. Mentira. Ele trabalha para alguém maior. Um homem de terno que vem de Brasília."""
        
        # Perguntas sobre Coltan/mapa/montanha
        elif contains_any(msg, ['coltan', 'mapa', 'montanha', 'metal', 'mineral', 'pedra', 'sagrado', 'tesouro']):
            return """*respira fundo, decidindo confiar em você*

Há conhecimento que nossos ancestrais guardaram. Um mapa coltan - o "Mapa da Montanha de Fogo" - não está em papel, está em nossas histórias.

Fala de uma montanha onde a "pedra fantasma" existe. O que vocês chamam de Coltan. Para nós, era pedra sagrada.

É por ISSO que querem nossa terra. Não é sobre soja. É sobre esse mapa coltan e o que está EMBAIXO dela."""
        
        # Perguntas sobre homem de terno/político
        elif contains_any(msg, ['terno', 'brasília', 'político', 'deputado', 'helicóptero', 'poderoso', 'chefe', 'manda']):
            return """O Gian me perguntou a mesma coisa.

O Valdemar não é o chefe. Ele obedece. Um político corrupto que vem de helicóptero, de Brasília. 

O Gian descobriu o nome dele: deputado Venturi. Ele disse que ia confrontá-lo. E então... desapareceu.

Esse deputado Venturi é quem realmente está por trás de tudo."""
        
        # Perguntas sobre Gian
        elif contains_any(msg, ['gian', 'jornalista', 'confiava', 'amigo']):
            return """*com respeito*

O Gian foi diferente dos outros. Ele nos OUVIU. Não veio para nos estudar como animais.

Ele acreditou em nossas histórias. Entendeu que nossa luta não é sobre atraso, mas sobre sobrevivência.

Foi por isso que eu mostrei a ele o conhecimento do mapa. *pausa triste* Espero não ter assinado a sentença de morte dele."""
        
        # Perguntas sobre terra/luta
        elif contains_any(msg, ['terra', 'luta', 'direito', 'ancestral', 'história']):
            return """Esta terra não é só propriedade. É memória viva.

Cada árvore, cada rio, cada pedra - tem história de mil anos. Nossos ancestrais estão aqui.

Mas para eles, é só "recursos naturais". Para desenvolver. Para lucrar. Como se a floresta fosse uma mina de ouro esperando para ser saqueada."""
        
        # Pergunta genérica
        else:
            return """Sou Yakamu, guardião das histórias e da sabedoria do meu povo.

Sei sobre o Mapa da Montanha de Fogo, a pedra sagrada (Coltan), e o homem de terno de Brasília.

Pergunte-me sobre nossa terra, a Sombra Roxa, o mapa secreto ou o Gian. Posso confiar em você?"""
    
    elif entity_id == 'politico':
        # Perguntas sobre Sombra Roxa
        if contains_any(msg, ['sombra', 'roxa', 'poluição', 'crime', 'rio', 'veneno', 'que', 'qual']):
            return """*sorriso frio e polido*

"Sombra Roxa"? Que termo dramático. Você deve ser jornalista. Ou... conhece o falecido Gian?

Olha, acidentes ambientais acontecem. Garimpo ilegal, sabe como é. O Brasil é grande, difícil de fiscalizar tudo.

*olhar penetrante*

Mas tenho certeza que você está aqui para discutir desenvolvimento sustentável, não é mesmo?"""
        
        # Perguntas sobre Coltan/conspiração/plano
        elif contains_any(msg, ['coltan', 'conspiração', 'plano', 'esquema', 'verdade', 'tudo', 'fazenda', 'confessa']):
            return """*ri baixo*

Ah, então você juntou as peças. Impressionante.

*acende charuto*

Sabe qual é a verdade? A Amazônia é o novo petróleo. E eu sou o dono do poço.

A conspiração coltan é simples: Terra indígena com bilhões nesse mineral. Uma fazenda como fachada para acesso. Garimpo discreto para processar. 

Genial, não acha? Essa é minha operação de conspiração coltan."""
        
        # Perguntas sobre Gian
        elif contains_any(msg, ['gian', 'jornalista', 'desapareceu', 'matou', 'morte']):
            return """*expressão sombria*

O Gian Kretzl. Brilhante, determinado... e imprudente.

Ele achou que eu estava "destruindo" a Amazônia. Que tolo. Eu estou COLHENDO ela.

*olhar frio*

Ele foi... descuidado. E agora você está seguindo os passos dele. Interessante escolha."""
        
        # Perguntas sobre Valdemar/Fazenda
        elif contains_any(msg, ['valdemar', 'fronteira']):
            return """O Valdemar? Um peão útil. 

A fazenda nunca foi sobre agricultura. Era sobre ter presença legal na região, próximo à reserva indígena.

Quando você controla a terra ao redor, é mais fácil "renegociar" os limites da reserva. Entende como funciona?"""
        
        # Perguntas sobre poder/política
        elif contains_any(msg, ['poder', 'político', 'deputado', 'influência', 'brasília']):
            return """*sorriso arrogante*

Poder não é sobre força. É sobre estar nos lugares certos, conhecer as pessoas certas.

Um projeto de lei aqui, uma emenda ali, um despacho "acelerado" acolá... e de repente, o impossível se torna lei.

A Amazônia tem trilhões esperando. E eu tenho as chaves."""
        
        # Perguntas diretas/confronto
        elif contains_any(msg, ['culpado', 'criminoso', 'prender', 'justiça', 'provas']):
            return """*riso frio*

Provas? Justiça? Que ingênuo.

Você acha que alguém vai me prender? Eu ESCREVO as leis. Eu NOMEIO os juízes.

Mas por favor, tente. Vai ser... educativo para você."""
        
        # Pergunta genérica
        else:
            return """Deputado Venturi, três mandatos consecutivos. Presidente da Comissão de Desenvolvimento da Amazônia.

*sorriso político* Sempre trabalhando pelo "progresso" do Brasil.

Pergunte-me sobre o Coltan, a fazenda, o Gian... ou melhor ainda, confronte-me com as provas que tem!"""

    # Fallback genérico mais inteligente
    return f"""*{nome} olha para você*

Desculpe, não entendi bem sua pergunta "{message}".

Tente perguntas mais diretas como: "O que é a sombra roxa?", "Você conhece o Gian?", "Qual é o plano?", etc.

Estou aqui para ajudar na investigação!"""
