str = "leizi"
str1 = "    1"
print(str1)
print(len(str))
print(str.count("i"))
# print(str.count("a"))
print(str.index("l"))
print("----------------------")
# str常用方法
# 1.
print(str1.isspace())
print(str1.isalnum())

# 2.
num_str = "\u00b2  "
print(num_str)
# 纯数字
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
# 方法的替换
print("------------------------")
hello_str = "hello world"
print(hello_str.startswith('hello'))
print(hello_str.endswith('world'))
print(hello_str.find("llo"))
print(hello_str.find("abc"))
# 替换字符串
print("--------------")
print(hello_str.replace("world","python"))
print(hello_str)
# 字符串拆分和链接
print("--------------")

str3 = "登鹳雀楼\t王之涣\t白日依山尽\t\n"
print(str3.split())
str4 = str3.split()
print(" ".join(str4))
# 字符串的切片
