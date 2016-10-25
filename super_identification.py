L = range(100)[1::2]
print(L)
l = list(range(100))[1::2]
print(l)
P = list(range(2, 5))  # range(i,j)生成一个列表[i,i+1,i+2,...,j-1],默认从0开始
print(P)
# help(range)
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
L1 = ['michael', 'jack', 'mary', 'rose', 'panpan']
len1 = len(L1)
# print(len1)
l = []
for x in range(len1 - 2):  # 通过循环从list的长度len1中取值
    l.append(L1[x])
print(l)
print(L1[0:2])  # 切片取值[0:2]表示，从索引0开始取值，直到索引2（但不包括2）
print(L1[:3])  # 索引3之前的所有元素
print(L1[2:4])  # 索引2到索引4的所有元素
print(L1[:-2])  # 倒数第二个元素之前的元素
print(L1[-2:])  # 倒数第二个元素之后的元素
l1 = list(range(100))
print(l1[:10:3])  # 前10个数，每2个取一个
print(l1[::5])  # 所有元素每5个取一个
t = (0, 1, 2, 3, 4, 5)  # 元组也是一种list，也可以切片
print(t[:3])
s = 'ABCDEFG'  # 对字符串进行切片
print(s[3:6])
'''
a[::-x],就是从后至上的输出，数字与数字之间隔x
a[y::-x],就是从第y个开始往前输出数字，数字与数字之间隔x
a[-y::-x],就是从倒数第y个数字开始往前输出，数字与数字之间隔x
...简而言之 前面的数值符号决定了他第一个输出的数字是从那边开始，
后面的数值符号决定了他是倒序还是正序
print(L[::1])=print(L[0::1])
而print(L[::-1])=print(L[9::-1])
并不是从0开始
'''
