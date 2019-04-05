# file = open("readme")
#
# while True:
#     text = file.readline()
#     if not text:
#         break
#     print(text,end="")
# file.close()

def copy_file():
    file_read = open("readme")
    file_write = open("readme01","w")
    text = file_read.read()
    file_write.write(text)
    file_read.close()
    file_write.close()


def cope_big_file():
    file_read = open("readme")
    file_write = open("readme01", "w")

    while True:
        text = file_read.readline()
        if not text:
            break
        file_write.write(text)

    file_read.close()
    file_write.close()

cope_big_file()