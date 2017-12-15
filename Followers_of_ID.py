#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:56:46 2017

@author: oliverbeatson
"""

import tweepy
import AccessKeys

# Uses keys from APP setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

# Creates list of followers for specified ID
print (api.followers_ids('????'))


