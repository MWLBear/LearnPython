# 单例模式
import day

class MusicPlayer(object):
    instance = None
    init_flag = False

    # 初始化方法只执行一次
    def __init__(self):
        if MusicPlayer.init_flag:
            return
        MusicPlayer.init_flag = True
        print("play")

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def test(self):
        print("test")

# 异常处理
def input_password():
    pwd = input("请输入密码:")
    if len(pwd) >= 8:
        return pwd
    ex = Exception("密码长度不够")
    raise ex

try:
    input_password()
except Exception as e:
    print(e)
 
print(day.__file__)




