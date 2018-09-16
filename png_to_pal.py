#!/usr/bin/env python

from PIL import Image
import struct
import sys

def image_to_bytes(i):
	w, h = i.size
	assert w * h >= 256

	palette = bytes()
	for y in range(h):
		for x in range(w):
			r, g, b = i.getpixel((x, y))
			palette += struct.pack('BBB', r, g, b)
			if len(palette) >= 768:
				return palette

i = Image.open(sys.argv[1])
palette = image_to_bytes(i.convert('RGB'))

with open(sys.argv[2], 'wb') as out:
	for i in range(14):
		out.write(palette)

