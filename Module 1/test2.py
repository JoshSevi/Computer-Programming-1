def get_integer_input(prompt):
    while True:
        try:
            username = str(input("Enter username: "))
            # Just return directly. No need for an invalid_input flag.
            return int(input(prompt))
        except ValueError:
            print('Invalid input, please enter a number')

# Where you see repetition in your code, consider using a data structure to
# address it. There are libraries that will give you the ordinals. Personally,
# I would just rephrase the input() prompt so that the ordinals are not needed.
ORDINALS = ('age', 'first', 'second')

# Get the integers.
fmt = 'Enter the {} number: '
a, b, c = [get_integer_input(fmt.format(o)) for o in ORDINALS]
print(a)
print(b * c)

# Or if you care only about the total, just get it directly.
#tot = sum(get_integer_input(fmt.format(o)) for o in ORDINALS)
#print(tot)