'''
排序也是在程序中经常用到的算法。
无论使用冒泡排序还是快速排序，
排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，
但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来。
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_grade(g):
    return g[1]


print(sorted(L, key=by_name))
print(sorted(L, key=by_grade, reverse=True))
