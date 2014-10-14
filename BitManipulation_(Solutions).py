#-------------------------------------------------------------------------------
# Title: 		Bit Manipulation
# Author:      	Andy Baek
# Created:     	12-09-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	Cracking the Coding Interview (Gayle Laakmann)
#-------------------------------------------------------------------------------

"""
1) Do binary addition (with only positive integers)
"""
def bitAdd(num1, num2):
	carry = 0
	result = 0
	for i in range(32):
		curPos = 2**i
		#sum = 0, 1, 2, or 3
		sum = ((curPos & num1) >> i) + ((curPos & num2) >> i) + carry
		if sum >= 2:
			carry = 1
		else:
			carry = 0
		if sum % 2 == 1:
			result += curPos
	return result
#tests:
assert bitAdd(1, 1) == 2
assert bitAdd(1, 13) == 14
assert bitAdd(34, 324) == 358
assert bitAdd(23, 0) == 23

"""
2) Given a and b, Find You should find the following sum modulo 10^9+7:
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





