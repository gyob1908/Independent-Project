#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:29:31 2017

@author: oliverbeatson
"""
# Code adapted from http://tweepy.readthedocs.io/en/v3.5.0/

# This code returns past 15 tweets regarding the 3 string searches

# Import of necassary modules

import tweepy
import AccessKeys

# Uses keys from APP setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

# Searches for keyword 'Labour'
# Then prints results

results = api.search(q="Labour")

for result in results:
    print (result.text)
    
# Searches for keyword 'Conservative'
# Then prints results

results = api.search(q="Conservative")

for result in results:
    print (result.text)   
    
# Searches for keyword 'bbcqt'
# Then prints results

results = api.search(q="bbcqt")

for result in results:
    print (result.text)  
    
