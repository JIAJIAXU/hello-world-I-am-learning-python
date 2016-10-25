def fact(n):
    if n == 1:
        return 1  # 设定fact(1)==1
    return n * fact(n - 1)  # 设定递归函数（函数内部含有函数本身），fact(n)=fact(n-1)*n


print(fact(5))
print(fact(4), fact(3), fact(2), fact(1))
'''
函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
return None可以简写为return。
'''
# 空函数
# def nop():
#   pass
#   pass语句什么都不做，那有什么用？
#   实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#   就可以先放一个pass，让代码能运行起来。
# 所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 尾递归，优化递归的调用，避免栈溢出
'''
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，
会导致栈溢出，可以通过尾递归的方法解决：在函数返回的时候，调用自身本身，
并且，return语句不能包含表达式
'''


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))

# 汉诺塔
# 将(n-1)个盘子从x(借助z)移到y
# 将第n个盘子从x移到z
# 将(n-1)个盘子从y移到z
# ......依次类推


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        hanoi(1, x, y, z)  # 将最底下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔的层数：'))
hanoi(n, 'x', 'y', 'z')
i = 1


def move(n, a, b, c):
    global i
    if n == 1:
        print('Step', i, ':', a, '-->', c)
        return
    move(n - 1, a, c, b)
    i = i + 1
    print('Step', i, ':', a, '-->', c)
    i = i + 1
    move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
i = 1
'''
对于给定的问题，要先分析其结构，然后用函数的形式表示这种结构
'''
