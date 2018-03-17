# Python也提供了自动装饰的语法糖
# 定义装饰器


def func(f):
    def newF(a, b):
        print('JRT')
        return f(a, b)
    return newF


# 使用Python为装饰器提供的语法糖，@后面是定义的装饰器，下一行紧跟要装饰的函数
# Python会自动把待修饰函数做参数给装饰器，然后用装饰器返回的新函数覆盖待装饰的函数
@func
def calc(a, b):
    res = 0
    for i in range(a, b):
        res += i
    return res


if __name__ == '__main__':
    print(calc(1, 101))
