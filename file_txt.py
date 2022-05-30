import streamlit as st
from io import StringIO

st.header("Welcome! ")

#INPUT
#Open a .txt file to read
uploaded_text_file = st.file_uploader("Please choose a .txt file")
if uploaded_text_file is not None:
  stringio = StringIO(uploaded_text_file.getvalue().decode("utf-8"))
  string_data = stringio.read()
  text = string_data
  st.subheader("Let's look at your text you have uploaded!")
  st.write(text)


#https://stackoverflow.com/questions/11914472/how-to-use-stringio-in-python3
