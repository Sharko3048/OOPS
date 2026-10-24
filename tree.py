class Tree:
    def __init__(self,value):
        self.value = value
        self.leftnode = None
        self.rightnode = None

count=0
total=0


def in_order_traversal(root):
    global count,total
    if root.leftnode != None:
        in_order_traversal(root.leftnode)
    print(root.value)
    count+=1
    total+=root.value
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

def insertion(root,add_value):
    if root == None:
        return Tree(add_value)
    elif root.value > add_value:
        root.leftnode = insertion(root.leftnode,add_value) 
    elif root.value < add_value:
        root.rightnode = insertion(root.rightnode,add_value)
    return root

def search(root,search_value):
    if root.value == search_value:
        return f"{root.value}, Value found"
    elif root.value > search_value and root.leftnode != None:
        return search(root.leftnode,search_value)
    elif root.value < search_value and root.rightnode != None:
        return search(root.rightnode,search_value)
    else:
        return -1

def in_order_succesor(root):
    current=root.rightnode
    while current != None and current.leftnode != None:
        current = current.leftnode
    return current

def in_order_predecessor(root):
    current=root.leftnode
    while current != None and current.rightnode != None:
        current = current.rightnode
    return current


def deletion(root,delete_value):
    if root.value == None:
        return root
    elif root.value > delete_value:
        root.leftnode = deletion(root.leftnode,delete_value)
    elif root.value < delete_value:
        root.rightnode = deletion(root.rightnode,delete_value)
    else:
        if root.leftnode == None:
            temp = root.rightnode
            root = None
            return temp
        elif root.rightnode == None:
            temp = root.leftnode
            root = None
            return temp
        else:
            print("deletion")
            temp = in_order_succesor(root)
            print(temp.value,"successor")
            v=root.value
            root.value=temp.value
            temp.value=v
            #root.rightnode = v
            temp.value = None
            print(root.leftnode.value,root.rightnode.value)
            root.rightnode = deletion(root.rightnode,temp.value)



root=Tree(12)
root.leftnode = Tree(7)
root.rightnode = Tree(18)
root.leftnode.leftnode = Tree(3)
root.leftnode.rightnode = Tree(10)
root.rightnode.leftnode = Tree(15)
root.rightnode.rightnode = Tree(20)

insertion(root,13)
in_order_traversal(root)
print(count,total)
#pre_order_traversal(root)
#post_order_traversal(root)
print(root)

result = search(root,21)
print(result)

deletion(root,7)
print(in_order_traversal(root))
#print(predecessor(root,10))
