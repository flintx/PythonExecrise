#!/usr/bin/python
#coding=utf-8

"""
第 0009 题：一个HTML文件，找出里面的链接
"""

from bs4 import BeautifulSoup

def find_the_link(filepath):
    links = []
    with open(filepath) as f:
        text = f.read()
        bs =BeautifulSoup(text)
        for i in bs.find_all('a'):
        	# print (i.attrs)
            links.append(i.attrs['href'])
    return links

if __name__ == '__main__':
    print (find_the_link('Show-Me-the-Code_show-me-the-code.html'))
