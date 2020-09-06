# [ML_Amazon_product_adviser_chat_bot]
[](#)
ML_Amazon_product_adviser_chat_bot.md
- [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md) 

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)


## Objective 
  
    1. Use beautifulsoup  to crawl amazon product info : Earily version 
    2. 

## Structure

### Parent
  - [Master](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)  
  - [mm.md](file:///C:/Local/Work/Key_Tools/Note/mm.md) 
  - [ML_todo.md](file:///C:/Local/Work/Key_Docs/Todo/ML_todo.md)
    
### Son 

##### Amazon

  - [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)  
 - [ML_Amazon_Train_Extract_skill_from_CV.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_Train_Extract_skill_from_CV.md)  
  - [ML_ebay_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_ebay_product_Crawler.md)   
  - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) 
  - [ML_Amazon_product_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_data_prepare.md)
  - [ML_Amazon_product_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Visualizer.md) 

##### Python files 

  -  [ML_master.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_master.py) 
  -  [ML_amazon_best_seller.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_best_seller.py) 
  - [ML_amazon_listing_download.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_listing_download.py)
  - [amazon_product_dictionary.py](file:///C:/Local/Work/ML_Name/Code/Test/amazon_product_dictionary.py)

## Todo

- [ ] Sort ML_Amazon_chat_bot [V_1][d_1]
- [ ] Plan for the next steps  
- [ ] Work on basic information extraction first
  - [ ] [target](#vision)
- [ ] Read the most important
  - [ ] [paper](#paper-1--deep-learning-for-specific-information-extraction-from-unstructured-texts)
- [ ] Named Entity Recognition : use spacy to train aspect ?

## Action 

  ### Sort ML_Amazon_chat_bot 
    - [∞](#sort-ml_amazon_chat_bot)
    - Regain all knowledge of ML 
  ### Plan for the next steps   
    - [∞](#work-next-steps)

- [ ]  Product time dimension monitoring : 
      - [∞](#153-product-time-dimension-monitoring)
  
## Vision

- Name : **Genie** :

  - Use aladdin theme for each of the sub project
  - Chat bot on amazon search , help user to make wise decision when shopping


### aladdin names 
Genie ; princess; 

## Objective

### Knowledge learnt

- What knowledge do you gain by this practice
  - Statistics ML: end to end.
  - Web service : Flask based web framework
  - Visualization : PowerBI
  - language processing :
  - product data mining and analysis

### Key benefit :

      - My pet project
      - Beneficial to the financial insight project

### Key principles

  1. Make MVP first : Frame work first, Get more detail later .
  2. how to Simplify, Well still keep the system integrity
  3. Each component/Building block have a file

### What is not todo :

    - Sub optimization :
    - build a MVP : for each component:
    - make the whole things work first.

## System Overview

### Building block

1. **Crawler** :

   1. Crawler from web for amazon web pages and comments
      1. Product basic information extraction <DONE> 
      2. Product time dimension monitoring : 
      3. Statistical analysis : 
      4. Build product graph : relationship between abstract :

2. **Classifier**

   1. Aspect matching with feature list and comment
   2. Aspect statistical
   3. Aspect training

3. **WebIO** :
   1. Chat bot :
   2. Use the job hunting and merging in.
   3. Data Visualization :
      1. Statistical Visualization.

### Key Technology

- 1. Use streamlet python web framework as input/ output.
  1. Use Python as Language
  1. Use bs_lib/scrapy simplified crawler.
  1. Use machine learning backbone
  1. use raspberry pi as fixed IP web app for future customer

## High level Work Plan

### Basic Amazon product work
    <DONE> ML_amazon_best_seller.py 
    - Get best_seller list 
    - download asin in best_seller list  into product info 
    - compare product information with product directory. 

### Product basic information extraction
    <DONE> ML_Amazon_product_Crawler.md ; quotes_spider.py 
      1 Extract key information from product. :
         - price. title listing.
         - history 

### Product time dimension monitoring
    NOTE : Current high level
    
    1. Run program periodicity 
    2. crawel the key information 

### Statistical analysis :

    1. Most frequent meaningful bi-words.
    2. Most mentioned meaningful model :

### Aspect word mining 
    
    1. Extract NP in Product feature list, 
    2. Extract NP in Product comments 
    3. Match and highlight Product dictionary with FL and Comments 
    4. Get the  character of the location of aspect word. 
    5. Train an NN (Tensorflow) to extract Aspect word without dictionary. 
  Reference of 

### Build product graph

-

## Key docs and data structure:

C:\Local\Work\ML_Name\Note\ML_Name_Nationality\ML_Name_Nationality.md

### Key python files.

- - 1.  [ML_master.py] :
        - [ML_master.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_master.py) 
        - Running the streamlit based web UI :
    2.  [ML_amazon_best_seller.py] :
        -  [ML_amazon_best_seller.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_best_seller.py) 
        - given search term: get the top 100 best seller.     :
        - Already in ML_master.   
    2.  [ML_amazon_listing_download.py] :
         - [ML_amazon_listing_download.py](file:///C:/Local/Work/ML_Name/Code/Test/ML_amazon_listing_download.py)
         - download file given a list of asin : use bs_lib.get_amazon_product_info(asin)
    4.  [amazon_product_dictionary.py] :
        - [amazon_product_dictionary.py](file:///C:/Local/Work/ML_Name/Code/Test/amazon_product_dictionary.py) 
        - processing and matching production dictionary vs asin product info -
          - 1. Load json file
            - load_product_listing_json
            1. Generate Product dictionary json file
               - load_product_dictionary_json
            - keywords :
          - 1. match and tag aspects into each listing sentences. **One last sentence. One aspect.**
            1. Highlight the key word match
            2. Give each aspect feature a value/discription.
               1. bass : 'xx sentence'
               2. waterproff : 'IPX'

### Key md files.

- - 1.  [ML_Amazon_product_adviser_chat_bot.md]: master file :
    2.
-
- -
- :

### Key data structure

#### asin list

##### Format

`asin_list_file.json`

    format :
    {
    "1": "B0742BV75P",
    "2": "B0719M4YZB",
    ...
    }

##### Example

- [asin_list_file.json](file:///C:/Local/Work/ML_Name/Code/Test/asin_list_file.json)
- [bluetooth+speaker.json](file:///C:/Local/Work/ML_Name/Code/Test/data/best_seller/bluetooth+speaker.json) : output of the best_seller scraping

#### Asin information dictionary

- [detail](#1332-asin-information-dictionary)

##### Format

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

##### Example

- [B07ZRVX6RM.json](file:///C:/Local/Work/ML_Name/Code/Test/data/asin/B07ZRVX6RM.json)

#### Product Dictionary :

core ideas

- [detail](#193-product-dictionary-definition)

##### What

- Provide aspects ->

##### Format

- - - get empty place to fill
      "feature_list": {
      "sound": {},
      "connectivity": {},
      "battery": {}
      }

##### Example

- [bt_speaker_product_dictionary.json](file:///C:/Local/Work/ML_Name/Code/Test/data/bt_speaker_product_dictionary.json)

## Core Ideas

### Noun phrase extraction

- - 1.  Highlight Noun phrase in an article

### Aspect Extraction and matching

#### the Aspect evaluation : Scores :

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

#### the Aspect, NP matching.

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

#### apsect tagging

1. first line of each listing : generate the aspects words

   1. sound
   2. price
   3. water proof

2. for each of the aspect words , tag the review article .
3. tag the comment according to aspect words and matched keywords.

issue : the accuracy of spacy is not good . see the example

task :
color tag the html according to identified words.'s identify (person etc)

aspect dictionary . : what are the feature to be considered when selecting :

### Product dictionary definition.

- build keywords then build structure.

- Expected result, : Product key aspect dictionary

#### Activity.

#### Product dictionary data structure

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

##### bluetooth speaker aspect dictionary

See - [](#what-is-aspects)

- [](#19321-bluetooth-speaker-aspect-dictionary)
- https://www.outeraudio.com/portable-bluetooth-speakers/

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

### Aspect Training

#### What is aspect

- [#Concepts and Knowledges](#1151-concept--aspect)

#### Feature extraction

- [](#194-feature-extraction)

  1. Some features is known should have stronger discriminative power by expert knowledge

  2. How to weight : sequential classifier. (Heavy weight of expert knowledge.vs machine learning.)
     - some name have strong indication of nationality :
     1. e.g ginsberg is a jewish name.
     2. Li is a chinese name.

#### Feature indictor location vs key aspect.

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

#### potential feature or indication of feature component.

    - is_capsulized : IC
    - is_in_product_title IPT
    - is_in_listing_title_line. ILT

#### MVP design : boot straping the feature indictor location vs key aspect.

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

### Semantical study

- - - 1. <Question: How to Semantically grouping a pack of words.>
      - Example : Bluetooth Connectivity.
        - 1. ,
        - 2. signal strength,
      2. How does number quantify :

research topic :

clustering word according to its semantic closeness :
cost - price should be close.

http://www.ilc.cnr.it/EAGLES96/rep2/node37.html#:~:text=Word%20clustering%20is%20a%20technique,to%20information%20retrieval%20and%20filtering.

#### Sentiment analysis

      1. Enhance the database by go though the typical names
      2. Indian name : identifier .
      3. Add statistical plot for the page.
      - 1. In this page : how many person in each nationality. (pie chart.)
           1. most / least .
        1. How does the trend increase and decrease over the year. (trended analysis .)
      1.

### Research new product example

### UI for the amazon :

## Work Completed

### Summary

- - 1. Scrap top 100 bluetooth listing and get 100 asin list. e.g 'bluetooth+speaker'
    2. Scrap each asin , get asin information dictionary
    3. Match product dictionary with asin information dictory

### scrap top 100 bluetooth listing.

`ML_amazon_best_seller.py`

#### Summary : - get the top 100 best seller.

##### Input :

- - 1. given search term: 'bluetooth+speaker'

#### Output

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

#### Implementation

- - 1. build google search page : build_google_search_page()
    2. Get 50 best seller asin for a best seller page : get_a_page_best_seller_asin(soup):
    3. get 100 best seller : get_best_seller_asin(Amazon_best_seller_page)
       1. get first 50 seller
       2. get next page link
       3. get next 50

### Product Info crawling and display :

#### Amazon product asin list :

- - 1.  Get amazon web product name list

`product_id_list_file.json`
format :  
 {
"1": "B0742BV75P",
"2": "B0719M4YZB",
...
}

#### Scraping of key infos of one listing's Asin

`bs_lib.py : get_amazon_product_info()`

##### Key product information

- - 1.  Price.
    2.  rating
    3.  producer
    4.  first comment time [later]
    5.  total comment:

##### Implementation : bs_lib.py : get_amazon_product_info()

- - - input : asin id
    - Output :
      - product info : dictionary json file
      - output_dir : 'C:/Local/Work/ML_Name/Code/Test/data/asin/'

#### Scrap a list of asin :

`ML_amazon_listing_download.py`
`amazon_product_dict = bs_lib.get_amazon_product_info(asin)`

- - 1. input : list is in `product_id_list_file.json`
    2. Output : Go though and scrap and save in output_dir :
       1. 'C:/Local/Work/ML_Name/Code/Test/data/asin/'

#### Display in streamlit

- [ML_master.py]

##### called in :

- - - ML_master.py : given a web interface :
    - - input text box : asin id
    - - output : scrap that asin and display product info

### product dictionary creation

#### Product dictionary data

- [detail](#1333-product-dictionary-)

##### Format

- - - get empty place to fill
      "feature_list": {
      "sound": {},
      "connectivity": {},
      "battery": {}
      }
- [bt_speaker_product_dictionary.json](file:///C:/Local/Work/ML_Name/Code/Test/data/bt_speaker_product_dictionary.json)

### product dictionary vs asin info

#### feature list title tagging :

- **classify each feature list title : belong to which aspect**
  - if the keyword of the aspect is in the feature list title
- Example :

#### feature list tagging :

- tag the whole feature list :
  run for all asin.json feature list.

## Work: Next steps

// NOTE Next step 
### Time dimension downloading 

### Display the crawled info in a flask website.  


### Highlighting the Aspect word location in the listing .

1.  to find the keyword component locations
2.  important. bootstrap.

### NP extraction of feature list :

- - - Run NP extraction to list all the noun
    - Output : for each feature list :
      - tagged NP_list :
      - tagged aspect: aspect keywords.


### detection of noun phrase in title :

which of the noun phrase is
how to train a more accurate noun phrase.

### side by side comparison of aspect.

- P1 listing line on connectivity
- P2 listing line on connectivity

Comparing of price:

- price range and aspect

  - price from 10-20 usd : percentage have feature x.

    4.coverage of product dictionary of the listing. which one is taged and which one does not.

### Relative importance of aspects.

- 3 aspects : what is the weight toward total buying decision.

### Statistical Analysis 100 best seller

Statistical Analysis 100 best seller
of ASIN feature list of

#### Text processing :

- [ML_Text_Process.md](file:///C:/Local/Work/ML_Name/Note/ML_Text_Process.md)

* - 1. Summarize the core parameter of a product :
    1. price range and histogram.
    1. Title keyword statistical analysis
    1. listing vs product dictionary

#### Objective.

360 degree overview :

- fast quick landscape. just for quick peaking.

  - Most brand in each category/price range.
  - Highest rating/comment in the price range.
  -

#### Summarize the core parameter of a product :

- - 1. best seller rank
    2. brand
    3. price

#### Aspects statistic

- Most covered aspects.
- Lest covered aspects.
- Keywords:
  - Most used keywords :
- NP:
  - Most used NP

#### Aspect commonality

- What is the commonality of the best seller:
  - Best seller has the following aspect :

#### price range and histogram.

- - 1. max, min, median, standard derivation statistical diagrams.
    2. weighted by sales number

#### Brand statistics

- Most brand in each category/price range.

#### price for value statistics

- Highest rating/comment in the category/price range.

#### Title analysis.

- - 1.  title keywords extraction and coverage.
    2.  Cluster of title keywords.
    3.  frequency analysis of the key words.

#### Listing vs product dictionary

##### Objective Done

- Current Categorize the listing according to know key character list: What is the next strategy?

##### Content.

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

##### product dictionary KC vs listing

##### Product KC coverage in listing

##### Most used and mentioned KC in feature listing

##### basic grammatical analyze

- - 1.  extract the NER, noun phrase in feature list

#### KC vs product :

- - 1. out of 100 products, which one have best bluetooth connectivity
    2. out of 100 products, which one have best sound quality
    3. out of 100 products, which one have longest battery life.
    4.
-

#### Side question:

    1. how to get 1000 best seller.




### Time tracker of each best saler

#### Objective.

- - 1. Can be quickly productive and show it to users.

##### How

- - 1. given product id : download and compare every day.
    2. mark a product and provide time_stampeded update
    3. check for:
       1. Ranking change. price curve,
       2. Comment increase: Daily increase.
       3. new comment,
       4. price change.

1. send alert my price

   - time dimension monitoring :
     - giving a product code, change across time. (price , rank , comment. )
   - automatically check every day.
   - Graph : Data structure of Amazon project

 Scrap 100 bluetooth tech article
##### Action

### Review Article : Highlight text keyword : Given product dictionary
[16-07]

#### What 
input: text paragraph 

Output : highlighted text : 
    keywords 
Summary : 
  - topic : 
  - keywords list : 

#### Content : 
  ##### Steps 
- - 1.  split the text into sentences : 
    2.  tag each sentence with topic and keywords (if there.) (15 min)
        1.  for each sentence : match with the dictionary for keywords 
        2.  def tag_sent_with_aspect_keyword(): 
    3. highlight the keyword that match in text and tag list the aspect for the text . 
       1. def highlight_text_with_aspect_keywords. keep all the article format. 
    4. revert to better highligher name recognation.


### product graph

### Competitor analysis.

see - [](#honey-droplist)

### Scrap 100 bluetooth tech article

- Get the overall information :
  - how many types of bluetooth speaker are there
  - how many types of microphone are there

#### Sub categories (types)

- the product have 3 kind of sub categories :

  - definition of the each categories.
  - pro and con of each category.

- formulate ; make structure, filling in the content

### Statistical survey of top 100 best saler - comments:

    1. What is the most informative comment.
               1. highly recommended .
               2. worst , 1 star, long and represetive .

#### download Comments.

#### User comment scoring each aspect

#### Visualization Plot radar diagram :

- [](#aspect-score-visualization-)

### Train aspect

IMPORTANT train aspect from NP :
for example : sound is trained as aspects word.

- [](#2116-train-aspect-output-example)

Can train aspect word from corporse : Extract aspect from corpus.

SEE Example : extract skill NP from resume :

- [ML_Amazon_Train_Extract_skill_from_CV.md]
- See - [#core idea](#194-feature-extraction) for detail

### Seller Perspective analysis

#### personality :

            1.  as a buyer to get the best product.
            2.  as a seller, find the best niche to sell.

#### Content :

- - 1.  monitor the price of a keywords and for effective ad promotion:
    2.  What is most sensitive to future? If I want to have a new product to developed.
        1. is this product price driving,
        2. feature driving
        3. or brand driving?

### UX design.

#### Objective.

- How to design to get the best web interface to help the user to make an informed decision : clean website.

#### Dialogue : chatbot format :

- Give me search item :

  - I give you a 360 degree overview :

    - Most brand in each category/price range.
    - Highest rating/comment in the price range.

    Implementation see - [](#statistical-analysis-100-best-seller)

  - I give you the known Key aspects : (Expert knowledge)

    <Question: What the Weight or relative importance of this aspects :>

    <Answer: >

        - topic identification of the articles. :
          - Most visited atrial : (high google search rank)
          - Most talked about feature. (length of the paragraph that talking about)
          -

  - What is the commonality of the best seller:
    - Best seller has the following aspect :

#### Sub categories (types)

- the product have 3 kind of sub categories :
  how many types of microphone are there

#### key aspect highlighting in web interface

### publish in a web-hosting. take input .

### study amazon API

## Use case and User experience :

### Generic

- As a user , I can input an Amazon comment and highlight which aspect it is talking about. .
- As a suer : I want to know what is most effective shopping strategy.

### User experience Example : Bluetooth speaker purchasing

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

### User experience and scenario : microphone purchasing

1. Use microphone, nice example.
2. what is the general landscape
   1. price range.
   2. what kind of **sub category** microphone we have :
      1. best ranking article in on the topic - lapel vs shotgun : - PC stand along.
      2. price range of each sub category
      3. pro and cons :
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

## Key reference product

### honey droplist

- check honey droplist :

  - https://www.joinhoney.com/ : Droplist
  - time to change

- How to get the promo code?
  - How to search the right website to get prompt code
  - check honey. : https://www.joinhoney.com/
  - honey promp code : https://www.joinhoney.com/page/DR-US-Evergreen-Simplified-Widget-Airpods-Yellow/

## Material info

### product name

- [ML_amazon_product_asin.json]

## Concepts and Knowledged

### Concept : Aspect

#### What is Aspects

the word that define one key area of the product :

sound
connectivity
are aspects.

see example  
<Question: What is the key task>

<Answer: Extract high value text and the domain of the whole text known>

If there is a more specific task and you have some additional information about the texts corpus, you could probably **state that some information is more valuable than the other**.

For example, to perform some analysis on a corpus of cooking recipes it would be important to **extract ingredients or dish names classes** from the texts.
<Cooking recipes -> ingredients>

The other example is extracting professional skills from the CVs’ corpus. If we could vectorise each CV by relating it with a vector of extracted skills it would let us perform much more successful industry positions clustering, for example.
<Resume CV -> Skill words>
Skill words are vectorized .

#### Train aspect Output Example

Can train aspect word from corporse : Extract aspect from corpus.
Identifiy which NP is aspect

IMPORTANT

1.  INPUT :
2.  CV: Data scientist, hands on expertise in **machine learning**, **big data**, **development**, **statistics** and **analytics**. With my team of data scientists implemented **Python machine learning model ensembles**, **stacking**, and **feature engineering** demonstrating high accuracy rates in predictive analytics. Created a recommender system using Doc2Vec words embeddings and neural networks.

3) Output Extracted professional skills:
   machine learning, big data, development, statistics, analytics, Python machine learning model ensembles, stacking, feature engineering, predictive analytics, Doc2Vec, words embeddings, neural networks.

### Concept : texts vectorization

Popular methods of texts vectorisation, such as tfidf, word2vec or GloVe models are using the whole document’s vocabulary to create its vector except of

1. Step 1: Stopwords removal
   stopwords (such as articles, pronouns, and other quite generic language elements bringing little semantic sense in such a statistical averaging procedure)

2. Step 2: Global word converstion : vectorization

<Global way : Convert each individual words into a unique vector >

Raise question : dont answer and think question

##### word2vec

https://www.tensorflow.org/tutorials/word2vec

##### GloVe

https://nlp.stanford.edu/projects/glove/
Introduction :

## Ref :

- [What is a noun phrase](https://www.softschools.com/examples/grammar/noun_phrases_examples/65/#:~:text=The%20other%20words%20modify%20the,I%20want%20a%20skate%20board.)

### Paper 1 : Deep learning for specific information extraction from unstructured texts

1. using LSTM on the resume for skill words IMPORTANT

#### - Website

- [Deep learning for specific information extraction from unstructured texts](https://towardsdatascience.com/deep-learning-for-specific-information-extraction-from-unstructured-texts-12c5b9dceada)
- [iki](https://iki.ai/)

#### - Github

- [code](https://gist.github.com/IntuitionEngineering/a6e6e8a1f942a528c97e1d01af782ea2#file-skills_extract_nn-py)

#### - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP1

demo page

### Paper 2 : White paper — Job Skills extraction with LSTM and Word Embeddings

#### - Local

- C:\Local\Work\ML_Name\Material\Amazon_Product\TP2

#### - Website

- [White paper — Job Skills extraction with LSTM and Word Embeddings](https://medium.com/@nikkisharma536/white-paper-job-skills-extraction-with-lstm-and-word-embeddings-d71d1f96024f)

* [paper Job Skills extraction with LSTM and Word Embeddings]](https://confusedcoders.com/wp-content/uploads/2019/09/Job-Skills-extraction-with-LSTM-and-Word-Embeddings-Nikita-Sharma.pdf)

- [The Best Portable Bluetooth Speaker: article on bluetooth](https://www.outeraudio.com/portable-bluetooth-speakers/)

- [Semantic distance](http://www.ilc.cnr.it/EAGLES96/rep2/rep2.html)

- [bluetooth speaker search](https://www.amazon.com/s?k=bluetooth+speaker&i=mi&ref=nb_sb_noss_2)

* [ ] Named Entity Recognition : use spacy to train aspect

* [Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities)
