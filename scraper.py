#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:36:20 2017

@author: oliverbeatson
"""

import requests
import bs4

page = requests.get("http://www.geog.leeds.ac.uk/courses/computing/practicals/python/web/scraping-intro/table.html")
content = page.text

soup = bs4.BeautifulSoup(content, 'html.parser')

table = soup.find(id="datatable")

trs = table.find_all('tr')
	
for tr in trs:
	tds = tr.find_all("td")
	for td in tds:
		print (td.text)
		