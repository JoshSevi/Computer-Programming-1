username = input("Enter username: ")


def get_input_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Invalid input, please enter a whole number.')


age = get_input_number('Enter age: ')

ORDINALS = ('first', 'second')
tmf = 'Enter the {} number: '
a, b = [get_input_number(tmf.format(i)) for i in ORDINALS]

print("The username is", username, "and the age is", age)
print('The product is', a * b)

# Trip ko lang po hehe
