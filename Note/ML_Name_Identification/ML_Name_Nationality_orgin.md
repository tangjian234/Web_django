# 1. [Name Nationality ]

- [ML_Name_Nationality](file:///c:/Local/Work/ML_Name/Note/ML_Name_Nationality.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

- [x] Read [paper](#paper-1)
- [x] Sort the [Topic](#topic)
- [x] Design Name vs Non-Name [classifier](#classifier)
  - [ ] Single input dimension
  - [ ] Multiple input demission
- [ ] Add more key nationality
  1. Add indian and German/italy name/ jewish for nationality classifier . (1 hour )
  2. Change all word into latin :
     1. Japanese from Japanese word to Latin : ditto Korean.

## 1.2. Vision

## 1.3. Objective and Key Results

### 1.3.1. Objective

- Build a classifier to distinguish person’s name’s origin/country.

### 1.3.2. Key Results

- Define the process of ML NLP [done]
- Build a name classifier with key techs : [Done]
  - Beg of words text vectorization
  - scikit-learn : classifier : native bayes, SVM etc.
- Stream lit webapp page demo [done]

## 1.4. Summary

### 1.4.1. Evaluation

P1 :
<Pro> : Good data science project complete step by step

## 1.5. Key doc

    2. Algorithms, Key Howtos, block design , architecture

### 1.5.1. Web IO :

- [flask-chatterbot-master](c:\Local\Work\ML_Name\Code\flask-chatterbot-master\)

### 1.5.2. Engine

- [ML_classifer :](c:\Local\Work\ML_Name\Code\flask-chatterbot-master\ML_classifer_test.py)
- Both training and testing.

## 1.6. Progress

- Name identifier MVP ready

### 1.6.1. Highlight

## 1.7. Roadmap

## 1.8. Topic:

1. Name identifier

## 1.9. Use case :

1. Name identifier

- As a user , I can input a name string and get the nationality of the person.

2. Name identifier

- As a user , I can input a webpage and get the human names highlighted.

3. Aspect highlighter

- As a user , I can input an Amazon comment and highlight which aspect it is talking about. .

4. Statistical analysis and visualization

- As a user , I can know the statistics of a web page and have them visualized.

## 1.10. Vision

    - Publish a in medium : key machine learning websites.
    - End to end design , arch and implement a ML system to solve a topic of interest.
    - My pet project.

## 1.11. Objective

- To Ultimately answer Social science topic :
  - What is the percentage of Chinese Nationality in STEM topics.
  - Given a name, what is the personal's nationality :

### 1.11.1. Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI

### 1.11.2. Key concepts

#### 1.11.2.1. STEM Names :

- 1. Patents inventers
  2. Paper authors.
  3. Factually member in a STEM department. e.g University Cambridge

## 1.12. System Overview

### 1.12.1. Building block

1. **Crawler** :
   1. Crawler from web get the STEM names
2. **Classifier**
   1. Build System that Classify of Chinese name
3. **WebIO** :
   1. web I/Output and visualize Result
      1. Statistical percentage.

### 1.12.2. Key Technology

- 1. Use web-service as input/ output. (Azure website)
  2. Use Python as Language
  3. Use Azure machine learning backbone
  4. Use previous simplified crawler.
  5. Use Pattern recognition as Name Nationality Classifer.

### 1.12.3. Key principles

1. Make MVP first : Frame work first, Get more detail later .
2. how to Simplify, Well still keep the system integrity
3. Each component/Building block have a file

## 1.13. System Design Detail

### 1.13.1. Building block construction

#### 1.13.1.1. Crawler :

- Crawler from web get the STEM names, [DONE]
- Crawler from web get the STEM subjects ,

##### 1.13.1.1.1. Short vs Long term design

- Short Longer: Manual download 100 Chinese, standard mainland Mandarin : from different places.
- Long Term : Crawler download 100000 Chinese name from database, using web crawler.

##### 1.13.1.1.2. Input

NONE

##### 1.13.1.1.3. Output

- List of names
  - in Json format

#### 1.13.1.2. Classifier

     1. Build System that Classify of Chinese name vs other names [DONE]
     2.  Build System that Classify of  Name vs  None Names .

##### 1.13.1.2.1. Short vs Long term design

1. Chinese vs Non-Chinese

- Short Term: use the lookup table to search [DONE]
- Long Term : use classifier to check [DONE]

2. Name vs Non-Name :

- Short Term: use simple one dimension classsifer .
- Long Term : use classifier to check

##### 1.13.1.2.2. Input

##### 1.13.1.2.3. Output

#### 1.13.1.3. IO :

1. I/Output and visualize Result
   1. Statistical percentage.

- [ ] Good input/output UI :
  - [ ] Give a webpage : provide the statistic of the name in the webpage.
    - [ ] Web link :
  - [ ] Scan the Chinese name

##### 1.13.1.3.1. Input

- Input name , display the nationality:

##### 1.13.1.3.2. Output

- List of names e
  - in Json forma

Creation of Corpse
Crawler to Get the names of the paper :

- First author?

- Steps :

  - Recognition of chinese name ;
    - Simple : 100 Known Chinese name : Fixed
    - Complex : use NN LSTM to recognition of name :

End result :

- visualization
  - Power BI

Challenges :

- complex : how to step by step simplify a issue.
- simplify :

[------------------------------------------------------------------------------------------------------------------------------------]: #

## 1.14. Draft

### 1.14.1. Thought

1. Chinese Names

   - Short : Just Chinese vs non-Chinese
   - Long :

2. Corpse building :
   - Short Longer: Manual download 100 Chinese, standard mainland Mandarin // WPR
   - Long Term : Crawler download 100000 Chinese name from database

- LSTM ?

- Statistical :

# 2. Progress

import json

with open('data.txt') as json_file:
data = json.load(json_file)

### 2.0.2. Extract name-generation python. (15 min )

generate_name() DONE

### 2.0.3. Get the loca for german (15 min ) DONE

German de_DE
France fr_FR
Italy it_IT
hindi hi_IN
japense ja
https://stackoverflow.com/questions/3191664/list-of-all-locales-and-their-short-codes

### 2.0.4. Create 10000 German name : ( 15 min)

Done

# 3. generate_name_file('de_DE',10000,'a1.csv')

### 3.0.5. Create 10000 Indian name latin : ( 15 min)

http://mylanguages.org/hindi_romanization.php

### 3.0.6. Japan ense to latin :

- [Japanese Translator | RomajiDesu](http://www.romajidesu.com/translator)

### 3.0.7. N gram coporpose.

https://www.ngrams.info/
get ngram training examples.

### 3.0.8. digit predictor : LSTM training first.

1.5 hours.

### 3.0.9. To summerize

15 \* 10 Done and excellent : but a little

1. Misc prepare
   1. Extract name-generation python. (15 min )
   2. Get the loca for german (15 min )
2. Create 10000 German name : ( 15 min)
3. Create 10000 Indian name : ( 15 min)
4. Create 10000 Japanese Name : (latin) ( 15\*2 min)
5. Train and classification ( 15\*2 min)
6. Summary ( 15 \* 2 30 min )
7. REST

### 3.0.10. streamlit web app template

1. Search for the mult-page layout for Streamlit.
   target : can make flask like layout.
   top have options.
   about ext
   NLP town demo :
   https://twitter.com/nlptown/status/1204760675098206216/photo/1

- [NLP Town | Let your texts work for you](https://www.nlp.town/)

- [Ultimate Regex Cheat Sheet - KeyCDN Support](https://www.keycdn.com/support/regex-cheatsheet)

### 3.0.11. web app deployment :

Heroku

Active the account.
ashited. go to

866 404 1270
1820
Oct this year
2pm, Percific

## 3.1. Reference


