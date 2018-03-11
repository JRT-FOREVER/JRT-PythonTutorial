print("输入算式，不同元素用空格隔开\n")
x,form,y=input().split()
x=float(x)
y=float(y)
if form is '+':
    res=x+y
if form is '-':
  res=x-y
if form is '*':
    res=x*y
if form is '^':
    res=x**y
if form is '/':
   if y!=0:
       res=x/y
   else:
       print("除数不能为零")
       exit()
print(x,form,y,"=",res)    
input()
