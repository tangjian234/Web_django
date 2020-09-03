

# !------------------------------------------------------------------------->
# Synopsis : 
#     Input: Given search term: 
#     Get the top 100 best seller's ASIN 
#
#  Documentation : 
#      ML_Amazon_product_adviser_chat_bot.md
# !------------------------------------------------------------------------->


# - [ML_amazon_best_seller.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_best_seller.py) 
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
import basic_data_lib
import re
import os
import string_lib
import web_lib
# Get the best seller page from google search.
# input : search term  : 
# output : 100 best seller in amazon. 

# 1. build google search page  
# 2. extract the first search result . 

# 3. Get the first 50 ids 
# 3. Get the last 50 ids 



AMAZON_SEARCH_URL_BASE='https://www.google.com/search?q=amazon+best+seller+'
# ANCHOR 1. build google search page  
def build_google_search_page(Search_item):
  # Func : 
  # Return : the amazon best seller link 
  Search_item = 'bluetooth'
  search_url= AMAZON_SEARCH_URL_BASE  + Search_item
  search_url
  #print("here",search_url)
  soup=bs_lib.get_soup(search_url)
  # two layers : class = rc / a have zgbs 
  #  zgbs is the best seller indicator.  
  title=soup.find(class_="rc").find_all("a", href=re.compile("zgbs"))[0]
  t=str(title)
  t
  link=string_lib.get_mid_string_in_between(t,"href=\"","\"")
  return(link)



#get_amazon_best_seller_page 

# ANCHOR 2. Get 50 best seller asin for a best seller page 

def get_a_page_best_seller_asin(soup):
  # 
  titles=soup.find_all(class_="aok-inline-block zg-item")
  asin=[str(i.find("a", href=re.compile("dp"))) for i in titles] 
  asin=[string_lib.get_mid_string_in_between(i,"/dp/","/") for i in asin]
  return(asin)

# main func : get best seller asin list from a 
def get_best_seller_asin(Amazon_best_seller_page):
  soup=bs_lib.get_soup(Amazon_best_seller_page)
  # first 50 best seller page 
  # class id / href has dp 
  asin= get_a_page_best_seller_asin(soup)
  # next 50 best seller 
  next_page =soup.find(class_="a-last").find_all("a", href=re.compile("zgbs"))[0]
  # between href= and \ 
  next_page =string_lib.get_mid_string_in_between(str(next_page),"href=\"",  "\"")
  next_page
  soup=bs_lib.get_soup(next_page)
  # second 50 best seller page
  next_asin= get_a_page_best_seller_asin(soup)
  asin= asin + next_asin
  return(asin)

LINK='https://www.amazon.com/Best-Sellers-Electronics-Portable-Bluetooth-Speakers/zgbs/electronics/7073956011' 
import file_lib
SEARCH_TERM="amazon+best+seller+bluetooth+speaker"
SEARCH_TERM="amazon+best+seller+bluetooth+headphone"
#Amazon_best_seller_page=build_google_search_page("bluetooth+speaker")

def ML_amazon_best_seller(g_search_item):
  base = 'amazon+best+seller+'
  g_search_item= '+'.join(g_search_item.split())
  g_search_item= base+ g_search_item
  search_item_num=1
  st.write(g_search_item)
  links = web_lib.get_google_search_result(g_search_item, search_item_num)
  st.write(links)
  Amazon_best_seller_page=links[-1]
  asin_list=''
  asin_list=get_best_seller_asin(Amazon_best_seller_page)
  st.write(asin_list)
  ASIN_OUT_DIR = 'C:/Local/Work/ML_Name/Code/Test/data/best_seller/'
  #asin_list=['a','b']
  OUT_DIR=ASIN_OUT_DIR+ g_search_item
  OUT_FILE= OUT_DIR+'.json'

  asin_list_dict=basic_data_lib.list_to_dict(asin_list)
  file_lib.json_dump(asin_list_dict,OUT_FILE)
  st.write(OUT_FILE)
