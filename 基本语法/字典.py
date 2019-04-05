leizi = {
    'name':'lz',
    'age':30,
    'school':'jd'
}
temp_dict = {
    'height':175,
    'age':40,
}
leizi.update(temp_dict)
print(len(leizi))

# 清空列表
leizi.clear()

print(leizi)
# print(leizi['name'])
for key in leizi.keys():
    print(key)


for value in leizi.values():
    print(value)

for key,value in leizi.items():
    print(key)
    print(value)


for name in leizi.items():
    print(name)