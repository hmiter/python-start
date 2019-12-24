#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============集合=============

# 1、list:  list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 用len()函数可以获得list元素的个数
print("classmates 的长度是", len(classmates))
# 取集合中的某一个
print(classmates[1])
# append() 函数在集合最后面追加
classmates.append('Adam')
print(classmates)
# insert() 指定位置增加
classmates.insert(1, 'Jack')
print(classmates)
# pop()删除list末尾的元素
gg = classmates.pop()
print(gg)
print(classmates)
# pop(i)删除指定位置的元素
gg = classmates.pop(1)
print(gg)
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# 2、tuple 元组 : tuple和list非常类似，但是tuple一旦初始化就不能修改
# 没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
classmates2 = ('Michael', 'Bob', 'Tracy1')
classmates3 = ('Michael', 'Bob', 'Tracy')
print(classmates2)

# 比较两个元组元素。
cmp(classmates2, classmates3)
# 计算元组元素个数。
len(classmates2)
# 返回元组中元素最大值。
max(classmates2)
# 返回元组中元素最小值。
min(classmates2)
# 将列表转换为元组。
tuple(classmates)

# 3、dict 字典 ：在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 添加元素
d['Adam'] = 67
print(d)
# 通过in判断key是否存在
print('Thomas' in d)
# dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas', -1))
# pop(key)要删除一个key
d.pop('Bob')
print(d)

# 4、set 不重复集合
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)