# Understanding class creation in Python

class BasicCalculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        total = self.a + self.b
        return total

    def subtraction(self):
        sub = self.a - self.b
        return sub     

    def multiplication(self):
        mult = self.a * self.b
        return mult

    def division(self):
        if self.b == 0:
            return "Error, cannot divide by 0!"
        div = self.a / self.b
        return div
    def show_all_results(self):
        print(f"--- Results for Numbers ({self.a}, {self.b}) ---")
        operations = {
            "Addition": ("+", self.addition),
            "Subtraction": ("-", self.subtraction),
            "Multiplication": ("*", self.multiplication), 
            "Division": ("/", self.division)
            }
        for label, (symbol, method) in operations.items():
            print(f"{label}: {self.a} {symbol} {self.b} = {method()}")
        print("-" * 40)

cal1 = BasicCalculator(10, 5)
cal2 = BasicCalculator(12, 6)

cal1.show_all_results()
cal2.show_all_results()
