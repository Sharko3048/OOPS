class Stack:
    def __init__(self,size):
        self.stack = []
        self.size=size
    def push(self,value):
        if len(self.stack) == self.size:
            print("overflow")
        else:
            self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            print("underflow")

        else:
            self.stack.pop()
    
    def display(self):
        print(self.stack)
    
    def size(self):
        print(self.size)
    
    def available_size(self):
        print(self.size - len(self.stack))
s = Stack(5)
s.push(8)
s.push(7)
s.push(21)
s.push(9)
s.push(1)
s.push(3)

s.display()
for i in range(6):
    s.available_size()
    s.pop()
    s.display()