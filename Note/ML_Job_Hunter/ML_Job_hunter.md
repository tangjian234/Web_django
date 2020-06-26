# [ML_Job_hunter.md]

- [ML_Job_hunter.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_hunter.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Sort and extend the plan [V_1][d_1]
  - [ ] [target](#vision)

## Progress

### Highlight

## Road map

## Topic:

## Vision

- Name : **Moby dick** :

  - Use Moby dick theme for each of the sub project

Moby dick themed
Cloud : what is general environment :
heat map :

Process :
Recommendation : according to resume :
resume aspects :
objective measurement of past history :
project attended :
each project as requirement for some tags
similar person have the qualification,
I have the qualification.

Career path planing : similarity recommendation .
in my career path, what is qualification I need to have .

arch : 25% have expert level of C++ skills.
PM :
Linkedin : 50% of a career has x degree , master degree.

Aspect : <tags: level>

A object : have x number of aspects:

B object : have y number of aspects :

how good is the matching.

What is the

## Objective

### Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI

### Key concepts

#### Aspects :

## System Overview

### Building block

1. **Crawler** :
   1. Crawler from web for amazon web pages.
2. **Classifier**
   1. Build System that Classify of Chinese name
3. **WebIO** :
   1. Chat bot :
   2. Answers :
   3. Use the job hunting and merging in.
   4. Data Visualization :
      1. Statistical Visualization.

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
