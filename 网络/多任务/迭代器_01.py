import time
from collections import Iterable
from collections import Iterator

'''
迭代器

实现 __iter__ 变成可迭代的对象

实现 __next__ 变成迭代器

'''

class Classmate(object):

    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)


    def __iter__(self):
        '''
        让对象变成可迭代的对象
        '''
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self,obj):
        self.obj = obj
        self.currentnum = 0

    def __iter__(self):
        pass

    def __next__(self):

        if self.currentnum < len(self.obj.names):
            ret = self.obj.names[self.currentnum]
            self.currentnum += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("123")
classmate.add("456")
classmate.add("789")

#
for name in classmate:
    print(name)
    time.sleep(1)

classmate_iterator = iter(classmate)

print(isinstance(classmate,Iterable))
print(isinstance(classmate_iterator,Iterator))