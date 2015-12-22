__author__ = 'Administrator'

# oop宏伟蓝图

""" 类是产生对象的工厂,每个对象都不同，有自己的命名空间
    类搜索属性的顺序是由下至上，从左到右
    每当调用附属于类的函数时，总会隐含着这个类的实例，也就是self参数

"""

"""
    每个Class语句会生成一个新的类对象
    每次类调用，就会生成一个新的实例对象
    实例自动连接至创建了这些实例的类
    类连接到其他超类的方式是，将超类列在头部括号内，左右顺序决定次序

    属性通常是在class语句中通过赋值语句添加，而不是在def中


"""
class C:
    def setName(self,name):
        self.name=name

# 通过赋值语句创建属性，首次赋值时才存在
class C2(C):{}

d1 = C2()
d2 = C2()
d1.setName("caesar")
d2.setName("ming")
print(d1.name)
print(d2.name)
# 在调用setName前，引用name会发生错误，解决的办法是在初始化时候进行setName
class C3(C):
    def __init__(self,who):
        self.name=who
    def setName(self,name):
        self.name=name

# init是构造函数

class Person:
    def say(self):
        print("Person")

class Man(Person):
    def say(self):
        print("Man")

class Woman(Person):
    def say(self):
        print("Woman")

p = Person()
p.say()

m = Man()
m.say()

w = Woman()
w.say()

# 多态