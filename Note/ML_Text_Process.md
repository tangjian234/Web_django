# 1. ML_Text_Process.md

- [ML_Text_Process.md](file:///C:/Local/Work/ML_Name/Note/ML_Text_Process.md)
  [![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
  [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
  [![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

- [ML_Text_Process.md](#summarize-the-html-text-processing)

## 1.2. Vision

## 1.3. Objective

## 1.4. Concepts

### 1.4.1. POS

#### 1.4.1.1. noun phrase grammar

    - Noun (N)- Daniel, London, table, dog, teacher, pen, city, happiness, hope
    - Verb (V)- go, speak, run, eat, play, live, walk, have, like, are, is
    - Adjective(ADJ)- big, happy, green, young, fun, crazy, three
    - Adverb(ADV)- slowly, quietly, very, always, never, too, well, tomorrow
    - Preposition (P)- at, on, in, from, with, near, between, about, under
    - Conjunction (CON)- and, or, but, because, so, yet, unless, since, if
    - Pronoun(PRO)- I, you, we, they, he, she, it, me, us, them, him, her, this
    - Interjection (INT)- Ouch! Wow! Great! Help! Oh! Hey! Hi!

#### 1.4.1.2. CC: conjunction, coordinating

    - & 'n and both but either et for less minus neither nor or plus so
    - therefore times v. versus vs. whether yet

#### 1.4.1.3. CD: numeral, cardinal

    - mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
    - seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
    - fifteen 271,124 dozen quintillion DM2,000 ...

#### 1.4.1.4. DT: determiner

    - all an another any both del each either every half la many much nary
    - neither no some such that the them these this those

#### 1.4.1.5. EX: existential there

there

#### 1.4.1.6. IN: preposition or conjunction, subordinating

    - astride among uppon whether out inside pro despite on by throughout
    - below within for towards near behind atop around if like until below
    - next into if beside ...

#### 1.4.1.7. JJ: adjective or numeral, ordinal

- - third ill-mannered pre-war regrettable oiled calamitous first separable
  - ectoplasmic battery-powered participatory fourth still-to-be-named
  - multilingual multi-disciplinary ...

#### 1.4.1.8. JJR: adjective, comparative

- - bleaker braver breezier briefer brighter brisker broader bumper busier
  - calmer cheaper choosier cleaner clearer closer colder commoner costlier
  - cozier creamier crunchier cuter ...

#### 1.4.1.9. JJS: adjective, superlative

- - calmest cheapest choicest classiest cleanest clearest closest commonest
  - corniest costliest crassest creepiest crudest cutest darkest deadliest
  - dearest deepest densest dinkiest ...

#### 1.4.1.10. LS: list item marker

- - A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005
  - SP-44007 Second Third Three Two \* a b c d first five four one six three
  - two

#### 1.4.1.11. MD: modal auxiliary

- - can cannot could couldn't dare may might must need ought shall should
  - shouldn't will would

#### 1.4.1.12. NN: noun, common, singular or mass

- - common-carrier cabbage knuckle-duster Casino afghan shed thermostat
  - investment slide humour falloff slick wind hyena override subhumanity
  - machinist ...

#### 1.4.1.13. NNP: noun, proper, singular

- - Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
  - Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
  - Shannon A.K.C. Meltex Liverpool ...
-

#### 1.4.1.14. NNS: noun, common, plural

- - undergraduates scotches bric-a-brac products bodyguards facets coasts
  - divestitures storehouses designs clubs fragrances averages
  - subjectivists apprehensions muses factory-jobs ...
-

#### 1.4.1.15. PDT: pre-determiner

- - all both half many quite such sure this

#### 1.4.1.16. POS: genitive marker

' 's

#### 1.4.1.17. PRP: pronoun, personal

- - hers herself him himself hisself it itself me myself one oneself ours
  - ourselves ownself self she thee theirs them themselves they thou thy us
-

#### 1.4.1.18. PRP\$: pronoun, possessive

- - her his mine my our ours their thy your

#### 1.4.1.19. RB: adverb

- - occasionally unabatingly maddeningly adventurously professedly
  - stirringly prominently technologically magisterially predominately
  - swiftly fiscally pitilessly ...

#### 1.4.1.20. RBR: adverb, comparative

- - further gloomier grander graver greater grimmer harder harsher
  - healthier heavier higher however larger later leaner lengthier less-
  - perfectly lesser lonelier longer louder lower more ...
-

#### 1.4.1.21. RBS: adverb, superlative

- - best biggest bluntest earliest farthest first furthest hardest
  - heartiest highest largest least less most nearest second tightest worst
-

#### 1.4.1.22. RP: particle

- - aboard about across along apart around aside at away back before behind
  - by crop down ever fast for forth from go high i.e. in into just later
  - low more off on open out over per pie raising start teeth that through
  - under unto up up-pp upon whole with you

#### 1.4.1.23. TO: "to" as preposition or infinitive marker

- to

#### 1.4.1.24. UH: interjection

- - Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
  - huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
  - man baby diddle hush sonuvabitch ...

#### 1.4.1.25. VB: verb, base form

- - ask assemble assess assign assume atone attention avoid bake balkanize
  - bank begin behold believe bend benefit bevel beware bless boil bomb
  - boost brace break bring broil brush build ...

#### 1.4.1.26. VBD: verb, past tense

- - dipped pleaded swiped regummed soaked tidied convened halted registered
  - cushioned exacted snubbed strode aimed adopted belied figgered
  - speculated wore appreciated contemplated ...

#### 1.4.1.27. VBG: verb, present participle or gerund

- - telegraphing stirring focusing angering judging stalling lactating
  - hankerin' alleging veering capping approaching traveling besieging
  - encrypting interrupting erasing wincing ...

#### 1.4.1.28. VBN: verb, past participle

- - multihulled dilapidated aerosolized chaired languished panelized used
  - experimented flourished imitated reunifed factored condensed sheared
  - unsettled primed dubbed desired ...

#### 1.4.1.29. VBP: verb, present tense, not 3rd person singular

- - predominate wrap resort sue twist spill cure lengthen brush terminate
  - appear tend stray glisten obtain comprise detest tease attract
  - emphasize mold postpone sever return wag ...

#### 1.4.1.30. VBZ: verb, present tense, 3rd person singular

- - bases reconstructs marks mixes displeases seals carps weaves snatches
  - slumps stretches authorizes smolders pictures emerges stockpiles
  - seduces fizzes uses bolsters slaps speaks pleads ...
-

#### 1.4.1.31. WDT: WH-determiner

that what whatever which whichever

#### 1.4.1.32. WP: WH-pronoun

- that what whatever whatsoever which who whom whosoever

#### 1.4.1.33. WRB: Wh-adverb

how however whence whenever where whereby whereever wherein whereof why

## 1.5. HTML

### Download one link single file into clipboard

<T- _10 min> <GOLD> <P1>

#### What

- - 1. Copy the link into clipboard 
  - 2. Run web.ps1
  - 3. Get the content as a md file in clipborad

#### Content

- - 1. get_webpage_content

#### Result

- - - [get_web_content.py]
    - [web.ps1]
    - [ML_Text_Process.md](#download-one-link-single-file-into-clipboard)


### 1.5.1. Summarize the html text processing

- [ ] Form a python function:

#### 1.5.1.1. what

- Finish organizing the article download
- use Different ways to get plain text from a html file

  - BeautifulSoup()
  - Browser()
  - html2text

#### web_lib

###### 1.5.1.2.1. web_lib : download_link_article()

- - -  use article lib to read a html 

###### 1.5.1.2.1. web_lib : link_title()

- - -  use Browser to read a html title 

###### 1.5.1.2.1. web_lib :  get_google_search_result()

- - - Google API to get link list

###### 1.5.1.2.1. web_lib : clip_board_get_url()

- - - Put url into clip board

#### bs_lib

##### 1.5.1.2.1. bs_lib : get_html_info()

- - - - use of BeautifulSoup :
    - get chunk of text, without markdown.

##### 1.5.1.2.2. bs_lib: : get_html_info_html2text

- - - - use of html2text :
      - get chunk of text, with markdown, good for streamlit





### Download review article 

review.ps1 : 'best review bluetooth speaker' 1
Function : download <number_of_search_items> with <search_item>

#### Master file I/O :

- - 1. input :
       1. search_item: 'best review bluetooth speaker'
       2. number_of_search_items : 1
    1. output :
       1. directory :
          1. C:/Local/Work/ML_Name/Code/Test/data/review_article/best_review_bluetooth_speaker/
       2. files :
          1. link_list_file : Link_list_best_review_bluetooth_speaker_1.json
          2. link_content_file: Best_Bluetooth_speakers_2020_portable_speakers_for_any_budget_TechRadar.json

#### ML_review_article_download.py steps : 

- - 1. Get command line input
    2. Build the output target search_item_dir
    3. Build the link_list_file name
    4. Use google search API: get_google_search_result() get link_list
       1. link_list is the `search result urls list`
    5. Save link_list into link_list_file
    6. Download each url into format : use `html2text` lib
       1. rank
       2. title
       3. url
       4. text_content : `in markdown format`

#### 1.5.1.3. Result

- [ML_review_article_download.py]
- [ML_Text_Process.md](#151-summarize-the-html-text-processing)

## 1.6. NLP tasks :

### 1.6.1. Noun Phrase Chunking

#### 1.6.1.1. Spacy_lib.py

    noun_phrase_generator_spacy(sent)
        - Func: Use spacy to NP generation
        - Return : list of NP in a sentence

#### 1.6.1.2. NLTK_lib.py

    noun_phrase_generator_nltk(sent)

    - Func: Generate noun phrase using nltk chunker
    - Return : list of NP in a sentence

      Use grammar :
       NP = "NP: {(<V\w+>|<NN\w?>|<JJ\w?>)+.*<NN\w?>}"

### 1.6.2. Part of speech tagging

#### 1.6.2.1. Spacy_lib.py

    pos_spacy(sent)

#### 1.6.2.2. NLTK_lib.py

    pos_nltk(sentence):

### 1.6.3. Sematic similarity

#### 1.6.3.1. Spacy_lib

     word_similarity_distance()

### 1.6.4. Visualization

### 1.6.5. Spacy_lib.py

    displacy_spacy

### 1.6.6. Classification

- (Naive Bayes, Decision Tree)

### 1.6.7. Sentiment analysis

### 1.6.8. Tokenization

- (splitting text into words and sentences)

### 1.6.9. Word and phrase frequencies

### 1.6.10. Parsing

### 1.6.11. n-grams

### 1.6.12. Word inflection

(pluralization and singularization) and lemmatization

### 1.6.13. Spelling correction

### 1.6.14. Add new models or languages through extensions

### 1.6.15. WordNet integration

## 1.7. String operations:

- get_embed(string,begin,end)

## 1.8. Reference

- [NLP_study.md](file:///C:/Local/Work/Python/Note/NLP/NLP_study.md)

### 1.8.1. POS tags

- [What are all possible pos tags of NLTK?](https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk)
