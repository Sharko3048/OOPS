class Student:
    def __init__(self,name,height,year,subjects):
        self.n=name
        self.h=height
        self.y=year
        self.s=subjects

    def show(self):
        print(f"Hi {self.n}, you are {self.h}cm tall and you are a Year {self.y} student and your subjects are {self.s}")

students=[]

Alex=Student("Alex",156,8,["Maths","Spanish","Economics","Psychology"])
Alex.show()
Alex.h=163
Alex.s.append("Geography")
Alex.show()

for i in range(3):
    people=Student(input("Enter your name: "),int(input("Enter your height (cm): ")),int(input("Enter your yeargroup: ")),[input("Enter your subject name: ") for j in range(4)])
    print()
    students.append(people)
students[-1].y=11
for i in students:
    i.show()
    print()


