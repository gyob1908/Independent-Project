#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 08:54:28 2017

@author: oliverbeatson
"""
# Code adapted from - http://www.davidrschuler.com/python_twitter_streaming/
#                   - http://tweepy.readthedocs.io/en/v3.5.0/
#                   - http://textblob.readthedocs.io/en/dev/

# Imports required libraries

import tweepy
from tweepy.streaming import StreamListener
import sqlite3
import json
import AccessKeys
from textblob import TextBlob

# Creates a table called Tweets in SQLite

conn = sqlite3.connect('twitter.db')
c = conn.cursor()
c.execute('''CREATE TABLE tweets
    (tweetText text,
    sentiment text,
    user text,
    followers integer,
    date text,
    location text)''')
conn.commit()
conn.close()

# Uses keys from API setup to access Twitter Account information
# Access Keys held in seperate folder

auth = tweepy.OAuthHandler(AccessKeys.ConsumerKey, AccessKeys.ConsumerSecret)
auth.set_access_token(AccessKeys.AccessToken, AccessKeys.AccessTokenSecret)

# Establishes API through tweepy

api = tweepy.API(auth)

# Creates link to database

conn = sqlite3.connect('twitter.db')
c = conn.cursor()


# Class for defining a Tweet

class Tweet():

    # Defines different parts of data on the tweet
    
    def __init__(self, text, sentiment, user, followers, date, location):
        self.text = text
        self.sentiment = sentiment
        self.user = user
        self.followers = followers
        self.date = date
        self.location = location


    # Defines inserting the data into the DB
    
    def insertTweet(self):

        c.execute("INSERT INTO tweets (tweetText, sentiment, user, followers, date, location) VALUES (?, ?, ?, ?, ?, ?)",
            (self.text, self.sentiment, self.user, self.followers, self.date, self.location))
        conn.commit()
        
# Stream Listener class       
        
class Listener(StreamListener):

    # When data is received
    
    def on_data(self, data):

        # Error handling
        
        try:

            # Convert data to JSON format
            
            tweet = json.loads(data)
            
            # Filter out retweets and quoted tweets to avoid duplication
            
            if not tweet['retweeted'] and 'RT @' not in tweet['text']:

                # Get user via Tweepy in order to obtain number of followers
                
                user_profile = api.get_user(tweet['user']['screen_name'])

                # Perform sentiment analysis on tweet text
                
                analysis = TextBlob(tweet['text'])
            
                
                # Assign all data to Tweet object by splitting up data in to relevent catagories
                
                tweet_data = Tweet(
                    str(tweet['text'].encode('utf-8')),
                    str (analysis.sentiment),
                    tweet['user']['screen_name'],
                    user_profile.followers_count,
                    tweet['created_at'],
                    tweet['user']['location'])

                
                # Print tweet text and sentiment analysis for visual check
                
                print(tweet_data.text)
                print (analysis.sentiment)

                # Inserts tweet data into database
                
                tweet_data.insertTweet()
                


        # Error message incase of errors
        except Exception as e:
            print(e)
            pass
        return True

        
if __name__ == '__main__':

    # Run the stream
    
    l = Listener()
    stream = tweepy.Stream(auth, l)

    # Filters the stream for these keywords
    
    stream.filter(track=['Labour Party', 'Conservative Party'])
    
   