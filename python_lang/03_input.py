#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python提供了一个input(python2.x 是 raw_input)，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字：
name = input()
print('hello,', name)


# 但是程序运行的时候，没有任何提示信息告诉用户，这样显得很不友好。幸好，raw_input可以让你显示一个字符串来提示用户，于是我们把代码改成：
name = input('please enter your name: ')
print('hello,', name)
