import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,MessagesPlaceholder

from langgraph.prebuilt import create_react_agent
def get_response_from_agent(model_name,model_provider,system_prompt,messages,allow_search):
        if model_provider=="Groq":
            llm=ChatGroq(model=model_name)
        elif model_provider=="OpenAI":
            llm=ChatOpenAI(model=model_name)
        prompt=ChatPromptTemplate.from_messages(
            [
            ("system",system_prompt),
            MessagesPlaceholder(variable_name="messages")
            ]
        )

            
        tools=[TavilySearch(max_results=2,api_key=TAVILY_API_KEY)] if allow_search else []
        agent=create_react_agent(
             model=llm,
             tools=tools,
             prompt=prompt
        )
        state={
            "messages":[HumanMessage(content=messages[-1])]
            }
        response=agent.invoke(state)
        messages=response.get("messages")
        answer_message=[message.content for message in messages if isinstance(message,AIMessage)]
        return answer_message[-1]


