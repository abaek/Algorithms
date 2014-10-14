#-------------------------------------------------------------------------------
# Title: 		Arrays and Strings
# Author:      	Andy Baek
# Created:     	12-09-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	Cracking the Coding Interview (Gayle Laakmann)
#-------------------------------------------------------------------------------

"""
1) Implement merge-sort
	Efficiency: O(nlogn)
"""
def mergesort(ar):
	if len(ar) <= 1:
		return ar
	else:
		#split in half and recurse
		ar1 = ar[:len(ar)/2]
		ar2 = ar[len(ar)/2:]
		ar1Sorted = mergesort(ar1)
		ar2Sorted = mergesort(ar2)
		#merge new sorted Array
		sortedAr = []
		curElem1 = 0
		curElem2 = 0
		maxElem1 = len(ar1Sorted)
		maxElem2 = len(ar2Sorted)
		while (True):
			#if either list ifs empty
			if curElem1 == maxElem1:
				sortedAr.extend(ar2Sorted[curElem2:])
				break
			elif curElem2 == maxElem2:
				sortedAr.extend(ar1Sorted[curElem1:])
				break
			#append lower element and continue
			elif ar1Sorted[curElem1] > ar2Sorted[curElem2]:
				sortedAr.append(ar2Sorted[curElem2])
				curElem2 += 1
			else:
				sortedAr.append(ar1Sorted[curElem1])
				curElem1 += 1
		return sortedAr
#tests:
assert mergesort([]) == sorted([])
assert mergesort([1]) == sorted([1])
assert mergesort([2, 1]) == sorted([2, 1])
assert mergesort([3, 1, 2]) == sorted([3, 1, 2])
assert mergesort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
2) Implement quick-sort	
	Efficiency: O(nlogn)
"""
def quicksort(ar):
	if len(ar) <= 1:
		return ar
	else:
		#pick pivot
		pivot = ar[0]
		lower = []
		higher = []
		#loop through elements and place in lower or hiher array
		for i in range(1, len(ar)):
			if ar[i] < pivot:
				lower.append(ar[i])
			else:
				higher.append(ar[i])
		#recurse and merge
		result = quicksort(lower)
		result.append(pivot)
		result.extend(quicksort(higher))
		return result
#tests:
assert quicksort([]) == sorted([])
assert quicksort([1]) == sorted([1])
assert quicksort([2, 1]) == sorted([2, 1])
assert quicksort([3, 1, 2]) == sorted([3, 1, 2])
assert quicksort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
3) Implement binary search
	#Efficiency: O(logn)
"""
def binSearch(ar, val):
	low = 0
	high = len(ar)
	curElem = (low+high)/2
	#start in middle and loop until high==low or found
	while(True):
		#not found
		if low == high:
			return False
		#found
		elif ar[curElem] == val:
			return True
		#recurse
		elif ar[curElem] < val:
			low = curElem + 1
			curElem = (low+high)/2
		elif ar[curElem] > val:
			high = curElem
			curElem = (low+high)/2
#tests:
assert binSearch([1], 1) 
assert binSearch([1, 3], 1)
assert binSearch([1, 3], 3)
assert binSearch([1, 3, 5], 1)
assert binSearch([1, 3, 5], 3)
assert binSearch([1, 3, 5], 5)
assert not binSearch([], 1)
assert not binSearch([1], 2)
assert not binSearch([1], 0)
assert not binSearch([1, 3], 2)
assert not binSearch([1, 3], 0)
assert not binSearch([1, 3], 4)
assert not binSearch([1, 3, 5], 0)
assert not binSearch([1, 3, 5], 2)
assert not binSearch([1, 3, 5], 4)
assert not binSearch([1, 3, 5], 6)


"""
4) Determine if 2 arrays are rotated versions of each other
	Efficiency: O(n^2)
"""
def rotatedArray(ar1, ar2):
	if len(ar1) != len(ar2):
		return False
	#try all starting positions in ar2
	for i in range(len(ar2)):
		ar2Pos = i
		ar1Pos = 0
		#go through all positions to make sure they match
		while(ar1[ar1Pos] == ar2[ar2Pos]):
			ar1Pos += 1
			ar2Pos += 1
			#finished
			if ar1Pos == len(ar1):
				return True
			#reached end of ar2
			if (ar2Pos == len(ar2)):
				ar2Pos = 0
	return False
#tests:
assert rotatedArray([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3])
assert rotatedArray([1, 1, 1, 2, 1, 1, 2, 1, 2], [1, 2, 1, 1, 1, 2, 1, 1, 2])
assert not rotatedArray([1, 1, 2, 1, 1, 2], [1, 2, 1, 2, 1, 1])
assert not rotatedArray([1, 2, 3, 4, 6, 6], [6, 5, 6, 1, 2, 3])


"""
5) Find all permutations of a string
	Efficiency: O(n!)
"""
def permutationsString(str):
	previousPerm = ['']
	#add characters one by one
	for curPos in range(len(str)):
		newPermutations = set()
		#loop through all permutations of one less length
		for perm in previousPerm:
			for pos in range(curPos+1):
				newPermutations.add(perm[:pos] + str[curPos] + perm[pos:])
		previousPerm = list(newPermutations)
	return previousPerm

#tests:
assert sorted(permutationsString('abc')) == sorted(['acb', 'abc', 'bca', 'cba', 'bac', 'cab'])
assert sorted(permutationsString('aab')) == sorted(['aba', 'aab', 'baa'])
assert permutationsString('aa') == ['aa']
assert permutationsString('') == ['']


"""
6) Reverse the words in a setence with one buffer space
	Efficiency: O(n)
"""
def reverseSentence(sentence):
	#reverse all characters in sentence
	sentenceLength = len(sentence)
	sentenceList = list(sentence)
	for i in range(sentenceLength/2):
		temp = sentenceList[i]
		sentenceList[i] = sentenceList[sentenceLength - i - 1]
		sentenceList[sentenceLength - i - 1] = temp
	startWord = 0
	#reverse each word
	for curChar in range(sentenceLength):
		if sentenceList[curChar] == ' ':
			endWord = curChar - 1
			for wordPos in range((endWord-startWord + 1)/2):
				temp = sentenceList[startWord + wordPos]
				sentenceList[startWord + wordPos] = sentenceList[endWord - wordPos]
				sentenceList[endWord - wordPos] = temp
			startWord = curChar + 1
	#reverse last word
	lastPos = sentenceLength - 1
	while True:
		if sentenceList[lastPos] == ' ':
			lastWordStart = lastPos + 1
			lastWordEnd = sentenceLength - 1
			for i in range((lastWordEnd - lastWordStart + 1)/2):
				temp = sentenceList[lastWordStart + i]
				sentenceList[lastWordStart + i] = sentenceList[lastWordEnd - i]
				sentenceList[lastWordEnd - i] = temp 
			break
		lastPos -= 1
	return ''.join(sentenceList)
#tests:
assert reverseSentence('hey how is it going everyone yo') == 'yo everyone going it is how hey'


"""
7) Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
	Efficiency: O(MxN)
"""
def setZeroesGrid(grid):
	#add rows anc columsn with 0's
    zeroCol = set()
    zeroRow = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                zeroCol.add(col)
                zeroRow.add(row)
    #set rows and columns with 0's
    for row in zeroRow:
        for i in range(len(grid)):
            grid[row][i] = 0
    for col in zeroCol:
        for i in range(len(grid[0])):
            grid[i][col] = 0
    return grid
#tests:
assert setZeroesGrid([[1, 1, 0], [1, 1, 1], [1, 0, 1]]) == [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
assert setZeroesGrid([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
assert setZeroesGrid([[0, 1, 1], [1, 1, 1], [1, 1, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert setZeroesGrid([[0, 1], [1, 1]]) == [[0, 0], [0, 1]]
assert setZeroesGrid([[1, 1], [1, 1]]) == [[1, 1], [1, 1]]

"""
8) Remove duplicates in a string with one buffer space
	Efficiency: O(n^2)
"""
def removeDuplicates(s):
    li =[]
    li.extend(s)
    tail = 1
    for i in range(1, len(li)):
        val = li[i]
        dup = False
        for j in range(tail):
            if val == li[j]:
                dup = True
                break
        if not dup:
            li[tail] = val
            tail += 1
    li2 = li[:tail]
    return ''.join(li2)
#tests:
assert removeDuplicates('abcbdaaefgahbhhbhbcefdfde') == 'abcdefgh'



"""
9) You are given a set of m strings all of length L (call this set s), and one string of length n (call this string str).
	(i.e. s = {'aaa', 'bbb', 'cac', 'cat'}, str = 'aaacatcacdddcataaabbbcaczzz'
	In this case, m = 4, L = 3, and n = 27)

	Find a contiguous permutation of all the words in s in a substring of str. 

	So in the example, the substring 'cataaabbbcac' of str is a continguous permutation of all the words in s. 
"""
def continguousString(listStr, str):
	L = len(listStr[0])
	m = len(listStr)
	n = len(str)
	setStrings = set()
	#add each listStr into set
	for i in range(m):
		setStrings.add(listStr[i])
	#keep track of longest length and longest string
	longestLength = 0
	longestString = ''
	#go through the long str L times
	for i in range(L):
		curLength = 0
		curString = ''
		#loop through every L'th position starting from i
		for j in range(i, (n-L), L):
			#check if substring in set
			if str[j:j+L] in setStrings:
				curLength += 1
				curString += str[j:(j+L)]
				#set new longest string
				if curLength > longestLength:
					longestLength = curLength
					longestString = curString
			else:
				curLength = 0
				curString = ''
	return longestString

#tests:
assert continguousString(['aaa', 'bbb', 'cac', 'cat'], 'aaacatcacdddcataaabbbcaczzz') == 'cataaabbbcac'






