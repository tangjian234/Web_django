# [Name Nationality ]( C:\Local\Work\ML\Name Nationality.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Read [paper](#paper-1)

## Hub

<!-- // REVIEW  Hub view -->

- <Name Nationality>:
  - Master file : hub of the files
  - Contain :
- <Setup>:
  - Master file : hub of the files
  - Kick starter
  - Contain : Python, Azure, Web infrastructure readiness
- <Tech>:
  - Technology study, reading
  - Contain : ML technology
  - []()
- <Crawler>:
  - Crawler from web get the STEM names
  - Contain : ML technology
  - []()
- <Classifier>:
  - Classify of Chinese name
  - Contain : ML technology
  - []()
- <IO>:
  - web I/Output and visualize Result
  - Contain : ML technology
  - []()

## Vision

    - Publish a in medium : key machine learning websites.
    - End to end design , arch and implement a ML system to solve a topic of interest.
    - My pet project.

## Objective

- To Ultimately answer Social science topic : what is the percentage of Chinese Nationality in STEM topics.

### Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service :
  - Visualization : PowerBI

### Key concepts

#### STEM Names :

- 1. Patents inventers
  2. Paper authors.
  3. Factually member in a STEM department. e.g University Cambridge

## System Overview

### Building block

<!-- // REVIEW  Building block Overview -->

1. Crawler :
   1. Crawler from web get the STEM names
2. Classifier
   1. Build System that Classify of Chinese name
3. WebIO :
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

- Crawler from web get the STEM names,

##### Short vs Long term design

- Short Longer: Manual download 100 Chinese, standard mainland Mandarin : from different places.
- Long Term : Crawler download 100000 Chinese name from database, using web crawler.

##### Input

NONE

##### Output

- List of names
  - in Json format

#### Classifier

     1. Build System that Classify of Chinese name

##### Short vs Long term design

- Short Longer: use the lookup table to search
- Long Term :

##### Input

##### Output

#### IO :

     1. I/Output and visualize Result
        1. Statistical percentage.

##### Input

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
