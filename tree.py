class Tree:
    def __init__(self,value):
        self.value = value
        self.leftnode = None
        self.rightnode = None



root=Tree(12)
root.leftnode = Tree(7)
root.rightnode = Tree(18)
root.leftnode.leftnode = Tree(3)
root.leftnode.rightnode = Tree(10)
root.rightnode.leftnode = Tree(15)
root.rightnode.rightnode = Tree(20)

print(root)