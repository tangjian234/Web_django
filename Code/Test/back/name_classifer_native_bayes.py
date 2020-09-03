# %%
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import re
from pathlib import Path
import sys
import file_lib as f_lib
import web_lib as w_lib
import string_lib as s_lib
import basic_lib as blb
import json_lib as j_lib
import glob
from sklearn.model_selection import train_test_split
import numpy as np
import os
import pandas as pd
from faker import Faker
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
# remember to make sure
# %%
# %%

# %%
# from sklearn.feature_extraction.text import CountVectorizer


# %%
# ANCHOR 1. Collecting and Generating the Name Data

def generate_name(country, num=5):
    fake = Faker(country)  # initialize the faker instance for chosen country
    print('\n{} Fake Names: '.format(country))
    for i in range(num):
        print(fake.name())  # just to save line, don't code like this.


generate_name('ja_JP')
generate_name('en_US')

# ANCHOR 2. Loading data :

# %%
# setting up path to the data file
PATH = os.path.abspath('')
PATH = os.path.join(PATH, 'data')
names = 'multi_class.csv'
# %%
# read in the data as panda dataframe
df = pd.read_csv(os.path.join(PATH, names))
df.sample(1000)

# %%
# ANCHOR Data Preprocessing

# Initialize and fit CountVectorizer with given text documents
vectorizer = CountVectorizer().fit(df['name'])

# use the vectorizer to transform the document into word count vectors (Sparse)
word_mat = vectorizer.transform(df['name'])


# %%
# # ANCHOR Encoding the Country Labels

# creating mapping from unique label texts to unique integers
# note this can be re-used to encode and decode the labels after as well

encoder = LabelEncoder().fit_transform(df['code'])
# encoder = OrdinalEncoder().fit_transform(df['code'])
y = encoder

# using the encoder to encode the entire dataset
# y = encoder.transform(encoder)


# %%


x_train, x_test, y_train, y_test = train_test_split(word_mat, y, test_size=0.3)

# %%
# instantiate the model as clf(classifier) and train it

# 1. Native Bayes
# clf = MultinomialNB()

# 2. support vector machine
# clf = svm.SVC(kernel='linear')  # Linear Kernel

# 3.Logistic Regression
clf = LogisticRegression()

clf.fit(x_train, y_train)


# %%
some_names = ['Jack Nicholson', 'Don Trump',
              '山本 裕樹', '陆 成', '伊藤 真綾', '青山 くみ子', 'Lourdes del Tur', 'Jose Llanos Amores', 'Lisa Jackson', '윤 예준']
x_t = vectorizer.transform(some_names)
pred = clf.predict(x_t)
f = list(LabelEncoder().fit(df['code']).classes_)
print([f[i] for i in pred])


# %%


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
