class ClassA:
    def hi(self):
        print("hello!")

class ClassB:
    def hi(self):
        print("Hallo")


    def another(self):
        print("In Class B.")

class ClassC(ClassA,ClassB):
    pass


c = ClassC()
c.hi()
c.another()