# 循环的使用
from function import my_abs
names = ["许家彪", "我爱你", "姚盼"]
for name in names:  # for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # 注意条件语句后面要加:
    sum = sum + x
    print(sum)  # 与上面都语句属于同一级，因此每次执行都要输出一次
print(sum)  # 上述语句执行结束之后执行，因此只输出最后的结果
sum = 0
for x in range(101):  # 注意条件语句后面要加:
    sum = sum + x
print(sum)
sum = 0
n = 100
while n > 0:
    sum += n
    n = n - 1
print(sum)
L = ['BART', 'LISA', 'JACK']
for x in L:
    print("Hello,", x, "!")  # 输出的字符之间有空格
a = 0
while a < len(L):
    print('Hello,%s!' % L[a])  # 输出的字符之间没有空格
    a = a + 1
a = 0
while a < len(L):
    print('Hello,', L[a], "!")  # 输出的字符之间有空格
    a = a + 1
# 遇到死循环时，用Ctrl+C退出程序，或者强制结束Python进程
x = 1   # 在循环语句中使用if语句和break来控制程序的执行，不然会进入死循环
while True:
    x += 1
    print(x)
    if x > 5:
        break
my_abs(-6)
my_abs(-6)
