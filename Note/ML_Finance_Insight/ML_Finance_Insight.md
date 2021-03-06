# ML_Finance_Insight.md

- [ML_Finance_Insight.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight/ML_Finance_Insight.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

- [ ] Sort and extend the plan [V_1][d_1]
  - [ ] [target](#vision)
- [ ] Read the most important
  - [ ] [paper](#paper-1--deep-learning-for-specific-information-extraction-from-unstructured-texts)

## 1.2. Progress

### 1.2.1. Highlight

## 1.3. Road map

## 1.4. Topic:

## 1.5. Vision

- Name : **Genie** :

  - Use aladdin theme for each of the sub project

- Chat bot on amazon search , help user to make wise decision :

language processing :
product data mining and analysis

### 3. How to get a trending financial data

    1. and what kind of insight can it bring. Publicly available data.

1.  log the input : mark the result

Check rosbersbary pi.

### User experience

1. What is most popular bluetooth headset product.

2. What is the key aspect of the a bluetooth category.

   - mining for aspect words :
     - How does a product score for each of the aspect.

3. Out-of-site context study

   1. Top article and content summary :

      - best bluetooth site : tech site.

   2. According to the content, which aspect is most highlighted. and most important.

4. According use : which aspect is most focused.
5. Which one have longest battery life.
6. Which have lowest price
7. Which one have most native ration

-

What is not todo :
Sub optimization :
build a MVP : for each component:
make the whole things work first.

Same for name classification.

## Arch Thought

### New structure ideal :

#### the Aspect/Topic is concrete and known :

    1. Limited: expert knowledge guided first :

    - - For bluetooth earpiece :
          the Aspect/Topic is concrete and known :

      - - A1 : Connectivity :
        - A2 : Sound Quality :
        - A3 : Battery life :

Total score = weighted score of the aspect: - radar diagram :
In all the listing:

- - 1. What kind of NP belong to each category:
  - 2. if one NP belong to the category, the NP of the sentence in the listing is likely to belong to the category.


    1. Boots strap
       Label -> classify -> re-label for non classified items.
       Boots strap : using to build a training database.
       1. End result :
          1. Mapping : NP with aspects :
             Example :

Question : in each price range, what is the most

1. How to rank the

### Feature extraction

    1. Some features is known should have stronger discriminative power by expert knowledge

    2. How to weight : sequential classifier. (Heavy weight of expert knowledge.vs machine learning.)
      -  some name have strong indication of nationality :
        1) e.g ginsberg is a jewish name.
        2) Li is a chinese name.

### Statistical analysis :

    1. Most frequent meaningful bi-words.
    2. Most mentioned meaningful model :

### Semantical study

- - - 1. <Question: How to Semantically grouping a pack of words.>
      - Example : Bluetooth Connectivity.
        - 1. ,
        - 2. signal strength,
      2. How does number quantify :

### Sentiment analysis

      1. Enhance the database by go though the typical names
      2. Indian name : identifier .
      3. Add statistical plot for the page.
      - 1. In this page : how many person in each nationality. (pie chart.)
           1. most / least .
        1. How does the trend increase and decrease over the year. (trended analysis .)
      1.

### UI for the amazon :

Dialogue : chatbot format :

- Give me search item :

  - I give you a 360 degree overview :

    - Most brand in each category/price range.
    - Highest rating/comment in the price range.

  - I give you the known Key aspects : (Expert knowledge)

    <Question: What the Weight or relative importance of this aspects :>

    <Answer: >

        - topic identification of the articles. :
          - Most visited atrial : (high google search rank)
          - Most talked about feature. (length of the paragraph that talking about)
          -

  - What is the commonality of the best seller:
    - Best seller has the following aspect :

## 1.6. Objective

### 1.6.1. Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI

### 1.6.2. Key concepts

#### 1.6.2.1. Aspects :

## 1.7. System Overview

### 1.7.1. Building block

1. **Crawler** :
   1. Crawler from web for amazon web pages and comments
2. **Classifier**
   1. Build System that Classify of Chinese name
3. **WebIO** :
   1. Chat bot :
   2. Answers :
   3. Use the job hunting and merging in.
   4. Data Visualization :
      1. Statistical Visualization.

### 1.7.2. Key Technology

- 1. Use web-service as input/ output. (Azure website)
  2. Use Python as Language
  3. Use Azure machine learning backbone
  4. Use previous simplified crawler.
  5. Use Pattern recognition as Name Nationality Classifer.

### 1.7.3. Key principles

1. Make MVP first : Frame work first, Get more detail later .
2. how to Simplify, Well still keep the system integrity
3. Each component/Building block have a file

## 1.8. System Design Detail

### 1.8.1. Building block construction

#### 1.8.1.1. Crawler :

- Crawler from web get the STEM names, [DONE]
- Crawler from web get the STEM subjects ,

##### 1.8.1.1.1. Versions and stages

1.  S1 :
2.  S2 :

##### 1.8.1.1.2. Input

- Amazon pages :
  - product pages.
  - comment pages

##### 1.8.1.1.3. Output

- listing :

#### 1.8.1.2. Classifier

#### 1.8.1.3.

##### 1.8.1.3.1. Input

- product listings

##### 1.8.1.3.2. Output

- Key extraction: aspect file tags :

#### 1.8.1.4. IO :

##### 1.8.1.4.1. Input

- Input name , display the nationality:

##### 1.8.1.4.2. Output

- visualization
  - Power BI

Challenges :

- complex : how to step by step simplify a issue.
- simplify :

### 1.8.2. Thought

1.

# 2. Progress

## 2.1. Readings

### 2.1.1. Using LSTM on the resume for skill words

- [paper](#paper-1--deep-learning-for-specific-information-extraction-from-unstructured-texts)

#### 2.1.1.1. Introduction

- [iki project](https://iki.ai/)

- [demo page](http://intuition.engineering/skills)

#### 2.1.1.2. Problem statement :

- In this post we shall tackle the problem of **extracting some particular information form an unstructured text.**

##### 2.1.1.2.1. Challenge

We needed to extract our users??? skills from their Curriculam Vitaes (CVs) even if they are written in an arbitrary way such as ???was deploying quantitative trading algorithms on production server???.

#### 2.1.1.3. Linguistic models

##### 2.1.1.3.1. unsupervised learning first

Modern linguistic models (ULMfit, ELMo) use unsupervised learning techniques such as creating RNNs embeddings on large texts corpora to gain some primal ???knowledge??? of the language structures before a more specific supervised training step.

##### 2.1.1.3.2. supervised learning later

In some cases on the contrary you need a model trained on a very specific and small dataset. These models possess nearly zero knowledge of the general linguistic structures and work only with special text features.

##### 2.1.1.3.3. supervised learning : small specific domain

A classic example would be a naive sentiment analysis tool for movie reviews or news datasets ??? the simplest working model could operate only with ???good??? or ???bad??? adjectives synonyms and some emphasising words presence. In our research we took advantages of both approaches.

#### 2.1.1.4. texts vectorization

Popular methods of texts vectorisation, such as tfidf, word2vec or GloVe models are using the whole document???s vocabulary to create its vector except of

1. Step 1: Stopwords removal
   stopwords (such as articles, pronouns, and other quite generic language elements bringing little semantic sense in such a statistical averaging procedure)

2. Step 2: Global word converstion : vectorization

<Global way : Convert each individual words into a unique vector >

Raise question : dont answer and think question

##### word2vec

https://www.tensorflow.org/tutorials/word2vec

##### GloVe

https://nlp.stanford.edu/projects/glove/
Introduction :

#### Specific task : extracting aspects from text

<Question: What is the key task>

<Answer: Extract high value text and the domain of the whole text known>

If there is a more specific task and you have some additional information about the texts corpus, you could probably **state that some information is more valuable than the other**.

For example, to perform some analysis on a corpus of cooking recipes it would be important to **extract ingredients or dish names classes** from the texts.
<Cooking recipes -> ingredients>

The other example is extracting professional skills from the CVs??? corpus. If we could vectorise each CV by relating it with a vector of extracted skills it would let us perform much more successful industry positions clustering, for example.
<Resume CV -> Skill words>
Skill words are vectorized .

#### Output Example

IMPORTANT

1.  INPUT :
2.  CV: Data scientist, hands on expertise in **machine learning**, **big data**, **development**, **statistics** and **analytics**. With my team of data scientists implemented **Python machine learning model ensembles**, **stacking**, and **feature engineering** demonstrating high accuracy rates in predictive analytics. Created a recommender system using Doc2Vec words embeddings and neural networks.

3) Output Extracted professional skills:
   machine learning, big data, development, statistics, analytics, Python machine learning model ensembles, stacking, feature engineering, predictive analytics, Doc2Vec, words embeddings, neural networks.

Key steps :
Stacking :
feature engineering
// ANCHOR now

#### Step 1: Parts of speech tagging

- As far as skills are mainly present in so-called noun phrases

- Build NLP POS tree :

  - Part of speech tagging method extracts noun phrases (NP) and builds trees representing relationships between noun phrases and the other parts of the sentence.

- Needs to define what is syntax structure of a noun entity :
  - Can be regex : For example : <DT>{0,1}<adj>{0,x}<N>{1,x}
  - NLTK : can extract NP ?

Input : sentences :
output : Noun Phrase :

Next : label NP : as : Skill vs Non-skill

#### Step 2: Deep learning architecture for candidates classification

##### Feature set design

Word vector contains:

1. binary feature :
   1. has number {0-0} : 1 mean has, 0 does not have
   2. has special char{#-+} : 1 has, 0 does not have
   3. Capitalisation of the first letter or of the whole word (SQL) :

Python3 : F0=1 ; F1=0 ; F3=1;
C++ : F0=0 : F1=1; F3=1
SQL : F0=0; F1=0 ;F3=1
foot : F0=0: F1=0; F3=0

4. F4: We also check if a word appears in the English language vocabulary and in some thematic lists such as names, geographical names, etc.
5. F5: . Usage of another binary feature describing presence of the popular English prefixes and suffixes in a candidate improved model???s performance up to 77.3%
6. F6 : And the addition of **one-hot vectors encoding parts of speech** to the models??? features set boosted our results to 84.6%
7. F7 : We used GloVe model vectors with 50 dimensions which improved our models??? performance up to 89.1% correct results on a test set.

##### Classification :

1. input layer 1 : Phrase :

   The first input layer takes a **variable** length **vector** comprised of the described above features of the candidate phrases which could have arbitrary number of words. This feature vector is processed with an LSTM layer.

   - <each word has Feature set of X dimension vector>
   - <variable length vector means word vector concatenation.>

Candidate phase :

- Natural language processing : [WF0 + WF1 + WF3 ]
- Java : WF0
- Neural network : WF0 + WF1

Question : if the rest is 0 : sh
if total length is 256 : will the result be 0 ?

2. input layer 2 : Context

For the given window size n we take n neighbouring words to the right and n words to the left of our candidate phrase, vector representations of these words are concatenated into the variable length vector and passed to the LSTM layer. We found that the optimal n=3.

n th word on the left + candidate phase + n th word on the right .

Responsible for Natural language processing in team

Responsible: WF-2
for : WF-1
[WF0 + WF1 + WF3 ]
in : WF4
team : WF5

WF-2 WF-1 [WF0 + WF1 + WF3 ] team : WF5

3. input layer 3 : Phase & Context

- Processes the vector with the **general information about the candidate phrase and its context**

- coordinatewise maximum and minimum values of word vectors in the phrase
- its context which, among the other information, represent the presence or absence of many binary features in the whole phrase.

The shape of the input vector :
<Core Quesition > important :
'''
I really confused with the input layers. what I have learned from the article is:
first layer: kinds of binary features(capitalization, appears in name dictionary , etc.) and word vectors
second layer: the same as first layer, but for context
third layer: a binary dense output to tell us whether each feature is 1 or 0
for example:
w-3, w-2, w-1, w0, w00, w1, w2, w3.
w-1,..w-3, w1,???w3 are context, w0,w00 are candidate phrase
features: first letter capitalized, occurrence of numbers, word in geographical dict,
w-3: 1 0 0
w-2: 0 0 1
w-1: 1 1 0
w0: 1 0 1
w00: 0 1 1
w1: 0 0 0
w2: 1 0 0
w3: 0 0 1
first layer: LSTM with w0, w00, t=2, [[1, 0, 1, 50dim w2v], [0, 1, 1, 50dim w2v]], input shape is (n, 2, 53)
second layer: LSTM with w-3, w-2, w-1, w1, w2, w3, t=6, ???, input shape is (n, 6, 53)
third layer: i don???t know how to compute it ???
so would u please explain that, many thks.
'''

the phase length can be 1, 2, 3: How to make it a input?

Shape the input layer :
https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/#:~:text=LSTM%20Input%20Layer,-The%20LSTM%20input&text=For%20example%2C%20below%20is%20an,and%20one%20Dense%20output%20layer.&text=In%20this%20example%2C%20the%20LSTM,layer%20must%20be%20three%2Ddimensional.

input layer is 3D format :

#### Results

## 2.2. Ref :

### 2.2.1. Paper 1 : Deep learning for specific information extraction from unstructured texts

1. using LSTM on the resume for skill words IMPORTANT

#### 2.2.1.1. - Website

- [Deep learning for specific information extraction from unstructured texts](https://towardsdatascience.com/deep-learning-for-specific-information-extraction-from-unstructured-texts-12c5b9dceada)
- [iki](https://iki.ai/)

#### 2.2.1.2. - Github

- [code](https://gist.github.com/IntuitionEngineering/a6e6e8a1f942a528c97e1d01af782ea2#file-skills_extract_nn-py)

#### 2.2.1.3. - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP1

demo page

### 2.2.2. Paper 2 : White paper ??? Job Skills extraction with LSTM and Word Embeddings

#### 2.2.2.1. - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP2

#### 2.2.2.2. - Website

- [White paper ??? Job Skills extraction with LSTM and Word Embeddings](https://medium.com/@nikkisharma536/white-paper-job-skills-extraction-with-lstm-and-word-embeddings-d71d1f96024f)

* [paper Job Skills extraction with LSTM and Word Embeddings]](https://confusedcoders.com/wp-content/uploads/2019/09/Job-Skills-extraction-with-LSTM-and-Word-Embeddings-Nikita-Sharma.pdf)
