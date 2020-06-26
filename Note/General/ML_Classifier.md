# ML_Classifier.md

- [ML_Classifier.md](file:///c:/Local/Work/ML_Name/Note/ML_Classifier.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Read [paper](#paper-1)
- [ ] Complete the summary of ML classifier from website [V_2][d_3]
  - [ ] [link](#encoding-the-country-labels)

## Reference

## Vision

    - Classify of Chinese name
    - Contain : ML technology

## Objective

- [Name Classification with Naive Bayes](https://towardsdatascience.com/name-classification-with-naive-bayes-7c5e1415788a)
- [Important classifier python implementation](file:///c:/Local/Work/ML_Name/Code/Test/ML_classifer.py)

## Process

### Collecting and Generating the Name Data

#### Installing scikit-learn

- remember to make sure sklearn is installed.
  https://docs.python.org/3.7/using/windows.html

In the latest versions of Windows, this limitation can be expanded to approximately 32,000 characters. Your administrator will need to activate the **“Enable Win32 long paths**” group policy,

### Taking a look at various names

- load csv data : 100,000 name so different nationality

### Data Preprocessing

#### - Convert names :

- Names need to be converted into numerical representation first

#### Bag-of-Words model

- each word/name assigned a unique number

This technique produces a vector with length of entire vocabulary, with each index position representing a unique word appears in the document, and the value in an index position expresses the frequency of the word that appear in a document/text.

<this 100,000 names means 100,000 word vocabulary : a vector with length of 100,000>

<each index location is the frequence of the word >

each word is uniquely represented .

This way, the order of the words in the document is not retained, but it’s a simple and intuitive way of representing a document by integers. Let’s take a look at this in action.

#### Library reference

https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html?highlight=countvectorizer#sklearn.feature_extraction.text.CountVectorizer

Convert a collection of text documents to a matrix of token counts

This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix.

If you do not provide an a-priori dictionary and you do not use an analyzer that does some kind of feature selection then the number of features will be equal to the vocabulary size found by analyzing the data.

#### code example

        vectorizer = CountVectorizer().fit(df['name'])
         word_mat = vectorizer.transform(df['name'])

### Encoding the Country Labels

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder

https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

    encoder = LabelEncoder().fit_transform(df['code'])

Encode target labels with value between 0 and n_classes-1.

This transformer should be used to encode target values, i.e. y, and not the input X.

Read more in the User Guide.

### Train and Evaluate the model

### Evaluation and Prediction

### Thoughts and Conclusion
