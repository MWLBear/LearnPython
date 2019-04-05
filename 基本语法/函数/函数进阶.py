
def measure():
    print("start...")
    temp = 39
    wetness = 50
    print("end....")
    return temp,wetness

reslut = measure()
print(reslut[0],reslut[1])

# 接受元组的数据
gl_temp,gl_weness = measure()
print(gl_temp)
print(gl_weness)

print("")
a = 6
b = 10

# python
a,b = b,a
print(a)
print(b)

def test(num,num_list):
    num = 1
    num_list += num_list

num = 2
num_list = [1,2,3]

test(num,num_list)

print("*"*20)
print(num)
print(num_list)

def print_info(name,gebder):
    gender_text = "woman"



def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)

print("*"*50)

demo(1,2,3,4,5,6,name="lz",age=19)
print("*"*50)
def demo1(*args,**kwargs):
    print(args)
    print(kwargs)

num = (6,6,6)
num_dict = {"name":"lz","age":20}
demo1(*num,**num_dict)

print("*"*50)
def sum_number(num):
    if num == 1:
        return 1
    temp = sum_number(num - 1)
    return num + temp

print(sum_number(5))




