#-------------------------------------------------------------------------------
# Title: 		Bit Manipulation
# Author:      	Andy Baek
# Created:     	12-09-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	Cracking the Coding Interview (Gayle Laakmann)
#-------------------------------------------------------------------------------

"""
1) Do binary addition
"""
def binAdd(num1, num2):
	return bin(int(num1, 2) + int(num2, 2))
#tests:
assert binAdd('010', '1011') == bin(13)


"""
2) Convert from base n to base m
"""
def convertBase(num, base1, base2):
	base10Num = int(num, base1)
	result = ''
	while base10Num != 0:
		result = str(base10Num % base2) + result
		base10Num /= base2
	return result
#tests:
assert convertBase('101', 2, 3) == '12'
assert convertBase('12', 3, 2) == '101'

"""
3) Given a and b, Find You should find the following sum modulo 10^9+7:
	Summation of (a xor (b shl i)) from i= 0 to 314159 (inclusive)
	where shl = shift left
"""
def shiftSummation(num1, num2):
    a = int(num1, 2)
    b = int(num2, 2)
    result = 0
    mod = ((10**9)+7)
    for i in range(314160):
        result += (a ^ (b << i))
    return result % mod






