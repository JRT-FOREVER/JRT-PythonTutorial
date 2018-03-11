from data_init import data_init
from data_store import data_store
from data_sort import data_sort
data = {}
data_init(data)
# print(data)
data_store(data, "关键字 参数")
data_store(data, "J RT")
data_store(data, "J AA")
data_store(data, "B RT")
full_name = input("输入全名，注意空格分隔开姓和名\n")
data_store(data, full_name)
label = input("输入要first_name 或者 last_name来指定查找的字段\n")
name = input("输入要查找字段:%s的值？\n" % label)
result = data_sort(data, label, name)
print(result)
