## Difference between Multithread and Multiprocess:
# The benefit of multiprocessing is that error or memory leak in one process 
# won't hurt execution of another process

#### Multiprocessing #############

# Create two process:
# 1. First is to calculate square of all numbers
# 2. Second one is to calculate cube of numbers

import time
import multiprocessing

square_result=[]

def calc_square(numbers):
    global square_result
    for n in numbers:
        # time.sleep(5)
        print('Square :', str (n*n))
        square_result.append(n*n)
    print('Within a process Result of square is ' + str(square_result))

def calc_cube(numbers):
    for n in numbers:
        # time.sleep(5)
        print('Cube :', str(n*n*n))


if __name__ == "__main__":
    
    arr =[2,3,8,9]

    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Result of square is ' + str(square_result))
    print('Done!!')

