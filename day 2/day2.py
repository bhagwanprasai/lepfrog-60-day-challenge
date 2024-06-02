#functions

def myfunction():
    print("hello")

myfunction()

#with arguments
def argfun(name,age):
    print(name + str(age))

argfun("bhagwan", age=30)

#return value

def ret(x):
    return x*5

print(ret(3))

#rescursion
def recur(k):
    if(k>0):
        result = k + recur(k - 1)
        print(result)
        return result #esplicit rerturn of the result
    else:
        result = 0
        return result
print("\n \n recursion example ")
recur(8)


#lambda
#function that take multiple arguments

x = lambda a, b,c: a + b + c
print(x(5,6,7))

def lamfun(n):
    return lambda a : a * n

doubler = lamfun(2)
tripler = lamfun(3)
print(doubler(11))
print(tripler(11))


#array
cars = ["honda","bmw","mercedes"]

cars.append("lamborghini")
cars.pop(2)

for x in cars:
    print(x)