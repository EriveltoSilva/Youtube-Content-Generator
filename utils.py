from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

def generate_script(prompt, video_length, creativity, api_key):
    # Template for generating 'Title'
    title_template = PromptTemplate(
        input_variables=['subject'],
        template='Por favor, crie um título para um vídeo de Podcast no Youtube com o tópico: {subject}'
    )

    # Template for generating 'Video Script' using search engine
    script_template = PromptTemplate(
        input_variables=['title', 'DuckDuckGo_Search','duration'],
        template="Crie um roteiro para um Podcast em vídeo no YouTube baseado neste título para mim. Título:{title} de duração: {duration} minutos usando estes dados de pesquisa {DuckDuckGo_Search}"
    )

    #Setting up OpenAI LLM
    llm = ChatOpenAI(temperature=creativity,openai_api_key=api_key,model_name='gpt-3.5-turbo-0613') 
    
    #Creating chain for 'Title' & 'Video Script'
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

    # https://python.langchain.com/docs/modules/agents/tools/integrations/ddg
    search = DuckDuckGoSearchRun()
    
    # Executing the chains we created for 'Title'
    title = title_chain.run(prompt)

    # Executing the chains we created for 'Video Script' by taking help of search engine 'DuckDuckGo'
    search_result = search.run(prompt)
    script = script_chain.run(title=title, DuckDuckGo_Search=search_result, duration=video_length)

    # Returning the output
    return search_result, title, script


