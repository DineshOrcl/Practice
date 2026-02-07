#lists
a = [1,'Hello',3.2]
print(a[0])
print(a[-1])
a.append('Sir Arthur conon Doyale')
print(a)
a.remove(3.2)
print(a)
a[2] = "Amend"
print(a)
print(len(a))

a = [1, 2, 3, 4]
x = a.pop(2)
a.remove(4)
print(x)
print(a)

lst = [5, 10, 15, 20]

lst.remove(15)
lst.pop(2)
del lst[0]
print(lst)

lst = [10, 20, 30]
#value = lst.pop(1)
del lst[1]
print(lst)


books = {"type":"fiction", "type":"nonfiction"}
print(books["type"])
books.popitem()
#print(books["type"])
books["type"] = "fiction"
books["price"] = 400
books["stock"] = 1000

for i in books:
    print(i,books[i])
for i,value in books.items():
    print(i,value)
print(books)

student = {"name": "Dinesh", "age": 25, "city": "Chennai"}

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

for value in student.values():
    print(value)


word = "banana"
count = {}

for i in word:
    count[i] = count.get(i,0) + 1

print(count) 

list1 = ["id", "name", "age"]
list2 = [101, "Arun", 25]

d = dict(zip(list1, list2))
print(d)

for ch in "Python":
    print(ch)

