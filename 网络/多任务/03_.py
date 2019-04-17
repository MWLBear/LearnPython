import threading
import time

#线程共享全局变量
#多线程共享全局变量问题 : 资源竞争

'''
全部变量

如果修改执行了,让全局变量指向了一个新的地方,必须使用 global
如果仅仅是修改了空间中的数据,此时不用必须使用 global

'''

#多线程 多任务 子线程和子线程之间共享全局变量
# 互斥锁 解决资源共享问题


g_num = 0
g_nums = [11,22]

def test1(temp):
    temp.append(33)
    # global g_num
    # g_num += 1
    print("test1 g_num = %s"%str(temp))

def test2(temp):
    temp.append(30)
    print("test2 g_num = %s"%str(temp))

mutex = threading.Lock()

def test3(num):
    global g_num
    mutex.acquire() # 加锁
    for i in range(num):
        g_num += 1
    mutex.release() #解锁
    print("test3 g_num = %d"%g_num)

def test4(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("test4 g_num = %d"%g_num)


def thread1():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    t2.start()
    print("main Thread g_nums = %s"%str(g_nums))

def thread2():
    t1 = threading.Thread(target=test3, args=(100000,))
    t2 = threading.Thread(target=test4, args=(100000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("main Thread g_num = %d" % g_num)



def main():
    thread2()

if __name__ == '__main__':
    main()
