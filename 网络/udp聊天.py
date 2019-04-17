import socket


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_msg():
    # 发送数据
    send_data = input("请输入要发送的数据:")
    dest_ip = input("请输入对方的 IP:")
    dest_port = input("请输入对方的 port:")
    dest_info = (dest_ip, int(dest_port))
    udp_socket.sendto(send_data.encode("utf-8"), dest_info)

def recv_msg():
    rec_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(rec_data[1]), rec_data[0].decode('gbk')))

def main():
    # 绑定信息
    udp_socket.bind(("",7899))
    while True:
        print("--------- 聊天器 ----------")
        print("1:发送数据")
        print("2:接收数据")
        print("0:退出系统")
        op = input("请输入功能:")
        if op == "1":
            send_msg()
        elif op == "2":
            recv_msg()
        elif op == "0":
            break
        else:
            print("输入有误,请重新输入!!")
if __name__ == '__main__':
    main()