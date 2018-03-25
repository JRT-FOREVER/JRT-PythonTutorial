def name_input():
    '''
    Enter white space seoarated name and return the tuple (first name, last name)
    :return: tuple (first name, last name)
    '''
    flag = 1
    while flag:
        try:
            [fn, ln] = input("\nPlease enter the name >>> ").split()
            flag = 0
        except:
            print("\nPlease check your name")
    return fn.lower(), ln.lower() # 用于不区分大小写


def choose_action():
    '''
    print instructions on the screen and return the action user chooose
    :return: int
    '''
    while 1:
        tag = int(input("\nWhat would you like to do?\n0. quit\n1. record\n2. search\n>>> "))
        if tag == 0 or tag == 1 or tag == 2:
            return tag
        else:
            print("\nPlease enter the right number!")


def search_input():
    '''
    用来输入要搜索的名字
    :return: tuple (name, tag)
    '''
    tag = 1 # 用来标记动作
    while tag:
        tag = int(input("\nWhich name do you want to search?\n0. quit\n1. first name\n2. last name\n>>> "))
        if not tag:
            return '', tag
        name = input("\nPlease enter the name >>> ")
        return name, tag


def search_name(name, tag):
    result = set({}) # 新建一个空集合来存放结果
    global name_book
    for n in name_book:
        if n[tag-1] == name.lower(): # 不区分大小写
            result.add(n)
    return result


def print_set(result):
    '''
    搜索结果是一个set，用来打印搜索结果（set）
    :param result: set
    :return: void
    '''
    for i in result:
        print("%s %s" % (i[0], i[1]))


def start_program():
    flag = 1  # 用来标记程序结束
    name_book = set()  # 这里用set是因为我想不到什么用字典的好方法了，就蒙了一个集合，在网上一找，发现python还真有这个内建数据类型，于是就很开心的使用了
    while flag:
        flag = choose_action()  # 同时用来标记应该进行的动作
        if flag == 1:
            name_book.add(name_input())  # add是set类型的一个方法，添加元素到集合
        elif flag == 2:
            i = search_input()
            if i[1] == 0:
                continue;
            print_set(search_name(i[0], i[1]))

