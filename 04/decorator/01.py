# 随便写的一个求和函数
def calc(a, b):
    res = 0
    for i in range(a,b):
        res += i
    return res


if __name__ == '__main__':
    a = calc(1, 101)
    print(a)
