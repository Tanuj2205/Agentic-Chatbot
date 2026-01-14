import streamlit as st
import os
from src.LanggraphAgenticAI.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title = "🤖 " + self.config.get_page_title(), layout = "wide")
        st.header("🤖 "+self.config.get_page_title())
        
        with st.sidebar:
            ## Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            ## LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                ## Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("GROQ API KEY",type="password")
                ## Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("PLEASE ENTER YOUR GROQ API KEY TO PROCEED!!!\n Don't have? Refer: https://console.groq.com.keys")
                    
            ## USECASE SELECTION
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)
        
            if self.user_controls["selected_usecase"] == "Chatbot with Web Search":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("PLEASE ENTER YOUR TAVILY API KEY TO PROCEED!!!\n Don't have? Refer : https://app.tavily.com/home")
        
        return self.user_controls           