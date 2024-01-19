class Employee(object):
    age = 25
    salary = 1000

    def ageSalaryRatio(self):
        print("method :" ,self.age / self.salary)

def ageSalaryRatio(age, salary):
    print("function : ", age/salary)

e1 = Employee()

e1.ageSalaryRatio()

ageSalaryRatio(30,3000)

pi = 3,14
r = 5
area = pi*r**2

def findArea(pi, r):
    area = pi*r**2
    print(area)

findArea(pi,r)