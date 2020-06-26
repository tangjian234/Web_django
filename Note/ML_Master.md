# 1. 1

- [ML_Master.md](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

## 1.2. Vision

    - Publish a in medium : key machine learning websites.
    - End to end design , arch and implement a ML system to solve a topic of interest.
    - My pet project.

## 1.3. Structure

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

### 1.3.8. PROJECT

#### 1.3.8.1. Name Nationality

- **Identify the nationality according to person's name**
- [ML_Name_Nationality](file:///c:/Local/Work/ML_Name/Note/ML_Name_Nationality.md)

##### 1.3.8.1.1. Name Nationality : Data Prepare :

     ###### Schoolers database
       - Download data from Schoolers database : [arxiv]
         - [ML_Name_Nationality_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_data_prepare.md)

     ###### 100 Chinese Name
       - Get 100 fixed Chinese last name:  100 ordinary name
         - [ML_Chinese_Name_100_names.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Chinese_Name_100_names.md)

##### 1.3.8.1.2. Name Nationality : Crawler

      - from web get the STEM names
        - [ML_Name_Nationality_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality/ML_Name_Nationality_Crawler.md)

##### 1.3.8.1.3. Name Nationality : Classifier

      -
      - [ML_Name_Nationality_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_Classifier.md)

##### 1.3.8.1.4. Name Nationality : Visualizer

      -
      - [ML_Name_Nationality_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Nationality/ML_Name_Nationality_Visualizer.md)

#### 1.3.8.2. Name Identification in a webpage

- [ML_Name_web_identification.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_web_identification.md)
  1. Identify the names presented in the webpage.

##### 1.3.8.2.1. Name Identification : Data Prepare :

      - [ML_Name_Identification_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_data_prepare.md)

##### 1.3.8.2.2. Name Identification : Crawler

      - [ML_Name_Identification_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Crawler.md)

##### 1.3.8.2.3. Name Identification : Classifier

      - [ML_Name_Identification_Classifier.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Classifier.md)

##### 1.3.8.2.4. Name Identification : Visualizer

      - [ML_Name_Identification_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Nationality_Visualizer.md)

#### 1.3.8.3. Amazon Product Adviser

- [ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)
  1. Chat bot on amazon search , help user to make wise decision :

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
