#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
from PIL import ImageFont, ImageDraw, Image
from datetime import datetime

WIDTH=240

def freespace(p):
    """
    Returns the number of free bytes on the drive that ``p`` is on
    """
    s = os.statvfs(p)
    return s.f_bsize * s.f_bavail

def text_centered(draw, y, text, font):
	x = (WIDTH - font.getsize(text)[0]) / 2.0
	draw.text((x,y), text, font=font)

def create_image(path):
	dir = os.path.dirname(os.path.abspath(__file__))
	input_file = os.path.join(dir, "nyan.png")
	font_file = os.path.join(dir, "ProggyClean.ttf")

	im = Image.open(input_file)
	draw = ImageDraw.Draw(im)

	# Current time
	n = datetime.now()
	font = ImageFont.truetype(font_file, 64)
	text_centered(draw, 12, n.strftime("%H:%M"), font)

	font = ImageFont.truetype(font_file, 32)
	gb_free = freespace('/mnt/disk1') / pow(1000,3)
	text_centered(draw, 70, "{0} GB free".format(gb_free), font)

	im.save(path, "PNG")

def get_image(self):
	path = "/tmp/image.png"
	create_image(path)
	return path

if __name__ == "__main__":
	create_image('test.png')
