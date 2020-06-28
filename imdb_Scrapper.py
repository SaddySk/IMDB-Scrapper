# -*- coding: utf-8 -*-
"""
Created on Sunday 28 June 2020 08:55:51

@author: Sk_Saddy
"""

import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.imdb.com/chart/moviemeter/?sort=ir,desc&mode=simple&page=1"

html = urllib.request.urlopen(url, context=ctx).read()
# Beautified Format
soup = BeautifulSoup(html, 'html.parser')

file = open('Movies.txt', 'w')

tags = soup.find_all('tr')
count = 0
for tag in tags:
    check = tag.find_next('th')
    if check != None:
        continue
    titleColumn = tag.find_next('td').find_next('td')
    name = titleColumn.find('a').string
    crew = titleColumn.find('a')['title']
    released = titleColumn.find('span').string
    rank = titleColumn.find('div').get_text()
    rank = rank.replace('\n', '')
    try:
        ratingColumn = titleColumn.find_next('td')
        ratings = ratingColumn.find('strong')['title']
    except:
        ratings = "NOT YET RELEASED"

    # Creating a list to write the contents in a file
    movie = list()
    movie.append("TITLE: " + name + ' ')
    movie.append(released + '\n')
    movie.append("RANK: " + rank + '\n')
    movie.append("DIRECTOR & STARS: " + crew + '\n')
    movie.append("RATINGS: " + ratings + '\n\n')

    file.writelines(movie)
    count += 1

file.close()
print("Data Scrapping done!")
print(count, " movies scrapped.")

