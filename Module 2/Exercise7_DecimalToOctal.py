print("Decimal to Octal Converter")
decimal = int(input("Enter a decimal integer: "))

print("Quotient Remainder Octal")
octal = " "
while decimal > 0:
    remainder = decimal % 8
    decimal = decimal // 8
    octal = str(remainder) + octal
    print("%5d%8d%12s" % (decimal, remainder, octal))

print("The octal representation is", octal)
