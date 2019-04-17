import socket
import tcp_01

# tcp_server 服务器
def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("",7899))
    # 让默认的套接字由主动变为被动
    tcp_server_socket.listen(128)

    #循环:调用多次 accept,从而为多个客服端服务
    while True:
    # 等待客户端的链接
        print("*"*50)
        print("等待一个新的客户端的到来.....")
        new_client_socket,clientAddr = tcp_server_socket.accept()
        print("新来的客户端的 IP 是 :%s 端口是:%s" % (str(clientAddr[0]),str(clientAddr[1])))

        #循环:为一个客服端服务
        while True:
            #接收客服端发送过来的请求
            recv_data = new_client_socket.recvfrom(1024)

            #rev 解开阻塞 1.客户端发送数据 2.客户端调用了 close 方法
            if not recv_data[0].decode('gbk'):
                break
            print("客户端发来的请求是:%s" % recv_data[0].decode("gbk"))
            #回送一部分数据到客服端
            new_client_socket.send("000000".encode("utf-8"))
        #客服端服务完毕
        new_client_socket.close()
        print("已经服务完毕")

    tcp_server_socket.close()

if __name__ == '__main__':
    main()