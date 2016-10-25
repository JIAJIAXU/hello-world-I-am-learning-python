from math import sqrt
if False:
    print("我爱你"),
    print(3 > 2),
    print('包含中文的str'),
    print(ord('a')),
    print('hello,woeld'),
    print(100 + 200),
    print(abs(-1)),
    x = abs(-10),
    print(x),
    f = abs,
    print(f),
    print(f(-10))
# 使用 if False :语句来屏蔽不需要运行的代码


def same(x, *fs):
    s = [f(x) for f in fs]
    return s


print(same(2, sqrt, abs))
print('Age: %s. Gender: %s' % (25, True))
# python 格式化方式，用%实现
#  %d   整数 %03d表示在整数d的前面加3个0
#  %f   浮点数 %.3f表示保留3位小数
#  %s   字符串
#  %x   十六进制整数
print('Hello, %s' % 'world')
print('%03d-%03d' % (3, 1))
print('%.3f' % 3.1415926)
