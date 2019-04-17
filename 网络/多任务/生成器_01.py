'''
生成器是一种特殊的迭代器

如果一个函数中有 yield 语句,那么这个就不在是函数,而是一个生成器的模板

'''

def creat_num(all_num):

    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "ok....."

obj = creat_num(50)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break

