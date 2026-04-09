# Classes = user defined blueprint or prototype

# A class will have methods, class variables, instance variables, constructors etc.

class Calc:
    num = 100
    
    def getData(self):
        return "I am now executing as a method in calss Calculator"

if __name__ == "__main__":  # This is a guard so that any action ouside the class doesn't get imported and executed in the receipiant file. It only gets executed when the file is where the code is
    obj1 = Calc() #this creats an object within the class, making "obj1" an instance.
    obj1.getData()
    obj1.num
    print("********")
    print(obj1.getData())
    print("^^^^^^^^^^^^")
    print(obj1.num)

# %%

class Calculator():
    num = 100

    def __init__(self, a, b):               # Constructor, a method automatically called when a new object is created under the class
        self.num1 = a
        self.num2 = b
        print("I'm called automatically when an object is created") # Rule of thumb: If the method name starts and ends with __ (like __init__), don't use return!
 
    def getData(self):
        return "I'm now executing as a method in the class"
    
    def Summation(self):
        return self.num1 + self.num2 + Calculator.num

if __name__ == "__main__":
    obj = Calculator(2, 3)
    print(obj.num)
    print(obj.Summation())

    obj2 = Calculator(1, 5)
    print(obj2.Summation())




