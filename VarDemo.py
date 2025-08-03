#Variable Declaration and Initialization
a = 10
b = 20
c = "Anshu Gori"
print(a, b, c)

#Assign different values to variables
u,v,w= 1, 2, "Anshu Gori"
print(u, v, w)

#Assign same value to multiple variables
x=y=z=100
print(x, y, z)

t = True
print(t)

complex_num = 3 + 4j
print(complex_num)
print(type(complex_num)) 

print(type(a), type(c), type(u), type(v), type(w), type(x), type(y), type(z), type(t), type(complex_num)) #TYPE OF VARIABLES



j=5j+22
k=65+3j
sum = j + k
print(sum)   #Sum of complex number

# Type Casting
typecasttt = 5
print(type(typecasttt))
print(type(str(typecasttt))) #converting integer into string 
print(typecasttt) 


p = "python"
int_p = type(str(p))
print(int_p)
print(type(int_p))
# we cannot convert string into integer but can do viceversa.


a=2
b=3

add = 2+3
sub = 3-2
reminder = 3%2
floor_division = 30//2 # kati choti divide hunxa  // Quotient calculate garxa output=15
exponent = 3**2
print(add, sub, reminder, floor_division, exponent)

name = str(input("Enter your name: "))
print(name)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
power = num1**num2
print(power)
print(f"{num1} to the power {num2} is {power}")