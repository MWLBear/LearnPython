import multiprocessing
import time
"""
进程 资源和代码的总和
线程 

代码->进程->线程

线程不能独立执行,必须依存在进程中
进程理解为工厂中的一条流水线,而其中的线程就是这个流水线的工人

优缺点:

    线程执行开销小,但不利于资源的管理和保存,进程相反
    
"""

def test():
    while True:
        print("1.......")
        time.sleep(1)
def test2():
    while True:
        print("2......")
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=test2)

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()