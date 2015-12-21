__author__ = 'Administrator'

x = 'spam'
while x:
    print(x, end = ' ')
    x = x[1:]

# python 中并没有 do until

x = 10
while x :
    x = x -1
    if x % 2 == 0 : continue
    print(x, end = ' ')

# 只有当continue不执行时，才会运行到print

# break 退出
""" while True:
    name = input('enter a name:')
    if name=='stop': break;
"""
x = 10
while x > 0:
    print(x)
    x -= 1
else:
    print('fushu')


