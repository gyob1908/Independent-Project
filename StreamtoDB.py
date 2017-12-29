#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 08:54:28 2017

@author: oliverbeatson
"""
# Code adapted from http://www.davidrschuler.com/python_twitter_streaming/

# Imports required libraries

import tweepy
from tweepy.streaming import StreamListener
import sqlite3
import json
import AccessKeys

# Uses keys from API setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

# Establishes API through tweepy

api = tweepy.API(auth)

# Creates link to database

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

# Class for defining a Tweet

class Tweet():

    # Data on the tweet
    
    def __init__(self, text, user, followers, date, location):
        self.text = text
        self.user = user
        self.followers = followers
        self.date = date
        self.location = location

    # Inserting the data into the DB
    
    def insertTweet(self):

        c.execute("INSERT INTO tweets (tweetText, user, followers, date, location) VALUES (?, ?, ?, ?, ?)",
            (self.text, self.user, self.followers, self.date, self.location))
        conn.commit()
        
# Stream Listener class
        
class Listener(StreamListener):

    # When data is received
    
    def on_data(self, data):

        # Error handling
        
        try:

            # Convert to JSON
            
            tweet = json.loads(data)

            # Filter out retweets and quoted tweets
            
            if not tweet['retweeted'] and 'RT @' not in tweet['text']:

                # Get user via Tweepy so we can get their number of followers
                user_profile = api.get_user(tweet['user']['screen_name'])

                # assign all data to Tweet object
                
                tweet_data = Tweet(
                    str(tweet['text'].encode('utf-8')),
                    tweet['user']['screen_name'],
                    user_profile.followers_count,
                    tweet['created_at'],
                    tweet['user']['location'])

                # Inserts tweet data into database
                
                tweet_data.insertTweet()
                print("success")

        # Error message incase of errors
        
        except Exception as e:
            print(e)
            pass
        return True
    
# Driver
        
if __name__ == '__main__':

    # Run the stream
    
    l = Listener()
    stream = tweepy.Stream(auth, l)

    # Filters the stream for these keywords
    
    stream.filter(track=['Labour', 'Conservative'])
    
    