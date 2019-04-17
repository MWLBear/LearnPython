import socket

IP = "172.20.10.2"
PORT = 7810

def client():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 链接服务器
    tcp_socket.connect((IP,PORT))
    #获取从服务器下载的文件名
    send_msg_name = input("请输入要下载文件的名字:")
    # 将文件名发送至服务器
    tcp_socket.send(send_msg_name.encode("utf-8"))
    # 接收服务器返回的文件数据
    recv_data = tcp_socket.recv(1024)
    # 保存数据到文件之中
    if recv_data:
        with open("[文件]"+send_msg_name,"wb") as f:
            f.write(recv_data)
    # 关闭套接字
    tcp_socket.close()

def main():
    client()

if __name__ == '__main__':
    main()



'''
注意点:
1.tcp服务器 一般需要绑定服务器,否则找不到这个服务器
2.tcp 客服端一般不绑定,因为主动链接服务器,所以确定好服务器的
    IP 和 port 信息就好,本地客户端可以随机
3.tcp 服务器中通过 listen 将socket创建出来的主动套接字变为被动的
    套接字
4.当客户端链接服务器时,就需要 connect 进行链接udp直接发送,tcp鼻血
    要链接才发送
5.当 tcp 客服端链接服务器时,服务器端会有一个新的 socket,这个套接字是用来标记
    这个客服端的,并单为这个客服端服务
6.listen 后的套接字是被动的套接字,用来接收新的客服端的链接请求的,而 accept 返回的新套接字
    是这个新客服端的
7.关闭 listen 后套接字意味着被动套接字关闭了,会导致新的客服端不能链接到服务器,但是
    之前链接成功的客户端正常通信
8.关闭 accept 返回的套接字意味着这个客服端已经服务完毕
9.当客户端套接字调用 close 后服务器会 recv 解堵塞,并且返回长度为 0,所以可以根据
    返回数据的长度来区别客服端是否已经下线
    
'''