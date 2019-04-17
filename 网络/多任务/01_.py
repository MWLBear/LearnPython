from time import sleep,ctime
import threading


def sing():
    for i in range(5):
        print("sing .....%d"%i)
        sleep(1)
def dance():
    for i in range(5):
        print("dance.....%d"%i)
        sleep(1)

if __name__ == '__main__':

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数量为:%d"%length)
        if length <= 1:
            break
        sleep(0.3)


