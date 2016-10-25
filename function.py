# help(abs)
# help(hex)  # 查询函数的功能
'''
>>> abs(1, 2) 调用函数时参数出错，调用函数的参数个数，参数类型都要匹配函数
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
'''
import math  # import表示导入函数
# print(max(1, 2))
# print(hex(1928394))
# print(ord('我'))
# print("1928394的十六进制为：" + hex(1928394))  # 1928394的十六进制为：0x1d6cca,输出的字符串间没有空格
# print("1928394的十六进制为：", hex(1928394))
# 1928394的十六进制为： 0x1d6cca,输出的字符串间有一个空格


def my_abs(x):  # def 定义函数，依次写出函数名、括号，括号中的参数，然后是冒号
    # 然后在缩进块中编写函数体，函数的返回值用return语句
    if not isinstance(x, (int, float)):
        raise TypeError('bad operal type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))
# print(my_abs("a"))  参数类型不符合，输出报错
# 参数检查
# 当传入不恰当的参数时，内置函数abs()会检查出参数错误
# 而我们定义的my_abs()没有参数检查，因此需要在函数中加入参数检查


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # 函数返回多个值,其实返回的是一个tuple


x, y = r = move(1, 2, 3, math.pi / 3)
print(x, y)
print(r)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type a')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type b')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type c')
    de = b**2 - 4 * a * c
    if de < 0:
        print("方程无实解")
    elif de == 0:
        x = -b / 2 * a
        print('x= ', x)
    else:
        x1 = (-b - math.sqrt(de)) / 2 * a
        x2 = (-b + math.sqrt(de)) / 2 * a
        print('x1=', x1, "\nx2=", x2)  # 如果使用return的话，则最后的输出结果为元组（，)


quadratic(1, 4, 1)                        # 使用print可以输出x1=的格式
quadratic(1, 1, -6)

'''
print(quadratic(1, -2, 1))  # 使用return时，使用这种方式输出
print(quadratic(1, 2, 1))
print(quadratic(1, 2, 2))
print(quadratic(1, 3, 1 / 4))
'''
