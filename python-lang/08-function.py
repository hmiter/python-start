#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ===================函数============

# 1、内建函数  https://docs.python.org/2/library/functions.html#abs
# abs()	divmod()	input()	open()	staticmethod()
# all()	enumerate()	int()	ord()	str()
# any()	eval()	isinstance()	pow()	sum()
# basestring()	execfile()	issubclass()	print()	super()
# bin()	file()	iter()	property()	tuple()
# bool()	filter()	len()	range()	type()
# bytearray()	float()	list()	raw_input()	unichr()
# callable()	format()	locals()	reduce()	unicode()
# chr()	frozenset()	long()	reload()	vars()
# classmethod()	getattr()	map()	repr()	xrange()
# cmp()	globals()	max()	reversed()	zip()
# compile()	hasattr()	memoryview()	round()	__import__()
# complex()	hash()	min()	set()
# delattr()	help()	next()	setattr()
# dict()	hex()	object()	slice()
# dir()	id()	oct()	sorted()

# 2、自定义函数 ：定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print my_abs(1)


# 返回多个值
def move(x, y, step, angle):
    nx = x + step * angle
    ny = y - step * angle
    return nx, ny

x, y = move(100, 100, 60, 6)
print x, ",", y


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)


# 可变参数 ： 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2, 3)


# 关键字参数  ： 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 参数组合 ：在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

# 递归函数 :在函数内部，可以调用其他函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(5)