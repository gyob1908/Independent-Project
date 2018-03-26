#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:29:31 2017

@author: oliverbeatson
"""

# This code returns limited number of tweets based on the 2 string searches

# Import of necassary modules

import tweepy
import AccessKeys
from textblob import TextBlob

# Uses keys from API setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

# Searches for keyword 'Labour' in tweets
# Perform sentiment analysis
# Then prints results

public_tweets = api.search(q="Labour")

for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)
    
# Searches for keyword 'Conservative' in tweets
# Perform sentiment analysis
# Then prints results

public_tweets = api.search(q="Conservative")

for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)  
    
    
    
