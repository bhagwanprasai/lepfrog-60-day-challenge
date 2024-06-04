class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

p1 = Person("bhagwan", 30)  # Pass arguments to the constructor

print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30

#object method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("bhagwawn", 36)
p1.myfunc()

#self parameter

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("bhagwan", 36)
p1.myfunc()


#module

import module as mx
mx.greeting("bhagwan")

a = mx.person1["age"]
print(a)

import platform

v = dir(platform)
print(v)
from module import person1
print(person1["age"])

