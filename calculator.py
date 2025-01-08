import math
def binary_calculator(bin1, bin2, operator):
    bit_length = []
    bin1_number = 0
    int_bin1 = int(bin1[::-1])
    x = len(bin1)
    for y in range(0, x):
        bit_length.append(2**y)
    for index in bin1:
        index = int(index)
        #print(int(bin1[index]))
        bin1_number += ((bit_length[index])*(int(bin1[index])))
        #print(bin1_number)
    #print(bit_length)
    #print(int_bin1)
    #print(bin1_number)
    #print(bin1[])
print(binary_calculator("00000000000000000000000001", "00000010", "+"))

