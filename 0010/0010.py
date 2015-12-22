#!/usr/bin/env python3
# coding:utf-8

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
import string

filed = string.ascii_letters + string.digits

IMAGE_MODE = 'RGB'
IMAGE_COLOR = (255, 255, 255)

Image_Font = '/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf'
Image_Path = '/home/zzf/my_python/PythonExecrise/0010/Identify_Code.jpg'


def GetRandomColor(color_range):
	left,right = color_range
	return (random.randint(left, right), random.randint(left, right), random.randint(left, right))

def GetRandomCode(code_len=4):
	return "".join(random.sample(filed, code_len))


# chance 噪点频率(%)
def GetIdentifyCode(text, path, image_size=(320, 240), color_range=(32,127), chance=2):
	im = Image.new(IMAGE_MODE, image_size, IMAGE_COLOR)
	draw = ImageDraw.Draw(im)

	width, height = image_size

	# 绘制噪点
	for w in range(width):
		for h in range(height):
			if chance < random.randint(1,100):
				draw.point((w,h), fill=GetRandomColor(color_range))

	font = ImageFont.truetype(Image_Font, 150)
	fontwidth, fontheight = font.getsize(text)

	text_len = len(text)

	x = (width - fontwidth) / 2
	y = (height - fontheight) / 2

	# 书写文字
	for c in text:
		draw.text((x,y), c, GetRandomColor(color_range), font)
		x += fontwidth / text_len

	im = im.filter(ImageFilter.BLUR)
	im.save(path)

def main():
	Text = GetRandomCode()
	GetIdentifyCode(Text, Image_Path)

if __name__ == '__main__':
	main()
