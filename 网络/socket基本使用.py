import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        dest_addr = ('172.20.10.3',8080)
        send_data = input("请输入要发送的数据:")
        if send_data == "exit":
            break
        s.sendto(send_data.encode('utf-8'),dest_addr)
    s.close()

if __name__ == '__main__':
    main()