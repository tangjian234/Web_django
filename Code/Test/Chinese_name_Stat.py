# %%
import glob
import json_lib as j_lib
import basic_lib as blb
import numpy as np
import string_lib as s_lib
import web_lib as w_lib
import file_lib as f_lib


import sys
from pathlib import Path
import re


def load_chinese_name(file_name):
    # Func:
    chinese_name = j_lib.load_json(file_name)
    chinese_name_pinyin = [x.lower() for x in chinese_name.keys()]
    return(chinese_name_pinyin)


def load_paper():
    file_path = "C:\Local\Work\ML_Name\Database"
    file_name = "paper.json"
    paper = j_lib.load_json_path(file_path, file_name)
    # p = re.compile(r"/\w+\s/")
    name_all = [v["names"].lower().split(",") for v in paper.values()]
    return(name_all)


def is_chinese_name(name, chinese_name):
    return(name in chinese_name)


def Computer_paper():
    name_all = load_paper()
    for authors in name_all:
        Chinese = [author.strip() for author in authors if author.split()[1]
                   in chinese_name]
        print(Chinese)


def computer_local_link(local_link):
    (_, authors) = w_lib.load_local_page(local_link)
    # print(authors)
    Chinese = [author.strip() for author in authors if author.split()
               [-1].lower() in chinese_name]
    p = len(Chinese)/len(authors)*100
    print(f"{p: 2.2f} Percent")
    return(len(Chinese), len(authors))
# Computer_local_link(local_link)

# %%

    # mypath="C:/Local/Work/ML_Name/Database/cs/"
    # get _files_from_path(mypath)


if __name__ == "__main__":
    config = j_lib.load_json(
        "C:\Local\Work\ML_Name\Code\Config\chinese_name_config.json")
    chinese_name = load_chinese_name(config["chinese_name_file"])
    local_link_example = "file:///C:/Local/Work/ML_Name/Database/cs/f19_8.html"
    mypath = config["out_put_html_dir"]
    files = f_lib.get_files_from_path(mypath)
    total, chinese = 0, 0
    for f in files:
        f = w_lib.local_file_to_web_link(mypath + f)
        number_of_chinese, number_total = computer_local_link(f)
        total = total+number_total
        chinese = chinese+number_of_chinese
    p = chinese/total*100
    print(f"{p: 2.2f} Percent")
    # mylist = [f for f in glob.glob("*.txt")]

    # print(glob.glob("C:/Local/Work/ML_Name/Database/cs/*.html"))
    # %%
    # print(f"Hello, My name is {name:>10} and I'm {age:2.2f} years old.")
