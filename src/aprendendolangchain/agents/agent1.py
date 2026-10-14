from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch #e uma biblioteca de pesquisa na web

from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
model_ai_gemini = os.getenv("MODEL_AI_GEMINI")
model_ai_groq = os.getenv("MODEL_AI_GROQ")
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
if(not gemini_api_key):
    raise ValueError("Falta o valor da variavel api do gemini")
if(not model_ai_gemini):
    raise ValueError("falta o modelo do gemini")
if(not tavily_api_key):
    raise ValueError("falta a chave api do tavily")
if(not groq_api_key):
    raise ValueError("Falta o valor da variavel api do groq")
if(not model_ai_groq):
    raise ValueError("falta o modelo do groq")


model = init_chat_model(
    model=model_ai_groq,
    model_provider="groq",
    api_key=groq_api_key
)



agente = create_agent(
    model=model,
    tools=[TavilySearch(api_key=tavily_api_key)],
    system_prompt="voce e um agente para respoder perguntas com oque voce sabe de conhecimento, se nao sabe responder algo, pesquise eu disponibiblizei a tool tavily do langChain!" #aqui estou so passando uma instrucao para o modelo
)

# pergunta = "qual a temperatura atual de maceio?"

# resposta = agente.invoke( #ja para um agente ele precisa de mais informacoes, ja que e mais complexto que uma pergunta e resposta comum, precisa do paramtro message para mandar uma mensagem pro modelo, e especificar a role, (se vai ser [user, system, prompt], user= mensagem de usuario, system = mensagem do sistem, prompt=mensagem de instrucao)
#     {"messages": [{"role":"user", "content": pergunta}]}
# )

# print(resposta["messages"][-1].content)#quer dizer dentro da variavel resposta, acessando a chave message da resposta do modelo e indo no indice da resposta -1 a ultima resposta de message vai estar na maioria das respostas, quer dizer, para o modelo, pergunta, resposta, pergunta e reposta