import pygame,sys,os
from pygame.locals import *

xing_ming = {}
ming_xing = {}

def clear():os.system('cls')

def menu1():
    """显示主菜单"""
    clear()
    print('#' * 60)
    print(' ' * 20,"欢迎使用姓名检索系统",' ' * 20)
    print(' ' * 9,'\033[1;31;40m','1','\033[0m',".输入姓名",' '*18,"2  .查找姓名",' '*9)
    print(' ' * 10,"3  .浏览姓名",' ' * 18,"4  .关闭程序",' ' * 9)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    menu2()
                    break
                elif event.key == K_DOWN:
                    menu3()
                    break
                elif event.key == K_KP_ENTER:
                    append()
                    break
    return

def menu2():
    clear()
    print('#' * 60)
    print(' ' * 20, "欢迎使用姓名检索系统", ' ' * 20)
    print(' ' * 10, "1  .输入姓名", ' ' * 18,  '\033[1;31;40m','2', '\033[0m', ".查找姓名", ' ' * 9)
    print(' ' * 10, "3  .浏览姓名", ' ' * 18, "4  .关闭程序", ' ' * 9)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    menu2()
                    break
                elif event.key == K_DOWN:
                    menu4()
                    break
                elif event.key == K_KP_ENTER:
                    find1()
                    break
    return

def menu3():
    clear()
    print('#' * 60)
    print(' ' * 20, "欢迎使用姓名检索系统", ' ' * 20)
    print(' ' * 10, "1  .输入姓名", ' ' * 18,  "2  .查找姓名", ' ' * 9)
    print(' ' * 9,'\033[1;31;40m', '3', '\033[0m', ".浏览姓名", ' ' * 18, "4  .关闭程序", ' ' * 9)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu1()
                    break
                elif event.key == K_RIGHT:
                    menu4()
                    break
                elif event.key == K_KP_ENTER:
                    show()
                    break
    return

def menu4():
    clear()
    print('#' * 60)
    print(' ' * 20, "欢迎使用姓名检索系统", ' ' * 20)
    print(' ' * 10, "1  .输入姓名", ' ' * 18, "2  .查找姓名", ' ' * 9)
    print(' ' * 10, "3  .浏览姓名", ' ' * 18, '\033[1;31;40m','4', '\033[0m', ".关闭程序", ' ' * 9)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu2()
                    break
                elif event.key == K_LEFT:
                    menu3()
                    break
                elif event.key == K_KP_ENTER:
                    pygame.quit()
                    sys.exit()
                break
    return

def append():
    clear()
    print('#' * 60)
    a = input("          请输入姓氏（输入q退出）：")
    b = input("          请输入名字（输入q退出）：")
    if a == 'q' or b == 'q':
        menu1()
    elif str(a) not in xing_ming and str(b) not in ming_xing:
        xing_ming[str(a)] = str(b)
        ming_xing[str(b)] = str(a)
        print("输入成功！")
    else:
        print("您输入的名或姓已经与某一已经存在的姓名重复了哦。")
    input("请按回车键退出")
    menu1()
    return

def find1():
    clear()
    print('#' * 60)
    print(' ' * 20,"您要查找名还是姓？",' ' * 20)
    print(' ' * 11, '\033[1;31;40m', '1', '\033[0m', ".姓氏", ' ' * 22, "2  .名字", ' ' * 11)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    find2()
                    break
                elif event.key == K_KP_ENTER:
                    clear()
                    print('#' * 60)
                    a = input(' ' * 20,"请输入姓氏：")
                    if str(a) in xing_ming:
                        print(' ' * 10,"查找结果：",str(a),xing_ming[str(a)])
                        input("请按回车键退出")
                        find1()
                    break
                elif event.key == K_ESCAPE:
                    menu1()
                    break
                    return

def find2():
    clear()
    print('#' * 60)
    print(' ' * 20, "您要查找名还是姓？", ' ' * 20)
    print(' ' * 11, "1  .姓氏", ' ' * 22, '\033[1;31;40m', '2', '\033[0m', ".名字", ' ' * 11)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    find1()
                    break
                elif event.key == K_KP_ENTER:
                    clear()
                    print('#' * 60)
                    a = input(' ' * 20, "请输入名字：")
                    if str(a) in ming_xing:
                        print(' ' * 10, "查找结果：", ming_xing[str(a)], str(a))
                        input("请按回车键退出")
                        find1()
                    break
                elif event.key == K_ESCAPE:
                    menu1()
                    break
                    return

def show():
    clear()
    print('#' * 60)
    print(xing_ming)
    input("按回车键退出")
    menu1()
    return

pygame.init()
screen=pygame.display.set_mode((640,360),0,32)
menu1()
