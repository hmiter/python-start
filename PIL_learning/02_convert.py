#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

from PIL import Image

try:
    Image.open("cat.jpg").save("cat.png");
except IOError:
    pass
