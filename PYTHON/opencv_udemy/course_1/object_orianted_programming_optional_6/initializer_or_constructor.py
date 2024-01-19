class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
    
a1 = Animal("dog", 2)
a2 = Animal("kedi", 4)
a3 = Animal("kuş", 4)

a1.getName()
