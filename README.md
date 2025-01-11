[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17650685)

# Binary Calculator

this Binary Calculator is a Python utility that performs simple operations on binary numbers. This tool uses addition, subtraction, multiplication, and division, enabling binary calculations with variable handling of binary inputs and outputs.
Features

    Binary Arithmetic: Performs calculations like addition, subtraction, multiplication, and division.
    Error Handling: Finds and reports invalid binary inputs or division by zero.
    Overflow Detection: Returns an "Overflow" message if results exceed the allowable range of an 8-bit binary number unless the variable binary handler is enabled.
    Bit Length Adaptation: Automatically adjusts calculations to display the larger of the two input binary lengths.

## Usage and Function Overview

binary_calculator(bin1, bin2, operator)

    Parameters:
        bin1 (str): First binary number as a string.
        bin2 (str): Second binary number as a string.
        operator (str): Operation to perform ("+", "-", "*", or "/").

    Returns:
        Binary result of the operation or an error message ("Error", "Overflow", or "NaN" for invalid operations).

Example Usage

## Addition
result = binary_calculator("00000100", "00000001", "+")
print(result)  # Output: 00000101

## Subtraction
result = binary_calculator("00001000", "00000100", "-")
print(result)  # Output: 00000100

## Multiplication
result = binary_calculator("00000110", "00000010", "*")
print(result)  # Output: 00001100

## Division
result = binary_calculator("00001000", "00000010", "/")
print(result)  # Output: 00000100

## Implementation Details
### Binary to Decimal Conversion

The calculator converts binary inputs into decimal numbers by iterating through each bit and summing the values based on their position.
Arithmetic Operations

After conversion, the arithmetic operation is performed on the decimal numbers.
Decimal to Binary Conversion

Once the operation is complete, the result is converted back into binary by iterating through descending powers of 2.
Error and Overflow Handling

    Invalid Input: Returns "Error" if a non-binary input is provided.
    Division by Zero: Returns "NaN" for division operations involving zero as the second operand.
    Overflow: If the result exceeds 8 bits (greater than 255 or less than 0), the function returns "Overflow".