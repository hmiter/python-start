#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1、if...else
print "if...else"
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称

# 2、if...elif...else
print "if...elif...else"
num = 5
if num == 3:            # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

# 3、while
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

# 4、for iterating_var in sequence:
for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit
