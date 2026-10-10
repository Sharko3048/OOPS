class Tree:
    def __init__(self,value):
        self.value = value
        self.leftnode = None
        self.rightnode = None

def in_order_traversal(root):
    if root.leftnode != None:
        in_order_traversal(root.leftnode)
    print(root.value)
    if root.rightnode != None:
        in_order_traversal(root.rightnode)

def pre_order_traversal(root):
    print(root.value)
    if root.leftnode != None:
        pre_order_traversal(root.leftnode)
    if root.rightnode != None:
        pre_order_traversal(root.rightnode)

def post_order_traversal(root):
    if root.leftnode != None:
        post_order_traversal(root.leftnode)
    if root.rightnode != None:
        post_order_traversal(root.rightnode)
    print(root.value)


root=Tree(12)
root.leftnode = Tree(7)
root.rightnode = Tree(18)
root.leftnode.leftnode = Tree(3)
root.leftnode.rightnode = Tree(10)
root.rightnode.leftnode = Tree(15)
root.rightnode.rightnode = Tree(20)
in_order_traversal(root)
print(root)
