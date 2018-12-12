#!/usr/bin/python
# -*- coding: UTF-8 -*-
# jpg转png

from PIL import Image

try:
    Image.open("cat.jpg").save("cat.png");
except IOError:
    pass
