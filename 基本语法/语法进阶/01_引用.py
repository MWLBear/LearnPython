
def test(num):
    print("%d adress in function is %d" % (num,id(num)))
    reslut = "hello"
    print("函数要返回的地址是 %d" % id(reslut))
    return reslut

a = 10
print("a adress is %d" % id(a))
test(10)
 