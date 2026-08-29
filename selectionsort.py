import random
list=[random.randint(0,20)for i in range(10)]
print(list)

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[j] < list[i]:
           list[j], list[i] = list[i],list[j] 
print(list)
