x = float(input('请输入第一个数字'))
form = input('请输入运算符')
y = float(input('请输入第二个数字'))
if form == '+':
    ans = x + y
elif form == '-':
    ans = x - y
elif form == '*':
    ans = x * y
elif form == '/':
    if y == 0:
        print('无法计算')
        input()
        exit()
    else:
        ans = x/y
elif form == '^' or '**':
    ans = x ** y
print('答案为',ans)
