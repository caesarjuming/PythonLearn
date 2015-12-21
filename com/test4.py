__author__ = 'Administrator'


# python 语句介绍
if 2 > 1:
    print("无括号")

# 括号是可选的
if (2 > 1):
    print("有括号")

# 缩进就是代码块的结束

# 一行多个语句用;分割
a = 1; b = 2; print(a+b)

mlist = [111,
         222,
         333]
print(mlist)

X = ('a' + 'b'
     + 'c')
print(X)

if(1 == 1 and
    2 == 2 and
    3 == 3
    ):
    print('hello')

X = 'a' + \
    'b'

print(X)

""" 交互
while True:
    reply = input('enter txt:')
    if reply == 'stop' : break
    print(reply.upper())
"""

S = '123'
T = 'abc'
print(S.isdigit())
print(T.isalpha())

# 用Try 处理错误
"""
while True :
    reply = input('enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad' * 3)
    else:
        print(int(reply) ** 2)
print('bye')

"""

