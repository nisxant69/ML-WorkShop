# Check number odd or even
a=int(input("Enter num1: "))
if a%2 == 0:
    print(f"{a} is a even number")
else:
    print(f"{a} is a odd number")

# Check the mark
# if mark >=80 distinction, 70 <= mark < 80 --> First Division
# 60<=mark<70 --> Second Division
# mark 50 <= mark <60 --->Third Division
# else Pass 

marks=int(input("Enter marks: "))
if marks>=80:
    print("Distinction")
elif marks>=70:
    print("First Division")
elif marks>=60:
    print("Second Division")
elif marks>=50:
    print("Third Division")
else:
    print("Bishnu Fail")