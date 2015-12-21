__author__ = 'Administrator'


# 元组,是不可以修改的

print((1, 2)+(3, 4))
print((1, 2)*4)

T = (1, 2, 3, 4)
print(T[0])
print(T[1:2])
print(T[1:3])
V = (50)
# integer
print(V)
# tup
VV = (50,)
print(VV)

T = ('b', 'c', 'a')
list(T).sort()
print(T)
tuple(T)
# T[0] = 'd'
# tuple didn't has T.sort() method
sorted(T)

# 这两个转换其实都是新生成一个对象

T = (3, 4, 5, 6, 7, 6)
M = [x+20 for x in T]
print(M)
print(T.index(5))
print(T.index(4, 0))
print(T.count(6))

# 其实元组的内容是可变的

T = (1, 2, [3, 4])
T[2][0] = 88
print(T)

# wrong T[2] = 'b'

# file

myFile = open("myFile.txt", "w")
# 返回的是写入的字符数
print(myFile.write("hello\n"))
myFile.write("world\t!")
myFile.close()

myFile = open("myFile.txt", "r")
print(myFile.readline())
print(myFile.readline())
myFile.close()

# read all
print(open("myFile.txt", "r").readline())

for line in open("myFile.txt", "r"):
    print(line, end="~")

b = open("data.bin", "wb")
b.write(b"\x00\x77\xff")
b.close()

b = open("data.bin", "rb")
print(b.readline())

# 写入文件中的一定是字符串所以我们需要手动转成字符串
F = open('datafile.txt', 'w')
F.write('ss'+'\n')
F.write('%s,%s,%s\n' % ('a', 'b', 'c'))
F.write(str(123) + '$' + '\n')
F.close()

chars = open('datafile.txt').read()
print(chars)
F = open('datafile.txt')
line = F.readline()
# 去掉终止符
print(line.rstrip())
print(int('10'))
# eval可以执行字符串
eval("print('hello,world')")

# pickle 可以储存原生Python对象
D = {'a': 1, 'b': 2}
F = open("datafile.pkl", 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open("datafile.pkl", "rb")
E = pickle.load(F)
print(E)

F = open("data.bin", 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('>i4sh', data)
print(values)


# 文件上下文管理器
with open('test.txt') as myFile:
    for line in myFile:
        print(line)

myFile = open('test.txt')
try:
    for line in myFile:
        print(line)
finally:
    myFile.close()

# 嵌套
L = ['abc', [(1, 2), ([3], 4)]]
print(L)
print(L[1][1][1])

# 分片操作可以Copy,字典的Copy方法，list

L = [1, 2, 3]
D = {'a': 1, 'b': 2 }
A = L[:]
B = D.copy()

print(A, B)

# 比较，相等性和真值
L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2)
print(L1 is L2)

# == 递归的比较值，is 是比较是否属于同一对象


L1 = 'spam'
L2 = 'spam'
print(L1 == L2)
print(L1 is L2)

# 因为Python会把字符串缓存

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2)
print(L1 == L2)
print(L1 > L2)

# python 中不同类型比较方法
""" 数字比较大小
    字符串按照字典顺序
    列表和元组按照从左到右顺序比较
    3.0不支持字典比较
    3.0不支持数字混合比较
"""

D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(D1 == D2)
# error print(D1 > D2)
print(sorted(D.items()) < sorted(D2.items()))

# python 中真假
print(bool("spam"))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(1))
print(bool(0.0))
print(bool(None))

#  类型，type本身也是一个type
print(type([1]) == type([]))
print(type([1]) == list)
isinstance([1], list)

import types
def f():
    pass
print(type(f) == types.FunctionType)

# 赋值是引用，而不是一个拷贝

L = [4, 5, 6]
X = L * 4
Y = [L] * 4
print(X)
print(Y)
L[0] = 99
print(X)
print(Y)

X = ['a']
X.append(X)

print(X)




