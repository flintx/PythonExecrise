#!/usr/bin/env python3
# coding : utf-8


import re


def CountWord(file):

	f = open(file, 'r')
	text = f.read()
	pa = "[a-zA-Z0-9]+"
	words = re.findall(pa, text)

	return len(words)


def main():
	print(CountWord("Gettysburg Address.txt"))


if __name__ == '__main__':
	main()

