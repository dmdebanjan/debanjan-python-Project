file = open('test.txt')

# print(file.read(5))
# print(file.readline())

# print line by line using readline method using while & readline

# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

# print line by line using readline method using while & readline
for line in file.readlines():
    print(line)

file.close()
