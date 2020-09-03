#amazon_product_dictionary.py
#- [amazon_product_dictionary.py](file:///C:/Local/Work/ML_Name/Code/Test/amazon_product_dictionary.py) 

# !------------------------------------------------------------------------->
#  Synopsis : 
#     Processing and matching production dictionary vs asin product info  
#  Documentation : 
#     ML_Amazon_product_adviser_chat_bot.md
# !------------------------------------------------------------------------->

import en_core_web_sm
from collections import Counter
from spacy import displacy
import spacy
import re
from bs4 import BeautifulSoup
import requests
import random
import nltk
import json
import json_lib
import pathlib
import bs_lib
import pathlib
import streamlit as st
product_ids = {
    1: 'B010OYASRG',
    2: 'B07WSH46LX',
    3: 'B016XTADG2',
    4: 'B01CQOV3YO',
    5: 'B07P39MLKH',
    6: 'B01HETFQKS',
    7: 'B01N4V4X5M',
    8: 'B07QK2SPP7',
    9: 'B07ZRVX6RM',
    10: 'B07NW3TW32',
}
product_ids_v1 = {
    1: 'B07MF9Q21L',
    2: 'B00N11SHI2',
    3: 'B07KR9TLM7',
    4: 'B016MO90GW',
    5: 'B01N4V4X5M',
    6: 'B078S4P3J9',
    7: 'B07N593KKQ',
    8: 'B07QK2SPP7',
    9: 'B07YXYKFFL',
    10: 'B0749F6FRS',
}
product_ids_v2 = {
    1: 'B0742BV75P',
    2: 'B0719M4YZB',
    3: 'B07BSKRM23',
    4: 'B07GTBRSCY',
    5: 'B077SHH27K',
    6: 'B07PDKWVL7',
    7: 'B07PJXG49Q',
    8: 'B06X1984NQ',
    9: 'B01CQOV3YO',
    10: 'B07HHNJCZL',
    11: 'B07DPVF8DQ',
}
dict_f_name = pathlib.Path(
    'C:\Local\Work\ML_Name\Code\Test\data\\bt_speaker_product_dictionary.json')

info_f_name = pathlib.Path(
    'C:\Local\Work\ML_Name\Code\Test\data\\asin\B016MO90GW.json')

product_id = product_ids[random.randint(1, (len(product_ids)))]


def clean_feature_list(feature_list):
    # Func: Remove the non feature list description in the feature list 
    feature_list = [x for x in feature_list if not (
        (x == "This fits your .") | (x == " Make sure this fits") | (x == "by entering your model number."))]
    return(feature_list)
# clean_feature_list()


def get_match(string):
  # Func:  Used to get the first sentence, which is the feature list title . Separated by the separator.
    separators = [': ', '- ', '; ', '】 ']
    # shortest no empty match

    valid_separators = [sp for sp in separators if sp in string]
    if valid_separators:
        res = ' '*10000  # long string

        for sp in valid_separators:
            s1 = string.split(sp)[0]
            if (len(s1) < len(res)):
                res = s1
        return(res)
    else:
        # one sentence
        return(string)


def get_feature_list_title(feature_list):
  # func : split out the title according to seperator
  # first sentence with Separated by the separator. 
    feature_list_title = [get_match(s.lower())
                          for s in feature_list]
    feature_list_title
    return(feature_list_title)



def process_product_dictionary(product_dict, product_info):
    # match product_dict vs asin_product info
    product_dict
    product_info

    #  Get feature list needs a title, which is the first sentence.
    feature_list = product_info["feature_list"]
    feature_list = clean_feature_list(feature_list)
    feature_list_title = get_feature_list_title(feature_list)

    # fill in the Product dictionary.
    product_dict["ASIN"] = product_info["ASIN"]
    product_dict["title"] = product_info["title"]
    product_dict["price"] = product_info["price"]
    st.write("match with --------------------\n")
    
    mat=tag_sent_with_aspect_keyword(feature_list_title,product_dict)
    # if there is any key word of the product aspect in the feature list title sentence 
    # it is a match. 
    # for f in feature_list_title:
    #     mat[f] = {}
    #     for kc in product_dict["feature_list"].keys():
    #         key_word_list = product_dict["feature_list"][kc]['key_word']
    #         fl = [k for k in key_word_list if k in f]
    #         if(len(fl) > 0):
    #             product_dict["feature_list"][kc]["match"][f] = fl
    #             mat[f][kc] = fl
    # product_dict
    
    mat
    return(product_dict)

def analyze_text_by_product_dict(text,product_dict):
  sentences=string_lib.split_text_to_sentences(text)  
  sentences=[s.lower() for s in sentences ]
  
  mat=tag_sent_with_aspect_keyword(sentences,product_dict)
  highlight_text_with_aspect_keywords(mat)
  return(mat)

def tag_sent_with_aspect_keyword(sentences,product_dict): 
      # Func :   for each sentence : match with the dictionary for keywords 
      mat = {}      
      for sent in sentences:
        mat[sent] = {}
        for aspect in product_dict["feature_list"].keys():
            key_word_list = product_dict["feature_list"][aspect]['key_word']
            # key_word_list : if the sentence content the these keywords 
            matched_key_word_list = [keyword for keyword in key_word_list if keyword in sent]
            if(len(matched_key_word_list) > 0):
                mat[sent][aspect] = matched_key_word_list
      return(mat)

def highlight_text_with_aspect_keywords(mat):
  # Func :  
  highlighted_text=''
  aspect_tags=[]
  for sent in mat: 
    # sent
    sent_highlight=sent
    for aspect in mat[sent]:
      aspect_tags.append(aspect)
      for key_word in mat[sent][aspect]:
        aspect_highlight='{'+aspect+'} '
        # aspect_highlight
        key_word_highlight= "**"+ key_word+"**"  + aspect_highlight
        # key_word_highlight
        sent_highlight=sent_highlight.replace(key_word,key_word_highlight)
    highlighted_text= highlighted_text+sent_highlight
  highlighted_text
  aspect_tags

import string_lib
import name_entity_reco 
import NLTK_lib
import spacy_lib
if __name__ == "__main__":

# init the 
  product_dict = json_lib.load_json(dict_f_name)
  product_info = json_lib.load_json(info_f_name)
  
  text6='''LONGER BATTERY PLAYTIME UP TO 14 HOURS - Play from morning till night; battery can play up to 14 hours at 2/3 volume; AUX IN Jack connect from TVs and non-Bluetooth devices with a 3.5mm Line-In cable for the Perfect Line-In Speaker; BUILT-IN Microphone for personal handsfree speakerphone calls from a Cellphone or iPhone; Light-weight just 10 oz, 5” long, 2.8” high INCLUDES Micro-USB charging cable; Official OontZ Angle 3 Carry Case available sold separately on Amazon ''' 
  #mat=analyze_text_by_product_dict(text6,product_dict)
  
  (text, entry_name_all)=name_entity_reco.get_entry_highlight(text6,'CARDINAL')
  text
  s= NLTK_lib.noun_phrase_generator_nltk(text6)
  s
  s1 = spacy_lib.noun_phrase_generator_highlight_spacy(text6)
  s1
  text6
  #mat
  
  # process_product_dictionary(product_dict, product_info)
