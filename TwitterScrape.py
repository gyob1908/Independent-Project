#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:40:39 2017

@author: oliverbeatson
"""
# Code adapted from http://tweepy.readthedocs.io/en/v3.5.0/

import tweepy
import AccessKeys

# Uses keys from API setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy

api = tweepy.API(auth)

# Brings through Tweets from users Twitter home page

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    print(user.screen_name)
