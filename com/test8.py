__author__ = 'Administrator'

# 14，迭代器和解析器

for x in [1, 2, 3, 4]: print(x ** 2, end='#')
for x in 'spam' :print(x * 2, end='!')

# for 循环可用于任何可迭代的对象

# 文件迭代器
f = open("test.txt", "r")
print(f.readline())

# 文件也有一个方法__next__方法，每调用一次，返回一行，但是和readline不同的是，如果到文件结尾，会引发异常stopIteration
print(f.__next__())
# error because it come to end print(f.__next__())

f = open("datafile.txt")
for line in f:
    print(line, end='@')

# 手动迭代 iter，next
# 调用f.__next__()等于调用next(f)
f = open("datafile.txt")
print(next(f))

# 当for循环开始时，会通过它传给iter内置函数
L = [1, 2, 3]
I = iter(L)

# 刚才一句对于文件不是必须的，因为文件对象就是自己的迭代器

print(iter(f) is f)

# 列表和其他一些对象则不是自己的迭代器,因为他们支持多次打开迭代器
print(iter(L) is L)
It = iter(L)
print(It.__next__())

L = [1, 2, 3]
I = iter(L)
while True:
    try:
        print(I.__next__())
    except StopIteration:
        print("exception")
        break

# 其他内置类型迭代器
D = {'a': 1, 'b': 2, 'c': 3}
for x in D.keys():
    print(D.get(x))

# 字典有个迭代器，一次返回一个Key
I = iter(D)
print(I.__next__())

# 最直接的作用，我们不再用D.keys方法
for x in D:
    print(x, D[x])

# 可迭代对象，一次返回一个值
R = range(5)
I = iter(R)
print(I.__next__())
print(I.__next__())

E = enumerate(R)
print(E)
I = iter(E)
print(I.__next__())
print(I.__next__())
print(list(enumerate('spam')))

# 列表解析
L = [1, 2, 3]
L = [x*2 for x in L]
print(L)

# 文件上使用列表解析
f = open('data.txt', 'r')
lines = f.readlines()
print(list(lines))
lines = [line.rstrip() for line in lines]
print(list(lines))

L = [li.upper() for li in open("data.txt", 'r')]
print(L)

# 收集P开头的字符串
L = [x for x in open("fileT1.txt", 'r') if x[0] == 'c']
print(L)

L = [str(x)+y for x in [1, 2, 3]  for y in ['a', 'b', 'c']]
print(L)

# map return a 可迭代 object
print(list(map(str.upper, open("fileT1.txt", 'r'))))
# zip ,enumerate, map 都返回可迭代对象

print(sum([1, 2, 3]))

# any 如果可迭代对象里面有真值，那么返回True
print(any([1, '', True, ]))
print(all([1, '', True, ]))
print(max([1, 2, 4]))
print(min([1, 2, 3]))
print(tuple(open("fileT1.txt", 'r')))
print('*&'.join(open("fileT1.txt", 'r')))
a, *b = open("fileT1.txt", 'r')
print(a, b)

set(open("fileT1.txt", 'r'))
print({line for line in open("fileT1.txt", 'r')})
print({ix: line for ix, line in enumerate(open("fileT1.txt", 'r'))})

def f(a, b, c) : print(a, b, c, sep='&')
f(1, 2, 3)

# *号是解参数，解开为单个的参数
f(*[1, 2, 3])

# *作为 unzip 功能
X = {1, 2}
Y = {3, 4}
A, B = zip(*zip(X, Y))
print(A, B)

# 除了文件和字典这样的内置迭代，字典方法keys，items，values都是迭代对象
print(list(zip('abc', 'def')))

# range是返回一个迭代器而不是在内存中的数据
V = range(10)
I = iter(V)
print(I.__next__())
print(I.__next__())
print(list(V))

# map zip filter 迭代器
M = map(abs, (1, -2, -3))
print(M.__next__())
print(next(M))
print(M.__next__())

Z = zip((1, 2, 3), ('a', 'b', 'c'))
print(list(Z))

for zz in Z:
    print(zz, end='%')

for x in filter(bool, ['a', 0, None, '']):
    print(x, end='@\n')

# range 不是自己的迭代器，手动迭代时需要用iter创建一个，可以创建多个迭代，会记住他们的位置
R = range(8)
I = iter(R)
I2 = iter(R)
print(next(I))
print(next(I2))
print(next(I))
print(next(I2))

# zip map filter 不支持多个迭代
Z = zip((1, 2, 3, 4), ('a', 'b', 'c', 'd'))
I = iter(Z)
I2 = iter(Z)

# the same value
print(I.__next__())
print(I2.__next__())
print(I.__next__())
print(I2.__next__())

# 字典视图迭代

D = dict(a=1, b=2, c=3)
print(iter(D.keys()).__next__())
# didn't work D.keys().__next__() 不是一个迭代器

