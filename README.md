PAcotes e oque eles fazem:
    langchain-core( Ele fornece componentes para várias partes de uma aplicação de IA):
        1. Prompts e mensagens
            Permite estruturar instruções para o modelo, separando mensagens de sistema, usuário e assistente.
            Exemplo: criar um prompt para recomendar filmes com base no gosto do usuário.

        2. Composição de fluxos com LCEL
            O LangChain Expression Language permite combinar componentes usando |, formando pipelines de processamento.
            Exemplo: prompt → modelo de IA → processamento da resposta.

        3. Documentos e RAG
            Oferece estruturas como Document, usadas para representar textos com metadados em sistemas de recuperação de informações.
            Exemplo: recuperar informações de uma base de jogos antes de gerar uma recomendação.

        4. Saídas estruturadas
            Ajuda a processar respostas de modelos em estruturas utilizáveis pelo Python, como objetos e dados validados.
            Exemplo: retornar título, gênero, nota e justificativa de um filme em vez de apenas texto livre.

    langchain:
        1. Integra modelos de IA
            Ajuda a conectar modelos de diferentes provedores e utilizá-los em aplicações com uma interface consistente.

        2. Cria agentes de IA
            Permite criar agentes que decidem quando utilizar ferramentas, como consultar uma API, pesquisar informações ou executar uma função Python.

        3. Facilita a construção de sistemas RAG
            Ajuda a combinar recuperação de documentos com geração de respostas, permitindo que a IA consulte uma base de conhecimento antes de responder.

        4. Organiza aplicações de IA
            Ajuda a integrar modelos, ferramentas e fontes de dados em aplicações Python, incluindo backends construídos com FastAPI.

    langhain-google-genai
    langchain-groq
    "langgraph-cli[inmem]"  = vai ser intalado o langgraph-cli -> langgraph api, uvicorn, langgraph-runtime tendo que esse[inmem ] e uma serie de pacotes a mais para serem intalados alem do langgraph-cli padrao


NO LCE: trabalhamos com runnable, ele e uma classe abstrata, que se deve ser somente herdada, e quer dizer:
    temos 3 tupos de execucao com o runnable:
        .Inoke(input):
            Execucao padrao: quero dizer recebe uma string, linguagem natural em input e devolve em linguagem natural em output
        .batch(inputs):
            Execucao em paralelo: recebe uma lista de inputs e processa a lista em paralelo das entradas simultaneamente e retorna uma lista de saidas
        .strem(input):
            Executa interativamente: recebe um texto em string e devole em chunks ou tokens a saida conforme elas ficam prontas, como no chat gpt
    
No caso o outuput ai ser igual ao input sempre em todos os caso, e mais como tudo vai ser runnable, ele vai intergrar .invoke(), .batch() e .stream tudo junto, e ai criar um runnable sequente:
    quer seria um conjunto de etapas para e executar em ordem.


Pipeline != agente

pipeline = manda uma pergunta e recebe uma resposta

langgraph dev = ele abre uma UI para o modelo de agente de IA que passou, mas se deve criar o seguinte arquivo para criar a pasta .langgraph_api que e UI
    cria um arquivo chamado langgraph.json
        {
        "dependencies": [
            "."
        ],
        "graphs": {
            "agent": "diretorio Arquivo agente":"nome do agente criado"
        },
        "env": ".env" # esse e o seu .env
        }