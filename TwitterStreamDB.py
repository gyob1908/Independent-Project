#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:46:21 2017

@author: oliverbeatson
"""
# Creates a database to store tweets

import sqlite3

conn = sqlite3.connect('twitter.db')
c = conn.cursor()
c.execute('''CREATE TABLE tweets
    (tweetText text,
    user text,
    followers integer,
    date text,
    location text)''')
conn.commit()
conn.close()