__author__ = 'Administrator'


# 列表与字典

print(len([1, 2, 3]))
print([1, 2, 3]+[4, 5, 6])
print(['NI!']*4)

print(3 in [1, 2, 3])

for x in [1, 2, 3]:
    print(x, end=' ')

res = [c*4 for c in ['c', 'd', 'e']]
print(res)
res = []
for c in 'HaHa':
    res.append(c*2)
print(res)

print(list(map(abs, [-1, -2, 1, 3])))

# 在原处修改

L = ['spam', 'jack', 'some', 'one']
L[0] = 'Carsar'
print(L)
# delete and insert
L[0:2] = ['aa', 'bb', 'cc']
print(L)

# 索引和分片都是在原处修改

# 列表方法调用
L.append('please')
print(L)
L.sort()
print(L)

# a.append()会在原处添加，L+[1,2,3]会新生成,sort也是原地排序
D = ['ab', 'Ad', 'dB']
D.sort(key=str.lower)
print(D)
D.sort(reverse=False)
# append method return a None Object
sorted(L, key=str.lower, reverse=False)

# the result didn't contain the initial param
sorted([x.lower() for x in ['as', 'Dd', 'c']], reverse=True)

L = [1, 2]
L.extend([3, 4, 5])
print(L)
print(L.pop())
print(L)
L.reverse()
print(L)
list(reversed(L))

L = ['a', 'b', 'c']
print(L.index('b'))
L.insert(1, 'd')
print(L)
L.remove('c')
print(L)

# delete the source param
L = [1, 2, 3]
del L[0]
print(L)
del L[1:]
print(L)

# 字典
D = {'spam': 1, 'jack': 2, 'caesar':3}
print(D['spam'])

len(D)
print('spam' in D)
print(list(D.keys()))

D['spam'] = ['a', 'b', 'c']
print(D)
D['spam'] = {'a': 1, 'b': 2}
print(D)
del D['spam']
print(D)
D['ww'] = 'cc'
print(D)

D = {'a': 1, 'b': 2}
print(list(D.values()))
print(list(D.items()))

print(D.get('jack'))
print(D.get('a'))
print(D.get('jack', 88))

# update 类似合并
D2 = {'c': 3, 'd': 4}
D.update(D2)
print(D)


print(D.pop('a'))
L = [1, 2, 3]
print(L.pop())
print(L.pop(1))

# 语言表

D = {'a': 'A', 'b': 'B', 'c': 'C'}
print([D[x] for x in D])

# 字典用法
"""
    1，字典没有顺序,不能执行分片，串联等操作
    2，对索引赋值会添加项
    3，键不一定总是字符串

"""

# 比较
L = [1, 2]
# error print(L[3])
D = {1: 'a', 2: 'b'}
D[3] = 100
print(D)

# 稀疏数组
Mix = {}
X = 1; Y = 2; Z = 3
Mix[(X,Y,Z)]='a'
print(Mix)

# 避免missing key
if (1, 2, 3) in Mix:
    print('a')
else:
    print('b')


try:
    print(Mix[(7, 8, 8)])
except KeyError:
    print("error")

print(Mix.get((7, 8, 8), 99))

# create dictionary in other way
D = dict(a=1, b=3)
print(D)
D = dict([('a', 'a'), (100, 200)])
print(D)

# 传入一个列表和默认值,the second parameter is the default value
D = dict.fromkeys([1, 2, 3], 5)
print(D)

L = list(zip([1, 2], ['a', 'b']))
print(L)
D = dict(zip([3, 4], ['c', 'd']))
print(D)

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {x: x**2 for x in [1, 2]}
print(D)

D = {c.lower(): c for c in ['D', 'A']}
print(D)

# default is none
D = dict.fromkeys(['a', 'b'])
print(D)

D = dict.fromkeys('hello')
print(D)

D = dict(a=1, b=2, c=3)
K = D.keys()
# k is a iterator
print(K)
print(list(K))

print(D.values())
print(D.items())
print(list(K)[0])

# 字典的key，value值视图是可改变的
D = {'a': 1, 'b': 2}
K = D.keys()
print(list(K))
del D['a']
print(list(K))
V = D.values()
print(list(K))
print(K | {'c': 3})
# error print(V | {'c': 3})
# key 返回的是集合，value不是的，所以key可以进行交集等操作

D = {'a': 1}
list(D.items())
print(D.items() | D.keys())
print(D.items() | D)

print(dict(D.items() | {('c', 3)}))

# key 没有排序方法，只能转换成list然后排序，或者用sorted
KS = D.keys()
for k in sorted(KS):
    print(k)



