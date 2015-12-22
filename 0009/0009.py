#!/usr/bin/env python3
# coding:utf-8


import re
import os
from bs4 import BeautifulSoup
import requests

Url = 'http://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0'}

def get_link_from_html(url):

	links = []

	html = requests.get(url, headers=Headers).content
	# print(html)
	soup = BeautifulSoup(html, 'lxml')

	for u in soup.find_all('a', href=True):

		#由于有些搜寻结果不含'href'键，所以会出现KeyError错误，有两种解决方式

		# Way 1
		# try:
		# 	links.append(u.attrs['href'])
		# except KeyError:
		# 	pass

		# Way 2
		if u is not None:
			links.append(u['href'])

	return links



def main():
	print(get_link_from_html(Url))


if __name__ == '__main__':
	main()
