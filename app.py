import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool , initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains import LLMMathChain , LLMChain

##set up the streamlit app

st.set_page_config(page_title="text to math paroblem and data seradch assistant", page_icon="|!!|")
st.title("text to math problem solver using google gemma 2 ")

groq_api_key= st.sidebar.text_input(label="Groq API Key" , type="password")

if not groq_api_key:
    st.info("please add your groq api key to continue ")
    st.stop()
    
llm=ChatGroq(groq_api_key=groq_api_key, model="Gemma2-9b-It")

##intialize tools

wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia" , 
    func=wikipedia_wrapper.run,
    description="a tool for searching the internet to find the various information on the topics mentioned"
)

##intialize the math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="calculator",
    func=math_chain.run,
    description="a tool for answering math related question . Only input mathematical expression need to provided"
)

prompt="""

you are agent tasked for solving user mathematical question . Logically arrive at the solution and provide a detailed explanantion
and display it point wise for the question below
Question:{question}
Answer:

"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)


## combine all the tools 

chain=LLMChain(llm=llm , prompt=prompt_template)

reasoining_tool=Tool(
    name="reasoning tool",
    func=chain.run,
    description="a tool for answering logic-based and reasoning question"
)


##imntialize the tools

assistant_agent=initialize_agent(
    tools=[wikipedia_tool , calculator , reasoining_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)


if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant",
         "content":"hi i am a chatbot who can answer all your answer"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])
    
    
## function to handle or generate reponse

# def generate_response(question):
#     response=assistant_agent.invoke({'input':question})
#     return response


#lets start the interaction


question=st.text_area("enter your question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes.Then I but a dozen apples and 2 packs of blueberries contains 25 berrires. How many total pieces of fruit do I have at the end?")
if st.button("find my answer"):
    if question:
        with st.spinner("generate response..."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            
            st_cb=StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant","content":response})
            st.write('## response')
            st.success(response)
    else:
        st.warning("Please enter the question")
            