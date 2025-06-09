from abc import ABC,abstractmethod

class Tesla(ABC):
    def runsOnFuel(self):
        print("This car runs on fuel")
    def runsOnBattries(self):
        print("This car runs on Battries")
    @abstractmethod
    def autoDrive(self):
        pass

class Model1(Tesla):
    def autoDrive(self):
        print("This car can autodrive or drive on itself without a driver")
    
car1 = Model1()
car1.autoDrive()
car1.runsOnBattries()
car1.runsOnFuel()