# 变量定义部分
xing_ming = {}
ming_xing = {}

# 函数定义部分
def menu():
    """显示主菜单"""
    print('#' * 60)
    print(' ' * 20,"欢迎使用姓名检索系统",' ' * 20)
    print(' ' * 10,"1  .输入姓名",' '*18,"2  .查找姓名",' '*9)
    print(' ' * 10,"3  .浏览姓名",' ' * 18,"4  .关闭程序",' ' * 9)
    a = input(">")
    if int(a) == 1:
        append()
    elif int(a) == 2:
        find()
    elif int(a) == 3:
        show()
    elif int(a) == 4:
        return

def append():
    print('#' * 60)
    a = input("          请输入姓氏（输入q退出）：")
    b = input("          请输入名字（输入q退出）：")
    if a == 'q' or b == 'q':
        menu()
    elif str(a) not in xing_ming and str(b) not in ming_xing:
        xing_ming[str(a)] = str(b)
        ming_xing[str(b)] = str(a)
        print("输入成功！")
    else:
        print("您输入的名或姓已经与某一已经存在的姓名重复了哦。")
    input("请按回车键返回上一级")
    menu()
    return

def find():
    print('#' * 60)
    print(' ' * 20,"您要查找名还是姓？",' ' * 20)
    print(' ' * 11,"1  .姓氏", ' ' * 22, "2  .名字", ' ' * 11)
    print("输入q返回上一级")
    a = input(">")
    if int(a) == 1:
        b = input("请输入您要查找的姓氏：")
        if str(b) in xing_ming:
            print("查找结果：",b,xing_ming[b])
    if int(a) == 2:
        b = input("请输入您要查找的名字：")
        if str(b) in ming_xing:
            print("查找结果：",ming_xing[b],b)
    input("请按回车键返回上一级")
    menu()
    return

def show():
    print('#' * 60)
    print(' ' * 20 ,"姓氏" , ' ' * 12,"名字")
    for i in xing_ming:
        print(' '*20,i,' '*14,xing_ming[i])
    input("按回车键返回上一级")
    menu()
    return

# 函数调用
menu()
