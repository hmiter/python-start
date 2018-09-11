#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 缩略图

from PIL import Image

try:
    im = Image.open("cat.jpg");
    x, y = im.size
    im.thumbnail((x // 2, y // 2))
    im.save("cat.jpg", "JPEG")

except IOError:
    pass
