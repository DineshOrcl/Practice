print('Hello,World!')

a = 10
b = 20
c = a + b
print("The addition of two numbers",a,",",b,"is",c)

#loop
for i in range(1, 9):
    print("Numbers:",i)

#Random
import random
 
number = random.randint(1,10)
guess = int(input("Guess anumber between 1 and 10; "))

if guess == number:
    print("You guesse`d it right!")
else:
    print("oops, The number was",number)


age = 25
print(age)

authors = ['Preeti Shenoy','Amish Tripati','Erin Morgenstein']
print(authors[1])
print('Erin Morgenstein' in authors)

#Datatype and operators
a = 10
print(type(a))
b = a + 10
print(b)
c = 3.14
print(type(c))
d = True
print(type(d))
e = "Hello"
print(type(e))
f = {"name" : "Dinesh"}
print(type(f))
g = (3,4)
print(type(g))
h = [1,"kumar"]
print("Datatype of h is: ",type(h))
i = {2,3,4}
print(type(i))
j = None
print(type(j))

list1 = [1, 2]
list2 = [1, 2]
print(list1 is list2)      # False (different objects)
print(list1 is not list2)  # True

