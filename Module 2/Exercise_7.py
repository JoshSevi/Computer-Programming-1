# Decimal to Octal and Octal to Decimal Converter

# Choice If-Else Code Block

choice = str("")

while choice != str("END"):
    print("To select between the Decimal to Octal or Octal to Decimal Converter...")
    print("Input A for Decimal to Octal")
    print("Input B for Octal to Decimal")
    print("Input END to exit the program")
    choice = input("Select Converter: ")

    if choice == str("A"):
        print("-----------------------------------")
        print("Decimal to Octal Converter Selected")
        print("-----------------------------------")

        # Decimal to Octal While Code Block

        decimal_input = int(input("Enter a decimal integer: "))

        if decimal_input == 0:
            print("The octal representation is:", decimal_input)
            print("----------------------------")

        else:
            print("Quotient Remainder Octal")
        
        octal_string = " "
        
        while decimal_input > 0:
            remainder = decimal_input % 8
            decimal_input = decimal_input // 8
            octal_string = str(remainder) + octal_string
            print("%5d%8d%12s" % (decimal_input, remainder, octal_string))
            print("The octal representation is:", octal_string)
            print("----------------------------")

    elif choice == str("B"):
        print("Octal to Decimal Converter Selected")
        
        # Octal to Decimal While Code Block

        octal_string_input = input("Enter a string of octal digits: ")
        decimal_output = 0
        exponent = len(octal_string_input) - 1

        for digit in octal_string_input:
            decimal_output = decimal_output + int(digit) * 8 ** exponent
            exponent = exponent - 1
        print("The decimal value is", decimal_output)
        print("--------------------")

    elif choice == str("END"):
        print("-------------------")
        print("Program terminated.")
        break

    else:
        print("-----------------------------")
        print("Selection invalid, try again")
        print("-----------------------------")