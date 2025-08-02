import streamlit as st
st.set_page_config(page_title="LangGraph Agent",layout="centered")
st.title("AI CHATBOT AGENTS")
st.write("Create and Interact with AI Agents ! ")
system_prompt=st.text_area("Define you AI Agent : ", height=70,placeholder="Type your system prompt here.....")
GROQ_MODEL_NAMES=["llama-3.3-70b-versatile","gemma2-9b-it","llama-3.1-8b-instant"]
OPENAI_MODEL_NAMES=["gpt-4o","gpt-3.5-turbo"]
provider=st.radio("Select Model Provider :",("Groq","OpenAI"))
if provider is "Groq":
    selected_model=st.selectbox("Select Groq Model :",GROQ_MODEL_NAMES)
elif provider is "OpenAI":
    selected_model=st.selectbox("Select OpenAI Models :",OPENAI_MODEL_NAMES) 
allow_websearch=st.checkbox("Allow Web Search")
user_query=st.text_area("What would you like to know ?  ", height=200,placeholder="Type your question here.....")
backend_url="http://127.0.0.1:9999/chat"
if st.button("Ask your agent !!"):
    if user_query.strip():
        import requests
        payload={
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt":system_prompt,
            "messages":[user_query],
            "allow_search":allow_websearch
        }
        response=requests.post(backend_url,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response :")
                st.markdown(response_data)


        
        