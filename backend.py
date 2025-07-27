from pydantic import BaseModel
from typing import List
class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str]
    allow_search:bool
from app import get_response_from_agent
from fastapi import FastAPI
app=FastAPI(title="LangGraph AI Agent")
allowed_model_names=["llama-3.3-70b-versatile","gemma2-9b-it","llama-3.1-8b-instant"]
@app.post("/chat/")
def chat_endpoint(request:RequestState):
    """
    API ENDPOINT TO INTERACT WITH THE CHATBOT USING LANGGRAPH AND SEARCH TOOLS.
    IT SELECTS THE MODEL SPECIFIED IN THE REQUEST
    """

    if request.model_name not in allowed_model_names:
        return{"error": "Invalid model name : select valid model. "}
    
    model_name=request.model_name
    model_provider=request.model_provider
    system_prompt=request.system_prompt
    messages=request.messages
    allow_search=request.allow_search
    response=get_response_from_agent(model_name=model_name,model_provider=model_provider,system_prompt=system_prompt,messages=messages,allow_search=allow_search)
    return response

if __name__== "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=9999)
