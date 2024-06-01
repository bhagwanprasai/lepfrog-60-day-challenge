print("day1")
a = 30
b = 40
#comments

#casting
x = str(3)
x = int(3.0)
str = float(3)
d = """helloworld"""
print(d[2:])
age = 36
text = f"my name is god, i am {age}yrs old"
print(text)

#booleans
print(bool("hello"))
print(bool(5))
print(isinstance(age, int))


#list
list1 = ["apple",True,36,"banana","cherry"]
print(list1)
print(len(list1))
print(type(list1))
#list of constrcutorss
mylist = list(("apple","banana"))
print(mylist)

#truple
#allows duplicate and is ordered and unchangeable
myturple = ("apple","banana")
print(myturple)

#sets
#sets items are unordered, unchangeable and donot allow duplicate value
myset = {"apple",36,40,True,"banana"}
print(myset)

#dictionaries are ordred changeable and no duplicate is allowed
#can conatin list
thisdic ={
    "name":"bhagwan",
    "age":"20",
    "year":"2004",
    "colors": ["red","yellow"]

}
print(thisdic)

#if 
if a > b:
    print("a is greater")
else:
    print("b is greater")
#shorthand if
if b > a : print("b is greater")

#shorthand else 
print("a") if a > b else print("b")


#whileloops 
i = 1
while i < 6:
    print(i)
    i += 1

#for lopps
for x in list1:
    print(x)

for x in d:
    print(x)

for x in range(2,9,2):
    print(x)
else:
    print("finally done")

color = ["red", "green", "blue"]
fruits  = ["apple", "cherry","banana"]
for x in color:
    for y in fruits:
        print(x,y)


