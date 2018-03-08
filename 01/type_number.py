"""
    Python中有丰富的数据类型,包括None,NotImplemented,Ellipsis
Number,Sequences,Set,Mappings,Callable Types
Modules,Custom classes,Class instances,I/O objects
Internal types
    这些是官方文档给出的，此处从实用性和必要性的角度来看，我们不关注这么多
我们只把类型分为数值类型（Integer(Boolean,Integer),Float,Complex)
序列类型(String，Tuple,List),映射类型(Dictionary),以及自定义的类
    个人观点，这样就足够了，剩下的可以参考官方文档，我翻译了关于数据类型的一部分
"""
# 数值类型
a = 1
print("a = ",a)
a, b, c, d = 1, True, 3.14, 4+2j
print(a, b, c, d)
print("四种数值类型: ", type(a), type(b), type(c), type(d))

a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)
e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)
e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)
e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)


