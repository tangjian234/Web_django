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
    mat = {}
    # if there is any key word of the product aspect in the feature list title sentence 
    # it is a match. 
    for f in feature_list_title:
        mat[f] = {}
        for kc in product_dict["feature_list"].keys():
            key_word_list = product_dict["feature_list"][kc]['key_word']
            fl = [k for k in key_word_list if k in f]
            if(len(fl) > 0):
                product_dict["feature_list"][kc]["match"][f] = fl
                mat[f][kc] = fl
    # product_dict
    
    mat
    return(product_dict)


# init the
product_dict = json_lib.load_json(dict_f_name)
product_info = json_lib.load_json(info_f_name)

process_product_dictionary(product_dict, product_info)

nlp = en_core_web_sm.load()

doc = nlp('Astonishing Sound: Breathtaking stereo sound with deep bass is delivered with exceptional clarity and zero distortion by two high-sensitivity drivers and a patented bass port.')
