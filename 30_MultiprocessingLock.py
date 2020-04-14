#### Lock : It is used to lock the access. So, that two process cannot access it at same time

import time
import multiprocessing

def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()  # To put a lock
        balance.value = balance.value +1
        lock.release()  # To relesae a lock

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()  # To put a lock
        balance.value = balance.value -1
        lock.release()  # To relesae a lock

if __name__ == "__main__":
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()         ## Creating a lock variable using lock class and pass it in processes
    d = multiprocessing.Process(target=deposit,args=(balance,lock)) ## Passing lock in process
    w = multiprocessing.Process(target=withdraw,args=(balance,lock)) ## Passing lock in process

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)



