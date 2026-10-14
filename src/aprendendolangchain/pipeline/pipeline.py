from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate#Classe usadapara estruturas os prompts qeu serao enviados aos modelos de chat
from langchain.chat_models import init_chat_model #facilita a integracao de varios provedores de modelos de IA para criacao dos agentes ou pipelines
from langchain_core.output_parsers import StrOutputParser #a resposta do modelo essa classe deixa agradavel para o usuario ler a resposta em string
from langchain_core.runnables import RunnableLambda # serve para trasformar funcoes que nao estao no Runnable como uma funcao feita pelo proprio programador em uma funcao que tenha Runnable e possa encaixar na chain quero dizer na pipeline

from dotenv import load_dotenv
import os



load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
model_ai_gemini = os.getenv("MODEL_AI_GEMINI")
model_ai_groq = os.getenv("MODEL_AI_GROQ")
groq_api_key = os.getenv("GROQ_API_KEY")
if(not gemini_api_key):
    raise ValueError("Falta o valor da variavel api do gemini")
if(not model_ai_gemini):
    raise ValueError("falta o modelo do gemini")
if(not groq_api_key):
    raise ValueError("Falta o valor da variavel api do groq")
if(not model_ai_groq):
    raise ValueError("falta o modelo do groq")


def deixar_maiusculo(texto:str) -> str:
    return texto.upper()



assunto: str = "The last of us"

prompt_tempalte = ChatPromptTemplate.from_template( #define o template para mandar o texto em string para o modelo
    template= "preciso que me explique em no maximo 10 linhas sobre: {assunto}"
)

model = init_chat_model(
    model=model_ai_groq,
    model_provider="groq",
    api_key=groq_api_key
)
parser = StrOutputParser() #transforma o resultado que vem do modelo de IA e apenas pega o texto puro

passo_extra = RunnableLambda(deixar_maiusculo)

pipeline = prompt_tempalte | model | parser | passo_extra #encadeia a acao do que a pipeline ira fazer 1: o promptTemplate pega o texto transforma em template com as instucoes e o assunto/pergunta, 2: passa o template para o modelo que le o template, gera a resposta e 3: com a resposta no computador local o StrOutputParser(), retira todo oque o modelo devolveu e so filtra o texto de resposta.


resultado = pipeline.invoke( # invocao pipeline faz todo o processamento e resposta e salva em resultado
    {
        "assunto": assunto
    }
)
print(resultado)