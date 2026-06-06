class Sports:
    #hidden variable
    _keycode="3048"
    def __init__(self,brand,model,fuel,colour):
        self.b=brand
        self.m=model
        self.f=fuel
        self.c=colour
        self._a=brand+model
        print(self._a)
    def getcolour(self):
        print(self.c,self._a)
    def setcolour(self,c):
        self.c=c
    def show(self):
        print(f"The {self.b} is the model {self.m} and is coated in a layer of {self.c} and runs on {self.f}")

#ferrari=Sports("Ferrari","SF90 XX Stradale","petrol","red")
#ferrari.getcolour()
#print(ferrari._keycode)

class Ferrari(Sports):
    def __init__(self,brand,model,fuel,colour,tyres,location):
        Sports.__init__(self,brand,model,fuel,colour)
        self.t=tyres
        self.l=location
    
    def show(self):
        print(f"The {self.b} is the model {self.m} and is coated in a layer of {self.c} and runs on {self.f}, it has {self.t} type of tyres and can be found in {self.l}")

Car = Ferrari("Ferrari","SF90 XX Stradale","Petrol","Red","Michelin","Italy")
Car.getcolour()
Car.setcolour("Blue")
Car.show()






        