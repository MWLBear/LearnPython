class Person:

    def __init__(self,name,age):

        self.name = name
        # 私有属性
        self.__age = age

    def run(self):
        print("run")
    def eat(self):
        print("eat")
    def __sect(self):
        print("私有方法")

class Cat:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("init.....")
    def __del__(self):
        print("%s delloc"%self.name)
    def __str__(self):
        return ("cat name is %s"%self.name)
    def eat(self):
        print("eat")
    def paly(self):
        print("play")

person = Person(name='123',age=10)
person.run()
person.eat()
print(person._Person__age)
person._Person__sect()

print("*"*50)
tom = Cat('tom',12)
# tom.eat()
# print(tom.name)
# tom.paly()
print(tom)
# print(id(tom))



