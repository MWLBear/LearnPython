name_list = ['lei','zs','zhangsan']
name_list[0] = 'ios'
print(name_list[0])
print(name_list[1])
print(name_list[2])

index = name_list.index('ios')

print(index)

# 增加
name_list.append('mm')
name_list.append('mm')
print(name_list)
name_list.insert(1,'123')
print(name_list)
test_list = ['uu','ii','ee']
name_list.extend(test_list)
print(name_list)

# 删除
name_list.remove('zs')
print(name_list)
name_list.pop()
print(name_list)


name_list.remove('mm')
print(name_list)
print(len(name_list))
print(name_list.count('mm'))

# 排序

name_list.sort(reverse=True)
print(name_list)

name_list.sort()
print(name_list)

name_list.reverse()
print(name_list)
if __name__ == '__main__':

    for name in name_list:
        print(name)
    pass
    # print(name_list.sort())
    # print(name_list.reverse())