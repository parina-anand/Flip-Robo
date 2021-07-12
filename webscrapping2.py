#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


# __Task 1__

# In[2]:


# lets connect to the web driver
driver = webdriver.Chrome(r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe")
url = 'https://www.naukri.com/'
driver.get(url)


# In[3]:


skill=driver.find_element_by_css_selector("#qsb-keyword-sugg")
skill.send_keys("Data Analyst")
location=driver.find_element_by_css_selector("#qsb-location-sugg")
location.send_keys("Bangalore")
search=driver.find_element_by_css_selector("#root > div.naukriHomePageContainer > div.topSection > section > div > form > div.search-btn > button")
search.click()


# In[4]:


job_title=[]
job_location=[]
company_name=[]
exp_req=[]

job_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tags[0:10]
company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:10]
location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
location_tags[0:10]
exp_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']")
exp_tags[0:10]


# In[5]:


for i in range(0,10):
    job_tag=job_tags[i].text
    job_title.append(job_tag)
    company_tag=company_tags[i].text
    company_name.append(company_tag)
    location_tag=location_tags[i].text
    job_location.append(location_tag)
    exp_tag=exp_tags[i].text
    exp_req.append(exp_tag)


# In[6]:


Job_details=pd.DataFrame({})
Job_details["Job Title"]=job_title
Job_details["Company Name"]=company_name
Job_details["Job Location"]=job_location
Job_details["Experience Required"]=exp_req


# In[7]:


Job_details


# __Task 2__

# In[8]:


driver.get("https://www.naukri.com/")


skill=driver.find_element_by_css_selector("#qsb-keyword-sugg")
skill.send_keys("Data Scientist")
location=driver.find_element_by_css_selector("#qsb-location-sugg")
location.send_keys("Bangalore")
search=driver.find_element_by_css_selector("#root > div.naukriHomePageContainer > div.topSection > section > div > form > div.search-btn > button")
search.click()


# In[9]:


job_title=[]
job_location=[]
company_name=[]
exp_req=[]

job_tags=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tags[0:10]
company_tags=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:10]
location_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
location_tags[0:10]
exp_tags=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']")
exp_tags[0:10]


# In[10]:


for i in range(0,10):
    
    job_tag=job_tags[i].text
    job_title.append(job_tag)
    company_tag=company_tags[i].text
    company_name.append(company_tag)
    location_tag=location_tags[i].text
    job_location.append(location_tag)
    exp_tag=exp_tags[i].text
    exp_req.append(exp_tag)


# In[11]:


Job_details=pd.DataFrame({})
Job_details["Job Title"]=job_title
Job_details["Company Name"]=company_name
Job_details["Job Location"]=job_location
Job_details["Experience Required"]=exp_req


# In[12]:


Job_details


# In[13]:


## Clicking on the Job to get discription

to_click=driver.find_element_by_xpath("//a[@class='title fw500 ellipsis']")
to_click.click()


# In[35]:


#data4=driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/section[2]")
data5=driver.find_element_by_xpath("//section[@class='job-desc']")
data5=driver.find_elements_by_class_name("job-desc")


# EVEN THOUGH MY X_PATH IS CORRECT< STILL UNABLE TO GET THE DATA


# __Task 3__

# In[37]:


chromedriver_path = r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe"
webdrivers = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdrivers.get("https://www.naukri.com/")


# In[38]:


skill=webdrivers.find_element_by_css_selector("#qsb-keyword-sugg")
skill.send_keys("Data Scientist")
#location=webdrivers.find_element_by_css_selector("#qsb-location-sugg")
#location.send_keys("Bangalore")
search=webdrivers.find_element_by_css_selector("#root > div.naukriHomePageContainer > div.topSection > section > div > form > div.search-btn > button")
search.click()
sleep(3)


# In[40]:


# selecting filter for location
loc_filter=webdrivers.find_elements_by_xpath("//span[@class='ellipsis fleft']")
for i in loc_filter:
    if i.text=="Delhi / NCR":
        i.click()
        break
sleep(3)
# Salary filter 

sal_filter=webdrivers.find_elements_by_xpath("//span[@class='ellipsis fleft']")
for i in sal_filter:
    if i.text=="3-6 Lakhs":
        i.click()
        break


# In[41]:


# Scraping data for the first 10 jobs.

job_title=[]
job_location=[]
company_name=[]
exp_req=[]

job_tags=webdrivers.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tags[0:10]
company_tags=webdrivers.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_tags[0:10]
location_tags=webdrivers.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
location_tags[0:10]
exp_tags=webdrivers.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']")
exp_tags[0:10]


# In[42]:


for i in range(0,10):
    
    job_tag=job_tags[i].text
    job_title.append(job_tag)
    company_tag=company_tags[i].text
    company_name.append(company_tag)
    location_tag=location_tags[i].text
    job_location.append(location_tag)
    exp_tag=exp_tags[i].text
    exp_req.append(exp_tag)


# In[43]:


Job_details=pd.DataFrame({})
Job_details["Job Title"]=job_title
Job_details["Company Name"]=company_name
Job_details["Job Location"]=job_location
Job_details["Experience Required"]=exp_req


# In[44]:


Job_details


# __Task 4__

# In[48]:


chromedriver_path = r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe"
webdrivers = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdrivers.get("https://www.glassdoor.co.in/index.htm")


# In[54]:


# go_sign_in=webdrivers.find_element_by_class_name("locked-home-sign-in")
go_sign_in=webdrivers.find_element_by_xpath("//button[@class='google gd-btn short']")
go_sign_in.click()


# In[69]:


# Signing in to Glassdoor


# __Task 5___

# In[72]:


chromedriver_path = r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe"
webdrivers = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdrivers.get("https://www.glassdoor.co.in/Salaries/index.htm")
sleep(5)


# In[ ]:


job=webdrivers.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/form/input[5]")
job.send_keys("Data Scientist")

location=webdrivers.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/form/input[6]")
location.send_keys("Noida")

search=webdrivers.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/form/button")
search.click()
sleep(3)


# __Task 6__

# In[95]:


chromedriver_path = r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe"
webdrivers= webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdrivers.get("https://www.flipkart.com/")


# In[97]:


search_field=webdrivers.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_field.send_keys("sunglasses")

search_btn=webdrivers.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_btn.click()


# In[98]:


brand=webdrivers.find_elements_by_xpath("//div[@class='_2WkVRV']")
brand_list=[]


# In[99]:


for i in range(len(brand)):
    print(brand[i].text)
    brand_list.append(brand[i].text)
description=webdrivers.find_elements_by_xpath("//a[@class='IRpwTa']")


# In[100]:


for i in range(len(description)):
    print(description[i].text)
price=webdrivers.find_elements_by_xpath("//div[@class='_30jeq3']")


# In[101]:


for i in range(len(price)):
    print(price[i].text)


# In[102]:


discount=webdrivers.find_elements_by_xpath("//div[@class='_3Ay6Sb']")


# In[103]:


for i in range(len(discount)):
    print(discount[i].text)


# In[104]:


next_page=webdrivers.find_element_by_xpath("//a[@class='_1LKTO3']")
#n_p=next_page.get_attribute('href')
for i in range(1,5):
    N_p='https://www.flipkart.com/search?q=sunglassessunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    sleep(2)
    webdrivers.get(N_p)


# In[105]:


next_page=webdrivers.find_element_by_xpath("//a[@class='_1LKTO3']")
n_p=next_page.get_attribute('href')
#webdrivers.get(n_p)
n_p


# In[106]:


N_p='https://www.flipkart.com/search?q=sunglassessunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+'5'


# In[107]:


webdrivers.get(N_p)


# In[ ]:


brand_name=[]

for i in range(len(brand)):
    brand_name.append(brand)
    if len(brand_name)<100:
        next_page.click()


# In[111]:


len(brand_list)


# In[109]:


def flipkart(url):
    name=[]
    chromedriver_path=r"C:\Users\91987\Desktop\New Web diver/chromedriver.exe"
    webdrivers= webdriver.Chrome(executable_path=chromedriver_path)
    sleep(2)
    webdrivers.get(url)
    sleep(2)
    
    search_field=webdrivers.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    search_field.send_keys("sunglasses")
    
    search_btn=webdrivers.find_element_by_xpath("//button[@class='L0Z3Pu']")
    search_btn.click()
    
    #next_page=webdrivers.find_element_by_xpath("//a[@class='_1LKTO3']")
    #n_p=next_page.get_attribute('href')
    brand=webdrivers.find_elements_by_xpath("//div[@class='_2WkVRV']")
    for j in range(len(brand)):
        name.append(brand[j].text)
        
    next_p("https://www.flipkart.com/search?q=sunglassessunglasses&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=")


# In[112]:


def next_p(link):
    for k in range(2,5):
        N_p=link+str(i)
        webdrivers.get(N_p)
        if len(name)<100:
            for m in range(len(brand)):
                name.append(brand)


# __Task 10__

# In[113]:


from selenium.common.exceptions import NoSuchElementException


# In[116]:


chromedriver_path = r"C:\Users\parin\Downloads\chromedriver_win32\chromedriver.exe"
webdrivers = webdriver.Chrome(executable_path=chromedriver_path)
webdrivers = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdrivers.get("https://www.amazon.in/")


# In[117]:


search=webdrivers.find_element_by_id("twotabsearchtextbox")
search.clear()
search.send_keys("Laptops")
search_click=webdrivers.find_element_by_xpath("//span[@id='nav-search-submit-text']")
search_click.click()


# In[123]:


# Applying filter 

#i7

filter_1=webdrivers.find_elements_by_xpath("//a[@class='a-link-normal s-navigation-item']/span")
for i in filter_1:
    if i.text == 'Intel Core i7':
        print(i.text)
        i.click()
        break


# In[124]:


# Applying filter 

#i9

filter_2=webdrivers.find_elements_by_xpath("//a[@class='a-link-normal s-navigation-item']/span")
for i in filter_2:
    if i.text=="Intel Core i9":
        print(i.text)
        i.click()
        break


# In[126]:


Title=[]
title=webdrivers.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for i in title[:10]:
    Title.append(i.text)
    
Price=[]
prices=webdrivers.find_elements_by_xpath("//span[@class='a-price-whole']")
for i in prices[:10]:
    Price.append(i.text)
    
ratings=[]
pages=webdrivers.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")

PG=[]
for i in pages[:10]:
    PG.append(i.get_attribute('href'))
for j in PG:
    webdrivers.get(j)
    try:
        star=webdrivers.find_element_by_xpath("//span[@id='acrCustomerReviewText']")
        star.click()
        rating=webdrivers.find_element_by_xpath("//span[@class='a-size-medium a-color-base']")
        ratings.append(rating.text)
    except NoSuchElementException as e:
        ratings.append("No ratings found")


# In[127]:


records=pd.DataFrame({'Title':Title,
                 'Price':Price,
                 'Ratings':ratings})
print(records)


# In[ ]:




