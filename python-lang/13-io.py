#!/usr/bin/python
# -*- coding: UTF-8 -*-

# raw_input函数
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

str = raw_input("请输入：")
print "你输入的内容是: ", str

# input函数
# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# [x*5 for x in range(2,10,2)]
str = input("请输入：")
print "你输入的内容是: ", str

# open 函数
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 语法：
# file object = open(file_name [, access_mode][, buffering])

# 打开一个文件
fo = open("foo.txt", "w")
fo.write("www.blog.mindasoft.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

# file.closed	返回true如果文件已被关闭，否则返回false。
# file.mode	返回被打开文件的访问模式。
# file.name	返回文件的名称。
# file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
# file.close()  关闭文件。关闭后文件不能再进行读写操作。
# file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。
# file.next() 返回文件下一行。
# file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size]) 读取整行，包括 "\n" 字符。
# file.readlines([sizehint]) 读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
# file.seek(offset[, whence]) 设置文件当前位置
# file.tell() 返回文件当前位置。
# file.truncate([size]) 截取文件，截取的字节通过size指定，默认为当前文件位置。
# file.write(str) 将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。