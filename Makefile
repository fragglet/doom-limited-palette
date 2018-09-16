
doom2.wad : limited.lmp
	./bootstrap.py < $< > $@

limited.lmp : limited.png
	./png_to_pal.py < $< > $@

