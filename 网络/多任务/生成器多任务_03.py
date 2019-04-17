import time


def task():
    while True:
        print("----1---")
        time.sleep(0.1)
        yield

def task1():
    while True:
        print("----2---")
        time.sleep(0.1)
        yield

def main():
   t1 = task()
   t2 = task1()
   while True:
       next(t1)
       next(t2)

if __name__ == '__main__':
    main()