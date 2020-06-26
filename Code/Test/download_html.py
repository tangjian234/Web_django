# %%

import sys
import os
from pathlib import Path
import codecs
from lxml import html
import requests
import json_lib as j_lib
import web_lib as w_lib
import re
from requests_file import FileAdapter
data_folder = Path("C: \Local\Work\ML_Name\Database")
# %%

# %%


def load_web_page(link):
    # Func: load a page given a link
    page = requests.get(link)
    tree = html.fromstring(page.content)
    X = "//div[@class = 'list-title mathjax']/text()"
    # '/div[@class="list-title mathjax"]/text()'

    # '/div[@class='list-title mathjax'][1]'
    title = tree.xpath(X)
    print(title)
# load_web_page(link)


def load_local_page(link):
  # Func : return
    s = requests.Session()
    s.mount('file://', FileAdapter())
    resp = s.get(link)
    tree = html.fromstring(resp.content)
    X = "//div[@class = 'list-title mathjax']/text()"
    title = tree.xpath(X)
    X = "//div[@class = 'list-authors']/a/text()"
    authors = tree.xpath(X)
    return(title, authors)
    # print(title)

# load_local_page(link)


def read_link_list(file):
    d = j_lib.load_json(file)
    return(d.values())


def download_link(url, file_name):
    r = requests.get(url, allow_redirects=True)
    file_path = "C:\Local\Work\ML_Name\Database\cs"
    file_name = Path(file_path) / file_name
    with open(file_name, "wb") as file:
        file.write(r.content)


def local_file_to_web_link(f):
    return("file:///" + f)
#    f = w_lib.local_file_to_web_link(mypath + f)


def test():
    # Func:

 # %%
    config = j_lib.load_json(
        "C:\Local\Work\ML_Name\Code\Config\chinese_name_config.json")
    mypath = config["out_put_html_dir"]


file = "C:\Local\Work\ML_Name\Database\link_list_t.json"
link_list = w_lib.read_link_list(file)
base_dir = "C:\Local\Work\ML_Name\Database"
# for link in link_list:
# download_link("https://arxiv.org/list/cs/1901?skip=0&show=200050")

for i, url in enumerate(link_list):
    print(url)
    p = re.compile(r"list\/(.*)\/(.*)\?")
    f_dir = p.search(url).group(1)
    f_dir = base_dir+f_dir
    f_name = p.search(url).group(2)
    file_name = f_dir+"_"+f_name+".html"
    # w_lib.download_link(url, f_dir, file_name)
    print(file_name)

    # file_name = "f1901.html"

    # download_link("https://arxiv.org/list/cs/1901?skip=0&show=200050")


if __name__ == "__main__":
    test()
