class Vehicle:
    def __init__(self, mark="",  speed=0):
        self.mark = mark
        self.speed = speed
    
    def accelerate(self, speed):
        self.speed += speed
        
    def stats(self):
        print(self.mark, self.speed )
    
    def __str__(self):
        return ("values" + self.mark)

class Car(Vehicle):
    def hornet(self):
        print("piii")
        
class Bicyle(Vehicle):
    def step(self):
        print("bike is moving")

v1 = Vehicle("Seat", 120)
v1.accelerate(15)
v1.stats()
# print(v1.__str__())
print(v1)

c1 = Car("BMW",100)
c1.accelerate(50)
c1.stats()

b1 = Bicyle("BH", 10)
b1.accelerate(15)
b1.stats()