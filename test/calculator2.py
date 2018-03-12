a = float(input("Please input the first number:\n>"))
b = input("Please input operator:\n>")
if b == '^':
    c = int(input("Please input a integer:\n>"))
    print("The result is:", a ** c)
else:
    c = float(input("Please input the second number:\n>"))
    if b == '+':
        print("The result is:", a + c)
    elif b == '-':
        print("The result is:", a - c)
    elif b == '*':
        print("The result is:", a * c)
    elif b == '/':
        print("The result is:", a / c)
    else:
        print("Please input +,-,*,/or^as an operator")
