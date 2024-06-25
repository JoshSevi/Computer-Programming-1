while True:
    user = input('enter username: ')

    try:
        user = float(user)
        print('INVALID')
        print()

    except ValueError:
        break

print(user)