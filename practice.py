import threading

def print_numbers():
   for i in range(10):
       print("thread-1 = ")

def print_numbers2():
   for i in range(5):
       print("thread-2")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers2)

t1.start()
t1.join()
t2.start()
