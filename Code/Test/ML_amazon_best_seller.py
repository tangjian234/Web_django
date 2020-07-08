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
# Get the best seller page from google search.
# input : search term  : 
# output : 100 best seller in amazon. 

# 1. build google search page  
# 2. extract the first search result . 

# 3. Get the first 50 ids 
# 3. Get the last 50 ids 

def get_embed(string,begin,end):
  # Func: Get the sub string between begin and end
  t=string
  t=t.split(begin)[1] 
  t=t.split(end)[0] 
  return(t)

AMAZON_SEARCH_URL_BASE='https://www.google.com/search?q=amazon+best+seller+'
# 1. build google search page  
def build_google_search_page(Search_item):
  # Func : 
  # Return : the amazon best saler link 
  Search_item = 'bluetooth'
  search_url= AMAZON_SEARCH_URL_BASE  + Search_item
  soup=bs_lib.get_soup(search_url)
  title=soup.find(class_="rc").find_all("a", href=re.compile("zgbs"))[0]
  t=str(title)
  t
  link=get_embed(t,"href=\"","\"")
  return(link)



def get_a_page_best_seller_asin(soup):
  titles=soup.find_all(class_="aok-inline-block zg-item")
  asin=[str(i.find("a", href=re.compile("dp"))) for i in titles] 
  asin=[get_embed(i,"/dp/","/") for i in asin]
  return(asin)

# main func : get best seller asin list from a 
def get_best_seller_asin(Amazon_best_seller_page):
  soup=bs_lib.get_soup(Amazon_best_seller_page)
  # class id / href has dp 
  asin= get_a_page_best_seller_asin(soup)
  next_page =soup.find(class_="a-last").find_all("a", href=re.compile("zgbs"))[0]
  next_page =get_embed(str(next_page),"href=\"",  "\"")
  next_page
  soup=bs_lib.get_soup(next_page)
  next_asin= get_a_page_best_seller_asin(soup)
  asin= asin + next_asin
  return(asin)
  # next 50 
LINK='https://www.amazon.com/Best-Sellers-Electronics-Portable-Bluetooth-Speakers/zgbs/electronics/7073956011' 
import file_lib
SEARCH_TERM="bluetooth+speaker"
Amazon_best_seller_page=build_google_search_page("bluetooth+speaker")
Amazon_best_seller_page
asin_list=get_best_seller_asin(Amazon_best_seller_page)
ASIN_OUT_DIR = 'C:/Local/Work/ML_Name/Code/Test/data/best_seller/'
#asin_list=['a','b']
OUT_DIR=ASIN_OUT_DIR+ SEARCH_TERM
OUT_FILE= OUT_DIR+'.json'

asin_list_dict=basic_data_lib.list_to_dict(asin_list)
file_lib.json_dump(asin_list_dict,OUT_FILE)