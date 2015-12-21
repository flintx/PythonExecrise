#!/usr/bin/env python3
# coding: utf-8

import os
import re

def CountOneDiary(path):
	word_dic = {}
	filename = os.path.basename(path)
	with open(path) as f:
		text = f.read()
		word_list = re.findall("[a-z]+", text)
		for w in word_list:
			if w in word_dic:
				word_dic[w] += 1
			else:
				word_dic[w] = 1

		sorted_word_list = sorted(word_dic.items(), key=lambda d:d[1])

		res = "在%s文件中，%s为关键词，共出现了%s次" %(filename, sorted_word_list[-1][0], sorted_word_list[-1][1])

		print(res)




def CountAllDiary(Dir):
	file_path = []
	for root, dirs, files in os.walk(Dir):
		for file_name in files:
			if file_name.lower().endswith("txt"):
				file_path.append(os.path.join(root, file_name))
	file_path.sort()
	for diary in file_path:
		CountOneDiary(diary)

def main():
	CountAllDiary(os.getcwd())



if __name__ == '__main__':
	main()
