text = "This is a sample text 99"
# num = 552
# print(type(text),type(num))
# print(len(text))  # len() function calculates length of string

# print(text*3)  # used to print same string multiple times

name="My name is Sudip"
print(name[0:8:2])   #output will bw m ae
# print(text[0:8:2])  

str_inp="Python is a Programming Language"
if "learning" in str_inp:
    print("Learning Exists")
else:
    print("It does not exist")

# "string" in str

str="I am going to learn Machine Learning"
print("Mach" in str)
print("gl" in str)
print("o lea" in str)

newStr=str.split() #o/p will be ['I', 'am', 'going', 'to', 'learn', 'Machine', 'Learning']
print(newStr)

newStrr="Hello, How are you?, Where are you from btw?"
finalnewStrr=newStrr.split(",")
print(finalnewStrr)
