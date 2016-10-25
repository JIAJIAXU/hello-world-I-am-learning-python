# function factor
def power1(x):
    print(x ^ 9)
power1(3)
'''
^表示二进制数的异或
byte b = 9;
byte b0 = 3;
System.out.println(b^b0^b0); // ?
9的二进制：00001001
3的二进制：00000011
  00001001(9)
^00000011(3)
=00001010(按位运算相同为0，不同为1)
^00000011(3)
=00001001(貌似还是9)
'''


def power(x, n=2):  # 设置默认参数，必选参数在前，默认参数在后
    print(x**2)  # x*x，x**2，表示平方
power(10)


def power(x, n):
    print(x**n)
power(5, 3)
'''
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了。所以，定义默认参数要牢记一点：
默认参数必须指向不变对象！要修改上面的例子，我们可以用None这个不变对象来实现：
'''


def add_end(L=[]):
    L.append('END')
    print(L)
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
add_end()
add_end()
# 定义可变参数，传入的参数的个数可变


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n**2
    return sum
print(calc([1, 2, 3]))  # 把参数作为list或者tuple输入函数
print(calc((1, 2, 3, 4, 5)))


def calc1(*numbers):  # 定义函数的参数为可变参数
    sum = 0
    for n in numbers:
        sum = sum + n**2
    print(sum)
calc1(1, 2, 3)  # 直接输入可变参数，不需list或tuple
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
nums = [1, 2, 3]  # 如果有一个人list或tuple，则可以在其前面加*，把list或tuple的元素转换为可变参数输入函数
calc1(*nums)
'''
可变参数允许你传入0个或任意个参数，
这些可变参数在函数调用时自动组装为一个tuple
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict
'''
# 关键字参数


def person(name, age, **kw):  # 关键字参数是一个dict，允许输入参数名和参数值
    print('name:', name, ',age:', age, ',other:', kw)
person('michael', 20, city='beijin', gender='male', job='scientist')
extra = {'city': 'beijing', 'job': 'engineer'}
person('jack', 24, city=extra['city'], job=extra['job'])
person('jack', 24, **extra)
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
'''
# 命名关键字参数
# 如果要限制关键字参数的名字，则可以用关键字参数
# 例如只接受city和job作为关键字参数


def person1(name, age, *, city, job):  # 命名关键字参数需要*隔开，*后面的参数被视为命名关键字参数
    print(name, age, city, job)
person1('xu', 23, city='beijing', job='student')  # 命名关键字参数必须传入参数名
# 混合参数


def f1(a, b, c=0, *arg, **kw):  # a,b为必选参数，c为默认参数，arg为可变参数，kw为关键字参数
    print('a=', a, 'b=', b, 'c=', c, 'arg=', arg, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):  # a,b为必选参数，c为默认参数，d为命名关键字参数，kw为关键字参数
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
f1(1, 2)
f2(1, 2, d=99, ext=None)
