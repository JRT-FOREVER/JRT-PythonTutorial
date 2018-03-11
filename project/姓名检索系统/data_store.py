# 数据存储
# 包导入的路径问题很坑啊
# pycharm把根目录当成项目所在路径
from data_sort import data_sort


def data_store(data, full_name):
    labels = ['first_name', 'last_name']
    names = full_name.split()
    # 注意存储名字到数据库的时候，要在姓和名的两个键下面都存储好相应的全名
    for label, name in zip(labels, names):
        result = data_sort(data, label, name) # 获取全名列表
        if result:
            result.append(full_name)
        else:
            data[label][name] = [full_name]

    pass
