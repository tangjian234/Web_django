# ML_Amazon_Train_Extract_skill_from_CV.md

- [ML_Amazon_Train_Extract_skill_from_CV.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_Train_Extract_skill_from_CV.md)

* [![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
  [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
  [![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)


## Structure

### Parent
  - [Master](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)  
  - [mm.md](file:///C:/Local/Work/Key_Tools/Note/mm.md) 
  - [ML_todo.md](file:///C:/Local/Work/Key_Docs/Todo/ML_todo.md)
    
### Son 

##### Amazon

  - [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)  
 - [ML_Amazon_Train_Extract_skill_from_CV.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_Train_Extract_skill_from_CV.md)  
  - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) 

## Todo
  - [ ] review and understand use LSTM to extract skill words from resume for
  - [∞](#211-using-lstm-on-the-resume-for-skill-words)

## Vision

## Objective

## Content

### 2.1.1. Using LSTM on the resume for skill words

- [paper](#paper-1--deep-learning-for-specific-information-extraction-from-unstructured-texts)

#### 2.1.1.1. Introduction

- [iki project](https://iki.ai/)

- [demo page](http://intuition.engineering/skills)

#### 2.1.1.2. Problem statement :

- In this post we shall tackle the problem of **extracting some particular information form an unstructured text.**

##### 2.1.1.2.1. Challenge

We needed to extract our users’ skills from their Curriculam Vitaes (CVs) even if they are written in an arbitrary way such as “was deploying quantitative trading algorithms on production server”.

#### 2.1.1.3. Linguistic models

##### 2.1.1.3.1. unsupervised learning first

Modern linguistic models (ULMfit, ELMo) use unsupervised learning techniques such as creating RNNs embeddings on large texts corpora to gain some primal “knowledge” of the language structures before a more specific supervised training step.

##### 2.1.1.3.2. supervised learning later

In some cases on the contrary you need a model trained on a very specific and small dataset. These models possess nearly zero knowledge of the general linguistic structures and work only with special text features.

##### 2.1.1.3.3. supervised learning : small specific domain

A classic example would be a naive sentiment analysis tool for movie reviews or news datasets — the simplest working model could operate only with “good” or “bad” adjectives synonyms and some emphasising words presence. In our research we took advantages of both approaches.

#### 2.1.1.4. texts vectorization

#### 2.1.1.5. Specific task : extracting aspects from text

Key steps :

Stacking :
feature engineering

// ANCHOR now

#### 2.1.1.7. Step 1: Parts of speech tagging

See [Concepts]()

- As far as skills are mainly present in so-called noun phrases

- Build NLP POS tree :

  - Part of speech tagging method extracts noun phrases (NP) and builds trees representing relationships between noun phrases and the other parts of the sentence.

- Needs to define what is syntax structure of a noun entity :
  - Can be regex : For example : <DT>{0,1}<adj>{0,x}<N>{1,x}
  - NLTK : can extract NP ?

Input : sentences :
output : Noun Phrase :

Next : label NP : as : Skill vs Non-skill

#### 2.1.1.8. Step 2: Deep learning architecture for candidates classification

see

##### 2.1.1.8.1. Feature set design

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
5. F5: . Usage of another binary feature describing presence of the popular English prefixes and suffixes in a candidate improved model’s performance up to 77.3%
6. F6 : And the addition of **one-hot vectors encoding parts of speech** to the models’ features set boosted our results to 84.6%
7. F7 : We used GloVe model vectors with 50 dimensions which improved our models’ performance up to 89.1% correct results on a test set.

##### 2.1.1.8.2. Classification :

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
w-1,..w-3, w1,…w3 are context, w0,w00 are candidate phrase
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
second layer: LSTM with w-3, w-2, w-1, w1, w2, w3, t=6, …, input shape is (n, 6, 53)
third layer: i don’t know how to compute it …
so would u please explain that, many thks.
'''

the phase length can be 1, 2, 3: How to make it a input?

Shape the input layer :
https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/#:~:text=LSTM%20Input%20Layer,-The%20LSTM%20input&text=For%20example%2C%20below%20is%20an,and%20one%20Dense%20output%20layer.&text=In%20this%20example%2C%20the%20LSTM,layer%20must%20be%20three%2Ddimensional.

input layer is 3D format :

#### 2.1.1.9. Results

## Reference
