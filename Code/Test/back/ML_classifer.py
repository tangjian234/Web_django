# %%
# !------------------------------------------------------------------------->
#  Synopsis : 
#     
#  Documentation : 
#    
# !------------------------------------------------------------------------->

import pickle
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pinyin
from sklearn.metrics import plot_confusion_matrix

import json
import re
from pathlib import Path
import sys
import file_lib as f_lib
import web_lib as w_lib
import string_lib as s_lib
import basic_lib as blb
import json_lib as j_lib
import glob
import numpy as np
import os
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt

# remember to make sure all module files are installed
# [Name Classification with Naive Bayes](https://towardsdatascience.com/name-classification-with-naive-bayes-7c5e1415788a)
# %%
# %%

# %%


# %%
# ANCHOR 1.Generate data

def generate_name(country, num=5):
    fake = Faker(country)  # initialize the faker instance for chosen country
    print('\n{} Fake Names: '.format(country))
    for i in range(num):
        print(fake.name())  # just to save line, don't code like this.


# generate_name('ja_JP')
# generate_name('en_US')

# ANCHOR 2. Loading data :

# %%
# setting up path to the data file


def load_data(file_name):
    # file_name = Path('C:\Local\Work\ML_Name\Code\Test\data\multi_class.csv')
    file_name = Path(file_name)
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
    # ANCHOR 3.1 Data Preprocessing : input Vectorization

    # Give each input(i.e name) a unique vector via bag-of-word method
    # Using bag of words to create the input feature 1-d
    # any 1-d input (word lists) can be convert into input feature matrix like it.
    # Initialize and fit CountVectorizer with given text documents
    # different CountVectorizer

    # use pinyin to train
    USE_PINYIN = False

    if (USE_PINYIN):
        py = [pinyin.get(x, format="strip", delimiter="") for x in df['name']]
        vectorizer = CountVectorizer().fit(py)
    else:
        vectorizer = CountVectorizer().fit(df['name'])

    # use the vectorizer to transform the document into word count vectors (Sparse)
    word_mat = vectorizer.transform(df['name'])
    input_data = word_mat

    # ANCHOR 3.2 Data Preprocessing : output Vectorization
    # Encoding the Country Labels
    # creating mapping from unique label texts to unique integers
    # note this can be re-used to encode and decode the labels after as well
    encoder = LabelEncoder().fit_transform(df['code'])

    # encoder = OrdinalEncoder().fit_transform(df['code'])
    output_data = encoder
    return(input_data, output_data)

C:/Local/Work/ML_Name/Code/Test/ML_classifer.py

# (input_data, output_data) = data_preprocessing(df)

# ANCHOR 4. Model training

# %%

def train_model(input_data, output_data, trained_model_file):
    # Func:

    # ANCHOR 4.1 Split into training and testing set

    x_train, x_test, y_train, y_test = train_test_split(
        input_data, output_data, test_size=0.3)

    # ANCHOR 4.2 instantiate the model as clf(classifier) and train it
    # 1. Native Bayes
    # clf = MultinomialNB()

    # 2. support vector machine
    # clf = svm.SVC(kernel='linear')  # Linear Kernel

    # 3.Logistic Regression
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    pickle.dump(clf, open(trained_model_file, 'wb'))
    verify_model(trained_model_file, df, x_test, y_test)
    return(clf, x_test, y_test)


#

# ANCHOR 5. Model testing
# %%


def test_model(trained_model_file, df):
    # Func:
    clf = pickle.load(open(trained_model_file, 'rb'))
    vectorizer = CountVectorizer().fit(df['name'])
    # transform encode the names by vectorizer
    x_t = vectorizer.transform(some_names)
    pred = clf.predict(x_t)
    # show the classes :
    class_names = list(LabelEncoder().fit(df['code']).classes_)
    # transfer index to content of outlist
    nationality = [class_names[i] for i in pred]
    Dict = dict(zip(some_names, nationality))
    dict_pretty_disp(Dict)


def dict_pretty_disp(Dict):
    print('='*20, "Result", '='*20)
    for i, key in enumerate(Dict):
        print(f"{i}.{key:20} -> {Dict[key]}")


def verify_model(trained_model_file, df, x_test, y_test):
    # Func: print confusion matrix
    clf = pickle.load(open(trained_model_file, 'rb'))
    disp_confusion_matrix(clf, df, x_test, y_test)


def disp_confusion_matrix(clf, df, x_test, y_test):
    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    titles_options = [("Confusion matrix, without normalization", None),
                      ("Normalized confusion matrix", 'true')]
    class_names = list(LabelEncoder().fit(df['code']).classes_)
    # class represent by first 2 char
    class_names = [c[0:2] for c in class_names]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(clf, x_test, y_test,
                                     display_labels=class_names,
                                     normalize=normalize)
        disp.ax_.set_title(title)
        print(title)
        print(disp.confusion_matrix)
    # plt.show()
    plt.show(block=False)
    plt.pause(23)
    plt.close()
# test_model(clf, df)
# %%


# %%
# ANCHOR Main:  Seting
TRAIN_MODEL = True
TRAINED_MODEL_FILE = 'trained_model.bin'
DATA_FILE_NAME = 'C:\Local\Work\ML_Name\Code\Test\data\multi_class_tst_pinyin.csv'
some_names = ['Jack Nicholson', 'li zhang',
              '山本 裕樹', 'wang wei', '伊藤 真綾', '青山 くみ子', 'Lourdes del Tur', 'Jose Llanos Amores', 'Lisa Jackson', '윤 예준']

if __name__ == '__main__':
    trained_model_file = TRAINED_MODEL_FILE
    df = load_data(DATA_FILE_NAME)
    if TRAIN_MODEL == True:
        (input_data, output_data) = data_preprocessing(df)
        clf = train_model(input_data, output_data, trained_model_file)
        #test_model(trained_model_file, df)
    else:
        test_model(trained_model_file, df)


# list(encoder.classes_)
# ['Arabic (Egypt)',
#  'Chinese (China)',
#  'English (United States)',
#  'French',
#  'Japanese',
#  'Korean',
#  'Norwegian',
#  'Portuguese (Brazil)',
#  'Russian',
#  'Spanish (Spain)']






