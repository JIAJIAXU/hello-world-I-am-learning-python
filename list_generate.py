# 列表生成式
L = []
for x in range(1, 11):  # 循环生成列表
    L.append(x * x)
print(L)
###########
l = [x * x for x in range(1, 11) if x % 2 == 0]  # 列表生成式，直接在列表中利用函数生成列表
print(l)
doulist = [m + n for m in 'ABC' for n in 'XYZ']  # 两层循环生成全排列
print(doulist)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)
L3 = [bb.lower() for bb in L1 if isinstance(bb, str)]
print(L3)
