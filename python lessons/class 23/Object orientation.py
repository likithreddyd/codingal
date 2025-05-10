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
    def study(self):
        print(f"{self.name} is studing")
    def play(self):
        print(f"{self.name} is playing")
    def walk(self):
        print(f"{self.name} is walking")
    def game(self):
        print(f"{self.name} is gaming")
    


likith = Human("likith",20,"male")
Akash = Human("Akash",20,"male")
Venkatesh = Human("venkatesh",20,"male")
Veer =  Human("veer",15,"male") 
kavita =  Human("Kavita",12,"female")
lakshmi =  Human("lakshmi",19,'female')

likith.eat()
Akash.run()
Venkatesh.study()
Veer.play()
kavita.walk()
lakshmi.game()


