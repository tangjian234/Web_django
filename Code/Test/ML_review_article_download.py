import sys
import web_lib
import file_lib
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
import name_entity_reco as ner

# Get the best seller page from google search.
# input : search term  :
# output : 100 best seller in amazon.

# 1. build google search page
# 2. extract the first search result .

# 3. Get the first 50 ids
# 3. Get the last 50 ids


# ANCHOR 1. build google search page


# ANCHOR 2. Get 50 best seller asin for a best seller page

def get_a_page_best_seller_asin(soup):
    #
    titles = soup.find_all(class_="aok-inline-block zg-item")
    asin = [str(i.find("a", href=re.compile("dp"))) for i in titles]
    asin = [string_lib.get_mid_string_in_between(i, "/dp/", "/") for i in asin]
    return(asin)

# main func : get best seller asin list from a


def get_best_seller_asin(Amazon_best_seller_page):
    soup = bs_lib.get_soup(Amazon_best_seller_page)
    # first 50 best seller page
    # class id / href has dp
    asin = get_a_page_best_seller_asin(soup)
    # next 50 best seller
    next_page = soup.find(class_="a-last").find_all("a",
                                                    href=re.compile("zgbs"))[0]
    # between href= and \
    next_page = string_lib.get_mid_string_in_between(str(next_page), "href=\"",  "\"")
    next_page
    soup = bs_lib.get_soup(next_page)
    # second 50 best seller page
    next_asin = get_a_page_best_seller_asin(soup)
    asin = asin + next_asin
    return(asin)


links = ''


def download_review_articles(links, out_dir):
    for i, link in enumerate(links):
        #link = 'https://www.soundguys.com/best-bluetooth-speakers-2488/'
        doc = {"rank": "",
               "title": "",
               "link": "",
               "text": "",
               }
        doc["rank"] = str(i)
        (doc["title"], doc["link"], doc["text"]
         ) = bs_lib.get_html_info_html2text(link)
        t = doc["title"]
        s = string_lib.clean_string(t)
        f_name = '_'.join(s.split())
        f_name = out_dir + f_name + '.json'
        print(i, ':', f_name)
        print(doc["link"])
        # st.write(doc["text"])
        file_lib.json_dump(doc, f_name)


# Use a download :
# Highlight
# download search_item with 100 :

OUT_DIR = 'C:/Local/Work/ML_Name/Code/Test/data/review_article/'
search_item = 'best review bluetooth speaker'
search_item_num = 100

if __name__ == "__main__":
    # argv[1] : search item
    search_item = sys.argv[1]
    search_item_num = int(sys.argv[2])

    #search_item_connect = '_'.join(search_item.split())
    search_item_connect = string_lib.join_words_with_delimiter(
        search_item, '_')
    search_item_dir = OUT_DIR + search_item_connect + '/'
    file_lib.create_dir(search_item_dir)
    print(search_item_dir)

    g_search_item = string_lib.join_words_with_delimiter(
        search_item, '+')

    link_file = search_item_dir + 'Link_list_' + \
        search_item_connect + '_'+str(search_item_num) + ".json"
    print(link_file)

    links = web_lib.get_google_search_result(g_search_item, search_item_num)
    file_lib.save_links_as_json(links, link_file)
    download_review_articles(links, search_item_dir)
"""
"""

# asin_list = get_best_seller_asin(Amazon_best_seller_page)
# ASIN_OUT_DIR = 'C:/Local/Work/ML_Name/Code/Test/data/best_seller/'
# # asin_list=['a','b']
# OUT_DIR = ASIN_OUT_DIR + SEARCH_TERM
# OUT_FILE = OUT_DIR+'.json'

# asin_list_dict = basic_data_lib.list_to_dict(asin_list)
# file_lib.json_dump(asin_list_dict, OUT_FILE)
