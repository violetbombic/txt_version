import streamlit as st
from io import StringIO
from nltk import word_tokenize, sent_tokenize

st.header("Welcome! ")

#INPUT
#Open a .txt file to read
uploaded_text_file = st.file_uploader("Please choose a .txt file")
if uploaded_text_file is not None:
  stringio = StringIO(uploaded_text_file.getvalue().decode("utf-8"))
  string_data = stringio.read()
  text = string_data
  #st.subheader("Let's look at your text you have uploaded!")
  #st.write(text)

#https://stackoverflow.com/questions/11914472/how-to-use-stringio-in-python3

import nltk
nltk.download('all')

if uploaded_text_file is not None:
  words_tokens = word_tokenize( text )

#st.write( words_tokens )


import re
text1=re.sub("([^A-Za-z])"," ",text)
st.write(text1)
