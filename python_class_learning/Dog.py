class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("%s岁%s在坐着" % (self.age, self.name))

    def rool_back(self):
        print("%s岁%s在打滚" % (self.age, self.name))


d1 = Dog("alis", 20)
d1.sit()
