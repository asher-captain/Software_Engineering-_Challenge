marks = int(input("Enter marks : "))

if marks>=90 :
    print("A")
elif marks >= 75 and marks < 90 :
    print("B")
elif marks >= 50 and marks < 75 :
    print("C")
else:
    print("F")

if marks < 50 :
    print("Fail")
else :
    print("Pass")
