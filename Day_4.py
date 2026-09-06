# command line calculator
a = float(input("Enter a : "))
b = float(input("Enter b : "))
operation = input("Enter operation +,-,*,%,/ : ")

if(operation == "+"):
    print("addition: ",a+b)
elif(operation == "-"):
    print("subtraction: ",a-b)
elif(operation == "*"):
    print("multiplication: ",a*b)
elif(operation == "%"):
    print("modulo: ",a%b)   
elif(operation == "/"):
    if(b == 0):
        print("error")
    else:
        print("division :",a/b)
else:
    print("Invalid operation")
