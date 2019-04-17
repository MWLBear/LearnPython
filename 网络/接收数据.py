import socket



def recive_send_socket():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    dest_ip = input("请输入对方的 IP:")
    dest_port = input("请输入对方的端口:")
    dest_info = (dest_ip,int(dest_port))
    print(dest_info)
    udp_socket.bind(("",7899))
    send_data = input("请输入想要发送的数据:")
    udp_socket.sendto(send_data.encode("utf-8"),dest_info)

    rec_data = udp_socket.recvfrom(1024)
    print("%s:%s"%(str(rec_data[1]),rec_data[0].decode("gbk")))


def main():
    udp_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr = ('',9090)
    udp_socket.bind(local_addr)
    while True:
        re_data = udp_socket.recvfrom(1024)
        rev_msg = re_data[0]
        from_data = re_data[1]
        print("%s:%s" % (str(from_data),rev_msg.decode('gbk')))

    udp_socket.close()

if __name__ == '__main__':
    recive_send_socket()