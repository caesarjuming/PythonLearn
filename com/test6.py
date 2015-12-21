__author__ = 'Administrator'

# if 测试和语法

if   1>2 :
    print(1)
elif 2>3 :
    print(2)
else:
    print(3)

# 类似switch
choice = 'a'
print({'a': 1, 'b': 2}[choice])

""" 语句是逐行执行的
    块和语句自动检测

    其实这章也没什么好记得，都是习惯
"""
# 任何非0数字都为真，非空对象为真
# 0，空对象，None都是假
# 比较相等会递归数据结构
# 比较相等测试会返回True和False

print(True and False)
print(True or False)
print(not True)

# or 和 and 有短路
print(2 or 3, 3 and 4)
print(() or {})

# 两个操作数都是真，会返回右侧的

# 类似的三元运算符,如果 b是真的，返回a,否则c

A = 'a' if not 'b' else 'c'
print(A)











