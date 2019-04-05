class Gun:
    def __init__(self,model):
        self.bullet_count = 0
        self.model = model
    def add_bullet(self,count):
        self.bullet_count += count
        print("添加[%d]个子弹"%count)

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹,请添加子弹")
            return
        self.bullet_count -= 1;
        print("[%s] 突突突....剩余子弹,%d"%(self.model,self.bullet_count))

    # def __str__(self):
    #     return "型号:%s ,剩余子弹:%d"%(self.model,self.bullet_count)

class Solider:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("%s没有枪,无法射击"%self.name)
            return
        print("冲啊.........勇士[%s]!!!"%self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()

ak47 = Gun("AK47")
xsd = Solider("徐三多")
# sxd.gun = ak47
xsd.fire()


