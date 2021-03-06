
# - [ML_master.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_master.py) 

 # - [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md) 


# https://github.com/Jcharis/Streamlit_DataScience_Apps/tree/master/NLP_App_with_Streamlit_Python

# !------------------------------------------------------------------------->
#  Synopsis : 
#     Master doc to Running the streamlit based web UI 
#  Documentation : 
#     ML_Amazon_product_adviser_chat_bot.md
# !------------------------------------------------------------------------->

"""
# App: NLP App with Streamlit (NLPiffy)
Author: [Jesse E.Agbe(JCharis)](https://github.com/Jcharis))\n
Source: [Github](https://github.com/Jcharis/Streamlit_DataScience_Apps/)
Credits: Streamlit Team,Marc Skov Madsen(For Awesome-streamlit gallery)
Description
This is a Natural Language Processing(NLP) Based App useful for basic NLP concepts such as follows;
+ Tokenization & Lemmatization using Spacy
+ Named Entity Recognition(NER) using SpaCy
+ Sentiment Analysis using TextBlob
+ Document/Text Summarization using Gensim/Sumy
This is built with Streamlit Framework, an awesome framework for building ML and NLP tools.
Purpose
To perform basic and useful NLP task with Streamlit,Spacy,Textblob and Gensim/Sumy
""" 
# Core Pkgs

from PIL import Image
import streamlit as st
import os


# NLP Pkgs
from textblob import TextBlob
import spacy
from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import name_nationality as nn
import name_entity_reco as ner
import ML_amazon_best_seller as best_seller
from newspaper import Article
import urllib.request
import itertools as it
import sys
import collections
import numpy as np

from bs4 import BeautifulSoup
import requests
import re
import nltk
import spacy
import streamlit as st
# NLP Pkgs

# Sumy Summary Pkg


# Function for Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

# Function to Analyse Tokens and Lemma


@st.cache
def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    # tokens = [ token.text for token in docx]
    allData = [('"Token":{},\n"Lemma":{}'.format(
        token.text, token.lemma_))for token in docx]
    return allData

# Function For Extracting Entities


@st.cache
def entity_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_)for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
    return allData

# C:\Local\Work\Web\Note\nlp-word-cloud.jpg


@st.cache
def name_nationality(my_text):
    return(0)


def main():
    """ NLP Based App with Streamlit """
    # see  ML_Master.md
    # Title
    st.title("Jian's work ")

    # sidbar title image
    image = Image.open('C:/Local/Work/ML_Name/Code/Lib/my_nlp-word-cloud.jpg')
    st.sidebar.image(image, caption='NLP Cloud',
                     use_column_width=True)
    st.sidebar.subheader("Natural Language Processing On the Go..")
    st.markdown("""
    	# Description
    	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
    	Tokenization,NER,Sentiment,Summarization : See 
    	""")

    # Name Nationality
    if st.sidebar.checkbox("Name Nationality Recongition"):
        st.subheader("Enter your names, seperated by , ")
        message = st.text_area("Enter Name", "Type Here ..")
        if st.button("Analyze"):
            nlp_name = nn.name_nationality(message)
            st.json(nlp_name)

    # Name entity recognition
    if st.sidebar.checkbox("Name Entity Recongition"):
        st.subheader("Enter your website ")
        message = st.text_area(
            "Input:  article web link;\n  Output : person's names in article\n Highlight the person's name in the article\n Example : https://finance.yahoo.com/news/why-us-china-relations-are-worsening-on-almost-every-front-213714768.html")
        if st.button("Analyze"):
            nlp_text = ner.Get_html_text(message)
            #nlp_text = nlp_text.replace("University ", "**University** ")
            (nlp_text, person_name_all) = ner.get_person_name(nlp_text)
            st.write(person_name_all)
            st.markdown(nlp_text)
    
    # Amazon Best seller 
    # Give a search lis
    if st.sidebar.checkbox("Amazon best seller list "):
                st.subheader("Enter your product search item ")
                message = st.text_area("Enter Name", "Type Here ..")
                if st.button("Analyze"):
                    best_seller.ML_amazon_best_seller(message)
                    #st.json(nlp_name)    
    
    # give a product ID : download Amazon Product Information 
    # see  ML_Master.md
    import bs_lib
    if st.sidebar.checkbox("Amazon Product"):
        st.subheader("Enter your product ID ")
        message = st.text_area(
            "ID: eg. B079K4TVPG")
        if st.button("Analyze"):            
            amazon_product_dict = bs_lib.get_amazon_product_info(message)
            st.write(amazon_product_dict)
    
    
    # 
    st.sidebar.subheader("About App")
    st.sidebar.text("NLP with Streamlit")
    st.sidebar.info("Cudos to the Streamlit Team")

    st.sidebar.subheader("By")
    st.sidebar.text("Jian Tang")


if __name__ == '__main__':
    main()
