from multiprocessing import Pool
import os,time,random

def test(msg):
    t_start = time.time()
    print("%s 开始执行,进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕*耗时%0.2f"%(t_stop-t_start))


po = Pool(3)
for i in range(0, 10):
    po.apply_async(test,(i,))
print("--------start------")
po.close() #关闭进程池,关闭后po不再接收新的请求
po.join() #等待 po 中所有的子进程执行完成,必须放在 close 语句之后
print("---------end-------")

