# Inheritance = aqcuiring properties from parent class

from Fundamentals.OOP import Calculator
class Child(Calculator):
    number = 200
    def __init__(self):     # If parent constructor is not default, has some code inside, has a meaning, we will need to add a child constructor to call the parent constructor
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.number + self.num + self.Summation()
    

obj3 = Child()
print(obj3.number)
print(obj3.num)
print(obj3.Summation())
print(obj3.getCompleteData())
