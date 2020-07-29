# 1. ML_Amazon_product_Crawler.md

- [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) )

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## 1.1. Todo

[09-07]

- - 1.  how to run proxy :
    2.  how to get the scrappy run, get the old work run
    3.  how to get header run
    4.
    5.  build a ps1 file , give a amazon link and get the product info open it using code

## 1.2. Vision

## 1.3. Objective

- develop anti -anti crawler

#### 1.3.0.1. Strategy.

[09-07]

1. Simple one : Run beautiful soup.

- - - bs_lib.py

2. More complex, long, comprehensive one runs crappy.

- develop anti -anti crawler

# 2. Scrappy 

## 2.1. Basic 

### 2.1.1. Basic run command 

scrappy crawl simple 
  - get the old work run

## 2.2. Logging 

### 2.2.1. ref 
  https://www.tutorialspoint.com/scrapy/scrapy_logging.htm

## 2.3. Setting 

- - 1. C:\Local\Work\Python\PyLib\scrapy\download\download\
    2.  [settings.py]

### 2.3.1. Normal parameters 
   1. in  [settings.py]
    OUTPUT_DIR='C:/Local/Work/material/Amazon/download/result/'
    
   1. `get_scrapy_setting()` 
   2. [conf_lib.py]    

#### 2.3.1.1. Howto
    from scrapy.utils.project import get_project_settings
    ID='OUTPUT_DIR'
    get_project_settings().get(ID)

### 2.3.2. how to get header run

- Multiple headers
  // STUB

### pass argument in scrapy crawl 

How to pass a user defined argument in scrapy spider

scrapy crawl myspider -a category='mycategory' -a domain='example.com'

### 2.3.3. How to run proxy

- - 1.  download `scrapy-rotating-proxies`
      - - [scrapy-proxy](https://blog.scrapinghub.com/scrapy-proxy)
        - [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)
    2.  Use a ROTATING_PROXY_LIST :
        1. in  [settings.py]
    3.  set the DOWNLOADER_MIDDLEWARES 
        1. in  [settings.py]
    4. Used Working proxy websit: 
       1. https://fanqiang.network/us-proxy  
          1.  "206.127.88.18:80",
               "35.230.21.108:80",
              '64.71.145.122:3128'
       http://spys.one/en/https-ssl-proxy/
        85.214.61.76:3128  
        https://free-proxy-list.net/
#### 3 ways of using proxy 
only work on simple doable issues : 

markdown hard issue to be done Um tomorrow
#### manual setting.
meta 



#### scrapy_proxy_pool
https://github.com/hyan15/scrapy-proxy-pool
#### rotating proxy 

##### reference 
- [using-a-custom-proxy-in-a-scrapy-spider](https://support.scrapinghub.com/support/solutions/articles/22000219743-using-a-custom-proxy-in-a-scrapy-spider)


- [EVERYTHING YOU NEED TO KNOW ABOUT USING A PROXY IN SCRAPY](https://limeproxies.com/blog/everything-about-using-proxy-in-scrapy/)

- [scrapy a specific url ](https://stackoverflow.com/questions/48146944/how-to-use-proxy-for-specific-url-in-scrapy-spider)

- [- summary](https://stackoverflow.com/questions/4710483/scrapy-and-proxies#:~:text=The%20easiest%20way%20to%20use,done%20depends%20on%20your%20shell.&text=1%2DCreate%20a%20new%20file,the%20following%20code%20to%20it.&text=Now%2C%20your%20requests%20should%20be%20passed%20by%20this%20proxy.)

### scrapy politely 
#### AutoThrottle

AutoThrottle extension
This is an extension for automatically throttling crawling speed based on load of both the Scrapy server and the website you are crawling.

- [howto](https://docs.scrapy.org/en/1.0/topics/autothrottle.html#autothrottle-extension)

    DOWNLOAD_DELAY = 1.5
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 2
    AUTOTHROTTLE_TARGET_CONCURRENCY = 6

#### DOWNLOAD_DELAY    

DOWNLOAD_DELAY = 1.5

### Beautiful Soup

- [Beautiful Soup and scrapy](https://www.datacamp.com/community/tutorials/amazon-web-scraping-using-beautifulsoup)

### 2.3.4. Use of Yaml 
<T-20 min>

#### 2.3.4.1. YAML Ain't Markup Language
  
  - `YAML` is a human-readable data-serialization language.
  -  It is commonly used for configuration files and in applications where data is being stored or transmitted.
    
#### 2.3.4.2. Simple file format : 

##### 2.3.4.2.1. Example      
- [scrappy_amazon_xpath.yaml]
    product_title:
      name: 
        attribute: id
        value:  productTitle
        text:  text() 
    product_info_table:
      name: 
        attribute: class
        value:  a-color-secondary a-size-base prodDetSectionEntry 
        text:  
          - text()
          - following-sibling::*//text()
             
#### 2.3.4.3. load file 
   1. `load_yaml_file()` 
   2. C:/Local/Work/Python/PyLib
   3. [conf_lib.py]    

#### 2.3.4.4. Access file 
   1. `get_xpath_item_conf()` 
   2. C:/Local/Work/Python/PyLib
   3. [scrapy_lib.py.py]   

##### 2.3.4.4.1. Example         
   attribute=xpath_conf['product_info_table']['name']['attribute']  
   output: attribute = class 

### 2.3.5. setup logging activity.

### 2.3.6. Use meta to transfer data 


### 2.3.7. Plan DONE 
  <T-15 min>
  5 record 

### 2.3.8. add manufacturer  DONE
 
<T-5 min>
  - [scrappy_amazon_xpath.yaml]
  - inside the product_info_table 


### 2.3.9. Retry DONE
- [retry](#239-retry-done)
<T-5 min>

#### File : 
- [quotes_spider.py]

#### What
- - 1. how to retry when the site refuse to serve :
       1.  robot check 
       2.   

#### Howto
- - 1. Get the title  
    1. If it has 'Robot' check : `retry`. 
    2. When you add that `dont_filter=True` , scrapy doesn't filter out the duplicate requests. So this time the request is processed.

##### Code example  
        title=response.xpath('//title/text()').get()
        if 'Robot' in title:
          print("------retry-----")
          yield scrapy.Request(url=response.url, callback=self.parse,dont_filter = True) 


### 2.3.10. local vs remote 
<T-10 min>

#### File : 
- [quotes_spider.py]

#### What

##### local vs remote Basic strategy : 
- [why](#local-vs-remote-basic-strategy-)
    - use remote download spider : simple  
      - first download min_html to local file : min_html
    - using simple_local  Process the min_html many times :
    - Why: 
      - dont get baned by run many times. 

##### Min_html: 
    - is the file that smallest html file that contain all necessary information. 
      1.  Example:   C:\Local\Work\material\Amazon\download\result\Quote-B07Z393DWN.html
  
##### Howto 
- - 1. Remote : 
      class Download_Test(scrapy.Spider):
          name = "simple" 

    2. Local :  
      class Download_Test_local(scrapy.Spider):
      name = "simple_local"

###  Min_html:  DONE
<T-10 min> 
#### What 
  - string operation and generate the min_html 
  - why see [why](#local-vs-remote-basic-strategy-)

#### Howto : 

##### Functions :  
  - Main function : `clean_html_body()` 
  - Removal of line break : `remove_line_break()`
    - line break for windows and unix :
      - \n|\r|\\n
    - re.sub(r'\n|\r|\\n', "", text)
  - Removal of content between blacklisted tags : `remove_content_between_tags()` : 
    - [settings.py]
      - BLACKLIST_TAGS= ['style','script','header','input']script, 


### Basic scrapy structure : 
<T-10 min> Done
#### File : 
- [quotes_spider.py]

#### hwo-to run 
  scrappy crawl simple 

#### 2 functions: 
##### Async request: 
- - 1. Async request: `start_requests()` : 
      - get the url list :
        - remote : http://
        - local : build local list : file://
      
      - launch request : 
           scrapy.Request(url=url, callback=self.parse) 
      
      - Request format :
        - url define   
        - call back function define 
        - meta : data passing  
##### process html response

    1. process html response :  `parse()`
       1. retry if necessary :
          1. why? see - [retry](#239-retry-done) 
       3. process : 
          1. remote : download min_html  
          2. local : extract product information from min_html
  

###  Add manufacturer  
<T-15 min> done 
  inside the product_info_table

###  Filter through the doc and sort
<T-10 min> <DONE>

#### File : 
- [quotes_spider.py]

## comment page 
### todo  
<T-15 min> <T+ 8:07>

#### rename 
product 
product_local
comment 
comment_local  


#### Move functions to scrapy_lib 
build_local_url_files

#### make a ps1 to goto scrapy. 

#### use of header : 
move to web_lib

### build the comment page link  
<T-20  min> <T+ 6:07>

#### Example : 

https://www.amazon.com/product-reviews/B07Z393DWN/ie=UTF8&filterByStar=one_star/ref=cm_cr_arp_d_viewopt_sr?filterByStar=one_star&pageNumber=1

- [scrapy_lib.build_comment_url]

### Get the comment by a new spider 
<T-20  min> <T+ 5:07>



### Get first page of a comment page . 
<T-25  min> 
no-reviews-section

#### find the xpath locator for next page. 
<T-15  min>

### Get next page of a comment page. 
<T-20  min>

## end 


### filter through the doc and sort
<T-10 min> 

#### File : 
- [scrapy_lib.py]


### Convert into web_lib  
#### File : 
- [scrapy_lib.py]

### scrape- hero

- overall structure on scrapy 

- [scrapehero](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

### user_agent 

#### wht is user agent 

The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

- [Definition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

#### Reference 

- [How to change user agent for Scrapy spiders](https://www.simplified.guide/scrapy/change-user-agent)

- [rotate user agent ](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

### 2.3.11. xpath : basic 
<T- 20 min>
 get_product_line_item

### 2.3.12. xpath : split and combine 

### 2.3.14. misc 

- - 1.  make crawler shortcut <DONE>
    1.  Fix web link <DONE>
    2.  curl <DONE>
    3.  make friends playlist <DONE>
    4.  quick sort the current existing work. 
    5.  close the tabs and save into <DONE>
    6.  clean desk : move stuff into 
    7.  list item : 
    8.  email to boss on latest process.
    9.  get the  

####  
- make crawler shortcut 


### hwo to use curl : 

####   Client URL
cURL (pronounced 'curl') is a computer software project providing a library (libcurl) and command-line tool (curl) for transferring data using various network protocols. The name stands for "Client URL", which was first released in 1997.

#### Proxy 
curl --proxy 205.185.116.235:8080 http://remote.example.org/

curl --proxy 205.185.116.235:8080 https://www.amazon.com/dp/B0791TX5P5

curl --proxy 205.185.116.235:8080 https://www.amazon.com/product-reviews/B0791TX5P5/ref=acr_dp_hist_1?ie=UTF8&filterByStar=one_star

#### Reference 
- [Everything curl](https://ec.haxx.se/usingcurl/usingcurl-proxies)

- [Using curl to automate HTTP jobs](https://curl.haxx.se/docs/httpscripting.html)

REVIEW : Question : how to make sense out of the curl output 

### mingw64 

- see mingw64 : a mini bash simulator  


### amazon super url 
Review : 
filterByStar=one_star 

STUB : complete according to example in *py

#### example 
https://www.amazon.com/product-reviews/B0791TX5P5/?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar

#### reference 
- [AMAZON SUPER URL](https://landingcube.com/amazon-super-url/)




# 3. Amazon information dictionary

## 3.1. Info 
https://webservices.amazon.com/paapi5/documentation/item-info.html#bylineinfo

https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/


ASIN : 
- title : id="productTitle"
- feature_list : id="feature-bullets"
- Brand: 
  - <a id="bylineInfo" class="a-link-normal" href="/AYL/b/ref=bl_dp_s_web_8188092011?ie=UTF8&amp;node=8188092011&amp;field-lbr_brands_browse-bin=AYL">Brand: AYL</a>
  - 
- manufacturer : 
  - <th class="a-color-secondary a-size-base prodDetSectionEntry">
Manufacturer
</th>
?? get the sibling 
- release_date : Date First Available 
  - 
- item_dimensions:
- size: 
- price : 
  - id="price_inside_buybox" 
  - <span class="a-size-base a-color-price">$21.99</span>

- rating : class_="reviewCountTextLinkedHistogram"
- no_of_comments : id="acrCustomerReviewText"
- producer : id="bylineInfo"
- best_seller_rank : id="SalesRank"
- link_to_all_reviews_in page : class_= a-expander-content reviewText review-text-content a-expander-partial-collapse-content


see : 
ByLineInfo
Brand 
Manufacturer
Contributors


## 3.2. xpath 
### 3.2.1. 
https://www.guru99.com/using-contains-sbiling-ancestor-to-find-element-in-selenium.html


productTitle

## 3.3. Amazon Product Advertising API

https://webservices.amazon.com/paapi5/documentation/quick-start/using-sdk.html




## 3.4. Reference
- [Scrapy 2.2 documentation](https://docs.scrapy.org/en/latest/index.html)
- [Scrapy 2.2 documentation: -logging ](https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-settings)
- [selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
- [Using your browser’s Developer Tools for scraping](https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools)

