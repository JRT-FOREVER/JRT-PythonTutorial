# 修改需求，现在每个函数在完成自己的功能之前，要先行打印字符串JRT
# 最简单的，修改函数定义即可


def calc(a, b):
    print('JRT')
    res = 0
    for i in range(a, b):
        res += i
    return res


if __name__ == "__main__":
    print(calc(1, 101))
