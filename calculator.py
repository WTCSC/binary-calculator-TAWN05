import math
def binary_calculator(bin1, bin2, operator):
    # The list of bits used to converte the bit number to decimal and decimal to bit
    bit_length = []

    # The decimal numbers used to do the math functions
    bin1_number = 0
    bin2_number = 0

    # Used to get the decimal number
    bin1 = (bin1[::-1])
    bin2 = (bin2[::-1])

    # The final solution in binary
    bin_solution = []

    # Temp var for decimal convertion
    i = 0

    # Finds the larger bit number for the varable bit_length so if one bit is 8 bit and the other is 10 bit_length will do 10 bit
    if len(bin1) >= len(bin2):
        max_bin_length = len(bin1)
    else:
        max_bin_length = len(bin2)
    
    # Debug
    #print(max_bin_length)

    # Makes the bit length based on the largest bin number
    for y in range(0, max_bin_length):
        bit_length.append(2**y)

    # Turns bin1 into a decimal number
    for index in bin1:

        if not all(char in '01' for char in bin1):
            return "Error"
        
        index = int(index)
        bin1_number += (index*(bit_length[i]))
        i += 1

    i = 0

    # Turn bin2 into a decimal number
    for index in bin2:

        if not all(char in '01' for char in bin2):
            return "Error"
        
        index = int(index)
        bin2_number += (index*(bit_length[i]))
        i += 1

    # All of the math operations for adding subtracting etc...
    if operator == "+":
        solution = (bin1_number + bin2_number)
    if operator == "-":
        solution = (bin1_number - bin2_number)
    if operator == "*":
        solution = (bin1_number * bin2_number)
    if operator == "/":
        if bin2_number == 0:
            return "NaN"
        solution = (bin1_number // bin2_number)

    # Switches the bit length so that the decimal number can be converted back to binary
    bit_length = (bit_length[::-1])


    #print(solution)


    #  COOL STUFF FOR MAX BIT CALCULATION!!!
    """
    # X is a temp var for making sure bit_length is capible of displaying the solution number
    x = bit_length[0]

    # If the solution can be divided more than once bit_length is not long enought to display the solution number
    if (solution / x) >= 2:
        # Creates a infinte loop to make sure the bit_length number is long enough
        False
        while True:
            if (solution / x) <= 2:
                # If the largest number in bit_length cannot be divided twice in solution number than bit_length is long enough then break
                break
            else:
                # Switchs the bit_length back to counting up order so another value can be added in order
                bit_length = bit_length[::-1]

                # Takes the max_bin_length number and adds the next power of 2 to the bit_length list
                bit_length.append(2**max_bin_length)

                # Switchs bit_length back to decimal to bit number
                bit_length = bit_length[::-1]

                # Sets x for the soultion / x check to see if bit_length is long enough
                x = bit_length[0]
                # Adds to max_bin_length if bit_length is still not big enough
                max_bin_length += 1

"""

    if solution > 255 or solution < 0:
        return "Overflow"

    # For each number in bit_length
    for x in bit_length:

        # Checks to see if this number is small enough to be expressed by this bit (if code above worked, this should be always true for the first bit)
        if (solution / x) >= 1:

            # Appends a 1 to the solution
            bin_solution.append("1")

            # Subtracts this bit total so that lesser bits can describe to remainder
            solution = (solution - x)
        else:
            # If the bit is to big than append 0
            bin_solution.append("0")
    
    return "".join(bin_solution)

#print(binary_calculator("00000100", "00000001", "+"))

