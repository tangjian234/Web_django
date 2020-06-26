# ML_Name_Identification.md

- [ML_Name_Identification.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification.md)

- [![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
  [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
  [![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

## Topic:

- Name identifier

## Progress

### Highlight

## Use case :

- As a user , I can automatically highlight the personal names of a webpage
- As a user , I can input a webpage and get the human names highlighted.

## Vision

- Ability to process webpage and give webpage information summary.
- First step of web information summery service. // STUB : x1 create full package scaffolding.
- Webpage highlighting.

## Road map

- One week from now : 24-06

## Future :

### use case  
As a user , I can know the statistics of a web page and have them visualized.

- Web page information summary service :
  - key info of webpage :
    - Title :
    - topic :
    - key words list :
      - tags :
    - Categorization :
      - tags :
    - summary text :
      - paragraph level
    - Key information list
      - names : name nationality etc.
      - digits :
        Other information of satisitical anlaysis .

## Objective and key result

### Knowledge learnt

### Key concepts

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
