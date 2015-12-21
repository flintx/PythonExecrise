#!/usr/bin/env python
# coding: utf-8

import string
import random

CodeNum = 2000
GroupLen = 2
GroupNum = 3

field = string.ascii_lowercase


def getRandom():
	return "".join(random.sample(field, GroupLen))


def connect():
	return " ".join([getRandom() for i in range(GroupNum)])


def generate(num):
	s = ""
	for i in range(num):
	 	s += connect()
	 	s += " "
	 	if i % 10 == 0:
	 		s += "\n"
	return s


def main():
	print()
	print(generate(CodeNum), file=open("./0006/diary_3.txt", "w"))


if __name__ == "__main__":
	main()
