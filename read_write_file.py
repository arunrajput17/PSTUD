
### File open modes
## r opens file for read only. Throws error if file does not exist.
## w opens file for writing only. If file doesnt exist then it will create new one. If it exist then it will overwrite it.
## r+ opens file for both reading and writing
## w+ opens file for reading and writing. If file doesnt exist then it will create new one. If it exist then it will overwrite it.
## a opens a file in append mode. Whatever you write to file get appended and original content will not be overwritten.

# 'w' mode will overwrite the file and 'a' mode will append the file

# f = open('D:\\Day Shift\\Zpyth\\funny.txt','w')

f = open('D:\\Day Shift\\Zpyth\\funny.txt','a')
f.write('\nI Love Python')

# f = open('D:\\Day Shift\\Zpyth\\funny1.txt','w')
# f.write('Teacher: Why are you late,Frank?\nFrank: Because of the sign.\nTeacher: What sign?\nFrank: The one that says"School Ahead, Go Slow".')

f.close()

### Reading
# We want to create a new file that has all the lines in the funny1.txt plus word count for each line

f= open('D:\\Day Shift\\Zpyth\\funny1.txt','r')
# print(f.read())  # for printing whole file
f_out = open('D:\\Day Shift\\Zpyth\\funny_wc.txt','w')

for line in f:
    # print(line)
    tokens= line.split(' ')
    f_out.write(' wordcount: '+str(len(tokens)) +' ' +line)
    # print(len(tokens))
    # print(str(tokens))


f.close()
f_out.close()

### Use of 'With' statement: No need to explicitly close the file by using with statement

with open('D:\\Day Shift\\Zpyth\\funny1.txt','r') as f:
    print(f.read())

print(f.closed)


##1. File input.txt contains numbers separated by comma as shown below,
# 6,8
# 7,6
# 2,8
# 9,5
# 9,6
# a. Write a function countNum(file_name,num) such that it returns number of
# occurrences of a number in that file. for example,
# countNum(“input.txt”,9) should return 2
# countNum(“input.txt”,100) should return 0




##b. Change input.txt so that when program ends it contains sum of all numbers in a line
# as shown below,
# 6,8,sum: 14
# 7,6,sum: 13
# 2,8,sum: 10
# 9,5,sum: 14
# 9,6,sum: 15