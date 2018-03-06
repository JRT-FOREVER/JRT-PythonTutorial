width = int(input("输入理想的宽度\n> "))
items = ['Apple', 'Milk', 'Soap', 'Beef', 'Pears', 'Cantaloupes']
prices = [5, 1, 6, 9, 30, 10]
priceWidth = 10
itemWidth = width - priceWidth
print('*' * width)
print('%-*s' % (itemWidth, 'item') + '%*s' % (priceWidth, 'price'))
print('*' * width)
for item, price in zip(items, prices):  # 使用内置函数zip()聚合两个序列已经说过了，此处配合使用了拆包语法
    print('%-*s' % (itemWidth, item) + '%*.2f' % (priceWidth, price))
print('*' * width)