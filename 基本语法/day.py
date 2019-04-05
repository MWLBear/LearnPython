import lz_message
import pygame

def hello():
    print("hello world")
    print("hello world")

def test():
    print('吃饭')

lz_message.send_message.send("1212")
print(lz_message.receive_message.receive())
