import threading
import time

class MyThread(threading.Thread):
    def run(self):
        self.login()
        self.register()

        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)
    def login(self):
        print("login")
    def register(self):
        print("register")

def main():
    print("lol...")

if __name__ == '__main__':

    t = MyThread()
    t.start()



