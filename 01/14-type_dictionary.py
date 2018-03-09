# 轮到字典了
# 吐槽一下：第一部分终于结束了，不知道现在还剩几个人在听啊
# 有了前面序列的基础，字典其实也就不难理解了，毕竟操作上有很多相似之处，只不过字典是一种映射
# 看看用以前的方法弄一个电话簿
from copy import deepcopy
names = ['mdzz0', 'mdzz1', 'mdzz2']
phones = ['01275', '02336', '03997']
for name in names:
    print(name+':'+phones[names.index(name)])

# 再看看字典版本
phone_dict = dict(zip(names, phones))
# print(type(phone_dict))
print(phone_dict)
# 上面的例子看出来，字典是更加接近于人类思维的数据类型，此外也展示了dict的功能
# dict()是一个类型函数，可以从映射来创建字典
print(dict([('mdzz0', '01'), ('mdzz1', '02')]))
print(dict(mdzz0='01', mdzz1='02'))  # 键不要加引号

# 一些字典操作
print(len(phone_dict))
print('mdzz1:'+phone_dict['mdzz1'])  # 字典索引方法
phone_dict['mdzz1'] = '01111'
print('mdzz1:'+phone_dict['mdzz1'])
print('mdzz1' in phone_dict)  # 检查字典中是否有该键
phone_dict['mdzz3'] = '00000'  # 字典可以动态添加项，而序列不可能那一个不存在的索引去访问
print(phone_dict)

# 依赖于字典的字符串格式化，之前说过了使用元组传入数据的字符串格式化
print("**********************************formatted string*********************************")
str_origin = "mdzz0:%(mdzz0)s\nmdzz1:%(mdzz1)s\nmdzz2:%(mdzz2)s"
str_formate =str_origin % phone_dict
print(str_formate)

template = '''\
<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>
'''
data = template % {'title':'My Page', 'text':'Welcome to my home page!'}
print(data)

print('************************************字典方法*************************************')
dict_test = {'a': '1'}
dict_test1 = dict_test  # 目前二者关联到同一个字典对象
print("dict_test:", dict_test)
print('dict_test1: ', dict_test1)
dict_test = {}  # 给dict_test关联到一个新字典，这时候两者就不再一样了
print('dict_test: ', dict_test)
print('dict_test1: ', dict_test1)
dict_test = {'a': '1'}
dict_test1 = dict_test  # 目前二者关联到同一个字典对象
dict_test.clear()  # 这样会清除掉原始字典，两个对象都变为空
print('dict_test: ', dict_test)
print('dict_test1: ', dict_test1)

# 浅拷贝，理解难度变大了哦
d = {'name': ['jrt', 'JRT']}  # 字典某个键对应的值又是一个新的容器,这样对于浅拷贝来说就是简单复制对象的值
c = d.copy()
d['name'].append('copy')
print('origin', d['name'])
print('copy:', c['name'])

d = {'name': ['jrt', 'JRT']}

dc = deepcopy(d)
d['name'].append('deepcopy')  # 对于深拷贝，当对象的值是引用时，会递归的复制，得到的拷贝和原始对象完全一致且独立
print('origin', d['name'])
print('deepcopy', dc['name'])
print(phone_dict.keys())
print(phone_dict.items())
print(phone_dict.values())

a = phone_dict.pop('mdzz0')
print('弹出的值：'+a)
print('弹出项后字典：', phone_dict)


phone_dict.popitem()
print('随机弹出一项后：', phone_dict)
phone_dict.popitem()
print('随机弹出一项后：', phone_dict)
phone_dict.popitem()
print('随机弹出一项后：', phone_dict)

# the end
# 是不是看到了希望呢？













