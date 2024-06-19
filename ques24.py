num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
operator=input("enter the operation you want to perform : ")
if operator=="+":
    add=num1+num2
    print("the addition of two number is {}".format(add))
elif operator=="-":
    if num1>num2:
        sub=num1-num2
    else:
        sub=num2-num1
    print("the subtraction of two number is {}".format(sub))
elif operator=="*":
    mul=num1*num2
    print("the multiplication of two number is {}".format(mul))
elif operator=="/":
    div=num1/num2
    print("the divison of two number is {}".format(div))
else:
    print("no operator found!")
