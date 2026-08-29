import random
list=[random.randint(0,20)for i in range(10)]
print(list)
count=0
swap=0
list=[9, 18, 10, 8, 2, 3, 2, 8, 5, 3]

for i in range(len(list)):
    for j in range(len(list)-1-i):
        count+=1
        if list[j] > list[j+1]:
            swap+=1
            list[j],list[j+1] = list[j+1],list[j]
print(list)
print(count)
print(swap)
count=0
swap=0
list=[9, 18, 10, 8, 2, 3, 2, 8, 5, 3]

for i in range(len(list)):
    for j in range(len(list)-1):
        count+=1
        if list[j] > list[j+1]:
            swap+=1
            list[j],list[j+1] = list[j+1],list[j]
print(list)
print(count)
print(swap)