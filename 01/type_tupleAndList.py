# 现在开始接受Python另外两种Sequence类型
# Tuple和List基本是一样的，只不过Tuple是不可变的类型
# 首先看所有序列类型所共有的操作

# 索引操作
str1 = input("What's your name?\n")
print(str1[0])
print(str1[-1])
print("索引字符串字面值: " + "JLU Robot Team"[-1])  # 序列的字面值也是可以进行索引操作的
print('索引列表字面值:', [1, 3, 5, 7, 9][2])
print('索引元组字面值:', (1, 3, 5, 7, 9)[2])

# 分片操作
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])
print(numbers[0:len(numbers)])
print(numbers[0:])
print(numbers[:len(numbers)])
print(numbers[0:100])
print(numbers[-len(numbers)-1:len(numbers)])
print(numbers[-3:-1])
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[-1:-11:-1])  # 到现在应该发现规律：
'''
    切片时，参数1指定的字符会显示，而参数2对应的字符不包含
    切片时，起始点应该在终止点之前，否则返回空序列
    步长参数默认为1，不能为0，可以为负，其规定的是前后顺序和切片间隔，此处的顺序依然是指实际顺序
'''

# 序列的加法和乘法
print([0, 1]*10)
print(numbers+[10])
print([None]*10)

# 成员运算符
print(1 in numbers)
print(11 in numbers)

# 方法
print(len(numbers))
print(tuple(numbers))
print(list((1, 2, 3)))
print("max:", max(numbers))
print("min:", min(numbers))
numbers.append(10)  # append()在列表结尾添加元素，原地操作
print(numbers)
ext = [11, 12, 13]
numbers.extend(ext)  # extend()给列表追加序列，原地操作
print(numbers)
numbers[len(numbers):] = [1, 2, 3, 2, 1]  # 上面的extend()函数可以通过切片来实现，其余很多的原地方法也可以用切片实现
print("现在含有重复元素的列表的列表:", numbers)
print("2重复的次数:", numbers.count(2))
print("第一个匹配元素的索引:", numbers.index(5))
numbers.insert(3, '你是谁？')
print(numbers)  # 给列表的指定位置添加元素，列表元素不必一致
a = numbers.pop()
print("最后一个元素%d被弹出:" % a, numbers)
a = numbers.pop(5)
print("索引为5的元素%d被弹出:" % a, numbers)
numbers.remove('你是谁？')  # 删除指定元素在列表中的首个匹配项
print("调用remove('你是谁？')之后:", numbers)
numbers.reverse()
print(numbers)
numbers.sort()  # 原地排序
# a = numbers.sort()是错误的
print("排序后:", numbers)
a = sorted(numbers)
print('异地排序:', a)
# 复杂一些的排序，这里不举例子了，大家可以自行尝试,sort()函数可以指定key和reverse参数，key是一个函数
string1 = ['1', '1111', '111', '1212', '12']
string1.sort(key=len, reverse=False)
print('看起来反常的排序:', string1)
string1.sort(key=len, reverse=True)
print('看起来反常的排序:', string1)

# (元组)是同样性质的东西，只不过不可变，这里略过





