#!/usr/bin/env python3
# coding:utf-8


import re
import os
from bs4 import BeautifulSoup
import requests
import urllib

Url = 'http://tieba.baidu.com/p/2166231880'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0'}


def download_pic(url):

	image_content = requests.get(url, headers=Headers).content
	# image_content = urllib.request.urlopen(url).read()
	file_name = os.path.basename(urllib.parse.urlsplit(url)[2])
	file_name = os.path.join(os.getcwd()+'/pic', file_name)
	# print(file_name)
	out = open(file_name, 'wb')
	out.write(image_content)
	out.close()

def get_pic(url):

	links = []

	html = requests.get(url, headers=Headers).content
	# html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, 'lxml')
	# print(soup)
	for u in soup.find_all('img', {"class": "BDE_Image"}):
		print(u)
		if u is not None:
			links.append(u['src'])
	links.sort()
	print(links)
	for link in links:
		download_pic(link)


def main():
	get_pic(Url)

if __name__ == '__main__':
	main()
