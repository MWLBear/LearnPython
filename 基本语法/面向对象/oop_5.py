class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")


class Dog(Animal):

    def brak(self):
        print("叫")


class Cat(Animal):
    def catch(self):
        print("抓")

class Xiaotian(Dog):

    def fly(self):
        print("飞")
    def brak(self):
        super().brak()
        print("god wang wang..... ")
xiaohei = Dog()
xiaohei.run()
xiaohei.drink()
print("")
xm = Cat()
xm.catch()
xm.drink()
xm.sleep()
print("")

xtq = Xiaotian()
xtq.drink()
xtq.fly()
