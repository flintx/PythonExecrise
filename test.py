import Image
import ImageFont
import ImageDraw


text = u"7"

im = Image.open('/home/zzf/portrait.jpg')

dr = ImageDraw.Draw(im)
font = ImageFont.truetype('Consolas.ttf', 34)

dr.text((im.size[0] * 0.85, im.size[1] * 0.05),
        text, font=font, fill="#ff0000")

im.show()
im.save('result.jpg')
