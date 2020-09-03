# %%

# !------------------------------------------------------------------------->
# Synopsis : 
#     Processing web content and highlight names 
#
# Input:  article Web link;
# Output : person's names in article Highlighted
#
# - use article to get webpage text content
# - use spacy for NER : 
#   Highlight the person's name in the article
#
#  Documentation : 
#      ML_Name_Identification.md
# !------------------------------------------------------------------------->


import configparser
import pickle
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pinyin
from sklearn.metrics import plot_confusion_matrix

import json
import re
from pathlib import Path
import sys
import file_lib as f_lib
import web_lib as w_lib
import string_lib as s_lib
import basic_lib as blb
import json_lib as j_lib
import glob
import numpy as np
import os
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
import streamlit as st

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

nlp = spacy.load("en_core_web_sm")

link = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020'
#link = 'https://www.amazon.com/Pyle-Wireless-Portable-Speaker-System/dp/B07L4ZTB9D?ref_=s9_apbd_orecs_hd_bw_b7ijb6h&pf_rd_r=EDHJNF1JGB0X93YWFFY4&pf_rd_p=4bb337e0-ad10-51c8-81e9-9fe76bed3238&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=7073956011'


def get_html_info(link):
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    return(article.title, link, article.text)


def Get_html_text(link):
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    article.authors
    return(article.text)


import string_lib



def get_entry_highlight(text,entry_ID):
    article = nlp(text)
    entry_name_all = [(ent.text, ent.start_char, ent.end_char, ent.label_)
                       for ent in article.ents if ent.label_ == entry_ID]
    for i, p in enumerate(entry_name_all):
        (_, st, end, _) = p
        shift = i*4
        text = string_lib.insert_char(text, st+shift, '**')
        text = string_lib.insert_char(text, end+shift+2, '**')

    return(text, entry_name_all)



def get_person_name(text):
    article = nlp(text)
    person_name_all = [(ent.text, ent.start_char, ent.end_char, ent.label_)
                       for ent in article.ents if ent.label_ == 'PERSON']
    for i, p in enumerate(person_name_all):
        (name, st, end, label) = p
        shift = i*4
        text = string_lib.insert_char(text, st+shift, '**')
        text = string_lib.insert_char(text, end+shift+2, '**')

    return(text, person_name_all)
