#读入txt文件，分姓名保存
xing = []
ming = []
with open('name.txt') as f:
    for line1 in f:
        x , m = line1.split()
        xing.append(x)
        ming.append(m)
#遍历查找
print('输入查找类型')
print('按姓查找输入1，按名输入2，按姓名查找输入3')
i = input()
print('请输入查找目标')
ser = input()
num = 0
if i == '1':
    for j in range(0,len(xing)):
        if ser == xing[j]:
            print(xing[j],ming[j])
            num = num+1
    if num == 0:
        print('没有结果')
elif i == '2':
    for j in range(0,len(ming)):
        if ser == ming[j]:
            print(xing[j],ming[j])
            num = num+1
    if num == 0:
        print('没有结果')
elif i == '3':
    x , m=ser.split()
    for j in range(0,len(xing)):
        if x == xing[j] and m == ming[j]:
            print(xing[j],ming[j])
            num = num+1
    if num == 0:
        print('没有结果')
else:
    print('输入不合法')
