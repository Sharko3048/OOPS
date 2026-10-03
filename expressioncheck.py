open=["{","[","("]
close=["}","]",")"]

expression = "(hello},[Johnny},(Chocolate)"

stack=[]
valid=True
for i in range(len(expression)):
    if expression[i] in open:
        stack.append(expression[i])
    elif expression[i] in close:
        index = close.index(expression[i])
        if len(stack) > 0 and open[index] == stack[-1]:
            stack.pop()
        else:
            valid = False
            break

if valid == False:
    print("Invalid")
else:
    print("Valid")