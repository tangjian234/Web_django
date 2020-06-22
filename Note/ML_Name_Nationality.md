# [Name Nationality ]

- [ML_Name_Nationality](file:///c:/Local/Work/ML_Name/Note/ML_Name_Nationality.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [x] Read [paper](#paper-1)
- [x] Sort the [Topic](#topic)
- [x] Design Name vs Non-Name [classifier](#classifier)
  - [ ] Single input dimension
  - [ ] Multiple input demission
- [ ] Add more key nationality
  1. Add indian and German/italy name/ jewish for nationality classifier . (1 hour )
  2. Change all word into latin :
     1. Japanese from Japanese word to Latin : ditto Korean.

## Key doc

### Web IO :

- [flask-chatterbot-master](c:\Local\Work\ML_Name\Code\flask-chatterbot-master\)

### Engine

- [ML_classifer :](c:\Local\Work\ML_Name\Code\flask-chatterbot-master\ML_classifer_test.py)
- Both training and testing.

## Progress

- Name identifier MVP ready

### Highlight

## Roadmap

## Topic:

1. Name identifier

## Use case :

1. Name identifier

- As a user , I can input a name string and get the nationality of the person.

2. Name identifier

- As a user , I can input a webpage and get the human names highlighted.

3. Aspect highlighter

- As a user , I can input an Amazon comment and highlight which aspect it is talking about. .

4. Statistical analysis and visualization

- As a user , I can know the statistics of a web page and have them visualized.

## Vision

    - Publish a in medium : key machine learning websites.
    - End to end design , arch and implement a ML system to solve a topic of interest.
    - My pet project.

## Objective

- To Ultimately answer Social science topic :
  - What is the percentage of Chinese Nationality in STEM topics.
  - Given a name, what is the personal's nationality :

### Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI

### Key concepts

#### STEM Names :

- 1. Patents inventers
  2. Paper authors.
  3. Factually member in a STEM department. e.g University Cambridge

## System Overview

### Building block

1. **Crawler** :
   1. Crawler from web get the STEM names
2. **Classifier**
   1. Build System that Classify of Chinese name
3. **WebIO** :
   1. web I/Output and visualize Result
      1. Statistical percentage.

### Key Technology

- 1. Use web-service as input/ output. (Azure website)
  2. Use Python as Language
  3. Use Azure machine learning backbone
  4. Use previous simplified crawler.
  5. Use Pattern recognition as Name Nationality Classifer.

### Key principles

1. Make MVP first : Frame work first, Get more detail later .
2. how to Simplify, Well still keep the system integrity
3. Each component/Building block have a file

## System Design Detail

### Building block construction

#### Crawler :

- Crawler from web get the STEM names, [DONE]
- Crawler from web get the STEM subjects ,

##### Short vs Long term design

- Short Longer: Manual download 100 Chinese, standard mainland Mandarin : from different places.
- Long Term : Crawler download 100000 Chinese name from database, using web crawler.

##### Input

NONE

##### Output

- List of names
  - in Json format

#### Classifier

     1. Build System that Classify of Chinese name vs other names [DONE]
     2.  Build System that Classify of  Name vs  None Names .

##### Short vs Long term design

1. Chinese vs Non-Chinese

- Short Term: use the lookup table to search [DONE]
- Long Term : use classifier to check [DONE]

2. Name vs Non-Name :

- Short Term: use simple one dimension classsifer .
- Long Term : use classifier to check

##### Input

##### Output

#### IO :

1. I/Output and visualize Result
   1. Statistical percentage.

- [ ] Good input/output UI :
  - [ ] Give a webpage : provide the statistic of the name in the webpage.
    - [ ] Web link :
  - [ ] Scan the Chinese name

##### Input

- Input name , display the nationality:

##### Output

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

## Draft

### Thought

1. Chinese Names

   - Short : Just Chinese vs non-Chinese
   - Long :

2. Corpse building :
   - Short Longer: Manual download 100 Chinese, standard mainland Mandarin // WPR
   - Long Term : Crawler download 100000 Chinese name from database

- LSTM ?

- Statistical :

# Progress

import json

with open('data.txt') as json_file:
data = json.load(json_file)


### Extract name-generation python.  (15 min )
generate_name() DONE

### Get the loca for german (15 min ) DONE
German de_DE
France fr_FR
Italy it_IT
hindi hi_IN
japense ja
https://stackoverflow.com/questions/3191664/list-of-all-locales-and-their-short-codes

###  Create 10000 German name : ( 15 min)
Done 
#generate_name_file('de_DE',10000,'a1.csv')

### Create 10000 Indian name latin  : ( 15 min)
http://mylanguages.org/hindi_romanization.php