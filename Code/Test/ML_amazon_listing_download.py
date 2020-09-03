
# !------------------------------------------------------------------------->
# Synopsis : 
#     Download file given a list of asin : use bs_lib.
#
#  Documentation : 
#      ML_Name_Identification.md
# !------------------------------------------------------------------------->


 # - [ML_amazon_listing_download.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_listing_download.py) 
 

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


# download file given a list of asin 
product_id_list_file = 'C:/Local/Work/ML_Name/Code/Test/asin_list_file.json'
product_id_list = json_lib.load_json(product_id_list_file)

for k in product_id_list.keys():
  asin=(product_id_list[k])
  amazon_product_dict = bs_lib.get_amazon_product_info(asin)