# 可是刚才那么做是不是有点麻烦呀，函数多的话总不能一个一个修改
# 所以我们可以写一个新函数


def calc(a, b):
    res = 0
    for i in range(a,b):
        res += i
    return res


def add(a, b):
    return a + b


def func(f, a, b):
    print("JRT")
    return f(a, b)


if __name__ == '__main__':
    print(func(calc, 1, 101))
    print(func(add, 1, 100))

