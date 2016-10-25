age = 20
if age <= 18:
    print('你的年龄太小')
else:
    print('成年人允许入内')
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
    # if语句的完整形式
    '''
    if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
    '''

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

h = input("请输入您的身高:")  # 输入的数据类型是字符串，因此要转换成浮点型float()
w = input("请输入您的体重:")
h1 = float(h)
h2 = h1 * h1
w1 = float(w)
r = w1 / h2
if r < 18.5:
    print("过轻")
elif 18.5 < r < 25:
    print("正常")
elif 25 <= r < 28.5:  # 严格来讲应该写成r>=25 && r<28.5
    print("肥胖")
else:
    print("过度肥胖")
age = 20
if age >= 6:
    print('teenager')
    if age >= 18:
        print('adult')
        if age >= 0:
            print('kid')
