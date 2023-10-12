import os
import streamlit as st
from utils import generate_script
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = str(os.getenv('OPENAI_API_KEY'))

# Stylling
st.markdown("""
<style>
div.stButton > button:first-child {
            background-color: #0099ff;
            color:#ffffff;
}
div.stButton > button:hover{
            background-color: #00ff00;
            color:#ffffff;
}
</style>
""", unsafe_allow_html=True)

if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] =''

st.title("❤️ YouTube Script Writing Tool")


# sidebar
st.sidebar.title("😁 Get in")
st.session_state['API_KEY'] = st.sidebar.text_input("What is your API Key?", type="password")
btnAPI = st.sidebar.button("Adicionar")
if btnAPI:
    if st.session_state['API_KEY'] != '':
        st.sidebar.write("Great to have you with us!😁💪")
    else:
        st.sidebar.write("Ouuu Noooo, API KEY field is empty😢😢")
# st.sidebar.image(".Youtube.jpg", width=300, use_column_width=True)

# Captures user inputs
prompt = st.text_input("Please provide the topic os the video", key="prompt")
video_length = st.text_input("Expected video length (in minutes)", key="video_length")
creativity = st.slider("Response Criativity Expected", 0.0, 1.0, 0.2, step=0.1)

#
button = st.button("Generate")

if button:
    if st.session_state['API_KEY']:
        search_result, title, script = generate_script(prompt=prompt, video_length=video_length, creativity=creativity, api_key=st.session_state['API_KEY'])
        st.success("❤️ Hope you like and enjoy this content script ❤️")

        st.subheader("Title💡")
        st.write(title)

        st.subheader("Your Video Script Content:📖📄")
        st.write(script)

        st.subheader("Check Out - DuckDuckGoo Search:🔍")
        with st.expander("Show me:"):
            st.info(search_result)
    else:
        st.error("Ooooooops!!! Please provide API KEY.....")

        
