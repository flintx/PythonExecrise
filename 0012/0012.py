#!/usr/bin/env python3
# coding:utf-8



file_path = "filtered_word.txt"


def load_filtered_words(path):
	filtered_words = []
	with open(path) as f:
		filtered_words = f.read().split('\n')
	return filtered_words

def check(text, filtered_words):
	for word in filtered_words:
		# print("*"*len(word))
		text = text.replace(word, "*"*len(word))
	print(text)




def main():
	filtered_words = load_filtered_words(file_path)
	while True:
		text = input('please input some words: ')
		check(text, filtered_words)



if __name__ == '__main__':
	main()
