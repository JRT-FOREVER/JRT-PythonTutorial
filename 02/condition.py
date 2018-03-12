from math import sqrt
# 现在开始来看看程序的流程控制，有了这些之后理论上就什么都可以做了,突出服务于使用的目的，这里真的很简单
# 先来看一看语法糖
# 序列解包1
dictionary = {'a': 1, 'b': 2, 'c': 3}
for key, value in dictionary.items():  # 这里就是一种unpacking
    print(key, value)
values = 1, 2, 3
# 序列解包1
x, y, z = values
print(x, y, z)
# 序列解包2
x, y, z = 1, 2, 3
print(x, y, z)
# 序列解包3
x, y = y, x
print(x, y, z)
# 链式赋值
x = y = 1
print(x, y)
# 增量赋值
x += 1
y **= 2
z /= 2
print(x, y, z)

# 分支结构
num = float(input("please input a number between 0~100\n>"))
assert(0 < num < 100)  # 使用断言
if num > 90:
    print("congratulations!")
elif num > 60:
    print("emmmmm")
else:
    print("sorry!")

name = input('whats your name?\n>')
if name.endswith('jrt'):
    if name.startswith('Mr.'):
        print('hello Mr. jrt')
    if name.startswith('Mrs.'):
        print('hello Mrs. jrt')
    else:
        print('hello jrt')
else:
    print("hello")


# 来算算数吧，输出10！,下面这两种循环都可以
i = 1
res = 1
while(i <= 10):
    res *= i
    i += 1
print(res)

res = 1
for i in range(1, 11):  # xrange()函数是更高效的，他返回的是一个可迭代对象，而range()返回的直接就是一个列表
    res *= i
print(res)

words = ['life', 'is', 'short', 'I', 'use', 'python']
for word in words:
    print(word)

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key + ':', d[key])

# 并行迭代的实现，很常见的用法
names = ['a', 'b', 'c']
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(name, ':', score)

print('********************************************************************')
strings = ['asfsfsf', 'bldfjgld', 'slfgsdfhgsidf', 'oertuwoehnccxvnm']
for string in strings:
    if 'fj' in string:
        print(string)
        index = strings.index(string)
        strings[index] = ''

strings = ['asfsfsf', 'bldfjgld', 'slfgsdfhgsidf', 'oertuwoehnccxvnm']
index = 0
for string in strings:
    if 'sid' in string:
        print(string)
        strings[index] = ''
index += 1


strings = ['asfsfsf', 'bldfjgld', 'slfgsdfhgsidf', 'oertuwoehnccxvnm']
# dict是具有(key,value)的  而类似的enumerate()函数可以返回序列的(index,value)
for index, string in enumerate(strings):
    if 'nm' in string:
        print(string)
        strings[index] = ''




for n in range(99,81,-1):
    res = sqrt(n)
    if res == int(res):  # 判断是否是整数
        print(n)
        break
else:
    print("nothing find")

# 列表推导式，小小的重点一下
print([x**2 for x in range(0, 100)])
print([x for x in range(0, 100) if x % 2 == 0])
# 下面这句话注意一点，这个可不是并行迭代，而是实现了多重循环的效果，找找笛卡尔积的感觉
print([x+y for x in range(0, 100) for y in range(100, 0, -1)])


# ok, that's all


