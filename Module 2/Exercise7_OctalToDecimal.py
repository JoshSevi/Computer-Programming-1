print("Octal to Decimal Converter")
octal = input("Enter a string of octal digits: ")

decimal = 0
exponent = len(octal) - 1
for digit in octal:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1

print("The integer value is", decimal)
