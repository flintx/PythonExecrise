#!/usr/bin/env python
# coding: utf-8

import string
import random

CodeNum = 200
GroupLen = 4
GroupNum = 4

field = string.ascii_letters + string.digits


def getRandom():
	return "".join(random.sample(field, GroupLen))


def connect():
	return "-".join([getRandom() for i in range(GroupNum)])


def generate(num):
	RandomCode = set()
	for i in range(num):
	 	RandomCode.add(connect())
	return RandomCode


def main():
	print(generate(CodeNum))


if __name__ == "__main__":
	main()
