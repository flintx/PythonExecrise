#!/usr/bin/env python
# coding: utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

ImagePath = "/home/zzf/"
FontPath = "/usr/share/fonts/truetype/ubuntu-font-family/"
PortraitFile = "portrait.jpg"
OutputFile = "output.jpg"


def DrawFont(image, Font):
    FontSize = min(image.size) / 4
    Font = ImageFont.truetype(Font, FontSize)
    draw = ImageDraw.Draw(image)
    draw.text((image.size[0] - FontSize, 4), '99', font=Font, fill=(255, 0, 0))


def main():
    im = Image.open(ImagePath + PortraitFile)
    font = FontPath + "UbuntuMono-B.ttf"
    DrawFont(im, font)
    im.save(ImagePath + OutputFile)


if __name__ == "__main__":
    main()
