import multiprocessing
import os,time,random

def file_copy(q,file_name,old_file_name,new_file_name):

    old_file_path = old_file_name + "/" + file_name
    new_file_path = new_file_name + "/" + file_name

    with open(old_file_path,"rb") as f:
       contet =  f.read()

    with open(new_file_path,"wb") as f:
        f.write(contet)

    # cpoy 向队列中写入一个消息
    q.put(file_name)

def main():
    old_file_name = input("请输入要 copy的文件名:")
    new_file_name = ""

    try:
        new_file_name = old_file_name+"[复件]"
        os.mkdir(old_file_name+"[复件]")
    except:
        pass
    file_lists = os.listdir(old_file_name)

    po = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()
    for file_name in file_lists:
        # 向进程池中添加任务
        po.apply_async(file_copy,args=(q,file_name,old_file_name,new_file_name))

    po.close()
    all_file_num = len(file_lists)


    while True:
        time.sleep(1)
        file_name = q.get()
        if file_name in file_lists:
            file_lists.remove(file_name)
        copy_rate = (all_file_num - len(file_lists)) * 100 / all_file_num
        print("\r拷贝的进度是%.2f %%"%(copy_rate)+ " "*50,end="")
        if copy_rate >= 100:
            break
    print()

if __name__ == '__main__':
    main()