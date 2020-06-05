# %%
import json_lib as jlb
import basic_lib as blb
import numpy as np
import string_lib as s_lib
import sys
from pathlib import Path
import re


def load_chinese_name():
    # Func:
    file_path = "C:\Local\Work\ML_Name\Database"
    file_name = "Chinese-100-surnames.json"
    chinese_name = jlb.load_json_path(file_path, file_name)
    chinese_name_pinyin = [x.lower() for x in chinese_name.keys()]
    return(chinese_name_pinyin)


def load_paper():
    file_path = "C:\Local\Work\ML_Name\Database"
    file_name = "paper.json"
    paper = jlb.load_json_path(file_path, file_name)
    # p = re.compile(r"/\w+\s/")
    name_all = [v["names"].lower().split(",") for v in paper.values()]
    return(name_all)


def is_chinese_name(name, chinese_name):
    return(name in chinese_name)

    # %%
if __name__ == "__main__":
    chinese_name = load_chinese_name()
    name = "cui"
    name_all = load_paper()
    for authors in name_all:
        Chinese = [author.strip() for author in authors if author.split()[1]
                   in chinese_name]
        print(Chinese)

    # %%
