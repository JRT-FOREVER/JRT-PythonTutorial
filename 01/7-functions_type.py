# 这一节都是类型转换函数，内容很简单
print("######bool():")
print(bool(1))
print(bool(0))
# boolean也是数值类型的一种，一切非0为True，0为False
print(bool(33))
print("######int():")
print(int(input("please input a number! >")))
print(int("36"))
print("######float():")
print(float(input("please input a float number! >")))
print("######complex():")
print(complex(input("please input a complex number! >")))
print("######str():")
print(str())  # str()没有参数的时候返回空字符''
print(str(None))
print(str(1+2j))
print(str(1234))
print("######bytearray():")  # 创建字节数组
'''
    字符集和编码规则是一个解释起来比较麻烦的东西广义的编码是指信息的不同表现形式之间的转换，
而此处我们特制字符(包括不可见的控制字符)在计算机中的表达从我们最熟知的ASCII字符集开始,我们
简单的讨论一下这个问题
    ASCII字符集是计算机诞生初期设计出来的字符集，他使用7个二进制位来表示字符，共可以表示
2^7=128种字符，涵盖了全部大小写英文字母，控制序列，和常用符号。
    随着计算机的全球化，考虑到各地区语言文字的差异，仅仅ASCII是不够用的，比如说中文仅仅常用
汉字就数以千计，更别说包括生僻字，繁体字，特殊符号在内的全部编码需求，于是出现了GBK2312字符
集，该字符集占用了两个字节(虽说没全用)，规定高字节小于等于127的延用ASCII而两个大于127的字节
则组合表示一个汉字，这样便涵盖了所用常用汉字，GBK字符集是进一步的扩充，包含了生僻字和繁体字。
    接下来一些各个国家便都有了自己的字符集，这样虽然在本地可以完成信息表示，但是非常不利于信息
交换，于是一些标准化组织重新设计了UNICODE字符集，兼容了全部的字符，不过这种字符集原本规定的编码
方案是无论什么字符全部占用三个字节，这从计算机容量的角度讲是严重不可取的，会让原本的ASCII编码字符集
占用空间膨胀为原来的三倍。
    后来人们将字符集和编码规则相分离，出现了UTF-8,UTF-16等等可变长编码规则，比较好的解决了这个
问题。
'''
# bytearray()用于根据输入参数创建字节数组，type()返回类型就是<class 'bytearray'>
print(bytearray("机器人小组JRT", "utf-8"))
print(bytearray("机器人小组JRT", "utf-16"))
print(bytearray("机器人小组JRT", "ansi"))
print(bytearray("机器人小组JRT", "gb2312"))
print(bytearray("机器人小组JRT", "gbk"))
print("######bytes():")
# type()测试的类型应该是<class 'bytes'>
print(bytes("机器人小组JRT", "gbk"))
print("######memoryview():")
v = memoryview(b'abcdefg')  # 小写b开头的字符串属于字节数组
print("直接输出字节数组", b'abcdefg')  # 这样并不能看到内存中字符编码值，故需要memroyview()来创建一个内存查看对象
print(v[1])
print(v[-1])
print("返回Unicode字符对应的整数ord():")
print(ord('a'))
print("返回整数所对应的Unicode字符chr():")
print(chr(97))
print("把整数转化为二进制bin():")
print(bin(15))
print("把整数转化为八进制oct():")
print(oct(10))
print("把整数转化为十六进制hex():")
print(hex(11))
print("根据参数创建元组类型tuple():")
print("根据参数创建列表类型list():")
print("根据传入参数创建字典dict():")
a = dict(a=1, b=2)
print(a)  # 字典类型用大括号标识
print("根据参数创建新的集合set():")
a = set(range(10))  # 注意range()默认从0开始
print(a)  # 集合是无序的
print("根据参数创建不可变集合frozenset():")
print("以序列(Sequence)为参数创建枚举对象enumerate():")
print("创建range对象range():")  # 这个还是比较常用的
a = range(1,100,2)
print(a)  # 这样仅仅会输出其类型
print(list(a))  # 转换为列表，1-100之间每隔两个数选取一个构成的序列
print("创建可迭代对象iter():")
print("创建切片对象slice():")
print("创建父类对象super():")
print("创建新object对象object():")  # 注意！该方法不接受任何参数
a = object()  # 创建一个普通的object对象，Object.object类是python所有类的基类
# a.attr = "error"会报错，因为object没有定义__dict__,故不能给object类的实例添加任何属性




