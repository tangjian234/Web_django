# ML_Name_Identification.md

- [ML_Name_Identification.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification.md)

- [![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
  [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
  [![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

- [ ] Check text topic extraction.
- [ ] - select list and NER [highlighter](#add-mark-to-html-file)

## Topic:

- Name identifier : NER : name entry recognition .
- Noun phrase Identification
- web statistical summary.

## Progress

[28-06]

- MVP is Done, NER is Recognized and highlighted; to be Summarized.
- Next : Identify the noun phrase.
- to be Complete the future work.(web Statistical work)

### Highlight

## Use case :

- As a user , I can automatically highlight the personal names of a webpage [Done]

- As a user, I can see the important noun phrase of a text. [Topic extraction]

- As a user , I can know the statistics of a web page and have them visualized.

## Vision

- Ability to process webpage and give webpage information summary.
- First step of web information summery service.
- Webpage highlighting.

## Road map

- One week from now : 24-06 MVP DONE and excess the

## Future

### Noun Phrase

### Web page

#### Web page information summary service :

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
      Other information of statistical analysis .

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

### Name entry recognition (NER)

- Input : webpage
- highlighted
- use article to get webpage text content
- use spacy for NER

#### Result :

- ML_Master.py: Name entry recognition section of
- name_entity_reco.py: C:\Local\Work\ML_Name\Code\Lib\name_entity_reco.py
  - nlp_text = ner.Get_html_text(message)

#### Crawler :

NONE : already trained.

#### Classifier

- use spacy : C:\Local\Work\ML_Name\Code\Lib\name_entity_reco.py
- get_person_name()

##### Input : webpage

### use article to extract key words.f

##### Output

#### IO :

- Display hightlighted marked up:
  - \*\*\*\* as highlighter
- use the markup

##### add mark to html file

urllib.request.urlretrieve("http://www.example.org/", "webpage.html")
st.write

### add the UI component

- selector list and NER highlighter

### Noun phase

- [ ] ### What is NP :

- [Noun Phrases Examples](https://www.softschools.com/examples/grammar/noun_phrases_examples/65/#:~:text=The%20other%20words%20modify%20the,I%20want%20a%20skate%20board.)

#### Crawler :

##### Input

##### Output

#### Classifier

##### Input

##### Output

#### IO :

##### Input

- Input name , display the nationality:

##### Output

### Webpage statistic

- Web Statistic according to spacey:

1. Find how many persons's of each nationality belong to
2. 2 are chinese and 3 are english.

## Reference

#### Python (NLTK) - more efficient way to extract noun phrases?

- [extract noun phrases](https://stackoverflow.com/questions/49564176/python-nltk-more-efficient-way-to-extract-noun-phrases)

#### How To Easily Recognize People’s Names In A Text

- [How To Easily Recognize People’s Names In A Text](https://thetokenizer.com/2013/08/25/how-to-easily-recognize-peoples-names-in-a-text/)

use google search to verify .

- [freebase](https://developers.google.com/freebase)

#### traditional NER use the spacy.

- [Named Entity Recognition with NLTK and SpaCy](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da#:~:text=Named%20entity%20recognition%20%28NER%29is%20probably%20the%20first%20step,can%20help%20answering%20many%20real-world%20questions%2C%20such%20as%3A)

https://spacy.io/usage/linguistic-features
https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da#:~:text=Named%20entity%20recognition%20%28NER%29is%20probably%20the%20first%20step,can%20help%20answering%20many%20real-world%20questions%2C%20such%20as%3A

- [Evaluation in a Spacy NER model](https://stackoverflow.com/questions/44827930/evaluation-in-a-spacy-ner-model)

Articles

- [Scrape and Summarize News Articles in 5 Lines of Python Code](https://towardsdatascience.com/scrape-and-summarize-news-articles-in-5-lines-of-python-code-175f0e5c7dfc)

* [news site 1](https://finance.yahoo.com/)

* [news site 2](https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020)
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

- [Python by Examples](http://python.omics.wiki/www/download-webpage)
