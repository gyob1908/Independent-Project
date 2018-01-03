#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:35:42 2018

@author: oliverbeatson
"""

import tweepy
import AccessKeys

# Uses keys from APP setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items(100):
    # Process the friend here
    print (friend)