#Writing text to a file
f = open("myfile.txt", 'w')
f.write("First line. \nSecond line. \n")
f.close()

#Writing Nmbers to a file
import random
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close()

#Reading Text from a File
f = open("myfile.txt", 'r')
text = f.read()
print(text)

#Reading Text from a File using for loop
f = open("myfile.txt", 'r')
for line in f:
    print(line)

#Reading Text from a file using while true loop
f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
#Reading Number from a File
f = open("integers.txt", 'r')
thesum = 0
for line in f:
    line = line.strip()
    number = int(line)
    thesum += number
print("The sum is", thesum)

#Reading Number from a File
f = open("integers.txt", 'r')
thesum = 0
for line in f:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        thesum += number
print("The sum is", thesum)