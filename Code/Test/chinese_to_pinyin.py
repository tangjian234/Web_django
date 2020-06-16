# https://pypi.org/project/pinyin/
# %%
import re
from pathlib import Path
import sys
import file_lib as f_lib
import pinyin

pinyin.get(u'你好')
pinyin.get('你好', format="strip", delimiter="")
pinyin.get('john smith', format="strip", delimiter="")

# %%
# ANCHOR 1. Loading data :


# setting up path to the data file


def load_data():
    file_name = Path(
        'C:\Local\Work\ML_Name\Code\Test\data\multi_class_tst_cn.csv')
    df = f_lib.load_csv_file(file_name)
    return(df)


# df = load_data()


# %%
# ANCHOR 3. Data Preprocessing
# Data Preprocessing :
# 1. Vectorization:  converting all kind input into unique digit vector as input matrix
# 3. Convert all output label into unique output


def data_preprocessing(df):
    # Func:
    out_put_file_name = Path("C:\Local\Work\ML_Name\Code\Test\multi_cn.csv")
    with open(out_put_file_name,   encoding='utf-8', mode="w") as file:
        file.write('code,name\n')
        for i in range(df['name'].size):
            code = list(df['code'])[i]
            x = list(df['name'])[i]
            x = pinyin.get(x, format="strip", delimiter="")
            x = x.title()
            file.write(f"{code},{x}\n")
    return(1)


# data_preprocessing(df)

# %%
if __name__ == '__main__':
    df = load_data()
    _ = data_preprocessing(df)
    print(_)


# %%
