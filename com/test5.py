__author__ = 'Administrator'

# 赋值，表达式，打印

"""
    赋值语句建立对象引用值
    变量在首次赋值时会被创建
    变量在使用前必须赋值
    执行隐式赋值，例如函数定义

"""
a = 1
b = 2
A, B = a, b
print(A, B)
A, B = B, A
# 赋值变量时，会临时创建一个元组，储存这些值
print(A, B)

[a, b, c] = (1, 2, 3)
print(a, b)
(a, b, c) = "abc"
print(a, b)

# 并列赋值语句支持右侧任何的迭代，但是右边的数目要和左边相同

string = 'spam'
a, b, c, d = string
print(b, c)

# error a, b, c =string

# 可以支持嵌套
((a, b), c) = 'sa', 'pm'
print(a, b)
print(c)

red, green, blue = range(3)
print(green)

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

# 在3.0中，可以使用通配符来解决参数不对应的问题

seq = [1, 2, 3, 4]
a, *b = seq
print(a, b)
*a, b = seq
print(a, b)

seq2 = [1, 2, 3, 4, 5]
a, *b, c = seq2
print(a, b, c)

# 对其他类型也是有效的
a, *b = 'spamspam'
print(a, b)

# 然后上面的就可以改写成
L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

# 带*可能只匹配一个，但是也会组成一个列表,如果是多余的，那么会赋予一个空列表

a, b, *c = [1, 2, 3]
print(a, b, c)

a, b, *c = 'ab'
print(a, b, c)

# error a, *b, *c = 'abcd' 不能两个*


# for 循环中使用
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

# 多目标赋值语句


a = b = c = 'spam'
print(a, b, c)

a = b = 0
print(a, b)
b = b + 1
print(a, b)
# 数字不支持在原处修改

# 如果是引用类型就可变了
a = b = []
a.append(1)
print(a, b)

# 增强赋值语句
x = 1
x += 1
print(x)

# -= += *= >>= X//=Y floor除法
# 用extend方法是在原处添加，比+快
L = [1, 2]
L.extend([3, 5])
print(L)

# 增强赋值以及共享引用，+=是对原来的操作，+是生成一个新的对象

# Python命名区分大小写，变量名没有类型，对象有

# print 没有完结


