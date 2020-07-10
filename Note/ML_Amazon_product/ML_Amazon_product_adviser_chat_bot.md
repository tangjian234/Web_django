# 1. [ML_Amazon_product_adviser_chat_bot]

- [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product_adviser_chat_bot.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

- [ ] Sort and extend the plan [V_1][d_1]
- [ ] Work on basic information extraction first
  - [ ] [target](#vision)
- [ ] Read the most important
  - [ ] [paper](#paper-1--deep-learning-for-specific-information-extraction-from-unstructured-texts)
- [ ] Named Entity Recognition : use spacy to train aspect ?

## 1.2. Vision

- Name : **Genie** :

  - Use aladdin theme for each of the sub project
  - Chat bot on amazon search , help user to make wise decision while shoping

## 1.3. Objective

### 1.3.1. Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI
  - language processing :
  - product data mining and analysis

### 1.3.2. Key benefit :

      - My pet project
      - Beneficial to the financial insight project

### 1.3.3. What is not todo :

    - Sub optimization :
    - build a MVP : for each component:
    - make the whole things work first.

-

### 1.3.4. Key concepts

#### 1.3.4.1. Aspects :

## 1.4. High level Work Plan

### 1.4.1. Basic Amazon product work

### 1.4.2. Product basic information extraction

      1 Extract key information from product. :
         - price. title listing.
         - history

### 1.4.3. Product time dimension monitoring

      - time dimension monitoring :
        - giving a product code, change across time. (price , rank , comment. )
      - automatically check every day.
      - Graph : Data structure of Amazon project

### 1.4.4. Statistical analysis :

    1. Most frequent meaningful bi-words.
    2. Most mentioned meaningful model :

### 1.4.5. Build product graph

## 1.5. Key docs and data structure:

### 1.5.1. Key python files.

- - 1.  [ML_master.py] :
        - Running the streamlit based web UI :
    2.  [ML_amazon_best_seller.py] :
        - given search term: get the top 100 best seller.
    3.  [ML_amazon_listing_download.py] :
        - download file given a list of asin : use bs_lib.get_amazon_product_info(asin)
    4.  [amazon_product_dictionary.py] :
        - processing and matching production dictionary vs asin product info -

### 1.5.2. Key md files.

- - 1.  [ML_Amazon_product_adviser_chat_bot.md]: master file :
    2.
-
- -
- :

### 1.5.3. Key data structure

#### 1.5.3.1. asin list

[detail](#1331-asin-list)

##### 1.5.3.1.1. Format

`asin_list_file.json`

    format :
    {
    "1": "B0742BV75P",
    "2": "B0719M4YZB",
    ...
    }

##### 1.5.3.1.2. Example

- [asin_list_file.json](file:///C:/Local/Work/ML_Name/Code/Test/asin_list_file.json)
- [bluetooth+speaker.json](file:///C:/Local/Work/ML_Name/Code/Test/data/best_seller/bluetooth+speaker.json) : output of the best_seller scraping

#### 1.5.3.2. Asin information dictionary

- [detail](#1332-asin-information-dictionary)

##### 1.5.3.2.1. Format

      {
      "ASIN": "B07ZRVX6RM",
      "title": """,
      "feature_list": [
      ],
      "price": "",
      "rating": ",
      "no_of_comments": "",
      "producer": "",
      "best_seller_rank": "",
      "date_first_available": ""
      }

##### 1.5.3.2.2. Example

- [B07ZRVX6RM.json](file:///C:/Local/Work/ML_Name/Code/Test/data/asin/B07ZRVX6RM.json)

#### 1.5.3.3. Product Dictionary :

- [detail](#1333-product-dictionary-)

##### 1.5.3.3.1. What

- Provide aspects ->

##### 1.5.3.3.2. Format

- - - get empty place to fill
      "feature_list": {
      "sound": {},
      "connectivity": {},
      "battery": {}
      }

##### 1.5.3.3.3. Example

- [bt_speaker_product_dictionary.json](file:///C:/Local/Work/ML_Name/Code/Test/data/bt_speaker_product_dictionary.json)

## 1.6. Work Completed

### 1.6.1. Summary

- - 1. Scrap top 100 bluetooth listing and get 100 asin list. e.g 'bluetooth+speaker'
    2. Scrap each asin , get asin information dictionary
    3. Match product dictionary with asin information dictory

### 1.6.2. scrap top 100 bluetooth listing.

`ML_amazon_best_seller.py`

#### 1.6.2.1. Summary : - get the top 100 best seller.

##### 1.6.2.1.1. Input :

- - 1. given search term: 'bluetooth+speaker'

#### 1.6.2.2. Output

- - 1. Output dir : ASIN_OUT_DIR = 'C:/Local/Work/ML_Name/Code/Test/data/best_seller/'
    2. list of asin file : same format as
       1. [detail](#1331-asin-list)

    `asin_list_file.json`

          format :
          {
          "1": "B0742BV75P",
          "2": "B0719M4YZB",
          ...
          }

#### 1.6.2.3. Implementation

- - 1. build google search page : build_google_search_page()
    2. Get 50 best seller asin for a best seller page : get_a_page_best_seller_asin(soup):
    3. get 100 best seller : get_best_seller_asin(Amazon_best_seller_page)
       1. get first 50 seller
       2. get next page link
       3. get next 50

### 1.6.3. Product Info crawling and display :

#### 1.6.3.1. Amazon product asin list :

- - 1.  Get amazon web product name list

`product_id_list_file.json`
format :  
 {
"1": "B0742BV75P",
"2": "B0719M4YZB",
...
}

#### 1.6.3.2. Scraping of key infos of one listing's Asin

`bs_lib.py : get_amazon_product_info()`

##### 1.6.3.2.1. Key product information

- - 1.  Price.
    2.  rating
    3.  producer
    4.  first comment time [later]
    5.  total comment:

##### 1.6.3.2.2. Implementation : bs_lib.py : get_amazon_product_info()

- - - input : asin id
    - Output :
      - product info : dictionary json file
      - output_dir : 'C:/Local/Work/ML_Name/Code/Test/data/asin/'

#### 1.6.3.3. Scrap a list of asin :

`ML_amazon_listing_download.py`
`amazon_product_dict = bs_lib.get_amazon_product_info(asin)`

- - 1. input : list is in `product_id_list_file.json`
    2. Output : Go though and scrap and save in output_dir :
       1. 'C:/Local/Work/ML_Name/Code/Test/data/asin/'

#### 1.6.3.4. Display in streamlit

- [ML_master.py]

##### 1.6.3.4.1. called in :

- - - ML_master.py : given a web interface :
    - - input text box : asin id
    - - output : scrap that asin and display product info

### 1.6.4. product dictionary creation

// ANCHOR now

#### 1.6.4.1. Product dictionary data

- [detail](#1333-product-dictionary-)

##### 1.6.4.1.1. Format

- - - get empty place to fill
      "feature_list": {
      "sound": {},
      "connectivity": {},
      "battery": {}
      }
- [bt_speaker_product_dictionary.json](file:///C:/Local/Work/ML_Name/Code/Test/data/bt_speaker_product_dictionary.json)

### 1.6.4. product dictionary vs asin info
 #### Hard matching : 
- **classify each feature list title : belong to which aspect**
  - if the keyword of the aspect is in the feature list title 
- Example :
  
## 1.7. Work: Next steps

### Plot radar diagram :

- [](#aspect-score-visualization-)

### 1.7.1. Scrap 100 bluetooth tech article

// STUB

### 1.7.2. Highlighting the product dictionary in the content.

1.  to find the feature component locations
2.  important. bootstrap.

// STUB

### 1.7.3. side by side comparison of aspect.

- P1 listing line on connectivity
- P2 listing line on connectivity

Comparing of price:

- price range and aspect

  - price from 10-20 usd : percentage have feature x.

    4.coverage of product dictionary of the listing. which one is taged and which one does not.

### 1.7.4. detection of noun phrase in title :

which of the noun phrase is
how to train a more accurate noun phrase.

### 1.7.5. publish in a web-hosting. take input .

### 1.7.6. study amazon API

## 1.8. Use case and User experience :

### 1.8.1. Generic

- As a user , I can input an Amazon comment and highlight which aspect it is talking about. .
- As a suer : I want to know what is most effective shopping strategy.

### 1.8.2. User experience Example : Bluetooth speaker purchasing

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

### 1.8.3. User experience and scenario : microphone purchasing

1. Use microphone, nice example.
2. what is the general landscape
   1. price range.
   2. what kind of **sub category** microphone we have :
      1. price range of each sub category
      2. pro and cons :
         1. effective description.
   3. what the most important key characters?
      1. task : KC identification :
         1. see `by features`
   4. for each of the key character deminsion, what is most recommended product.
      1. branded product (high end )
      2. Sound quality. best
      3. bluetooth range.
         1. best connectivity product. (hard parameter):
         2. 1. hard parameter : distance.
   5. How does the some recommended products comparing using the matrics of key characters ?
      1. see `Compare with similar items` in a product
         1. B01MTB55WH
      2. critics for it is too simple. And that's less informative..
      3. three points need to be vastly improved to be more Informative and useful :
         1. `Read reviews that mention`
         2. `By feature`
         3. `Compare with similar items`

## 1.9. Core Ideas

### 1.9.1. Noun phrase extraction

- - 1.  Highlight Noun phrase in an article

### 1.9.2. Aspect Extraction and matching

#### 1.9.2.1. the Aspect evaluation : Scores :

- Assumption:

  1. Limited: expert knowledge guided first :

  - - For bluetooth earpiece :
      the Aspect/Topic is concrete and known :

    - - A1 : Connectivity :
      - A2 : Sound Quality :
      - A3 : Battery life :

Total score = weighted score of the aspect: - radar diagram :
In all the listing:

##### Aspect score Visualization :

- Radar diagram

#### 1.9.2.1. the Aspect, NP matching.

##### Objective

define and match the NP with aspects

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

#### 1.9.2.2. apsect creation

1. first line of each listing : generate the aspects words

   1. sound
   2. price
   3. water proof

2. for each of the aspect words , tag the review article .
3. tag the comment according to aspect words.

issue : the accuracy of spacy is not good . see the example

task :
color tag the html according to identified words.'s identify (person etc)

aspect dictionary . : what are the feature to be considered when selecting :

### 1.9.3. Product dictionary definition.

- build keywords then build structure.

- Expected result, : Product key aspect dictionary

#### 1.9.3.1. Activity.

- 1. Load json file

  - load_product_listing_json

  1. Generate Product dictionary json file

     - load_product_dictionary_json

  - keywords :

- 1. match and tag aspects into each listing sentences. **One last sentence. One aspect.**
  2. Highlight the key word match
  3. Give each aspect feature a value/discription.
     1. bass : 'xx sentence'
     2. waterproff : 'IPX'

#### 1.9.3.2. Product dictionary data structure

product hieratically key aspect structure. Object oriented.

- Product dictionary <PD>

  - key aspect <KA>
    - Key words <KW>
    - Key characters <KC>

  1.  Product dictionary contain key aspects.
  2.  Key aspects contain keywords and key characters
      1.  **Key aspect contain keywords that describe/characterize the key aspect.** can be further breakdown into structures.


        Example :
          Bluetooth speaker <PD> : {
               Sound<KA> : {
                 key words list [KW]: [Range,bass, stereo]
                 Sound spectrum range <KC>  : {
                     - bass,
                     - middle
                     - high
                 }
                 volume <KC>:
                   - loudness
               },
                Connectivity<KA> : {

                }
          }

- [Audio Spectrum](https://www.teachmeaudio.com/mixing/techniques/audio-spectrum)

##### 1.9.3.2.1. bluetooth speaker aspection dictionary

https://www.outeraudio.com/portable-bluetooth-speakers/

"key factors"

- size :
- connectivity
- Sound
  - Sound Quality:
  - mid
  - low
  - bass, whoffer
- Portability (more on that below)
- Design
  - Design Quality and Materials
- Waterproof
  - Waterproof Ratings and Durability
- Battery
  - Battery Life
- Connectivity
- Bluetooth Range and Connectivity
- price
  - Value for Money

bluetooth product will have + connectivity

object inheritance : tree.

Postive noun :
negative noun : negative sentense .

1.  object oriented relationship : **key aspect belong a a category of devices,**

    1.  all bluetooth device has
        1.  connectivity
        2.  battery
        3.  charger
        4.  water proof
    2.  all product has **price** aspect
    3.  all speaker has **sound quality** aspect.

### 1.9.4. Feature extraction

    1. Some features is known should have stronger discriminative power by expert knowledge

    2. How to weight : sequential classifier. (Heavy weight of expert knowledge.vs machine learning.)
      -  some name have strong indication of nationality :
        1) e.g ginsberg is a jewish name.
        2) Li is a chinese name.

### 1.9.5. Feature indictor location vs key aspect.

Identify and potential feature component location :

feature component :  
 Have the power to discriminate between the 2 classes :

Expert knowledge:
Bluetooth : key aspect :

- Key aspect word is in a certain location, these location/Feature indict if it is a key aspect.

- Key aspect and the feature component. Reverse bootstrap,

  1. use expert knowledge to find a location of the feature component,
     - e.g sound is the key aspect word, where is sound normally in the listing (title, heading )
     - as the main Noun phrase of listing heading? Is it always in capital chance of it is in capital is really high (What is the percentage?)

  2) Use feature component to identify other Key aspect :

keyword spotting in the listing :

- give a key word, evaluate its effectiveness and importance.
- highlight the keywords.

- Miss catching, the light that does not have keywords.

- Evaluate feature's discriminative power, before and after adding the feature.

#### 1.9.5.1. potential feature or indication of feature component.

    - is_capsulized : IC
    - is_in_product_title IPT
    - is_in_listing_title_line. ILT

#### 1.9.5.2. MVP design : boot straping the feature indictor location vs key aspect.

-> feature component location list

download 100 listings of bluetooth speaker :
give 100 link.

- extract 100 product listing. (Bluetooth speaker)
- 2 input frame, key aspect word
- highlight the key aspect word in listing.

  - mark it is matched (IC,IPT, ILT)
  - mark it does not belong to any of the indicator.
    - a new potential feature indicator is found.

- format of the product listing summary

      {
          "product_id":
          {
          "title" : "",
          "listing" : "",
          "price" : "",
          },
      }

  - Show product listing using streamlit : input a id :
  -

### 1.9.6. Semantical study

- - - 1. <Question: How to Semantically grouping a pack of words.>
      - Example : Bluetooth Connectivity.
        - 1. ,
        - 2. signal strength,
      2. How does number quantify :

research topic :

clustering word according to its semantic closeness :
cost - price should be close.

http://www.ilc.cnr.it/EAGLES96/rep2/node37.html#:~:text=Word%20clustering%20is%20a%20technique,to%20information%20retrieval%20and%20filtering.

### 1.9.7. Sentiment analysis

      1. Enhance the database by go though the typical names
      2. Indian name : identifier .
      3. Add statistical plot for the page.
      - 1. In this page : how many person in each nationality. (pie chart.)
           1. most / least .
        1. How does the trend increase and decrease over the year. (trended analysis .)
      1.

### 1.9.8. Research new product example

#### 1.9.8.1. Amazon microphone

- What is the key aspects of amazon microphone :
  key words .
- what is key sub Category?
  step 1 : best ranking article in on the topic - lapel vs shotgun : - PC stand along.
  Expected outcome:

- Excellent shopping experience.
- Just speak loud and clear. Never get yourself muffled.
- Maybe because of too small voice instead of the microphone.

### 1.9.9. UI for the amazon :

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

## 1.10. System Overview

### 1.10.1. Building block

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

### 1.10.2. Key Technology

- 1. Use web-service as input/ output. (Azure website)
  2. Use Python as Language
  3. Use Azure machine learning backbone
  4. Use previous simplified crawler.
  5. Use Pattern recognition as Name Nationality Classifer.

### 1.10.3. Key principles

1. Make MVP first : Frame work first, Get more detail later .
2. how to Simplify, Well still keep the system integrity
3. Each component/Building block have a file

## 1.11. Steps planning

### 1.11.1. Statistical survey of top 100 best saler - listing:

#### 1.11.1.1. Text processing :

- [ML_Text_Process.md](file:///C:/Local/Work/ML_Name/Note/ML_Text_Process.md)

Noun\_

#### 1.11.1.2. Objective.

- fast quick landscape. just for quick peaking.

#### 1.11.1.3. items

- - 1. Summarize the core parameter of a product :
    2. price range and histogram.
    3. Title analysis.
    4. listing vs product dictionary

#### 1.11.1.4. Summarize the core parameter of a product :

- - 1. best seller rank
    2. brand
    3. price

#### 1.11.1.5. price range and histogram.

- - 1. max, min, median, standard derivation statistical diagrams.
    2. weighted by sales number

#### 1.11.1.6. Title analysis.

- - 1.  title keywords extraction and coverage.
    2.  Cluster of title keywords.
    3.  frequency analysis of the key words.

#### 1.11.1.7. Listing vs product dictionary

##### 1.11.1.7.1. Objective Done

- Current Categorize the listing according to know key character list: What is the next strategy?

##### 1.11.1.7.2. Content.

- - 1.  Product KC coverage in listing
        1.  especially what is not covered KC
    2.  Most used and mentioned KC in feature listing

    3.  Have all the basic grammatical analyze and think.
        1.  extract the NER, noun phrase.
    4.  what feature is the **key most price driver**.
    5.  Feature vs price correlation.
        1.  brand?
        2.  a specific feature such as waterproof/battery life?
    6.  Feature vs comment , best seller correlation :

##### 1.11.1.7.3. product dictionary KC vs listing

##### 1.11.1.7.4. Product KC coverage in listing

##### 1.11.1.7.5. Most used and mentioned KC in feature listing

##### 1.11.1.7.6. basic grammatical analyze

- - 1.  extract the NER, noun phrase in feature list

#### 1.11.1.8. KC vs product :

- - 1. out of 100 products, which one have best bluetooth connectivity
    2. out of 100 products, which one have best sound quality
    3. out of 100 products, which one have longest battery life.
    4.
-

#### 1.11.1.9. Side question:

    1. how to get 1000 best seller.

### 1.11.2. Time tracker of each best saler

#### 1.11.2.1. Objective.

- - 1. Can be quickly productive and show it to users.

##### 1.11.2.1.1. How

- - 1. given product id : download and compare every day.
    2. mark a product and provide time_stampeded update
    3. check for:
       1. Ranking change. price curve,
       2. Comment increase: Daily increase.
       3. new comment,
       4. price change.

##### 1.11.2.1.2. Action

- send alert my price
- check honey droplist :

  - https://www.joinhoney.com/ : Droplist
  - time to change

- How to get the promo code?
  - How to search the right website to get prompt code
  - check honey. : https://www.joinhoney.com/
  - honey promp code : https://www.joinhoney.com/page/DR-US-Evergreen-Simplified-Widget-Airpods-Yellow/

### 1.11.3. Statistical survey of top 100 best saler - comments:

    1. What is the most informative comment.
               1. highly recommended .
               2. worst , 1 star, long and represetive .

### 1.11.4. Seller Perspective analysis

#### 1.11.4.1. personality :

            1.  as a buyer to get the best product.
            2.  as a seller, find the best niche to sell.

#### 1.11.4.2. Content :

- - 1.  monitor the price of a keywords and for effective ad promotion:
    2.  What is most sensitive to future? If I want to have a new product to developed.
        1. is this product price driving,
        2. feature driving
        3. or brand driving?

### 1.11.5. UX design.

#### 1.11.5.1. Objective.

- How to design to get the best web interface to help the user to make an informed decision : clean website.

#### 1.11.5.2. Sub categories

- the product have 3 kind of sub categories :

  - definition of the each categories.
  - pro and con of each category.

- formulate ; make structure, filling in the content

## 1.12. System Design Detail

### 1.12.1. Building block construction

- [ ] Named Entity Recognition : use spacy to train aspect

- [Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities)

#### 1.12.1.1. Crawler :

- Crawler from web get the STEM names, [DONE]
- Crawler from web get the STEM subjects ,

##### 1.12.1.1.1. Versions and stages

1.  S1 :
2.  S2 :

##### 1.12.1.1.2. Input

- Amazon pages :
  - product pages.
  - comment pages

##### 1.12.1.1.3. Output

- listing :

#### 1.12.1.2. Classifier

#### 1.12.1.3. .

##### 1.12.1.3.1. Input

- product listings

##### 1.12.1.3.2. Output

- Key extraction: aspect file tags :

#### 1.12.1.4. IO :

##### 1.12.1.4.1. Input

- Input name , display the nationality:

##### 1.12.1.4.2. Output

- visualization
  - Power BI

Challenges :

- complex : how to step by step simplify a issue.
- simplify :

### 1.12.2. Thought

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

We needed to extract our users’ skills from their Curriculam Vitaes (CVs) even if they are written in an arbitrary way such as “was deploying quantitative trading algorithms on production server”.

#### 2.1.1.3. Linguistic models

##### 2.1.1.3.1. unsupervised learning first

Modern linguistic models (ULMfit, ELMo) use unsupervised learning techniques such as creating RNNs embeddings on large texts corpora to gain some primal “knowledge” of the language structures before a more specific supervised training step.

##### 2.1.1.3.2. supervised learning later

In some cases on the contrary you need a model trained on a very specific and small dataset. These models possess nearly zero knowledge of the general linguistic structures and work only with special text features.

##### 2.1.1.3.3. supervised learning : small specific domain

A classic example would be a naive sentiment analysis tool for movie reviews or news datasets — the simplest working model could operate only with “good” or “bad” adjectives synonyms and some emphasising words presence. In our research we took advantages of both approaches.

#### 2.1.1.4. texts vectorization

Popular methods of texts vectorisation, such as tfidf, word2vec or GloVe models are using the whole document’s vocabulary to create its vector except of

1. Step 1: Stopwords removal
   stopwords (such as articles, pronouns, and other quite generic language elements bringing little semantic sense in such a statistical averaging procedure)

2. Step 2: Global word converstion : vectorization

<Global way : Convert each individual words into a unique vector >

Raise question : dont answer and think question

##### 2.1.1.4.1. word2vec

https://www.tensorflow.org/tutorials/word2vec

##### 2.1.1.4.2. GloVe

https://nlp.stanford.edu/projects/glove/
Introduction :

#### 2.1.1.5. Specific task : extracting aspects from text

<Question: What is the key task>

<Answer: Extract high value text and the domain of the whole text known>

If there is a more specific task and you have some additional information about the texts corpus, you could probably **state that some information is more valuable than the other**.

For example, to perform some analysis on a corpus of cooking recipes it would be important to **extract ingredients or dish names classes** from the texts.
<Cooking recipes -> ingredients>

The other example is extracting professional skills from the CVs’ corpus. If we could vectorise each CV by relating it with a vector of extracted skills it would let us perform much more successful industry positions clustering, for example.
<Resume CV -> Skill words>
Skill words are vectorized .

#### 2.1.1.6. Output Example

IMPORTANT

1.  INPUT :
2.  CV: Data scientist, hands on expertise in **machine learning**, **big data**, **development**, **statistics** and **analytics**. With my team of data scientists implemented **Python machine learning model ensembles**, **stacking**, and **feature engineering** demonstrating high accuracy rates in predictive analytics. Created a recommender system using Doc2Vec words embeddings and neural networks.

3) Output Extracted professional skills:
   machine learning, big data, development, statistics, analytics, Python machine learning model ensembles, stacking, feature engineering, predictive analytics, Doc2Vec, words embeddings, neural networks.

Key steps :
Stacking :
feature engineering
// ANCHOR now

#### 2.1.1.7. Step 1: Parts of speech tagging

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

## 2.2. Material info

### 2.2.1. product name

amazon web product name

1. normal

   1. B07QBMJW6W
   2. B00NB2MCI2
   3. B07YV84PTM
   4. B07PWPYHM3
   5. B079QB9BD7
   6. B08B5YNVFW
   7. B087KGR54J
   8. B087KGR54J
   9. B07KY63Z3R
   10. B07ZGCNX14

2. bluetooth speaker: amazon.com

   1. B010OYASRG
   2. B07WSH46LX
   3. B016XTADG2
   4. B01CQOV3YO
   5. B07P39MLKH
   6. B01HETFQKS
   7. B07XJ8B9NV
   8. B07QK2SPP7
   9. B07ZRVX6RM
   10. B07NNF7WH1

3. bluetooth speaker: amazon.co.uk
   1. B010OYASRG
   2. B07WSH46LX
   3. B016XTADG2
   4. B01CQOV3YO
   5. B07P39MLKH
   6. B01HETFQKS
   7. B07XJ8B9NV
   8. B07QK2SPP7
   9. B07ZRVX6RM
   10. B07NNF7WH1

## 2.3. Ref :

- [What is a noun phrase](https://www.softschools.com/examples/grammar/noun_phrases_examples/65/#:~:text=The%20other%20words%20modify%20the,I%20want%20a%20skate%20board.)

### 2.3.1. Paper 1 : Deep learning for specific information extraction from unstructured texts

1. using LSTM on the resume for skill words IMPORTANT

#### 2.3.1.1. - Website

- [Deep learning for specific information extraction from unstructured texts](https://towardsdatascience.com/deep-learning-for-specific-information-extraction-from-unstructured-texts-12c5b9dceada)
- [iki](https://iki.ai/)

#### 2.3.1.2. - Github

- [code](https://gist.github.com/IntuitionEngineering/a6e6e8a1f942a528c97e1d01af782ea2#file-skills_extract_nn-py)

#### 2.3.1.3. - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP1

demo page

### 2.3.2. Paper 2 : White paper — Job Skills extraction with LSTM and Word Embeddings

#### 2.3.2.1. - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP2

#### 2.3.2.2. - Website

- [White paper — Job Skills extraction with LSTM and Word Embeddings](https://medium.com/@nikkisharma536/white-paper-job-skills-extraction-with-lstm-and-word-embeddings-d71d1f96024f)

* [paper Job Skills extraction with LSTM and Word Embeddings]](https://confusedcoders.com/wp-content/uploads/2019/09/Job-Skills-extraction-with-LSTM-and-Word-Embeddings-Nikita-Sharma.pdf)

- [The Best Portable Bluetooth Speaker: article on bluetooth](https://www.outeraudio.com/portable-bluetooth-speakers/)

- [Semantic distance](http://www.ilc.cnr.it/EAGLES96/rep2/rep2.html)

- [bluetooth speaker search](https://www.amazon.com/s?k=bluetooth+speaker&i=mi&ref=nb_sb_noss_2)
