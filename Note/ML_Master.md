# 1. 1

- [ML_Master.md](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)
[](#)

## Howto  
     - make all information in right place [2.5 hours]

      1.  Configure the file structure : make it nested folder like: MASTER as example. [15*2]
          1. Make a good breadcream is good enough.
          2. format : Key Header in Captial letter.
            1. title
            2. link :
            3. Detail

    Result : c:\Local\Work\ML_Name\Note\
    See favoirte

## Structure

### Parent
  - [Master](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)  
  - [mm.md](file:///C:/Local/Work/Key_Tools/Note/mm.md) 
  - [ML_todo.md](file:///C:/Local/Work/Key_Docs/Todo/ML_todo.md)
    
### Son 

##### ML_Amazon

  - [**ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)  
  - [* ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) 
 - [* ML_Amazon_Train_Extract_skill_from_CV.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_Train_Extract_skill_from_CV.md)  



  - [ML_ebay_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_ebay_product_Crawler.md)   
  - [ML_Amazon_product_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_data_prepare.md)
  - [ML_Amazon_product_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Visualizer.md) 


##### General  
  - [*ML_Text_Process.md](file:///C:/Local/Work/ML_Name/Note/ML_Text_Process.md)
  - [ML_Format.md](file:///C:/Local/Work/ML_Name/Note/ML_Format.md) 
  - [ML_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_data_prepare.md)
  - [ML_NLP_study.md](file:///C:/Local/Work/ML_Name/Note/ML_NLP_study.md)   


##### ML_Name_Identification

  - [ML_Name_Identification.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification.md)
  - [ML_Name_Identification_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Classifier.md)

  - [ML_Name_Identification_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Crawler.md) 
  - [ML_Name_Identification_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_data_prepare.md)
  - [ML_Name_Identification_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Visualizer.md) 
  - [ML_Name_Nationality](file:///c:/Local/Work/ML_Name/Note/ML_Name_Nationality.md)

####  ML_Job_Hunter
  - [ML_Job_hunter.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_hunter.md)
  - [ML_Job_Hunter_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Crawler.md) 
  - [ML_Job_Hunter_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Classifier.md)   
  - [ML_Job_Hunter_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_data_prepare.md) 
  -  [ML_Job_Hunter_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Visualizer.md)


<!------------------------------------------------------------------------->



## 1.1. Todo

      - [x] ML OKR and Plan [ 1 hour ]
      1. Scaffolding for the key python data science library. (45 min)

- [ ] scaffolding :
      1. sort the library of ML study
- [ ] Howto run : ML_Master
      - [∞](#howto-run--ml_master)

## Actions 

  1. Crawler : [15_min] 
     1. link [3_min] <DONE>
     2. Separate 2 files : crawler and chatbot. [12_min] <DONE>
  2. Summary of most import topic of each documents. 
     1. chatbot [10_min] <DONE>
        1. given search term: get the top 100 best seller.
        2. download file given a list of asin  
        3. processing and matching production dictionary vs asin product info
     2. cv [10_min] 


## 1.2. Vision

    - Publish a in medium : key machine learning websites.
    - End to end design , arch and implement a ML system to solve a topic of interest.
    - My pet project.

## 1.3. Structure

### Howto run : ML_Master

#### what
  - [x] Find all python files and structures 
    [10_min]
    - [x] Streamlit :   srun <DONE>
    - [x] ML_todo  section : 
  - [x]  library summary and quick review. 
    [25_min]
    - [ML_Master.md](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)

#### hwoto   

- - 1. Streamlit :   srun  <DONE>
      -  srun:     srun.ps1 C:\Local\Work\ML_Name\Code\Test\ML_master.py

    2. work structure tree :  <DONE>
      1. ML_Name
      2. Amazon_product 
    3. Move to master <DONE>
       1. [15_min]
    4. review each detail :
       1. Result : no detail yet. 
    5. collection information : C:/Local/Work/ML_Name/Code/Test

    6. connect to ML_master.py : read ML_Amazon_product_adviser_chat_bot.md



### 1.3.1. Key Technology

- 1. Use web-service as input/ output. (Azure website)
  2. Use Python as Language
  3. Use Azure machine learning backbone
  4. Use previous simplified crawler.
  5. Use Pattern recognition as Name Nationality Classifer.

### 1.3.2. Key Technology

- Key framework of ML process :
  - Problem statement : define key parameter of the work
  - Crawler : obtain raw data.
  - Data preparation : data cleaning,
  - Classification : using classifier such as svm and LSTM for training and testing,
  - Visualization : visualize the end result in webapps .

### 1.3.3. Key principles

1. Make MVP first : Frame work first, Get more detail later .
2. how to Simplify, Well still keep the system integrity
3. Each component/Building block have a file

### 1.3.4. Summary :

NLP Projects:

1. - name_nationality : identify name's nationality
2. - name_identification : identify name in a webpage
3. - Amazon_Product_Adviser : provide advise for amazon buyer
4. - Finance_Insight : Get insight from finance data
5. - Job_Hunter : Help user and hirer to better hunt for job.
6. - Job_Hunter : Help user and hirer to better hunt for job.

### 1.3.5. MAIN DOC :

NLP_Master.py

- [NLP_Master.py](file:///C:/Local/Work/Python/PyLib/NLP_Master.py)

### 1.3.6. Text processing

- [ML_Text_Process.md](file:///C:/Local/Work/ML_Name/Note/ML_Text_Process.md)

### 1.3.6. STUDY

1. **ML Technology study, reading**
   - [ML_study.md](file:///c:/Local/Work/ML_Name/Note/ML_study.md)
     - Reading of importing website documentations regarding the ML
2. **NLP Study**
   - [ML_NLP_study.md](file:///C:/Local/Work/ML_Name/Note/ML_NLP_study.md)

### 1.3.7. PROCESS

#### 1.3.7.1. Setup

1.  **Setup the environment**
    - [ML_Setup.md](file:///c:/Local/Work/ML_Name/Note/ML_Setup.md)
      - Kick starter
      - Install necessary documents/Library/SW for ML
      - Contain : Python, Azure, Web infrastructure readiness

#### 1.3.7.2. Data Preparation

1.  **General Knowledge and framework** on data prepares .
    1. [ML_data_prepare.md](file:///c:/Local/Work/ML_Name/Note/General/ML_data_prepare.md)

#### 1.3.7.3. Crawler

- **General Knowledge and framework** on web Crawler
  - [ML_Crawler.md](file:///c:/Local/Work/ML_Name/Note/ML_Crawler.md)

#### 1.3.7.4. Classifier

- **Classify module**
  - [ML_Classifier.md](file:///c:/Local/Work/ML_Name/Note/ML_Classifier.md)
    - Core classifier Knowledged : Native, LSTM etc.

#### 1.3.7.5. Web IO

##### 1.3.7.5.1. Webapp and visualizations

- - Web I/Output and visualize Result -[ML_Web_IO.md](file:///c:/Local/Work/ML_Name/Note/ML_Web_IO.md)

##### 1.3.7.5.2. Streamlit

- [ML_WebIO_Streamlit_study.md](file:///C:/Local/Work/ML_Name/Note/ML_WebIO/ML_WebIO_Streamlit_study.md)

##### 1.3.7.5.3. Flask

- [ML_WebIO_Flask_study.md](file:///C:/Local/Work/ML_Name/Note/ML_WebIO/ML_WebIO_Flask_study.md)

##### 1.3.7.5.4. Djingo

    - [ML_WebIO_Flask_Djingo.md](file:///C:/Local/Work/ML_Name/Note/ML_WebIO/ML_WebIO_Flask_Djingo.md)

### 1.3.8. PROJECTS

IMPORTANT ML run   

#### Howto run : ML_Master
  - [∞](#howto-run--ml_master)
- - 1. Master directory 
      - Test : C:\Local\Work\ML_Name\Code\Test
      - Lib  : C:\Local\Work\ML_Name\Code\lib
          - name_entity_reco.py
          - name_nationality.py

- - 1. Master file : run 
    - srun.ps1 .\ML_master.py

#### Summary 

1. Name Nationality 
   - **Identify the nationality according to person's name**
    name_nationality.py

2. Name Identification in a webpage
  **Identify the names presented in the webpage.**
  name_entity_reco.py

3. amazon product 
   
   1. - [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product_adviser_chat_bot.md)


   2. collection information : C:/Local/Work/ML_Name/Code/Test
       1. amazon_product_dictionary.py
       2. ML_review_article_download.py
       3. ML_amazon_best_seller.py
       4. ML_amazon_listing_download.py
       5. download_link.py
    
    1. connect to 

#### 1.3.8.1. Name Nationality

- **Identify the nationality according to person's name**

- [ML_Name_Nationality.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality.md) 

##### Input

- - 1. list of names : jian tang,john smith

##### Output 

- - 1. name's nationality : china , uk etc 

##### Core function 
  In .\ML_master.py
  nn.name_nationality(message) from : name_nationality.py 

##### 1.3.8.1.1. Name Nationality : Data Prepare :
  **Information** Databases to be used 
  1. Schoolers database
       - Download data from Schoolers database : [arxiv]
         - [ML_Name_Nationality_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_data_prepare.md)

  2. 100 Chinese Name
       - Get 100 fixed Chinese last name:  100 ordinary name
         - [ML_Chinese_Name_100_names.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Chinese_Name_100_names.md)

##### 1.3.8.1.2. Name Nationality : Crawler

  1. from web get the STEM names
        - [ML_Name_Nationality_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_Crawler.md) 
        - **empty**  [19-08]

##### 1.3.8.1.3. Name Nationality : Classifier

    
  1. [ML_Name_Nationality_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_Classifier.md)
    - **empty** [19-08]

##### 1.3.8.1.4. Name Nationality : Visualizer

  1.  [ML_Name_Nationality_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_Visualizer.md)
    - **empty** [19-08]


#### 1.3.8.2. Name Identification in a webpage
  
**Identify the names presented in the webpage.**

- [ML_Name_web_identification.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_web_identification.md)
  [Python_File] : pp name_entity_reco.py 

##### Input
- - 1. article web link 

##### Output 
- - 1. person's names in article  
  - 2. Highlight the person's name in the article 

##### core function 
    from  name_entity_reco : 
    nlp_text = ner.Get_html_text(message)
    (nlp_text, person_name_all) = ner.get_person_name(nlp_text)

##### 1.3.8.2.1. Name Identification : Data Prepare :

      - [ML_Name_Identification_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_data_prepare.md)

##### 1.3.8.2.2. Name Identification : Crawler

      - [ML_Name_Identification_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Crawler.md)

##### 1.3.8.2.3. Name Identification : Classifier

      - [ML_Name_Identification_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Classifier.md)

##### 1.3.8.2.4. Name Identification : Visualizer

      - [ML_Name_Identification_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Nationality_Visualizer.md)

#### 1.3.8.3. Amazon Product Adviser

**Chat bot on amazon search , help user to make wise decision** :
- [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)
 
##### Input
- - 1. Enter your product ID : ASIN 

##### Output 
- - 1. product information 


##### core function    
    amazon_product_dict = bs_lib.get_amazon_product_info(message)


##### 1.3.8.3.1. Amazon Product Adviser : Data Prepare :

      - [ML_Amazon_product_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_data_prepare.md)

##### 1.3.8.3.2. Amazon Product Adviser : Crawler

      - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md)

##### 1.3.8.3.3. Amazon Product Adviser : Classifier

      - [ML_Amazon_product_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Classifier.md)

##### 1.3.8.3.4. Amazon Product Adviser : Visualizer

       - [ML_Amazon_product_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Visualizer.md)

#### 1.3.8.4. Finance Insight

- 1. Extract insight from Finance data using ML

##### 1.3.8.4.1. Finance Insight : Data Prepare :

- [ML_Finance_Insight_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight/ML_Finance_Insight_data_prepare.md)

##### 1.3.8.4.2. Finance Insight : Crawler

- [ML_Finance_Insight_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight/ML_Finance_Insight_Crawler.md)

##### 1.3.8.4.3. Finance Insight : Classifier

- [ML_Finance_Insight_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight/ML_Finance_Insight_Classifier.md)

##### 1.3.8.4.4. Finance Insight : Visualizer

- [ML_Finance_Insight_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Finance_Insight/ML_Finance_Insight_Visualizer.md)

#### 1.3.8.5. Job Hunter

- 1.  Help user and hirer to better hunt for job.

##### 1.3.8.5.1. Job Hunter : Data Prepare :

- [ML_Job_Hunter_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_data_prepare.md)

##### 1.3.8.5.2. Job Hunter : Crawler

- [ML_Job_Hunter_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Crawler.md)

##### 1.3.8.5.3. Job Hunter : Classifier

- [ML_Job_Hunter_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Classifier.md)

##### 1.3.8.5.4. Job Hunter : Visualizer

- [ML_Job_Hunter_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Job_Hunter/ML_Job_Hunter_Visualizer.md)

## 1.4. Result

C:\Local\Work\Python\PyLib\NLP_master.py

##### 1.4.0.5.5. One liner

- Stream based webapp
- Container for all NLP work .

# 2. Work

## 2.1. -06

1. Add 4 future Master task. 10 min [T-24-06-1]

   1. rename py
   2. add 4 more
   3. 2 layer?
      NEXT
      1. Quick check on the radio instead of check box
      2. Quick Summary of structure .
      3. Layout, 2 separate layer of
      4. target : ML web, ML Master




