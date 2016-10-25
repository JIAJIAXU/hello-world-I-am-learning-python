# Python内置的字典：dict
# 建立key-value存储，为每个对象建立一个索引,key不能重复
d = {'michael': 95, 'bob': 75, 'tracy': 85}
print(d['michael'])
print(d['bob'])
print(d)
d['adam'] = 67
print(d['adam'])
d['adam'] = 89  # 由于一个key只能对应一个value，因此对同一个key多次输值时，后面的会覆盖前面的
print(d['adam'])
# print(d['thomas'])  # key不存在，输出报错
print('thomas' in d)  # 检查dict中是否存在某个对象
print(d.get('thomas', -1))  # 检查dict中是否存在某个对象，如果不存在这返回None或自己制定的value
print(d.get('thomas'))
print(d.pop('bob'))
print(d)
# dict的key必须是不可变对象.在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key：
# >>> key = [1, 2, 3] key不能为list
# >>> d[key] = 'a list' ，输出会报错
# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])  # 一个set只能放入一个list作为对象
print(s)
s = set((1, 2, 3))  # 元组作为set的一个对象
print(s)
s = set([1, 1, 2, 2, 3, 3])  # 重复的元素在set中自动被过滤
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # set交集
print(s1 | s2)  # set并集
'''
因为Set本质上是一个引用类型，
它的赋值时赋予地址，而不是数值。
所以 a = s， b = s之后，a和b指向了同一块内存，
其实可以说是同一个东西
'''
s = set([1, 2, 3])
a = s
a.add(45)
print(a)  # 输出结果1,2,3,4
b = s
b.add(5)
print(b)  # 输出结果1,2,3,4,5
u = a & b
print(u)  # 输出结果1,2,3,4,5
u = a | b
print(u)  # 输出结果1,2,3,4,5
