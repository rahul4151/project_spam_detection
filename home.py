# home.py
import streamlit as st
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import *

def clean_data(txt):
        txt = txt.lower()
        txt = word_tokenize(txt)
        txt = [t for t in txt if t not in punctuation]
        txt = [t for t in txt if t not in stopwords.words("english")]
        txt = (" ").join(txt)
        return txt

def home_page():

    f = open("vector.pkl","rb")
    tv = load(f)
    f.close()
    
    f = open("model.pkl","rb")
    model =load(f)
    f.close()
    
    st.title("Spam Msg Detection")
    
    # Create a form using st.form()
    with st.form("My Form"):
        text = st.text_area("Enter your text here", height=200)
        submit_button = st.form_submit_button("Submit")
        ctxt = clean_data(text)
        vtxt = tv.transform([ctxt])
        res  = model.predict(vtxt)
        if res[0] == "spam":
             msg = "SPAM"
             background_color = "red"
        else:
             msg = "HAM"
             background_color = "green"
    
    # Process the form submission
    if submit_button:
        styled_msg = f"<div style='text-align: center; background-color: {background_color}; padding: 10px;'>{msg}</div>"
        st.write(styled_msg, unsafe_allow_html=True)
    