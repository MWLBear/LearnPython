#! /usr/local/bin/python3

import card_tools

if __name__ == '__main__':
    while True:
        card_tools.show_menu()
        action = input("请输入希望执行的操作:")
        print("你选择的操作是【 %s 】" % action)
        if action in ["1", "2", "3"]:
            #
            if action == '1':
                card_tools.new_card()
            # show all
            elif action == "2":
                card_tools.show_all()
            # check info
            elif action == "3":
                card_tools.search_card()
            pass
        elif action == "0":
            print("退出登陆")
            break
        else:
            print("你输入的不正确，请重新输入")


