
### File open modes
## r opens file for read only. Throws error if file does not exist.
## w opens file for writing only. If file doesnt exist then it will create new one. If it exist then it will overwrite it.
## r+ opens file for both reading and writing
## w+ opens file for reading and writing. If file doesnt exist then it will create new one. If it exist then it will overwrite it.
## a opens a file in append mode. Whatever you write to file get appended and original content will not be overwritten.

# 'w' mode will overwrite the file and 'a' mode will append the file

# f = open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny.txt','w')

f = open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny.txt','a')
f.write('\nI Love Python')

# f = open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny1.txt','w')
# f.write('Teacher: Why are you late,Frank?\nFrank: Because of the sign.\nTeacher: What sign?\nFrank: The one that says"School Ahead, Go Slow".')

f.close()

### Reading
# We want to create a new file that has all the lines in the funny1.txt plus word count for each line

f= open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny1.txt','r')
# print(f.read())  # for printing whole file
f_out = open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny_wc.txt','w')

for line in f:
    # print(line)
    tokens= line.split(' ')
    f_out.write(' wordcount: '+str(len(tokens)) +' ' +line)
    # print(len(tokens))
    # print(str(tokens))


f.close()
f_out.close()

### Use of 'With' statement: No need to explicitly close the file by using with statement

with open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\funny1.txt','r') as f:
    print(f.read())

print(f.closed)


# #1. File input.txt contains numbers separated by comma as shown below,
# 6,8
# 7,6
# 2,8
# 9,5
# 9,6
# a. Write a function countNum(file_name,num) such that it returns number of
# occurrences of a number in that file. for example,
# countNum(“input.txt”,9) should return 2
# countNum(“input.txt”,100) should return 0

def countNum(file_name,num):
    fname='D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\'+file_name

    f_in = open(fname,'r')

    list=[]
    for i in f_in:
        # print(i)
        list.append(i[0])
        list.append(i[2])
    # print(list)
        
    count=0
    
    for j in list:
        if j==str(num):
            count=count+1
    if count==0:
        print('Number not availble in list and count is '+str(count))
    else:
        print('Count of number '+str(num)+ ' is ' +str(count))
    f_in.close()

countNum('Input.txt',9)
countNum('Input.txt',100)

############# Other way##############

def countNum1(file_path,num1):
    count1=0
    with open(file_path,'r') as fp1:
        for line1 in fp1.readlines():
            # print(line1)
            tokens1=line1.split(',')
            count1 += count_num_in_tokens(tokens1,num1)
    return count1

def count_num_in_tokens(tokens1,num1):
    count1=0
    for token1 in tokens1:
        if num1 == int(token1):
            count1 +=1
    return count1

c= countNum1('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\Input.txt',9)
print('count',c)





##b. Change input.txt so that when program ends it contains sum of all numbers in a line
# as shown below,
# 6,8,sum: 14
# 7,6,sum: 13
# 2,8,sum: 10
# 9,5,sum: 14
# 9,6,sum: 15

f2=open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\Input1.txt','r')
f2_out=open('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\Input1_wc.txt','w')

# print(f2.read())

for k in f2:
    # print(k)
    f2_out.write('Sum is '+ str(int(k[0])+int(k[2]))+' of '+k)

f2.close()
f2_out.close()
print('ok')


############## Other way################

def sum_numbers(file_input_path2,file_output_path2):
    output_lines=[]
    with open(file_input_path2,'r') as fp2:
        for line2 in fp2.readlines():
            tokens2= line2.split(',')
            total = sum_tokens(tokens2)
            output_lines.append('sum: '+ str(total)+ ' | '+ line2)
        with open(file_output_path2,'w') as fw2:
            fw2.writelines(output_lines)


def sum_tokens(tokens2):
    sum=0
    for token2 in tokens2:
        sum +=int(token2)
    return sum

sum_numbers('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\Input2.txt',
'D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\Input2_wc.txt')