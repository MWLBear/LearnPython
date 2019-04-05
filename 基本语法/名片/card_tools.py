# all card dict
#! /usr/local/bin/python3
card_list = []
def show_menu():
    print("*"*50)
    print("欢迎使用「名片管理系统」V 1.0")
    print("")
    print('1.新增名片')
    print('2.显示全部')
    print('3.搜索名片')
    print("")
    print("0退出系统")
    print("*"*50)
def new_card():
    print("-"*50)
    print("add new card")
    name_str = input("please add name : ")
    phone_str = input("please add phone : ")
    qq_str = input("please add qq : ")
    emali_str = input("please add email : ")
    card_dict = {
        "name":name_str,
        "phone":phone_str,
        "qq":qq_str,
        "email":emali_str
    }
    card_list.append(card_dict)
    print(card_list)
    print("add %s card sucess  " % name_str)
def show_all():
    print("-"*50)
    print("show all card")
    if len(card_list) == 0:
        print("没有名片记录，请使用新增功能添加名片！")
        return
    # 打印表头
    for name in ["姓名","电话","QQ","email"]:
        print(name,end="\t\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s"%(card_dict['name'],
                                          card_dict['phone'],
                                          card_dict['qq'],
                                          card_dict["email"]))
def search_card():
    print("-"*50)
    print("search card")
    name = input("请输入要查询的名字：")
    for card_dict in card_list:
        if card_dict["name"] == name:
            print("have find name %s" % name)

            for name in ["姓名", "电话", "QQ", "email"]:
                print(name, end="\t\t\t")

            print("")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict['name'],
                                                  card_dict['phone'],
                                                  card_dict['qq'],
                                                  card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("sorry not search %s" % name)
def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择想要执行的操作 "
                       "【1】 修改 【2】 删除 【0】 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info( find_dict["name"] ,"name :")
        find_dict["phone"] = input_card_info(find_dict["phone"] ,"phone :")
        find_dict["qq"] = input_card_info(find_dict["qq"] ,"qq :")
        find_dict["email"] = input_card_info(find_dict["email"] ,"email :")

        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")
    else:
        return
def input_card_info(dict_value,tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
