# List = Mutable Element haru ghatbadh garna sakxa
# Tuple = Immutable Element haru ghatbadh garna sakinna

list = [1,2,2,3,4,5,6,7,"Kamal","AI","ML"]
print(type(list))
print(len(list))
print(list)
print(list[0])

tuple = (1,2,3,"Machine", "Learning")
print(type(tuple))
print(len(tuple))
print(tuple)


for i in list:
    print(i,end=" ")
for i in tuple:
    print(i,end=" ")

for i in enumerate(list):
    print(i,end=" ")

list.append("YO MAILE ADD GAREKO")  #List ma add garne
list.insert(0,"First")  #Desired location ma add garna (pos,val)
print(list)

list.remove(2) #List bata remove garne tyo diyeko value
#yedi hataiyeko element list ma repeat vako xa vane suruma jun xa tyo matra remove hunxa
list.pop(2) #List bata tyo indexko value remove garne
print(list)

listAi=["Machine",2,"Learning",6,"Workshop"]
listAi.pop(1)
listAi.remove(6)
print(listAi)

concatedList=list+listAi   # Duita List jodne ya concat garne 
print(concatedList)


# TUPLE CHAI CONCATENATION MATRA HUNXA
tuple1=(0,1,2)
tuple2=(3,4,5)
finalTuple=tuple1+tuple2
print(finalTuple)

# LIST COMPREHENSION
# list_num=[2,3,4,5,6,7]
# list_sqr=[]
# for i in list_num:
#     i=i**2
#     list_sqr.append(i)
# print(list_sqr)

list_num=[2,3,4,5,6,7]
squared=[i**2 for i in list_num]
print(squared)

# 1 to 20 range ko even number using list comprehension
sqrd=[]
for i in range(1,21):
    if i%2==0:
        sqrd.append(i)
print(sqrd)

even = [i for i in range(1,21) if i%2==0]
print(even)

# Dictionary in PYTHON      {key:value} pair
dict={"First":1,"Second":2,"Third":3}
print(type(dict))
print(dict)

print(dict.keys())
print(dict.values())

dict["Fourth"]=4  # Add new key value to dictionary
print(dict)

for i in dict:              # Yesle Key print garxa
    print(i)
for i in dict.values():     # Yesle Values print garxa
    print(i)
for i in dict.items():      # Yesle Duitai Key ra Value print garxa
    print(i)


#LIST IN DICTIONARY

dict1 = {"Subject":["Python","Java","C","Rust","C++"], "Marks":[67,85,69,87,45]}
for i in dict1:              
    print(i)
for i in dict1.values():     
    print(i)
for i in dict1.items():      
    print(i)