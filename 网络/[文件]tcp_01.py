import socket


def main():

    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip = input("请输入要链接服务器的 IP:")
    server_port = input("请输入要链接的服务器的port:")
    send_data = input("请输入要发送的数据:")
    tcp_socket.connect((server_ip,int(server_port)))
    tcp_socket.send(send_data.encode("utf-8"))
    tcp_socket.close()

if __name__ == '__main__':
    main()