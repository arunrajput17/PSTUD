## Sharing Data between Process : Value and Array (Sharing value using them)

import multiprocessing


def calc_square(numbers,result,v):
    v.value = 5.67  # Updating the value of v inside child process and access it outside the child
    for idx,n in enumerate(numbers):        # enumerate function will give index and value both
        result[idx] = n*n
    # print('Inside process ' + str(result[:]))

if __name__ == "__main__":
    numbers=[2,3,5]
    ### Declaring shared memory variable
    result = multiprocessing.Array('i',3) # Using Array
    v = multiprocessing.Value('d',0.0) # Example by using value as variable v and assigning it some value
    
    p = multiprocessing.Process(target=calc_square,args=(numbers,result,v))

    p.start()
    p.join()

    print('Outside the process Array', result[:])
    print('Outside the process Value', v.value)
    
    