#source: http://codercareer.blogspot.ca/p/dynamic-interview-questions.html

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

def hi(n):
	return n