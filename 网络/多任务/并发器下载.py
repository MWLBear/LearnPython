import urllib.request
import gevent

def down_load_image(imageurl):
   re =  urllib.request.urlopen(imageurl)
   data = re.read()
   image_name = imageurl.split("/")[-1]
   # print(image_name)
   with open(image_name,"wb") as f:
       f.write(data)

def main():
    gevent.joinall([
        gevent.spawn(down_load_image,"https://rpic.douyucdn.cn/appCovers/2017/09/22/1760931_20170922133718_big.jpg"),
        gevent.spawn(down_load_image,"https://rpic.douyucdn.cn/appCovers/2017/09/17/2308890_20170917232900_big.jpg")
    ])

if __name__ == '__main__':
    main()