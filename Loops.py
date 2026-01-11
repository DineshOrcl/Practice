for i in range(1,11):
    print(i)

for i in "Python":
    print(i)    

for i in range(1,21):
    if i % 2 == 0:
        print("Even numbers between 1 and 20 are : ",i)

total = 0
for i in range(1,51):
    total = total + i
    print(total)

colors = ["red", "green", "blue", "yellow"]

import time
for m in range(len(colors)):
    print(colors[m])
    time.sleep(1)