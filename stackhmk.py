class Stack:
    def __init__(self,size):
        self.stack = []
        self.size=size
    def push(self,value):
        if len(self.stack) == self.size:
            print("overflow")
        else:
            self.stack.insert(0,value)

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

ui=input("Enter your word here: ")
lisT=list(ui)
s = Stack(6)
for i in range(len(lisT)):
    s.push(lisT[i])

s.display()


