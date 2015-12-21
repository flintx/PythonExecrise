#!/usr/bin/env python3
# coding :utf-8

import os
from PIL import Image

iPone_Width = 1136
iPhone_Height = 640
Path = '/home/zzf/my_python/PythonExecrise/0005/image/'

def Resize2iPhone5(image, name):
	im = Image.open(image)
	w,h = im.size

	if w > iPone_Width:
		h = h * iPone_Width // w
		w = iPone_Width
	if h > iPhone_Height:
		w = w * iPhone_Height // h
		h = iPhone_Height

	image_resized = im.resize((w,h), Image.ANTIALIAS)
	image_resized.save(name)

def Change_Size(path):
	for root, dirs, files in os.walk(path):
		for file_name in files:
			if file_name.lower().endswith("jpg") or file_name.lower().endswith("png"):
				image_path = os.path.join(root, file_name)
				file_new_name = "iPone5_" + file_name
				Resize2iPhone5(image_path, file_new_name)

def main():
	Change_Size(Path)

if __name__ == '__main__':
	main()
