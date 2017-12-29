#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:56:46 2017

@author: oliverbeatson
"""
# Code adapted from http://tweepy.readthedocs.io/en/v3.5.0/
# Code brings through list of followers for specified ID

import tweepy
import AccessKeys
import datetime

# Uses keys from APP setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

sleeptime = 20
pages = tweepy.Cursor(api.followers, screen_name="******").pages()

while True:
    try:
        page = next(pages)
    except tweepy.TweepError:
        page = next(pages)
    except StopIteration:
        break
    
for user in page:
       print(user.screen_name)

       