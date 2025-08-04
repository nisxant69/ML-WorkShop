# ##while loop
# i=1
# while i<10:
#     print(i)
#     i += 1
# else:
#     print("loop terminated")

# TAKE AGE INPUT AND CHECK AGE VALID OR NOT 

age=int(input("Eneter your age: "))
while age<0 or age>100:
    print("You are DED")
    break
else:
    print("YOU ARE A LIVING PERSON OF AGE: ",age,"years")


    