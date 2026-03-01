a=int(input("enter a value:"))
b=int(input("enter another value:"))
op=input("enter operator:")
if (op=="+"):
    print(a+b)
elif(op=="-"):
    print(a-b)
elif(op=="*"):
    print(a*b)
elif(op=="/"):
    if(b==0):
        print("b cannot be zero")
    else:
        print(a/b)
elif(op=="%"):
    print(a%b)
elif(op=="//"):
    print(a//b)
elif(op=="**"):
    print(a**b)
else:
    print("invalid operator")
