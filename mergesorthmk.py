import random
list=[random.randint(0,20)for i in range(10)]
print(list)

def merge(l,mid,h):
    temp=[]
    start1=h
    start2=mid-1
    while start1 >= mid and start2 >= l:
        if list[start1] > list[start2]:
            temp.append(list[start1])
            start1-=1
        else:
            temp.append(list[start2])
            start2-=1
    while start1 >= mid:
        temp.append(list[start1])
        start1-=1
    while start2 >= l:
        temp.append(list[start2])
        start2-=1
    k=0
    print(temp)
    for i in range(l,h+1):
        list[i]=temp[k]
        k+=1


def divideandconquer(l,h):
    if l < h:
        print("success")
        mid=(l+h)//2
        divideandconquer(l,mid)
        divideandconquer(mid+1,h)
        merge(l,mid,h)

divideandconquer(0,9)
print(list)