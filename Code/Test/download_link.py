# %%

import sys
import os
from pathlib import Path
import codecs
from lxml import html
import requests
import re
from requests_file import FileAdapter
import web_lib
import file_lib
data_folder = "C:\Local\Work\ML_Name\Database\\"
import streamlit as st
# %% 

out_dir = data_folder+'bt_speaker_info\\'
out_dir
link_list_file=out_dir+'link_list.txt'
link_list_file
def download_link():
  link_list=file_lib.read_text_file(link_list_file)
  
  for link in link_list:
    if not (re.search(r'^#',link)):
      web_lib.download_link_article(out_dir,link)
download_link()