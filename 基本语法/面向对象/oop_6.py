class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print("%s and %s paly game"%(self.name,dog.name))
        dog.game()

class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s game........dadi"%self.name)
    # 静态方法
    @staticmethod
    def run():
        print("run")

class XiaotianDog(Dog):
    def game(self):
        print("%s fly.......sky"%self.name)

dog = XiaotianDog("wc")

xm = Person("xm")
xm.game_with_dog(dog)

class Tool(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_coount(cls):
        print(cls.count)


print("")
tool = Tool("l")
tool2 = Tool("s")
tool3 = Tool("l")
print("-")
Tool.show_tool_coount()