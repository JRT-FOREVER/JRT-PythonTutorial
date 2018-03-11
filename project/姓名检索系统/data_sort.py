def data_sort(data, label, name):
    """   
    :param data: 数据库名称
    :param label: 查找方式，姓还是名
    :param full_name: 对应于查找方式，输入要查找的名字中的字段
    :return: nothing
    
    """
    return data[label].get(name)  # dict.get(key),返回对应的value
