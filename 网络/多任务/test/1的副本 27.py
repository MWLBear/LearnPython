
import multiprocessing
import os,time,random

def file_copy(file_name,old_file_name,new_file_name):
    print("cpoy文件:从%s---->%s 文件名是:%s"%(old_file_name,new_file_name,file_name))
    old_file_path = old_file_name + "/" + file_name
    new_file_path = new_file_name + "/" + file_name
    with open(old_file_path,"rb") as f:
        contet =  f.read()
    
    with open(new_file_path,"wb") as f:
        f.write(contet)

def main():
    old_file_name = input("请输入要 copy的文件名:")
    new_file_name = ""
    try:
        new_file_name = old_file_name+"复件"
        os.mkdir(old_file_name+"复件")
    except:
        pass
    file_lists = os.listdir(old_file_name)

po = multiprocessing.Pool(3)

print(old_file_name)
print(new_file_name)

for file_name in file_lists:
    po.apply_async(file_copy,args=(file_name,old_file_name,new_file_name))
    
    po.close()
    po.join()

if __name__ == '__main__':
    main()
