#!/usr/bin/env python3
# coding:utf-8


import re
import os
from bs4 import BeautifulSoup
import requests

Url = 'http://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0'}

def Html2Article(url):

	html = requests.get(url, headers=Headers).content
	# print(html)
	soup = BeautifulSoup(html, 'lxml')
	code = soup.select("#cnblogs_post_body")
	code = str(code[0])
	code = re.compile(r'<[^>]+>').sub('', code)
	code = code.replace('&lt;','<')
	code = code.replace('&gt;','>')
	code = code.replace('&amp;','&')
	print(code)


def main():
	Html2Article(Url)


if __name__ == '__main__':
	main()
