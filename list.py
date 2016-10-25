classmate = ["许家彪", "姚盼"]  # list数据类型
print(classmate[0])
print(classmate[1])
print(len(classmate))
# 类的索引的范围为0~n-1
# 最后一个元素的索引是len(classmates) - 1
# classmate[-1]为倒数第一个元素
print(classmate[-1])
classmate.insert(1, "我爱你")  # 插入元素到类的指定位置
print(classmate[0], classmate[1], classmate[2])
classmate.pop()  # 删除类的最后一个元素，注释前两个空格，后面一个空格
# "姚盼"
print(classmate)
classmate.pop(1)  # 删除类的指定位置的元素
# "姚盼"
print(classmate)
classmate.insert(1, "我爱你")
classmate.insert(2, "姚盼")
print(classmate)
classmate[1] = "爱"
print(classmate)
L = ["XUJIABIAO", "姚盼", "1314"]  # list中的数据类型可以不同
print(L)
classmate.insert(0, L)  # list中的元素也可以是另一个list
print(classmate)  # list中含有其他list时则为二维list（或者更高维）
print(L[1])
print(classmate[0][2])  # 二维数组
# 另一种有序列表叫元组：tuple。
# tuple和list非常类似，但是tuple一旦初始化就不能修改,指向的元素不变，元素内的元素可以改变
classmate = ("hah", "qaq", "lol")  # 逗号后面加空格，=左右加空格
print(classmate)  # tuple表示的是元组，可以对其中的元素进行访问，却无法修改
t = (1)  # t=(1)与t=(1,)有区别，前者表示1这个数，后者表示（1，）这个元组
print(t)
t = (1,)
print(t)
'''
定义的不是tuple，是1这个数！
这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，
计算结果自然是1。
'''
a = ["A", "B"]
b = ('a', 'b', a)
c = b
print(b[0])
print(b[1])
print(b[2])
b[2][0] = 'aa'  # 元组的三个元素为'a','b',a，虽然元组的元素是不变的，但list a的元素是可以改变的
b[2][1] = 'bb'
print(b[0])
print(b[1])
print(b[2])
print(c)
L1 = ['apple', 'google', 'microsoft']
L2 = ['java', 'python', 'ruby', 'php']
L3 = ['adam', 'bart', 'lisa']
L = [L1, L2, L3]
print(L[0][0])
print(L[1][1])
print(L[2][2])
L = list(range(100))  # 100个元素
print(L)
L = [range(100)]  # 只有一个元素
print(L)
a = (1, 2, 3, 4)  # (1,2,3,4)这个元组本身是不变的，而变量a只是指向它，所以可以对a重新赋值
x = a
a += a
print(a)
print(x)
a = [1, 2, 3, 4]
x = a
a += a  # [1,2,3,4]数组对象本身发生了改变
print(a)
print(x)
a = 'ABC'
b = a
a += a
print(b)
print(a)

