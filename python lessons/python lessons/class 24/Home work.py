class Animal:
        def __init__(self,a,b):
         self.name = a
         self.age = b
        print("A human is created")

        def eat(self):
         print(self.name," is eating")

       
       
       
         print(self.name,"is walking")

Likith =Animal("Likith",16)
Akash =Animal("Akash",20)
print(Likith.name)
print(Likith.age)

print(Akash.name)
print(Akash.age)

Likith.eat()
Akash.eat()