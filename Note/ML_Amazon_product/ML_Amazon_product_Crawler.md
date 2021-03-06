# ML_Amazon_product_Crawler.md
**shortcut crawl.ps1**  

- [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) 

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)


## Structure Hi mom

  ### Parent
    - [Master](file:///c:/Local/Work/ML_Name/Note/ML_Master.md)  
    - [mm.md](file:///C:/Local/Work/Key_Tools/Note/mm.md) 
    - [ML_todo.md](file:///C:/Local/Work/Key_Docs/Todo/ML_todo.md)
      
  ### Sibling 

  ##### Amazon

    - [**ML_Amazon_product_adviser_chat_bot.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_adviser_chat_bot.md)  
  - [*ML_Amazon_Train_Extract_skill_from_CV.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_Train_Extract_skill_from_CV.md)  
    - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md) 


    - [ML_ebay_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_ebay_product_Crawler.md)   
    - [ML_Amazon_product_data_prepare.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_data_prepare.md)
    - [ML_Amazon_product_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Visualizer.md) 
    - [∞](#)

## Todo

  - [ ] test 2 scraper in a same time 
  - [x] Simple 
  - [x] How to run proxy 
    - [x] - [Link](#234-how-to-run-proxy)
  - [x] Header 
  - [x] full review 
  - [x] Save the result into a json file : 
  - [ ] Return download the ASIN page 
  - [ ] Periodically Product info monitoring 
    -    - [∞](#periodically-product-info-monitoring)
  - [ ] Review amazon native api: [Amazon_API](#amazon-native-api)
  - [ ] Review scrape hero : [Scrapehero]
  - [ ] Review amazon super URL.[_](#amazon-super-url) 
  - [ ] ebay :  Make a ebay bidding app 
  - [ ] VPN for scraping - [∞](#vpn-for-scraping)


  
## Vision

  ### Result code 

    - [Result code](C:\Local\Work\Python\PyLib\scrapy\download\download\spiders\quotes_spider.py)


## Objective

  - develop anti -anti crawler ： see 
  - - 1.  how to run proxy :
      1.  how to get the scrappy run, get the old work run
      2.  how to get header run 
      3.  build a ps1 file , give a amazon link and get the product info open it using code
   1. Use Scrapy to crawl amazon product info : later version 
  
  ### Strategy.

    1. Simple one : Run beautiful soup.

       - bs_lib.py

    2. More complex, long, comprehensive one runs scrappy.

        - quotes_spider.py

  ### Reference:  scrape- hero

  - overall structure on scrapy 

  - [scrapehero](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)


## Basic 
  // MARK : Basic run command 
  
  ### Result

      - [Result code](../../../Python/pylib/scrapy/download/download/spiders/quotes_spider.py) 
      - [scrapy_lib.py](../../../Python/pylib/scrapy_lib.py)
      - [string_lib.py](../../../Python/pylib/string_lib.py)
      - [web_lib.py](../../../Python/pylib/web_lib.py)

  ### Basic run command 
      
      - scrapy crawl product : download product page 
      - scrapy crawl product_local : process local product page 
      - scrapy crawl comment : download comment page 
      - scrapy crawl comment_local :  process local comment page 

  ### Basic scrapy structure : 

  #### File : 
  - [quotes_spider.py](../../../Python/pylib/scrapy/download/download/spiders/quotes_spider.py)

  #### hwo-to run 

    scrappy crawl product 

  #### 2 Functions: 

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
    

## Setting and configuration. 
// MARK:　Setting and configuration. 
  
  ###  Setting file 
  
  // NOTE: Setting file  

  - 1. C:\Local\Work\Python\PyLib\scrapy\download\download\
    2.  [settings.py](../../../Python/pylib/scrapy/download/download/settings.py)
    3.  [conf_lib:yaml](../../../Python/pylib/conf_lib.py)

  ### Pass argument in scrapy crawl 

    <Question:> How to pass a user defined argument in scrapy spider

    - scrapy crawl myspider -a category='mycategory' -a domain='example.com'
        -  Pass parameter : -a asin='mycategory'
        -  Get self.asin= getattr(self,'asin','')
        -  

  ### Normal parameters : settings.py:
// NOTE: Setting : 
    1. in  [settings.py]
      OUTPUT_DIR='C:/Local/Work/material/Amazon/download/result/'
      
    1. `get_scrapy_setting()` 
    2. OUTPUT_DIR = scrapy_lib.get_scrapy_setting('OUTPUT_DIR')
        1. OUTPUT_DIR_COMMENT
        2. INPUT_URL_LIST
        3. BLACKLIST_TAGS
    
    3. [quotes_spider.py]    

  #### Howto
      
      from scrapy.utils.project import get_project_settings
      ID='OUTPUT_DIR'
      get_project_settings().get(ID)

  ### How to get header run : web_lib.py
      - user agent 
      - [web_lib.py] 
      - get_random_header() 
        - HEADER_LIST ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36' ]

  #### user_agent 

  ##### wht is user agent 

  The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

  - [Definition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

  ##### Reference 

  - [How to change user agent for Scrapy spiders](https://www.simplified.guide/scrapy/change-user-agent)

  - [rotate user agent ](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

  ### How to run proxy :settings.py:

  - - 1.  download `scrapy-rotating-proxies`
        - - [scrapy-proxy](https://blog.scrapinghub.com/scrapy-proxy)
          - [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)
      2.  Use a ROTATING_PROXY_LIST :
          1. in  [settings.py]
      3.  set the DOWNLOADER_MIDDLEWARES 
          1. in  [settings.py]
      4. Used `Working proxy website`: 
        1. https://fanqiang.network/us-proxy  
            1.  "206.127.88.18:80",
                "35.230.21.108:80",
                '64.71.145.122:3128'
        http://spys.one/en/https-ssl-proxy/
          85.214.61.76:3128  
          https://free-proxy-list.net/

  #### 3 ways of using proxy 

  ##### manual setting.
    meta : set 
          self.header = {'User-Agent': user_agent}
          self.meta_proxy= {"proxy":"207.144.111.230:8080"} 
      
      #yield scrapy.Request(url=url, callback=self.parse,headers=self.header,meta=self.meta_proxy)


  ##### scrapy_proxy_pool

  - [scrapy-proxy-pool](https://github.com/hyan15/scrapy-proxy-pool)

  ##### rotating proxy 

  #### Reference 
  - [using-a-custom-proxy-in-a-scrapy-spider](https://support.scrapinghub.com/support/solutions/articles/22000219743-using-a-custom-proxy-in-a-scrapy-spider)


  - [EVERYTHING YOU NEED TO KNOW ABOUT USING A PROXY IN SCRAPY](https://limeproxies.com/blog/everything-about-using-proxy-in-scrapy/)

  - [scrapy a specific url ](https://stackoverflow.com/questions/48146944/how-to-use-proxy-for-specific-url-in-scrapy-spider)

  - [- summary](https://stackoverflow.com/questions/4710483/scrapy-and-proxies#:~:text=The%20easiest%20way%20to%20use,done%20depends%20on%20your%20shell.&text=1%2DCreate%20a%20new%20file,the%20following%20code%20to%20it.&text=Now%2C%20your%20requests%20should%20be%20passed%20by%20this%20proxy.)

  
  


  
  
  web_lib.py

    - https://github.com/clarketm/proxy-list

  ### Summarize the proxy download and validity check

  #### Proxy Information : 
  // TODO : Proxy information : 
    - elite : 
    - https : 
  
  #### what
    1. download proxy from sites and 
    2. run checking to see if it is working. 


  #### Proxy sites : 
  -  list site that You can find proxies
    - // TODO : list site that You can find proxies
  
  #### 
  
  - find working proxy from site by running 
    -  Gather 20 proxy. 
    -  lib/proxy_check.py. 
  
  #### Hwoto

    scrapy_lib.get_proxy_from_sites()
    download from sites 

    1. file: 
        1. lib/proxy_check.py 
        2. scrapy_lib.py : 
    2. input: NONE
    3. output : validated proxy list :  
    
    4. Key function : 
       1. scrapy_lib.get_proxy_from_sites
        download https proxy from 2 websites : 100 each time
	     1. scrapy_lib.check_proxy_list_validity 

    5. add the list to : 
        1. c:\Local\Work\Python\PyLib\scrapy\download\download\settings.py 

    6. save the final result in 
        1.  c:\Local\Work\Python\PyLib\scrapy\download\download\valid_proxy_list_save.py

  #### Learnt : 
      -  
  12812 NE, 113th ST , Kirkland, WA,98033

  ### Use Nordvpn as proxy 
  // NOTE:  nordvpn
  
    - Get use the united states #5294 : work 
    - which nordvpn work 
  
  #### Select 10 working nordvpn 
      - #5294 YES 
      - #5280 YES 
      
      - #8158 NO 
  
  scrapy crawl product
  
  ### Use of Yaml 

  <T-20 min>

  #### YAML Ain't Markup Language
    
    - `YAML` is a human-readable data-serialization language.
    -  It is commonly used for configuration files and in applications where data is being stored or transmitted.
      
  #### Simple file format : 

  ##### Example      
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
              
  #### load file 
    1. `load_yaml_file()` 
    2. C:/Local/Work/Python/PyLib
    3. [conf_lib.py]    

  #### Access file 
    1. `get_xpath_item_conf()` 
    2. C:/Local/Work/Python/PyLib
    3. [scrapy_lib.py]   

  ##### Example         
    attribute=xpath_conf['product_info_table']['name']['attribute']  
    output: attribute = class 

  #### Product xpath : 
  ASIN : 
    1. title : 
      1. id="productTitle"
    2. feature_list : 
      1. id="feature-bullets"
    3. Brand: 
      1. List : 
          1. - <a id="bylineInfo" class="a-link-normal" href="/AYL/b/ref=bl_dp_s_web_8188092011?ie=UTF8&amp;node=8188092011&amp;field-lbr_brands_browse-bin=AYL">Brand: AYL</a>
      - 
    4. manufacturer : 
      - <th class="a-color-secondary a-size-base prodDetSectionEntry">
    </th>
        ?? get the sibling 
        - release_date : Date First Available 
          - 
    5. item_dimensions:
    6. size: 
    7. price : 
      - id="price_inside_buybox" 
      - <span class="a-size-base a-color-price">$21.99</span>

    8. rating : 
      1. class_="reviewCountTextLinkedHistogram"
    9.  no_of_comments : 
        1.  id="acrCustomerReviewText"
    10. producer : 
        1.  id="bylineInfo"
    11. best_seller_rank : 
        1.  id="SalesRank"
    12. link_to_all_reviews_in page : 
        1.  class_= a-expander-content reviewText review-text-content a-expander-partial-collapse-content

  #### Reference 

  - [Amazon_API](https://webservices.amazon.com/paapi5/documentation/item-info.html#bylineinfo)
  - [Scrapehero](https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/)
  

  ### scrapy politely : anti crawl detection 

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

  ### Retry if robot.txt 

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


## Amazon page processing 
// MARK:　Page processing 

  - 1. build link strings 
  - 2. process product page 
    3. process comment page  


  ### Link String operation 
  
  #### create local url from web url 
    - in download product class 
    - get_file_name_from_url(response.url)
    - f_name='Quote-%s.html' % id
    

  #### create local url from web urls lists 
  - in download product_local class 
  - build_local_url_files(urls,OUTPUT_DIR)

  #### create comment url 
    - in Download_comment class 
    - build_comment_url(asin,star_id,page_num) 
      - in start_requests()
    
    - get_comment_file_name_from_url(asin,star_id,page_num)
      - in parse()

  #### create local comment file name 
    - in Download_Test_comment_local class 
    - get_local_comment_names(dir,asin,star_id)
    - 


  ### local vs remote 
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
            name = "product" 

      2. Local :  
        class Download_Test_local(scrapy.Spider):
        name = "product_local"

  ###  Min_html : HTML file processing   

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
        - BLACKLIST_TAGS= ['style','script','header','input']
        - 

  #### File : 
    - [quotes_spider.py]

  - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md)[](） 

  ###  Download Remote product page  
    - [∞](#download-remote-product-page)
  #### Get product page . 
    - get a list of urls  
    - build a local file name 
    - clean the script and style
    - save a local html 
    - 
  ###  Process product page  
    
    - get_amazon_product_info_string(txt,xpath_conf)
    - use xpath processing - [Link](#245-xpath--basic) 
    - scrapy crawl product_local

  #### product info table 
  get_product_info_table

  #### product description 
  get_product_description_table

  #### Get customer review 

  ##### Get customer star percentage  
  get_product_review_percent_table

  ##### Get customer detail 
  get_product_customer_review_card

  ### merge and run product_all for periodically
    - product_all
    - product_remote
    - product_local 

  #### hwoto
    - process_save_from_text() : 
      - save into product info dictionary as in product_local



  ###  run multiple period

  https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679

  pip install timeloop

  scrapy schedule periodical program

    scrapy-do-cl schedule-job --project download --spider product --when 'every 1 to 2 minutes'
    
    scrapy-do-cl schedule-job --project quotesbot --spider toscrape-css --when 'every 5 to 15 minutes' scrapy schedule periodical program

  #### my curl
  C:\Users\tangj_1iyy\AppData\Local\Apps\cURL\bin\mycurl http://localhost:6800/schedule.json -d project=download -d spider=product

  #### reference 

  ##### Howto 
  - [GitHub - scrapy/scrapyd: A service daemon to run Scrapy spiders](https://github.com/scrapy/scrapyd)

  ##### Documentation
  - [Scrapyd — Scrapyd 1.2.0 documentation](https://scrapyd.readthedocs.io/en/stable/)
  - [Scrapyd — Scrapy 2.3.0 documentation](https://docs.scrapy.org/en/latest/topics/scrapyd.html)
  - [GitHub - scrapy/scrapyd-client: Command line client for Scrapyd server](https://github.com/scrapy/scrapyd-client)

  ##### Youtube  
  - [Deploy Scrapy spiders locally - Scrapyd - YouTube](https://www.youtube.com/watch?v=PZKH5S0C8EI)

  - [Introduction to Scrapy API | Practical Python Web Scraping Tutorial (Part 1 of 2) - YouTube](https://www.youtube.com/watch?v=lNajD34Sfmg)

  #####  Tutorial
  - [A Minimalist End-to-End Scrapy Tutorial (Part IV) | by Harry Wang | Towards Data Science](https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-iv-3290d76a2aef)


  ### Use python command to run spider. 
  c:\Local\Work\Python\PyLib\scrapy\download\download
  https://stackoverflow.com/questions/21662689/scrapy-run-spider-from-script
  #### what
   
  #### hwoto
   - search ''

  ### Proxy checker : 
  [45_min]



    #### Objective 

    1. understand the Proxy checker 

    #### Howto

    1. move the paraser and modularize it .  [15_min]  
        - input_arg_lib.py 
    2. decompose the checker 
    3. removal global veriable    - 
    4. merge checker with downloader into proxy_list_lib
        1. 
    5. integrate the proxyChecker.py 
        1. run and only get 10 valid proxy address 
    6. modify settings and load proxy_list_it 
    
    #### what

    1. Reference : https://github.com/iw4p/proxy-scraper
    2. Local : C:\Local\Work\Python\PyLib\proxy-scraper-master
    3. run : 
        1. Get the scrap
          1. python proxyScraper.py -p https
        2. Check the validity of the 
          1. python proxyChecker.py -p https -t 20 -s amazon.com -i input.txt 
        3. rsp.ps1 product
        4. rsp.ps1 product_local

    #### Result

    1. move the paraser and modularize it 
    2.   
        1. https://www.simplifiedpython.net/python-threading-example/#:~:text=Python%20Threading%20Example%201%20Step%20%231%3A%20Import%20threading,the%20thread%20after%20completion%20of%20the%20task.%20
    3. merge checker with downloader into proxy_list_lib
    4. remove 



  ### run python in the background 

    #### hwoto
        - [How to constantly run Python script in the background on Windows?](https://stackoverflow.com/questions/59125493/how-to-constantly-run-python-script-in-the-background-on-windows)
    #### example 
        pythonw.exe pythonw.exe C:\\Python\Scripts\moveDLs.py




  #### Test the process

  ####  the process
  Get-Process -Name pythonw
  #### Kill the process 
  Stop-Process -Name pythonw

  https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/stop-process?view=powershell-7


  C:\Local\Work\material\Amazon\download\result

  ### Import with path 

  ###  Use python command to run spider. 
  .\run_per.py

  ###  Use Asych-scheduler to run periodically 
  .\run_per.py


  ### ScrapydWeb by my8100 



  ###  Download Remote Comment page  

  #### Comment Link  Example : 

  https://www.amazon.com/product-reviews/B07Z393DWN/ie=UTF8&filterByStar=one_star/ref=cm_cr_arp_d_viewopt_sr?filterByStar=one_star&pageNumber=1

  - [scrapy_lib.build_comment_url]

  #### Get the comment by a new spider 

  #### Get first page of a comment page . 
    - give a asin , build a link 
    - build a local page, 
    - clean the script and style
    - save a local html 
    
  #### find the xpath locator for next page. 

  next_page=response.url.replace(f'pageNumber={self.page_num}',f'pageNumber={self.page_num+1}')

  #### Get next page of a comment page. 
  if (next_page): 
    next_page=response.url.replace(f'pageNumber={self.page_num}',f'pageNumber={self.page_num+1}')
  next page numbering

  ###  Process Comment page  

  #### Browser operation : get the xpath 

  #####  xpal : chrome  
  - - 1. 
      2.  
  #####  firefox 
  - - 1. Example  
      2.  
  ##### chrome 

  ### xpath :

####  basic 
 - example : get_product_line_item()
 - use yaml file to build the xpath string : 
 - example : 
    xpath_string=f'//{tag}[contains(@{attribute},"{value}")]'

  - see: xpath_location_builder(attribute='id',value='',tag = '*'):s

#### Step : 
  1. Go to basic location : xpath_builder
  2. Get all following text(): xpath_location_get_text

####  Split and combine  

get_product_info_table

#### Locate the location anchor : 

location = xpath_location_builder(attribute,value)

#### Example 
 - Use for  Concatenation of different lines.
  title = [
  " ".join(item.xpath(text[1]))
  for item in 
  response.xpath(location) ]
<xref:UID>
#### Get the individual fields. 

  for i in title :
    r=re.compile('(.*?)--(.*?)out of 5 stars--\s+--(.*?)--\s+--(.*?)--(.*?)--\s+--(.*?)--')
    (name,star,title,review_time,verified,content)=r.search(i).groups()
    #print('name', name,star,title,review_time,verified,content)
    s= (name,star,title,review_time,verified,content)

#### regex : 
  - Lazy match (.*?)
[](#myheader)


  ### Amazon super url 
  
  Review : 
  filterByStar=one_star 

  STUB : complete according to example in *py

  #### example 
  https://www.amazon.com/product-reviews/B0791TX5P5/?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar

  #### reference 
  - [AMAZON SUPER URL](https://landingcube.com/amazon-super-url/)

  ### Amazon Native API
  - [Amazon_API](https://webservices.amazon.com/paapi5/documentation/item-info.html#bylineinfo)

  ### Amazon Scrape hero 

  objective : review the structure 
  - [Scrapehero](https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/)

## Amazon Periodic download in Raspberry pi

// MARK: Amazon Periodic download 

  ### Objective 
     1. Ability to download Amazon ASIN list in Raspberry pi
     2. Work Periodically
     3. 
  
  ### Planning 

  #### what

    1. periodically download product and get price etc 
    2. 
  #### Steps   
  
  #### Howto

    1. every 10 min as test : 
    2. - scrappy crawl product 
    3. - scrappy crawl product_local : 
        1. Save 
          1. the price ,   
          2. best seller rank bsr 
          3. number of  review. 
        2. with time mark 
      4. save as same product_
      5. create a file_with time_stamp  
        1. fix the time stamp issue 

  #### Result 
  run Output : - C:\Local\Work\ML_Name\Code\Test\data\asin 

  #### Run periodically with task Scheduler :  windows 
    - [∞](#run-periodically-with-task-scheduler--windows)

  ##### what
    - the price item in the task Scheduler.  
    - run 
      - start with c:\Local\Work\Python\PyLib\scrapy\download\
      - C:\Python38\Scripts\scrapy.exe crawl product
      - C:\Python38\Scripts\scrapy.exe crawl product

  - provide a list of top 10 best seller 

  ##### task scheduler security context

  #### Run periodically with task Scheduler : python  
  apscheduler
  
  https://stackoverflow.com/questions/44228851/scrapy-on-a-schedule

  https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679

  https://stackoverflow.com/questions/44228851/scrapy-on-a-schedule

  You can use 

  https://www.programmersought.com/article/51911377370/

  ##### Run Async 

  #### Proxy 


  ### Plan   
  
     1.   Install library : see [.](#fix-lib-problem-in-raspberry-pi)
     2.   Activate Nordvpn : see [](#vpn-for-scraping)   
     3.   Simple run a run_per.py [](#simple-run-a-run_perpy---apscheduler)    
          1.  Run every 10 min 
          2.  prepare for everyday running for amazon asin download 
     4.  Work Together with django [](#work-together-with-django)
  

  ### Rerun and port scrappy in windows 
    
  #### Find pervious Scheduler in windows 
      - C:\Local\Work\Python\PyLib\scrapy\download\download\spiders\run_per.py 
   
  #### Rerun Amazon  
  // NOTE: Amazon rerun 
    
  #####  Go to Amazon directory : 
      - spider.ps1  : go to spider directory 
      - lib : go to python library directory 
    
  #####  Setting :     
      - INPUT_URL_LIST :
        - 'C:/Local/Work/material/Amazon/download/url_list.json' 
        - asin_list
        - asin_list_best_seller_bluetooth
      - OUTPUT_DIR : 'C:/Local/Work/material/Amazon/download/result/'
        
  #####  Run : in folder : 
      - in folder : C:\Local\Work\Python\PyLib\scrapy\download\download\spiders
      - scrapy crawl product
      - scrapy crawl product_local

  #### Find hwoto run best proxies 
      - proxy list : 
  
  #### Disable Proxy and enable nordvpn  
      - scrapy crawl product
      - enable nordvpn  
      - disabled proxy 
      - see [Use Nordvpn as proxy](#Use-Nordvpn-as-proxy-)
      


   #### Add comment and underhand to run_spider_1() 
    - C:\Local\Work\Python\PyLib\scrapy\download\download\spiders\run_per.py 
    - python3  run_per.py

   #### Make relative file directory : 
    - 
   #### Re-verify it work in windows  
    - DONE 

  ### Make library work 

  ### Install Raspberry pi streamlit

  Raspberry pi streamlit
  https://discuss.streamlit.io/t/raspberry-pi-streamlit/2900?page=2

  ####  Install the dependency
    1. sudo apt-get install libatlas-base-dev
  
  ####  Install the dependency
    pip install streamlit 

  ### Run and port scrappy in Raspberry pi
   
   #### Install scrapy into Raspberry pi
    https://peppe8o.com/use-raspberry-pi-as-your-personal-web-crawler-with-python-and-scrapy/
    
    - sudo apt install python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    - sudo pip3 install scrapy

   scrapy crawl product
   
   #### Install lib module in Raspberry pi
   - - inside cut_env environment 

   - list of lib to be installed for in Raspberry pi 
    
    -  First try in the local PC , pip install, to make sure  
    -  Raspberry pi install take long time 
   
    pip install scrapy-utils
    pip install scrapy
    pip install pandas
    pip install scipy
    pip install streamlit 
    pip install beautifulsoup4
    pip install html2text
    pip install matplotlib
    pip install free-proxy
    pip install googlesearch 

    pip install torrequest
    pip install torpy
    pip install stem
    pip install fake_useragent
   
   
    pip install pip-module-scanner
  // NOTE: Lib install 
  Question : how to set the path lib path right.   
  
  #### Build directory for scrapy  
      - E:\home\pi\scrapy
      - Asin-download 
        - Code : 
        - Result : 
    
    - C:\Local\Work\Python\PyLib\scrapy\download\download\spiders\run_per.py 
    - check if the directory is matching 
      - e.g settings = run_path("C:/Local/Work/Python/PyLib/scrapy/download/download/spiders/quotes_spider.py")
   
   #### Command line : 
    - python3 run_per.py    
   E:\home\pi\scrapy\download\download\spiders
   #### Expected result :
     - Downloaded ASIN file in Result json. 
    



  ### PYTHONPATH setup in Raspberry pi
  
  #### Result 
  put the  Following code in to quotes_spider.py 
```    
    import sys
    sys.path.append('/home/pi/pylib')
```    
  #### Test file 
    /home/pi/pylib/test_lib_dependency.py

  #### In python file 
    import sys
    sys.path.append('/home/pi/pylib')
    print('\n'.join(sys.path))

  #### Set in bashrc
  
  ### Make a direct download version of scrapy  
  
  #### Why 
      - Skip the middle level step 
      - easier for Raspberry pi direct download. 
      - first test in pc, then on Raspberry pi

  // MARK : Current: Make a direct download version of scrapy  


  ### Apscheduler 

   #### Objective 
    - Run python app in background 
   ##### hwoto
      - [How to constantly run Python script in the background on Windows?](https://stackoverflow.com/questions/59125493/how-to-constantly-run-python-script-in-the-background-on-windows)
  
    ##### example 
      pythonw.exe pythonw.exe C:\\Python\Scripts\moveDLs.py

   
   ##### Introduction 
  - [Introduction](https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6)

   #### Time 
    https://stackoverflow.com/questions/29765039/how-to-use-apscheduler-with-scrapy  

    - date: use when you want to run the job just once at a certain point of time
    - interval: use when you want to run the job at fixed intervals of time
    - cron: use when you want to run the job periodically at certain time(s) of day

   #### add_job 
  
    - [add_job](https://apscheduler.readthedocs.io/en/stable/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job)

    - Target : every 24 hours : use interval 

   #### Triggers 
    - https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html
    Example 
    sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')


  #### Run every 10 min from start_date to end_date
    scheduler.add_job(process.crawl, 'interval', args=[Download_Test],  minutes=10, start_date='2020-12-1 01:10:00', end_date='2020-12-1 02:10:00')

  #### Run every date  : use cron 
  https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6

  Schedule to run the task on every hour:
  sched.add_job(job_function, 'cron', hour='*')

  #### Run multiple jobs 

  
  ### Fix lib problem in Raspberry pi

    #### Result 
      install the req.txt  
    #### Objective 
      1. add lib path to default Raspberry pi Pythonpath   
          1. Add directory in python code. 
    #### search 
      gss ''
    #### test 
      python3     /home/pi/pylib/test_lib_dependency.py

      pip install -r req.txt 
  
  #### need lib   
    import clipboard
    import validators
    from mechanize import Browser
    from proxy_requests import ProxyRequests
    from newspaper import Article
    
    #### Dependency files  in requirement : 
    workon cut_env 
    pip install --use-feature=2020-resolver -r req.txt  
    
    in req.txt 
      yagmail
      clipboard
      validators
      mechanize
      proxy_requests
      newspaper3k
      scrapy-utils
      scrapy
      pandas
      scipy    
      beautifulsoup4
      html2text
      matplotlib
      free-proxy
      googlesearch-python 
      PyYAML (need pip install -U PyYAML)
      twisted
      apscheduler
      schedule

  streamlit 

    removed 
    - Solution : Remove Dist Package and RUN
      - sudo rm -rf /usr/lib/python3/dist-packages/yaml
      - sudo rm -rf /usr/lib/python3/dist-packages/PyYAML-*
    
  #### 
    - display : PYTHONPATH 

    /home/pi/pylib/test_lib_dependency.py
    


  ### VPN for scraping 

  #### Conclusion 
      - use nordvpn to scrap 
      - nordvpn c us5294 : connect to a server : country 
      - see [Key setting](#nordvpn--key-setting)
      - Always fixed in us5294 
    
    #### nordvpn : key setting 
      1. nordvpn status : check status 
      2. nordvpn c us5294 : connect to a server : country 
      3. nordvpn d  : disconnect 
      
      ##### Reference
      - [Installing and using NordVPN on Debian](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Elementary-OS-and-Linux-Mint.htm)
    
    #### Question
      1.   What are the drawbacks for the NordVPN 
        1.    Can it to sustain long time scrapy  

    #### Reference 
    - [ML_Amazon_product_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Crawler.md#vpn-for-scraping) 

    - [- 5000 IPs are a lot to scrape: Easy Hide IP](https://www.vpncomparison.org/best-vpn-for-web-scraping/)

    ##### 5000 IPs

      5000 IPs are a lot to scrape: Easy Hide IP What are you doing
    easyhideipEasy-Hide-IP VPN: Over 5,000 IPs worldwide are available for you to make use of with this VPN. The cool thing about it is the fact that you can choose the frequency in which you change your IP automatically. For example, you can have the IP of your changed every minute, every five minutes or every hour and so on. This gives you the freedom you have been looking for, to engage in web data extraction. Other than that, you connect with one click and on multiple devices. There is no data limit, and you need not worry about logs. A free trial is available as a test drive. Then, the cost of your monthly subscription is pretty affordable, and there is full money refund guarantee.

  ### Simple run a run_per.py  : Apscheduler

  #### What :  
    -  run_per.py: /home/pi/scrapy/download/download/spiders/run_per.py
    -  Result directory :  /home/pi/scrapy/download/result

  #### Howto

    1. start the Raspberry pi : v2 
    2. 

  #### Fixed peroidc parameter 
     scheduler.add_job(process.crawl, 'interval', args=[Download_Test],  minutes=10, start_date='2020-12-1 01:20:00', end_date='2020-12-1 02:10:00')

  #### Read from a scheudle file 
  // MARK : Start Periodic 
    Perodic : minutes=10,     
    Start_time:   start_date='2020-12-1 01:20:00', 
    End_time: end_date='2020-12-1 02:10:00')
  
  #### Check the status of the scheduler  
  - which jobs are running 

  ### Work Together with django 

  // TODO : Work Together with django to run peridoic task 

  1. From django launch run_per.py 
    /home/pi/scrapy/download/download/spiders/run_per.py
    1.  Specify the start end parameter : 
  
  2. Processing the result python scraping is done. 
     1. Time is complete : run a program at a specific time 
     2. Call back  Call back function when result is done 

  // MARK : Now ; End Periodic 




## Tools 

  ### scrapy logging file
  [20_min] gold 

  #### print out silently scrapy 

  - [python - How to save Scrapy crawl Command output - Stack Overflow](https://stackoverflow.com/questions/16650397/how-to-save-scrapy-crawl-command-output)

  if you want to get the output from runspider command.
  scrapy runspider scraper.py -o some.json -t json 2> some.text


  mycurl http://localhost:6800/schedule.json -d project=download -d spider=product
  

  ### hwo to use curl : 

  ####   Client URL
  cURL (pronounced 'curl') is a computer software project providing a library (libcurl) and command-line tool (curl) for transferring data using various network protocols. The name stands for "Client URL", which was first released in 1997.

  #### curl Proxy 
  curl --proxy 205.185.116.235:8080 http://remote.example.org/

  curl --proxy 205.185.116.235:8080 https://www.amazon.com/dp/B0791TX5P5

  curl --proxy 205.185.116.235:8080 https://www.amazon.com/product-reviews/B0791TX5P5/ref=acr_dp_hist_1?ie=UTF8&filterByStar=one_star

  #### Reference 
  - [Everything curl](https://ec.haxx.se/usingcurl/usingcurl-proxies)

  - [Using curl to automate HTTP jobs](https://curl.haxx.se/docs/httpscripting.html)

  REVIEW : Question : how to make sense out of the curl output 

  ### mingw64 

  - see mingw64 : a mini bash simulator  
 
## Reference

  ### Scrapy documentation
    - [Scrapy 2.2 documentation](https://docs.scrapy.org/en/latest/index.html)

    - [Scrapy 2.2 documentation: -logging ](https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-settings)
    - [selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
    - [Using your browser’s Developer Tools for scraping](https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools)

    - [Amazon Product Advertising API](https://webservices.amazon.com/paapi5/documentation/quick-start/using-sdk.html)
    - [xpath](https://www.guru99.com/using-contains-sbiling-ancestor-to-find-element-in-selenium.html)


  ### Scrapy from within a Python script
    @crawl 
    How to run Scrapy from within a Python script
    https://stackoverflow.com/questions/13437402/how-to-run-scrapy-from-within-a-python-script

  ### An elegant way to run periodic tasks in python
    @crawl 
    https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679 

# Next step  

  
## Visualization 

  Next See :  - [ML_Amazon_product_Visualizer.md](file:///C:/Local/Work/ML_Name/Note/ML_Amazon_product/ML_Amazon_product_Visualizer.md) 

# Follow Up 

## Run streamlit in Raspberry pi
// MARK: Run streamlit in Raspberry pi
// TODO : Hwoto streamlit in Raspberry pi

### 10.16. find the srun simple display on the srun 
[20_min]
  - run scrapy as normal python : 
    - python x
 
## 
  // TODO : Hwo to Run python app in background 

#####   ff 

### JSON or RDB To save

#### Objective 
   1.   Technical understanding and comparison between 2 technology 
  
  - Which is better :
    - RDB : faster  And more efficient
    - JSON ： easy to read. 


#### reference
  - Undoubtedly, RDB is the most efficient one, both in terms of storage and query response.
  -  I personally do not see any point in using xml and json as these have been traditionally used for exchange of data and are inefficient for storage and queries.
  - 

## End 


## eBay :  Make a ebay bidding app
