#!/usr/bin/env python3
# coding:utf-8

import os

Codesuflist = ['.py', '.c', '.h', '.cpp', '.cs', 'sh', '.asm', '.php', '.htm', '.html', '.css', '.m']
dir_path = "/home/zzf/Vimfile"


def walk_dir(Dir):
	file_path = []
	for root, dirs, files in os.walk(Dir):
		for file_name in files:
			PreAndSuf = os.path.splitext(file_name)
			suf = PreAndSuf[1]
			if suf in Codesuflist:
				file_path.append(os.path.join(root, file_name))
	return file_path

def count_lines(path):

	file_name = os.path.basename(path)
	all_lines = 0
	empty_lines = 0
	comment_lines = 0

	with open(path) as f:
		for line in f.read().split('\n'):
		# for line in f.readlines():
			if line.strip().startswith("#") and file_name.endswith(".py"):
				comment_lines += 1
			elif line.strip().startswith("//"):
				comment_lines += 1
			elif line.strip().startswith("/*") or line.strip().endswith("*/"):
				comment_lines += 1

			if len(line) == 0:
				empty_lines += 1

			all_lines += 1

		strs = " file name: %s \n empty lines: %d \n comment lines: %d \n all lines: %d \n"%(file_name, empty_lines, comment_lines, all_lines)

		print(strs)

	return all_lines



def main():
	Lines = 0
	for path in walk_dir(dir_path):
		Lines += count_lines(path)
	print(" all file lines: " + str(Lines))


if __name__ == '__main__':
	main()
