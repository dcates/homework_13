
# coding: utf-8

# In[1]:


#importing dependancies
from splinter import Browser
from bs4 import BeautifulSoup
#from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
#for twitter api
# Dependencies
import json
import tweepy
#pandas for table scraping
import pandas as pd


# In[2]:


#setting driver up
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#url for mars news
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[4]:


#getting mars news title and paragraph
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#setting variables
news_title = soup.find('div', class_='content_title').text
news_P = soup.find('div', class_='article_teaser_body').text


# In[5]:


#Printing text out
news_P


# In[6]:


#Printing text out
news_title


# In[7]:


#url for mars image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


#Setting up beautiful soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

featured_image_url = soup.find_all('article', class_='carousel_item')
featured_image_url


# In[9]:


#searching for href
for img in featured_image_url:
    link = img.a['data-fancybox-href']
link


# In[10]:


#setting full path of image
url_string = 'https://www.jpl.nasa.gov'
image_path = url_string + link
image_path


# In[11]:


#Mars weather twitter account https://twitter.com/marswxreport?lang=en


# In[12]:


#ending up using twitter api to make pull
#url for mars image
#url = 'https://twitter.com/marswxreport?lang=en'
#browser.visit(url)

#getting mars tweet
#html = browser.html
#soup = BeautifulSoup(html, 'html.parser')

#mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
#mars_weather


# In[13]:


# Import Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[14]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[15]:


# Target User
target_user = "MarsWxReport"


# In[16]:


# Get all tweets from home feed
public_tweets = api.user_timeline(target_user)


# In[17]:


public_tweets
for tweet in public_tweets:
    m_weather = f'{tweet["text"]}'


# In[18]:


#printing weather
m_weather


# In[19]:


#url for mars table
url = 'https://space-facts.com/mars/'


# In[20]:


#pulling all tables from url
tables = pd.read_html(url)
tables


# In[21]:


#putting first table into a dataframe
df = tables[0]
df


# In[22]:


#adding column headers
df.columns = ['Attributes','Value']


# In[23]:


#setting index
df.set_index('Attributes')


# In[24]:


#generate html from dataframe
html_table = df.to_html()
html_table


# In[25]:


#remove unwanted new lines
html_table.replace('\n', '')


# In[26]:


#finding mars images of hemispheres


# In[27]:


#high res image of cerberus hem
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
browser.click_link_by_text('Sample')
img1 = browser.windows.current = browser.windows[1]
img1


# In[28]:


#high res image of Schiaparelli hem
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
browser.click_link_by_text('Sample')
img2 = browser.windows.current = browser.windows[1]
img2


# In[29]:


#high res image of Syrtis Major hem
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
browser.click_link_by_text('Sample')
img3 = browser.windows.current = browser.windows[1]
img3


# In[30]:


#high res image of cerberus Valles Marineris
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
browser.click_link_by_text('Sample')
img4 = browser.windows.current = browser.windows[1]
img4


# In[ ]:


#close out browser
browser.driver.close()

