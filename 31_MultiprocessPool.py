## Multiprocesssing Pool
from multiprocessing import Pool
import time

def f(n):
    sum=0
    for x in range(10000):
        sum += x*x
    return sum


if __name__ == "__main__":
    ## With Pool
    t1=time.time()
    p = Pool()
    result= p.map(f,range(1000)) # Increase the number processing time will increase
    p.close()
    p.join()

    print('Pool took : ',time.time()-t1)


    ## Without Pool
    t2=time.time()
    result=[]
    for x in range(1000):   # Increase the number processing time will increase
        result.append(f(x))

    print('Serial Processing took : ',time.time()-t2)

    # print(result)


### Code to use selected number of process only

# def fun(n):
#     return n*n

# if __name__ == "__main__":
#     p = Pool(processes=3)   # DEfine how many number of process you want to use
#     result = p.map(fun,[1,2,3,4,5])
#     for n in result:
#         print(n)