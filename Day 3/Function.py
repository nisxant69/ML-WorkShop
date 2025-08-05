# def functionName():
#     print("Hello World")
# functionName()

# def sum2num(num1,num2):   #Parameter
#     print(num1+num2)
# sum2num(1,2)              #Argument


# Take user input and add two number
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# def Sum(a,b):
#     return a+b;
# print(Sum(num1,num2))


# Check even or odd
# def checkEvenOrOdd(num):
#     if num%2==0:
#         print(f"{num} is a even number")
#     else:
#         print(f"{num} is a odd number")
# num=int(input("Enter a num: "))
# checkEvenOrOdd(num)

#check odd or even using range
# def checkNum(num):
#     if num%2==0:
#         print(f"{num} is a even number")
#     else:
#         print(f"{num} is a odd number")

# for i in range(1,21):
#     checkNum(i)


#check odd or even by taking user input for range
# def checkNum(rang):
#     for i in range (1,rang):
#         if i%2==0:
#             print(f"{i} is a even number")
#         else:
#             print(f"{i} is a odd number")

# num=int(input("Enter a range: "))
# checkNum(num)

# Addition substraction division and multiplication via single function
def allCalculation(num1,num2):
    # a,b,c,d=num1+num2,num1*num2,num1/num2,num1-num2 #yesari pani milxa 
    # print(f"{a,b,c,d}")
    print(f"Sum: {num1+num2}")
    print(f"product: {num1*num2}")
    print(f"Division: {num2/num1}")
    print(f"Substraction: {num2-num1}")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
allCalculation(num1,num2)

