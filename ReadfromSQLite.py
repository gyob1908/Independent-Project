#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:10:35 2017

@author: oliverbeatson
"""

import sqlite3
from sqlite3 import Error
 
# Create connection to database
# Brackets indicate the database name 

def create_connection(twitter):

    try:
        conn = sqlite3.connect('twitter.db')
        return conn
    except Error as e:
        print(e)
 
    return None
 
# Brings through all text from tweets
# Could be altered to bring through other or all information relating to tweets   
    
def select_all_tweets(conn):

    cur = conn.cursor()
    cur.execute("SELECT tweettext FROM tweets")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = "/Applications/University/anaconda3\twitter.db"
 
# create a database connection
    conn = create_connection(database)
    with conn:
        
        print("Tweets")
        select_all_tweets(conn)
 
 
if __name__ == '__main__':
    main()