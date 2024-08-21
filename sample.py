import streamlit as st

st.title("welcome to my web based ai application!")
st.header("chat bot")
#st.subheader("vishnuprasaath")

import google.generativeai as genai

genai.configure(api_key="AIzaSyBoPr95TzPs1bOTBamWMajCPBjl-FbdTUE")


text=st.text_input("enter your question:")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
    



