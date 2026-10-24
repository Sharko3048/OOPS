class Tree:
    def __init__(self,value):
        self.value = value
        self.leftnode = None
        self.rightnode = None

def count(root):
    count=0
    if root != None:
        count+=1
        if root.leftnode != None:
            count+=1
        if root.rightnode != None:
            count+=1
        return(count)
    else:
        return(count)


root=Tree(10)
root.leftnode = Tree(5)
root.rightnode = Tree(5)
num=count(root)
print(num)