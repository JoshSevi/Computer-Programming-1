#this program demonstrates the Counter Class

#Import the Counter class from the counter module

from counter import Counter

tally = Counter()
tally.reset()
#tally.setLimit(2)
tally.click()
tally.click

result = tally.getValue()
print("Value", result)

tally.click()
result = tally.getValue()
print("Value", result)