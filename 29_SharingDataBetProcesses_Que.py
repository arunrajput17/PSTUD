## Sharing Data between Process : Que (Sharing value using them)

import multiprocessing


def calc_square(numbers,q):
    
    for n in numbers:        
        q.put(n*n)  # adding data in the que
   

if __name__ == "__main__":
    numbers=[2,3,5]
    ### Declaring shared memory que
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()
    
    print('Outside the process Array')
    while q.empty() is False:
        print(q.get())
    
    
    