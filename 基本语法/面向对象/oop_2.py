# 小明爱跑步

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __del__(self):
        print("delloc")

    def eat(self):
        print("%s love eat,after eat to run"%self.name)
        self.weight += 1.0

    def run(self):
        print("%s love run "%self.name)
        self.weight -= 0.5

    def __str__(self):
        return "my name is %s and weight is %.2f kg"%(self.name,self.weight)


xiaoming = Person("xiaoming",80.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
print('*'*50)


