import gevent
import time
import random
from gevent import monkey


# 将程序中的耗时操作的代码,换为 gevent 中自己实现的模块

monkey.patch_all()

def f(name):
    for i in range(10):
        print(name,i)
        time.sleep(random.random())

if __name__ == '__main__':

    gevent.joinall([
        gevent.spawn(f,"work1"),
        gevent.spawn(f,"work2")
    ])


# 熟练使用 代码搬运工