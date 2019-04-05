num_one = 1

def demo1():
    global num_one
    num_one = 2
    print("%d" % num_one)

def demo2():
    print("%d" % num_one)


demo1()
demo2()