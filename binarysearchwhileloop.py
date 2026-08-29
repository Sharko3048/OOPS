import random
list=[random.randint(0,20)for i in range(10)]
list.sort()
print(list)
l=0
h=len(list)-1
key=8
found=False

#while found == False:
while l <= h:
    mid = (l+h)//2
    if list[mid] == key:
        print("Found")
        found = True
        break
    elif list[mid] < key:
        l=mid+1
    elif list[mid] > key:
        h=mid-1

if found == False:
    print("Value not found")
elif found == True:
    print("Value found at index",mid)
