#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:40:39 2017

@author: oliverbeatson
"""

import tweepy
import datetime
import AccessKeys

# Uses keys from APP setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

# Establishes API through tweepy
api = tweepy.API(auth)

# Brings through Tweets from Twitter home page
# Brackets allow for time period
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            datetime.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 200:
        print (follower.screen_name)
        
# Checks to see how many requests can be made within the hour    
# print (api.rate_limit_status())    
