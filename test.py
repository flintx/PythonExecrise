#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from BeautifulSoup import BeautifulSoup

links = ["http://www.tuftsalumni.org"]

def print_hrefs(link):
    htmlSource = urllib.urlopen(link).read()
    soup = BeautifulSoup(htmlSource)
    data = soup.fetch('a')
    # print data
    for item in data:
        print item['href']

for link in links:
    print_hrefs(link)
