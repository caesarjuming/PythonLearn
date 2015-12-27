__author__ = 'Administrator'

"""
    类代码编写基础

"""

"""
    class 语句创建类对象并将其赋值给变量名
    class 语句内赋值会创建类的属性

    像函数那样调用类会创建新的实例对象
    每个实例对象继承类的属性并创建自己的命名空间
    在方法内对self做赋值运算时创建每个实例对象自己的属性

"""

class FistClass:
    def setData(self, value):
        self.data = value
    def disPlay(self):
        print(self.data)


x = FistClass()
y = FistClass()

x.setData('aaa')
y.setData(123)

x.disPlay()
y.disPlay()

# 如果在调用setData之前调用display就会出错，因为在赋值时候才创建的变量
x.data = 'newData'

x.disPlay()
x.newparm = 'newparm'
print(x.newparm)

""" 类通过继承进行定制

    超类在类开头的括号中
    类从超类中继承属性
    实例会继承类中所有可读取的属性

"""
class SecondClass(FistClass):
    def disPlay(self):
        print("SecondClass %s" % self.data)

s1 = SecondClass()
# setData in FirstClass
s1.setData(222)
s1.disPlay()

# 重载


# 类是模块内的属性，导入一个模块，可以使用其中的类

# 类可以截获运算符，也就是运算符重载

""" 当类构造时候调用构造方法 __init__
    当调用+号的时候，调用__add__
    当调用print时候，调用__str__

"""
class ThirdClass:
    def __init__(self, data):  # 构造方法
        self.data = data
    def __add__(self, other):  # +
        return ThirdClass(self.data + "," + other.data)
    def __str__(self): # print
        return '[Third %s ]' % self.data
    def __mul__(self, other): # *
        self.data *= other.data

a = ThirdClass("小明")
b = ThirdClass("隔壁老王")
print(a)
print(a + b)
c = ThirdClass(3)
d = ThirdClass(5)
d * c
print(d)

# the simplest class
class emp:
    pass
emp.name = 'jack'
emp.age = 28
print(emp.name+":"+str(emp.age))

e1 = emp()
e2 = emp()

print(e1.name)
print(e2.name)

print(list(emp.__dict__.keys()))
print(e1.__class__)