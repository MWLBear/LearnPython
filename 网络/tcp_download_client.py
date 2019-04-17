import socket
PORT = 7810

def send_file_2_client(new_client,client_addr):

    file_name = new_client.recv(1024).decode("utf-8")
    print("客服端(%s)需要下载的文件是:%s"%(str(new_client),file_name))
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
    except Exception as e:
        print("没有要下载的文件")

    if file_name:
        new_client.send(file_content)

def server():
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.bind(("",PORT))
    tcp_server.listen(128)
    while True:
        new_client,client_addr = tcp_server.accept()
        # 调用发送文件的函数
        send_file_2_client(new_client,client_addr)

    new_client.close()
    tcp_server.close()

if __name__ == '__main__':
    server()