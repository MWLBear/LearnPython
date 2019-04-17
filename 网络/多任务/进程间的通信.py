import multiprocessing

def test():
    pass

def main():
   q = multiprocessing.Queue(3)
   q.put("1")
   q.put("2")
   q.put((1,2,4))

   print(q.get())
   print(q.full())
   print(q.empty())

if __name__ == '__main__':
    main()