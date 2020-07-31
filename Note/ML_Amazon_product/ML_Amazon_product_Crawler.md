# 1. ML_Amazon_product_Crawler.md

- [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) )

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)



- [ ] test 2 scraper in a same time 
- [x] Simple 
- [x] How to run proxy 
  - [x] - [Link](#234-how-to-run-proxy)
- [ ] Header 
## 1.1. Todo

- - 1.  how to run proxy :
    2.  how to get the scrappy run, get the old work run
    3.  how to get header run 
    5.  build a ps1 file , give a amazon link and get the product info open it using code

## 1.2. Vision

### 1.2.1. Result code 


- [Result code](C:\Local\Work\Python\PyLib\scrapy\download\download\spiders\quotes_spider.py)


## 1.3. Objective

- develop anti -anti crawler ： see 

#### 1.3.0.1. Strategy.

  1. Simple one : Run beautiful soup.

     - bs_lib.py

  2. More complex, long, comprehensive one runs scrappy.

      - quotes_spider.py

#### 1.3.0.2. Reference:  scrape- hero

- overall structure on scrapy 

- [scrapehero](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)



# 2. Scrappy 

## 2.1. Basic 

### 2.1.1. Basic run command 

    - scrappy crawl product : download product page 
    - scrappy crawl product_local : process local product page 
    - scrappy crawl comment : download comment page 
    - scrappy crawl comment_local :  process local comment page 

### 2.1.2. Basic scrapy structure : 

<T-10 min> Done
#### 2.1.2.1. File : 
- [quotes_spider.py]

#### 2.1.2.2. hwo-to run 
  scrappy crawl product 

#### 2.1.2.3. 2 functions: 
##### 2.1.2.3.1. Async request: 
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

##### 2.1.2.3.2. process html response

    1. process html response :  `parse()`
       1. retry if necessary :
          1. why? see - [retry](#239-retry-done) 
       3. process : 
          1. remote : download min_html  
          2. local : extract product information from min_html
  

## 2.2. Setting and configuration. 

- - 1. C:\Local\Work\Python\PyLib\scrapy\download\download\
    2.  [settings.py]
    3.  [conf_lib:yaml]

### 2.2.1. Pass argument in scrapy crawl 

  <Question:> How to pass a user defined argument in scrapy spider

  - scrapy crawl myspider -a category='mycategory' -a domain='example.com'
      -  Pass parameter : -a asin='mycategory'
      -  Get self.asin= getattr(self,'asin','')
      -  
### 2.2.2.  Normal parameters : settings.py:
   1. in  [settings.py]
    OUTPUT_DIR='C:/Local/Work/material/Amazon/download/result/'
    
   1. `get_scrapy_setting()` 
   2. OUTPUT_DIR = scrapy_lib.get_scrapy_setting('OUTPUT_DIR')
      1. OUTPUT_DIR_COMMENT
      2. INPUT_URL_LIST
      3. BLACKLIST_TAGS
   3. [quotes_spider.py]    

#### 2.2.2.1. Howto
    
    from scrapy.utils.project import get_project_settings
    ID='OUTPUT_DIR'
    get_project_settings().get(ID)

### 2.2.3. 2.2.2.How to get header run : web_lib.py
    - user agent 
    - [web_lib.py] 
    - get_random_header() 
      - HEADER_LIST ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36' ]

#### 2.2.3.1. user_agent 

##### 2.2.3.1.1. wht is user agent 

The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

- [Definition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

##### 2.2.3.1.2. Reference 

- [How to change user agent for Scrapy spiders](https://www.simplified.guide/scrapy/change-user-agent)

- [rotate user agent ](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

### 2.2.4.  How to run proxy :settings.py:

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

#### 2.2.4.1. 3 ways of using proxy 

#### 2.2.4.2. manual setting.
  meta : set 
        self.header = {'User-Agent': user_agent}
        self.meta_proxy= {"proxy":"207.144.111.230:8080"} 
    
    #yield scrapy.Request(url=url, callback=self.parse,headers=self.header,meta=self.meta_proxy)


#### 2.2.4.3. scrapy_proxy_pool
https://github.com/hyan15/scrapy-proxy-pool

#### 2.2.4.4. rotating proxy 

##### 2.2.4.4.1. reference 
- [using-a-custom-proxy-in-a-scrapy-spider](https://support.scrapinghub.com/support/solutions/articles/22000219743-using-a-custom-proxy-in-a-scrapy-spider)


- [EVERYTHING YOU NEED TO KNOW ABOUT USING A PROXY IN SCRAPY](https://limeproxies.com/blog/everything-about-using-proxy-in-scrapy/)

- [scrapy a specific url ](https://stackoverflow.com/questions/48146944/how-to-use-proxy-for-specific-url-in-scrapy-spider)

- [- summary](https://stackoverflow.com/questions/4710483/scrapy-and-proxies#:~:text=The%20easiest%20way%20to%20use,done%20depends%20on%20your%20shell.&text=1%2DCreate%20a%20new%20file,the%20following%20code%20to%20it.&text=Now%2C%20your%20requests%20should%20be%20passed%20by%20this%20proxy.)


### 2.2.5. Use of Yaml 
<T-20 min>

#### 2.2.5.1. YAML Ain't Markup Language
  
  - `YAML` is a human-readable data-serialization language.
  -  It is commonly used for configuration files and in applications where data is being stored or transmitted.
    
#### 2.2.5.2. Simple file format : 

##### 2.2.5.2.1. Example      
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
             
#### 2.2.5.3. load file 
   1. `load_yaml_file()` 
   2. C:/Local/Work/Python/PyLib
   3. [conf_lib.py]    

#### 2.2.5.4. Access file 
   1. `get_xpath_item_conf()` 
   2. C:/Local/Work/Python/PyLib
   3. [scrapy_lib.py.py]   

##### 2.2.5.4.1. Example         
   attribute=xpath_conf['product_info_table']['name']['attribute']  
   output: attribute = class 

#### 2.2.5.5. Product xpath : 
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

#### 2.2.5.6. Reference 
https://webservices.amazon.com/paapi5/documentation/item-info.html#bylineinfo

https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/

 

### 2.2.6. scrapy politely : anti crawl detection 

#### 2.2.6.1. AutoThrottle

AutoThrottle extension
This is an extension for automatically throttling crawling speed based on load of both the Scrapy server and the website you are crawling.

- [howto](https://docs.scrapy.org/en/1.0/topics/autothrottle.html#autothrottle-extension)

    DOWNLOAD_DELAY = 1.5
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 2
    AUTOTHROTTLE_TARGET_CONCURRENCY = 6

#### 2.2.6.2. DOWNLOAD_DELAY    

DOWNLOAD_DELAY = 1.5

### 2.2.7. Beautiful Soup

- [Beautiful Soup and scrapy](https://www.datacamp.com/community/tutorials/amazon-web-scraping-using-beautifulsoup)

### 2.2.8. Retry if robot.txt 

<T-5 min>

#### 2.2.8.1. File : 
- [quotes_spider.py]

#### 2.2.8.2. What
- - 1. how to retry when the site refuse to serve :
       1.  robot check 
       2.   

#### 2.2.8.3. Howto
- - 1. Get the title  
    1. If it has 'Robot' check : `retry`. 
    2. When you add that `dont_filter=True` , scrapy doesn't filter out the duplicate requests. So this time the request is processed.

##### 2.2.8.3.1. Code example  
        title=response.xpath('//title/text()').get()
        if 'Robot' in title:
          print("------retry-----")
          yield scrapy.Request(url=response.url, callback=self.parse,dont_filter = True) 


## 2.3. Amazon page processing 
- - 1. build link strings 
  - 2. process product page 
    3. process comment page  

### 2.3.1. Link String operation 
 
#### 2.3.1.1. create local url from web url 
  - in download product class 
  - get_file_name_from_url(response.url)
  - f_name='Quote-%s.html' % id
  

#### 2.3.1.2. create local url from web urls lists 
 - in download product_local class 
 - build_local_url_files(urls,OUTPUT_DIR)

#### 2.3.1.3. create comment url 
  - in Download_comment class 
  - build_comment_url(asin,star_id,page_num) 
    - in start_requests()
  
  - get_comment_file_name_from_url(asin,star_id,page_num)
    - in parse()

#### 2.3.1.4. create local comment file name 
  - in Download_Test_comment_local class 
  - get_local_comment_names(dir,asin,star_id)
  - 


### 2.3.2. local vs remote 
<T-10 min>

#### 2.3.2.1. File : 
- [quotes_spider.py]

#### 2.3.2.2. What

##### 2.3.2.2.1. local vs remote Basic strategy : 
- [why](#local-vs-remote-basic-strategy-)
    - use remote download spider : simple  
      - first download min_html to local file : min_html
    - using simple_local  Process the min_html many times :
    - Why: 
      - dont get baned by run many times. 

##### 2.3.2.2.2. Min_html: 
    - is the file that smallest html file that contain all necessary information. 
      1.  Example:   C:\Local\Work\material\Amazon\download\result\Quote-B07Z393DWN.html
  
##### 2.3.2.2.3. Howto 
- - 1. Remote : 
      class Download_Test(scrapy.Spider):
          name = "product" 

    2. Local :  
      class Download_Test_local(scrapy.Spider):
      name = "product_local"

###  2.3.3. Min_html : HTML file processing   

<T-10 min> 
#### 2.3.3.1. What 
  - string operation and generate the min_html 
  - why see [why](#local-vs-remote-basic-strategy-)

#### 2.3.3.2. Howto : 

##### 2.3.3.2.1. Functions :  
  - Main function : `clean_html_body()` 
  - Removal of line break : `remove_line_break()`
    - line break for windows and unix :
      - \n|\r|\\n
    - re.sub(r'\n|\r|\\n', "", text)
  - Removal of content between blacklisted tags : `remove_content_between_tags()` : 
    - [settings.py]
      - BLACKLIST_TAGS= ['style','script','header','input']
      - 

#### 2.3.3.3. File : 
  - [quotes_spider.py]


###  2.3.4. Download Remote product page  

#### 2.3.4.1. Get product page . 
  - get a list of urls  
  - build a local file name 
  - clean the script and style
  - save a local html 
  - 
###  2.3.5. Process product page  
  
  - get_amazon_product_info_string(txt,xpath_conf)
  - use xpath processing - [Link](#245-xpath--basic) 
  - scrapy crawl product_local

#### 2.3.5.1. product info table 
get_product_info_table

#### 2.3.5.2. product description 
get_product_description_table

#### 2.3.5.3. Get customer review 

##### 2.3.5.3.1. Get customer star percentage  
get_product_review_percent_table

##### 2.3.5.3.2. Get customer detail 
get_product_customer_review_card


###  2.3.6. Download Remote Comment page  

#### 2.3.6.1. Comment Link  Example : 

https://www.amazon.com/product-reviews/B07Z393DWN/ie=UTF8&filterByStar=one_star/ref=cm_cr_arp_d_viewopt_sr?filterByStar=one_star&pageNumber=1

- [scrapy_lib.build_comment_url]

#### 2.3.6.2. Get the comment by a new spider 

#### 2.3.6.3. Get first page of a comment page . 
  - give a asin , build a link 
  - build a local page, 
  - clean the script and style
  - save a local html 
  
#### 2.3.6.4. find the xpath locator for next page. 

 next_page=response.url.replace(f'pageNumber={self.page_num}',f'pageNumber={self.page_num+1}')

#### 2.3.6.5. Get next page of a comment page. 
 if (next_page): 
  next_page=response.url.replace(f'pageNumber={self.page_num}',f'pageNumber={self.page_num+1}')
 next page numbering

###  2.3.7. Process Comment page  

#### 2.3.7.1. Browser operation : get the xpath 

#####  2.3.7.1.1. xpal : chrome  
- - 1. 
    2.  
#####  2.3.7.1.2. firefox 
- - 1. Example  
    2.  
##### 2.3.7.1.3. chrome 

### 2.3.8. xpath :

####  2.3.8.1. basic 
 - example : get_product_line_item()
 - use yaml file to build the xpath string : 
 - example : 
    xpath_string=f'//{tag}[contains(@{attribute},"{value}")]'

  - see: xpath_location_builder(attribute='id',value='',tag = '*'):s


#### 2.3.8.2. Step : 
  1. Go to basic location : xpath_builder
  2. Get all following text(): xpath_location_get_text

####  2.3.8.3. Split and combine  

get_product_info_table

#### 2.3.8.4. Locate the location anchor : 

location = xpath_location_builder(attribute,value)

#### 2.3.8.5. Example 
 - Use for  Concatenation of different lines.
  title = [
  " ".join(item.xpath(text[1]))
  for item in 
  response.xpath(location) ]

#### 2.3.8.6. Get the individual fields. 

  for i in title :
    r=re.compile('(.*?)--(.*?)out of 5 stars--\s+--(.*?)--\s+--(.*?)--(.*?)--\s+--(.*?)--')
    (name,star,title,review_time,verified,content)=r.search(i).groups()
    #print('name', name,star,title,review_time,verified,content)
    s= (name,star,title,review_time,verified,content)

#### 2.3.8.7. regex : 
  - Lazy match (.*?)


## 2.4. Tools 

### 2.4.1. hwo to use curl : 

####   2.4.1.1. Client URL
cURL (pronounced 'curl') is a computer software project providing a library (libcurl) and command-line tool (curl) for transferring data using various network protocols. The name stands for "Client URL", which was first released in 1997.

#### 2.4.1.2. Proxy 
curl --proxy 205.185.116.235:8080 http://remote.example.org/

curl --proxy 205.185.116.235:8080 https://www.amazon.com/dp/B0791TX5P5

curl --proxy 205.185.116.235:8080 https://www.amazon.com/product-reviews/B0791TX5P5/ref=acr_dp_hist_1?ie=UTF8&filterByStar=one_star

#### 2.4.1.3. Reference 
- [Everything curl](https://ec.haxx.se/usingcurl/usingcurl-proxies)

- [Using curl to automate HTTP jobs](https://curl.haxx.se/docs/httpscripting.html)

REVIEW : Question : how to make sense out of the curl output 

### 2.4.2. mingw64 

- see mingw64 : a mini bash simulator  
 
## 2.5. Reference
- [Scrapy 2.2 documentation](https://docs.scrapy.org/en/latest/index.html)
- [Scrapy 2.2 documentation: -logging ](https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-settings)
- [selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
- [Using your browser’s Developer Tools for scraping](https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools)

- [Amazon Product Advertising API](https://webservices.amazon.com/paapi5/documentation/quick-start/using-sdk.html)
- [xpath](https://www.guru99.com/using-contains-sbiling-ancestor-to-find-element-in-selenium.html)
 
### 2.5.1. amazon super url 
Review : 
filterByStar=one_star 

STUB : complete according to example in *py

#### 2.5.1.1. example 
https://www.amazon.com/product-reviews/B0791TX5P5/?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar

#### 2.5.1.2. reference 
- [AMAZON SUPER URL](https://landingcube.com/amazon-super-url/)
