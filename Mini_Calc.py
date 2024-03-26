print ("Welcome to Mini Clac!")
fun=input("What operation would you like to perform Add/Sub/Mul/Div?")
if(fun=="add"):
    a=int(input("Input first number:"))
    b=int(input("Input second number:"))
    print(a+b)
elif(fun=="sub"):
    print("Note: First number minus second number.")
    a=int(input("Input first number:"))
    b=int(input("Input second number:"))
    print(a-b)
elif(fun=="mul"):
    a=int(input("Input first number:"))
    b=int(input("Input second number:"))
    print(a*b)
elif(fun=="div"):
    print("Note: First number divided by second number.")
    a=int(input("Input first number:"))
    b=int(input("Input second number:"))
    print(a/b)
else:
    print("Invalid operation.")