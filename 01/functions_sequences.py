# Python主要三种序列类型，字符串(str)，列表(list)，元组(tuple)。
# 他们都是比较复杂的数据类型，或者称作复合数据类型(建立在原子类型之上)。
print("all：判断可迭代对象的每个元素是否都为True值 ")
print(all([1, 2]))
print(all([0, 1, 2]))
print(all(()))  # 判断空元组
print(all({}))  # 判断空字典
print("any：判断可迭代对象的元素是否有为True值的元素")
print(any([0, 1, 2]))
print(any([1, 2, 3]))
print(any([]))  # 判断空列表
print(any({}))  # 判断空字典
print("filter：过滤可迭代对象的元素,借助于其他的方法")


def if_even(x):
    return x%2 == 0  # 当x是偶数的时候返回True,否则返回False
# 下面的filter()函数会依次把列表的每个元素传给自定义的过滤函数，若返回值为False则过滤掉该元素
post_filter = list(filter(if_even, list(range(10))))
print(post_filter)

print("map：使用指定方法去作用传入的每个可迭代对象的元素，生成新的可迭代对象")
print(list(map(ord, 'JRT')))
print(list(map(chr, [74, 82, 84])))

print("next：返回可迭代对象中的下一个元素值")
# 注意，是对迭代器的操作
test = iter('JRT')
print(next(test))
print(next(test))
print(next(test))
# print(next(test)) 继续这样做会报错，已经迭代到迭代器的结尾
# 为了在迭代结束抛出更有意义的信息，我们可以为next()函数指定一个default参数
print(next(test, 'StopIteration'))
print("reversed：反转序列生成新的可迭代对象")
test = range(10)
print("反转前：", list(test))
print("反转后：", list(reversed(test)))
print("sorted：对可迭代对象进行排序，返回一个新的列表")
test = list(range(99, -1, -1))
print("排序前：", test)
test = sorted(test)
print("排序后：", test)
print("zip：聚合传入的每个迭代器中相同位置的元素，返回一个新的元组类型迭代器")
x = ('J', 'R', 'T')
print(list(zip(x,reversed(x))))


