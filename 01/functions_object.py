print("help：返回对象的帮助信息")
print("dir：返回对象或者当前作用域内的属性列表")
print("id：返回对象的唯一标识符")
print("hash：获取对象的哈希值")
print("type：返回对象的类型，或者根据传入的参数创建一个新的类")
print("len：返回对象的长度")
print(len('abcd'))  # 字符串
print(len(bytes('abcd', 'utf-8')))  # 字节数组
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))  # 字典
print(len({'a', 'b', 'c', 'd'}))  # 集合
print(len(frozenset('abcd')))  # 不可变集合
print("ascii：返回对象的可打印表字符串表现方式")
print("format：格式化显示值")
print("vars：返回当前作用域内的局部变量和其值组成的字典，或者返回对象的属性列表")



