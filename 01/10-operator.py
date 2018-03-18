# 算数运算符：+ - *  / % ** //
print("1 + 1 =", 1 + 1)
print("2 - 1 =", 2 - 1)
print("5 * 3 =", 5 * 3)
# python2中整数之间的除法只能得到整数，如果要得到小数需要让一个操作数编程浮点数：10.0/3
# python3中已经没有这样的要求，代码的书写越来越贴近自然语言
print("10 / 5 =", 10 / 5)
print("10 / 3 =", 10 / 3)
# 由于浮点数在内存中的存储问题，浮点数是不精确的，所以不建议直接比较两个浮点数的大小关系
print("10 % 3 =", 10 % 3)
# /除法永远返回浮点数，要想得到整数需要使用下面的整除法
print("10 // 3 =", 10 // 3)
print("2 ^ 10 =", 2 ** 10)

# 关系运算符：> < >= <= != ==
print("2<3:", 2 < 3)
print("3>2:", 3 > 2)
print("3=3:", 3 == 3)
print("5!=6:", 5 != 5)
print("5>=4:", 5 >= 4)
print("5<=4:", 5 <= 4)
# 逻辑运算符：and  or  not
print("not False = ", not False)
print("False and True = ", False and True)
print("False and False = ", False and False)
print("True and True = ", True and True)
print("False or True = ", False or True)
print("False or False = ", False or False)
print("True or True = ", True or True)
# 位运算符  & | ^ ~ << >>   不太容易理解，无所谓
print(bin(0b1010 & 0b1100))  # 1000
print(bin(0b1010 | 0b1100))  # 1110
print(bin(0b1010 ^ 0b1100))  # 0110
print(~0b00011100)  # 二进制就是0001 1100，取反变为1110 0011(负数是补码),原码(10011101),就是-29
a = 10  # 0000 1010
b = -10  # 1000 1010 -> 11110101 -> 11110110
print(a << 2)  # 0010 1000
print(a >> 2)  # 0000 0010
print(b << 2)  # 1101 1000 -> -1010 1000 -> -40
print(b >> 2)  # 1111 1101 -> -1000 0011 -> -3

# 赋值运算符

# 成员运算符   in   not in

a = 1
b = 20
li = [1, 2, 3, 4, 5 ];
print(a in li)  # True
print(b in li)  # False
print(a not in li)  # False
print(b not in li)  # True

# 身份运算符  is    is not
a = 1
b = 1
print("a is b :", a is b)  # is 判断的是两个变量是否引用到相同的单元，而==判断的是值
a = []
b = []
print("a is not b :", a is not b)







