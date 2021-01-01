import math 
x=int(input("enter your first integer="))
o=input("enter the operator sign=")

if o=="+":
    y=int(input("enter your second integer="))
    print("sum=",x+y)
elif o=="-":
    y=float(input("enter your second integer="))
    print("subtraction=",x-y)
elif o=="*":
    y=int(input("enter your second integer="))
    print("multiply=",x*y)
elif o=="^":
    y=float(input("enter your second integer="))
    print(x,"to the power",y,"=",x**y)
elif o=="sin":
    y=0
    print(math.sin(x))
elif o=="cos":
    y=0
    print(math.cos(x))
elif o=="tan":
    y=0
    print(math.tan(x))
elif o=="#":
    print("convert it into degree=",math.degrees(x))
elif o=="@":
    print("convert into radian=",math.radians(x))
elif o=="!":
    print("factorial=",math.factorial(x))
elif o=="|":
    x=int(input("enter first integer="))
    y=int(input("enter the second integer="))
    print("gcd=",math.gcd(x,y))
elif o=="%":
    y=int(input("enter the second integer="))
    print("remaider=",math.remainder(x,y))
elif o=="$":
    print("sqrt root=",math.sqrt(x))