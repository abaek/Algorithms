#source: http://codercareer.blogspot.ca/p/dynamic-interview-questions.html

#Maximum Sum of All Consecutive Sub-arrays
def maxSumSubArray(ar):
	lengthAr = len(ar)
	maxSumEndIndex = [-1 for i in range(lengthAr)]
	for i in range(lengthAr):
		if (ar[i] > maxSumEndIndex[i-1] + ar[i]):
			maxSumEndIndex[i] = ar[i]
		else:
			maxSumEndIndex[i] = maxSumEndIndex[i-1] + ar[i]
	return max(maxSumEndIndex)

#print maxSumSubArray([1, -2, 3, 10, -4, 7, 2, -5])


#Maximal Length of Incremental Subsequences
def maxIncreasingSubSequence(ar):
	lengthAr = len(ar)
	maxEndAtIndex = [-1 for i in range(lengthAr)]
	for i in range(lengthAr):
		maxLength = 0
		curNum = ar[i]
		for j in range(i):
			if curNum > ar[j] and maxEndAtIndex[j] > maxLength:
				maxLength = maxEndAtIndex[j]
		maxEndAtIndex[i] = maxLength + 1
	return max(maxEndAtIndex)


#Edit Distance
#Implement a function which gets the edit distance of two input strings.
#There are three types of edit operations: insertion, deletion and substitution.
#Edit distance is the minimal number of edit operations to modify a string from one to the other.




def coinProblem(ar, val):
	#stores min coins to make value i using first j coins (-1 if impossible)
	result = [[-1 for i in range(val+1)] for j in range(len(ar))]
	for i in range(len(ar)):
		result[i][0] = 0
	for i in range(1, val+1):
		if i % ar[0] == 0:
			result[0][i] = i/ar[0]
	for i in range(1, len(ar)):
		for j in range(1, val+1):
			if j < ar[i]:
				result[i][j] = result[i-1][j]
			elif result[i][j-ar[i]] != -1:
				if result[i-1][j] == -1:
					result[i][j] = result[i][j-ar[i]] + 1
				else:
					result[i][j] = min(result[i-1][j], result[i][j-ar[i]] + 1)
			else:
				result[i][j] = result[i-1][j]
	for line in result: print line
	return result[len(ar)-1][val]


def coinProblem2(ar, val):
	#result[C] = min coins needed for #C or False if impossible
	result = [-1 for i in range(val+1)]
	result[0] = 0
	for i in range(val+1):
		for coin in ar:
			if i >= coin and result[i-coin] != -1:
				if result[i] == -1:
					result[i] = result[i-coin] + 1
				else:
					result[i] = min(result[i-coin]+1, result[i])
	print result
	return result[val]


#backpack no repetition
#items = [(weight, value), ...]
def backpack(items, weight):
	#stores max value with max weight i
	result = [[-1 for i in range(weight+1)] for j in range(len(items))]
	#initialize first row with only item 1
	for i in range(weight+1):
		if i >= items[0][0]:
			result[0][i] = items[0][1]
		else:
			result[0][i] = 0
	#recurse through adding 1 more item, take max(include item, don't include item)
	for i in range(1, len(items)):
		for curWeight in range(weight+1):
			if curWeight >= items[i][0]:
				result[i][curWeight] = max(result[i-1][curWeight-items[i][0]] + items[i][1], result[i-1][curWeight])
			else:
				result[i][curWeight] = result[i-1][curWeight]
	for line in result: print line
	return result[len(items)-1][weight]


