#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 需要安卓pillow第三方库：pip install pillow

from PIL import Image

try:
    im = Image.open("cat.jpg");
    print(im.format, im.size, im.mode)
    print(im.info)
    im.show()
except IOError:
    pass
