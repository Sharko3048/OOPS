import random
numbers=[]
for i in range(10):
    numbers.append(random.randint(1,20))
list=[random.randint(1,20)for i in range(10)]
print(numbers)
key=input("Enter a number between 1 and 20: ")
key=int(key)
if key in numbers:
    print("Yay found value",numbers.index(key))
else:
    print("Value aint there buddy")

for i in numbers:
    if i == key:
        print("found")
        break
else:
    print("not found")

found=False
for i in numbers:
    if i == key:
        found=True
        break

if found:
    print("value found at",numbers.index(key))
else:
    print("value isnt in the list")