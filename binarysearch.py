import random
list=[random.randint(0,20)for i in range(10)]
list.sort()
print(list)
l=0
h=len(list)-1
key=8
found=False

def binary_search(l,h):
    mid=(l+h)//2
    if l <= h:
        if list[mid] == key:
            print("found")
            return mid
        elif list[mid] < key:
            l=mid+1
            return binary_search(l,h)
        elif list[mid] > key:
            h=mid-1
            return binary_search(l,h)
    else:
        return -1

result=binary_search(l,h)
if result == -1:
    print("Value is not in list")
else:
    print(f"Value found at {result}")
