class Human:
    def __init__(self,a,b):
        self.name = a
        self.age = b
        print("A human is created")

    def eat(self):
        print(self.name," is eating")

    def walk(self):
        print(self.name,"is walking")
    
    def sleep(self):
        print(self.name,"is sleeping")

Likith = Human("Likith",16)
Akash = Human("Akash",20)
print(Likith.name)
print(Likith.age)

print(Akash.name)
print(Akash.age)

Likith.eat()
Akash.eat()
