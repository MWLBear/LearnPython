info_tuple = ('zhangsan','19',1.75)

print(info_tuple[0])

print(len(info_tuple))
print("%s 年龄是 %s 身高是 %.2f" % info_tuple)

print(type(info_tuple))
list = list(info_tuple)
list.append('1234')
print(list)
print(type(list))