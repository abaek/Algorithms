"""
1) Do binary addition (with 32 bit positive integers)
	ex: bitAdd(1, 13) -> 14
	Efficiency: O(n)
	Difficulty: 4
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
