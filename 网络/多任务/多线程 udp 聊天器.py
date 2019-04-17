import socket
import threading


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def recv_msg():
    while True:
        revdata = udp_socket.recvfrom(1024)
        print(revdata)

def send_msg(dest_ip,dest_port):
    while True:
        send_data = input("请输入要发送的数据:\n")
        udp_socket.sendto(send_data.encode("gbk"),(dest_ip,dest_port))

def main():
    udp_socket.bind(("",7890))

    dest_ip = "172.20.10.3"
    dest_port = 8080

    t_recv = threading.Thread(target=recv_msg)
    t_send = threading.Thread(target=send_msg,args=(dest_ip,dest_port))

    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()