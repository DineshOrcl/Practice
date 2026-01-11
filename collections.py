sports = ['cricket','soccer','baseball']

print(sports[0])
for i in sports:
    print(i)

employees = {'name': 'Dinesh','age': 35,'hobby': 'reading'}
print(employees)

for i in employees:
    print(i,employees[i])

number = [1,2,3,4,5]
total = sum(number)
print(total)
print(sum(number))

number.append(6)
number.remove(2)

import time
time.sleep(2)
print(number)

#order preserved
numbers = [1,2,3,2,4,1,5]

unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)

#Reverse a list without using reverse()
numbers = [10, 20, 30, 40, 50]

reverse_list = numbers[::-1]
print(reverse_list)

#Find largest and smallest number in a list
numbers = [10,5,80,45]

print(numbers,'max:',max(numbers))
print(numbers,'min:',min(numbers))

numbers = [10, 25, 5, 80, 40]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Max:", max_num)
print("Min:", min_num)


#dictionaries
key = ["id","name","dept"]
value = [1,"Dinesh","IT"]

result = dict(zip(key,value))
print(result)