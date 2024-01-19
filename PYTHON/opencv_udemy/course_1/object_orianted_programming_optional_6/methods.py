class Square(object):

    edge = 5 #meter
    area = 0

    def area1(self):
        self.area = self.edge* self.edge
        print(self.area)


s1 = Square()
print(s1)
print(s1.edge)
s1.area1()
s1.edge = 7
s1.area1()
