# 然而上次的做法本质上已经是定义新函数了，并不是我们想要的做法


def calc(a, b):
    res = 0
    for i in range(a, b):
        res += i
    return res

# 定义装饰器


def func(f):
    def newF(a, b):
        print('JRT')
        return f(a, b)
    return newF


# 应用装饰器
calc = func(calc)

if __name__ == '__main__':
    print(calc(1, 101))
