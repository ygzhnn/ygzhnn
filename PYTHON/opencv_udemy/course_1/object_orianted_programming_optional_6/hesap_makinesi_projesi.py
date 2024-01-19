class Calculator:

    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        print(self.value1 + self.value2)

    def multiply(self):
        print(self.value1 * self.value2)

v1 = int(input("first value: "))
v2 = int(input("second value: "))

c1 = Calculator(v1,v2)

while True:
    choose = int(input("choose Add(1) or Multiply(2): "))

    if choose <= 2:
        if choose == 1:
            c1.add()
        else:
            c1.multiply()
        break
    else:
        print("Please enter a valid operation number (1 or 2)")

        
        
        

