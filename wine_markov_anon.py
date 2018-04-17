
# coding: utf-8

# In[2]:


import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import os
import seaborn as sns
import missingno as msno
import plotly.graph_objs as go
import markovify
import tweepy #https://github.com/tweepy/tweepy

#import wine reviews dataset and set up twitter API
wine = pd.DataFrame(pd.read_csv('wine.csv',index_col=[0]))

wine = wine.drop_duplicates('description')
wine = wine[pd.notnull(wine.price)]
#print(wine.shape)

consumer_key = 
consumer_secret  = 
access_key  = 
access_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# In[3]:


# set variety and location of wine for review
wine_variety = 'Bordeaux-style Red Blend'
location = 'Bordeaux'
text = wine[wine['variety'].str.contains(wine_variety,na=False) 
            & wine['province'].str.contains(location,na=False)][['description','title']]
#print(text.head)
#print(text.shape)
#print(text.dtypes)


# In[4]:


text_model_review = markovify.Text(text['description'],state_size=3)
text_model_title =  markovify.NewlineText(text['title'],state_size=3)


# In[5]:


# generate a title and review of wine, then post to twitter
review = []
for i in range(3):
    review.append(text_model_review.make_short_sentence(100))
    #print(review)

#review_title=''
review_title = text_model_title.make_short_sentence(40,test_output=False)


status = location + ' ' + review_title + ': ' + ' '.join(review)
print(status)

# save reviews to a text file for future chuckles
with open('reviews.csv','a',newline='',encoding="utf-8") as reviews:
    writer = csv.writer(reviews)
    writer.writerow(status)

#api.update_status(status)

