# [ML_Finance_Insight.md]

- [ML_Finance_Insight.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight.md)

- [![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
  [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
  [![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Sort the name websites : axriv
- [ ] Sort the current doc : remove the

## Progress

- Name Nationality MVP ready
-

### Highlight

**Output** : Classifer : C:\Local\Work\ML_Name\Code\Lib\name_nationality.py

## Roadmap

- one day to complete the summary of work

## Topic:

1. Name Nationality

## Use case :

- As a user, I can get the nationality of the person by given a list of names,
- As a user , I can input a name string and get the nationality of the person.

## Vision

## Objective

- Given a name, what is the personal's nationality :

- Together with name identification , to ultimately answer Social science topic :
  - What is the percentage of Chinese Nationality in STEM topics.

### Knowledge learnt

- Key framework of ML process :

  1. - Problem statement : define key parameter of the work
  2. - Raw data Crawler : obtain .
  3. - Data preparation : data cleaning, conversion :
  4. - Classification : using classifier such as SVM and LSTM for training and testing,
  5. - Visualization : visualize the end result in webapps .

- Text vectorization via beg of words
- Stream lit based webapp Data visualization

### Key process parameter definition :

#### Raw data Crawler :

- Generate data for bootstrap

- Use python faker to create 10000 names for key nationalities .
  - Japanese, Hindi, German, Italy,
- [Crawler.md]

#### Data preparation :

- Converted every names into latin format :

  - Japanese, Hindi, Chinese
  - [Data_preparation.md]

File data reading format :
configure file
[]
:
csv file

#### Classification:

1.  Use scikit-learn to train

    https://scikit-learn.org/stable/

4) List of current languages are : 1.

### Key File used and parameters.

- [Main_file]

  - C:\Local\Work\ML_Name\Code\Test

- [Data]

  - C:\Local\Work\ML_Name\Code\Test\data

- [Configuration]

  - CONF_FILE = 'C:\Local\Work\ML_Name\Code\Test\ML_classifer_ger_ita.cfg'

- [List_of_languages]

      [
          0:"Chinese (China)"
          1:"French"
          2:"German (Germany)"
          3:"Hindi (India)"
          4:"Italian (Italy)"
          5:"Japanese (Japan)"
          6:"Norwegian"
          7:"Portuguese (Brazil)"
          8:"Russian"
          9:"Spanish (Spain)"
          10:"UK English"
          11:"US English"
      ]

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

##### UI of the existing interface :

cosmetic :

1. best color for text for a chatbot ?
   <Question: what is the optimail interface for the >

<Answer: no color so fa >

Generate data for bootstrap

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
