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
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

if uploaded_text_file is not None:
  words_tokens = word_tokenize( text )

#st.write( words_tokens )


import re
if uploaded_text_file is not None:
  text1=re.sub("([^A-Za-z])"," ",text)
#st.write(text1)


from string import punctuation
puncts = punctuation
puncts_list = [ s for s in puncts ]
#st.write( puncts_list )


from nltk.corpus import stopwords 
if uploaded_text_file is not None:
  badwords = stopwords.words('english')
  #st.write( badwords )
 
  
  if uploaded_text_file is not None:
    badwords.extend(puncts_list) 
    #st.write( badwords )
    
  if uploaded_text_file is not None:
    text2 = text1.split()
    no_short_words = [word for word in text2 if len(word) <= 2]
    new_text = ",".join(text2)
    badwords.extend(no_short_words)
    st.write(new_text)

