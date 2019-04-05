class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型:%s\n总面试:%.2f [剩余: %.2f] \n家具:%s"%(self.house_type,self.area
                                                        ,self.free_area,self.item_list))
    def add_item(self,item):
        if item.area > self.free_area:
            print("添加的:[%s]的面积过大,无法添加"%item.name)
            return
        if self.free_area == 0:
            print("房屋剩余面积不足,无法添加")
            return
        # list_dict = {"name":item.name,"area":item.area}
        self.item_list.append(item.name)
        self.free_area -= item.area
        print("add %s"%item.name)

bed = HouseItem("席梦思",78)
chest = HouseItem("衣柜",90)
table = HouseItem("餐桌",2)

my_house = House("3室一厅",90)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)


print(my_house)