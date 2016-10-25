# 迭代
from collections import Iterable
d = {'a': 56, 'b': 76, 'c': 76}
for key in d:
    print(key)
for ch in 'i love you':
    print(ch)
'''
当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
'''
print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
for k, v in d.items():  # 对d的所有元素取值
    print(k, v)
for value in d.values():  # 对d的key的取值
    print(value)
print(1 + 2)
