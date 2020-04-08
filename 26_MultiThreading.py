## Multithreading (Example os Mom Cooking with taking care of baby and attending phone call)

## For a given list of numbers print square and cube of every numbers
## For example: Input:[2,3,8,9]
## Output: Square list - [4,9,64,81] cube list - [8,27,512,729]

import time
import threading

square_numbers =[]
def calc_square(numbers):
    print('calculate square numbers')
    for n in numbers:
        time.sleep(0.2)
        print('sqaure:',n*n)
        square_numbers.append(n*n)

def cal_cube(numbers):
    print('calculate cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)


if __name__ == "__main__":

    arr=[2,3,8,9]

    t =time.time()

    ## Before threading we call this way
    # calc_square(arr)
    # cal_cube(arr)

    ## After threading
    t1 = threading.Thread(target=calc_square,args=(arr,))
    t2 = threading.Thread(target=cal_cube,args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Result of square numbers :' + str(square_numbers))
    
    print('done in:', time.time()-t)
    print('Hah... I am done with all my work now!')

    # time before multithreading is 1.6925840377807617

    # After multithreading it is taking 0.8529384136199951

