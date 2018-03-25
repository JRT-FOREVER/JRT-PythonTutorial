# exp = raw_input("Please input your expression >>> ")
operator = ['^', '/', '*', '-', '+']
# exp = str(input("Please input your expression >>> "))
# exp = exp.split(' ')
# j = 0
# for i in range(len(exp)):
#     if exp[i].isdigit():
#         dgt[j] = exp.pop(0)
#         j += 1
#     elif exp[i] in operator:
#         op[k] = exp.pop(0)
#         k += 1
#
#
# exp = str(input("Please input your expression >>> ")).split()
# while (len(exp) - 1):
#     while '^' in exp:
#         index = exp.index('^')
#         exp.pop(index)
#         exp.insert(index - 1, int(exp.pop(index - 1)) ** int(exp.pop(index - 1)))

# 以上都是废代码
operator = ['^', '/', '*', '-', '+'] # 定义一个列表来存储符号，方便下面用循环。
def compute(exp):
    '''
    以处理好的已经把运算符和数字分割好的、并以他们作为元素的列表作为输入，计算出所给表达式的值（不带括号）
    :param exp:
    :return:
    '''
    while (len(exp) - 1): # 当表达式的值没有被撇的只剩一个的时候（见列表的pop()方法）
        for op in iter(operator): # 从operator列表里按顺序取元素，注意operator列表中的元素顺序应是运算符的运算顺序。
            while op in exp:
                index = exp.index(op) # 存储下要计算的预算符的位置
                exp.pop(index)
                if op == '^':
                    exp.insert(index - 1, float(exp.pop(index - 1)) ** float(exp.pop(index - 1)))
                    # 这四个插入（insert）是同样的道理。拿出运算符左边的（exp.pop(index - 1)）和右边的（exp.pop(index - 1)\
                    # 并把他们强制转化为float（精度高）然后运算得出结果并把它插入到被撇掉的那三个的位置。
                if op == '/':
                    exp.insert(index - 1, float(exp.pop(index - 1)) / float(exp.pop(index - 1)))
                if op == '*':
                    exp.insert(index - 1, float(exp.pop(index - 1)) * float(exp.pop(index - 1)))
                if op == '-':
                    exp.insert(index - 1, float(exp.pop(index - 1)) - float(exp.pop(index - 1)))
                if op == '+':
                    exp.insert(index - 1, float(exp.pop(index - 1)) + float(exp.pop(index - 1)))
                    # 这里的四个判断是迫不得已才写的，本来想直接用一个循环了事，但是那样的话，比如"float(exp.pop(index - 1))
                    #  + float(exp.pop(index - 1)"中的运算符就没办法更改，所以最后我只想到了判断这一种方法。
    return exp[0]

def recur_parenth(exp):
    '''
    通过递归来一层层（从最外层到最里层）去括号，然后再一层层（从最里层到最外层）把值返回回来。
    :param exp:
    :return:
    '''
    if '(' in exp:
        index1 = exp.index('(')
        exp.pop(index1)
        exp.reverse()
        index2 = len(exp) - exp.index(')') - 1
        exp.reverse()
        exp.pop(index2) # 这些步骤主要是找到一对儿括号并用index1和index2标记出他们的位置，然后从exp中撇掉'('和')'，其中reverse()也是\
        # 想不出别的好方法的无奈之举。
        exp[index1:index2] = [recur_parenth(exp[index1:index2])] # 截取原来包含在括号中的部分，并计算它们的值
        return compute(exp)
    return compute(exp) # 递归出口，当exp没有括号只有表达式时，返回该表达式之值。



exp = str(input("Please input your expression with spaces to separate your numbers from operator  >>> ")).split()
# 输入表达式并用字符串的split()方法把他们分隔开（split()方法的默认参数是split(' ')，故省略）
print(recur_parenth(exp))

# 这个程序有一个巨大的缺陷，就是必须要用空格来区分开符号与数字，这样的话就十分的僵硬，慢慢儿改进把。
# 还有一个缺陷是算不了太大的数
# 另一个缺陷是没有错误提醒
