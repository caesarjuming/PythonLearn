__author__ = 'Administrator'

# python处理的每一样东西都是对象，像模块，函数，类都是对象。
# Python是强类型的，也就是只能对相应类型做相应的操作，例如只能对字符串进行字符串操作，但他是动态类型

# python数字类型有整数，浮点类型，复数，十进制数，有理分数，集合等
print(1+1)
print(2.11+3)
print(2*4)
print(2**3)

import math
print(math.pi)
print(math.sqrt(4))
import random
print(random.random())
print(random.choice([1,2,3,4]))

# 字符串
name = 'jack'
print(name)
print(name[0])
print(len(name))

print(name[-1])
print(name[len(name)-1])
# 分片,取出1到3之间的字符，不包括3，return a new object
print(name[1:3])
print(name[1:])
print(name[:])
print(name[:3])

print(name[:-1])
print(name*8)
print("hello,"+name)
# it's wrong //print(1+"hello"),不能两种类型进行相加

# 不可变性
firstName = "caesar"
# firstName[1] = "b" it doesn't work
print(firstName[1]+'z')

# 类型特定方法

print(firstName.find('c'))
print(firstName.find('z'))
print(firstName.replace('c', '@'))
print(firstName)

str1 = "aaa,bbb,ccc,ddd"
print(str1.split(',')[1])
print(str1.upper())
print(str1.lower())
print(str1.isalpha())

str2 = '\n\naaa\n\n\t'
print(str2.rstrip())

print("%s hello,world %s" % ("a", "b"))
print("{0} hello,world {1}".format("a", "b"))

# 寻求帮助
s1 = "aaa"
print(dir(s1))
print(dir(s1.lower))

s2 = '\b\b\bc'
print(len(s2))
print(ord('a'))
print(ord('A'))

# add a enter
s3 = """jack

jack
        """

print(s3)

s4 = """jack ''''  " "" a
"""

print(s4)

L = [1, 's', 2.2]
print(L)
print(L+[1, 2, '5'])
print(L)

print(L.append("D"))
print(L)
print(L.pop(2))
print(L)

M = ["b", "a", "c"]
print(M.sort())
print(M)
print(M.reverse())
print(M)


# wrong print(M[99])

# 嵌套
W = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(W[0][1])

row1 = [row[1] for row in W]
print(row1)
print([row[1]+1 for row in W])
print([row[1]+3 for row in W if row[1] % 2 == 0])
print([W[i][i] for i in [1, 2]])
print([c*2 for c in 'spam'])

# 迭代器
G = (sum(m) for m in W)
print(next(G))

# 运行各项然后产生结果
print(list(map(sum, [[1, 2, 3], [4, 5, 6]])))
print({sum(row) for row in [[1, 2, 3], [4, 5, 6]]})
P = [[1, 2, 3], [4, 5, 6]]
print({i: sum(P[i]) for i in range(2)})

# ord 转换为ASCII码
print([ord(w) for w in ['a', 'b', 'c']])
print({jj: ord(jj) for jj in ['1', '2', '3']})

# 字典 字典没有可靠的顺序
myName = {"firstName": "jack", "lastName": "ming", "age": 5}
print(myName["firstName"])
print(myName["lastName"])
myName["age"] += 1
print(myName)

secondName = {}
secondName["firstName"] = "caesar"
secondName["secondName"] = "wang"
print(secondName)

# 解决嵌套
Ronaldo = {"name": {"firstName": "Cristiano ", "lastName": "Ronaldo"},
            "age": 88,
            "like": ["girl", "food"]
            }
print(Ronaldo)
print(Ronaldo["name"]["firstName"])
print(Ronaldo["like"][1])
Ronaldo["like"].append("pat")
print(Ronaldo)

# 通常最后一个引用失效后，对象会被垃圾回收

KS = {"a": 1, "b": 2, "c": 3}
print(KS.keys())
KSS = list(KS.keys())
KSS.sort()
print(KSS)
# 无序的
for x in KS:
    print(x, ":", KS[x])

# 通过内置函数排序，有序的
for xx in sorted(KS):
    print(xx, ":", KS[xx])

for c in 'abc':
    print(c.upper())

time = 4
while time > 0:
    print("hello!"*time)
    time -= 1

print([mm*2 for mm in [1, 2, 3, 4]])

print('b' in 'abc')

if 'b' not in 'aac':
    print("miss")

DD = {"a": 1, "b": 2, "c": 3}
print(DD.get("d", -1))
print(DD['D']if 'D' in "abc" else -2)

# 元组，不可改变的列表

tup = (1, 2, 3)
print(tup + (4, 5))
print(tup[0])
# tup[0]=3 error 不能改变
print((1, 2, ['a', 'b'], 'c'))

# 写文件
f = open("data.txt", "w")
f.write("bbb\nccc,ddd")
f.close()

# 读文件
ff = open("data.txt", "r")
print(ff.read())
print(ff.read().split(",")[0])
ff.close()

# 二进制
print(open("data.txt", "rb").read())

# 集合
ss = set("aaaabbb")
print(ss)
Y = {'a', 'b', 'd', 'd'}
print(Y)
print(ss, Y)
print(ss & Y)
print(ss | Y)
print(ss - Y)

print(1/3)
print(1/3+2/3)

import decimal
dd = decimal.Decimal(3.14)
dd += 1
print(dd)

decimal.getcontext().prec = 3
print(decimal.Decimal(1)/decimal.Decimal(3))

from fractions import Fraction

# 分数运算

f = Fraction(2, 3)
f += 1
f + Fraction(1, 3)
print(f)

print(bool("aaa"))
print(None)

print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print("yes")

if isinstance(L, list):
    print("yes!")

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]


    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker("aaa", 100)

bob.giveRaise(1)

print(bob.lastName())
print(bob.pay)

