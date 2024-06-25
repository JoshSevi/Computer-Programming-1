thesum = 0.0
count = 0
average = 0

data = input("Enter a number or just enter to quit: ")
while data != "":

    number = float(data)
    thesum += number
    count += 1
    average = thesum / count
    data = input("Enter a number or just enter to quit: ")

print("The sum is", thesum)
print("The average is", average)
