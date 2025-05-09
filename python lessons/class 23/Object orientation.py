class Human:
    def __init__(self,a,b,c):
       self.name = a
       self.age = b
       self.gender = c
       print("A human is created,name is {self.name},age is {self.age},gender is {self.gender}")

    def eat(self):
        print(f"{self.name} is eating")
    def run(self):
        print(f"{self.name} is running")
    


likith = Human("likith",20,"male")
Akash = Human("Akash",20,"male")
Venkatesh = Human("venkatesh",20,"male")

likith.eat()
Akash.run()
Venkatesh.eat()

# git add .
# git commit -m "we have learnt print and comment"
# git push