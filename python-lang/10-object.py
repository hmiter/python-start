#!/usr/bin/python
# -*- coding: UTF-8 -*-

# =================面向对象=========
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print bart.name
bart.print_score()

# 继承和多态

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()