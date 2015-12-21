"""
1) Implement merge-sort.
	ex: mergesort([5, 1, 3]) -> [1, 3, 5]
	Efficiency: O(nlogn)
	Difficulty: 3
"""
def mergesort(ar):
	if len(ar) <= 1:
		return ar
	else:
		# Divide and recurse.
		ar1 = ar[:len(ar)/2]
		ar2 = ar[len(ar)/2:]
		ar1Sorted = mergesort(ar1)
		ar2Sorted = mergesort(ar2)

		# Merge.
		sortedAr = []
		curElem1 = 0
		curElem2 = 0
		maxElem1 = len(ar1Sorted)
		maxElem2 = len(ar2Sorted)
		while (True):
			# If one list is empty, append the rest of other list.
			if curElem1 == maxElem1:
				sortedAr.extend(ar2Sorted[curElem2:])
				break
			elif curElem2 == maxElem2:
				sortedAr.extend(ar1Sorted[curElem1:])
				break
			# Add lower element.
			elif ar1Sorted[curElem1] > ar2Sorted[curElem2]:
				sortedAr.append(ar2Sorted[curElem2])
				curElem2 += 1
			else:
				sortedAr.append(ar1Sorted[curElem1])
				curElem1 += 1
		return sortedAr
# Tests:
assert mergesort([]) == sorted([])
assert mergesort([1]) == sorted([1])
assert mergesort([2, 1]) == sorted([2, 1])
assert mergesort([3, 1, 2]) == sorted([3, 1, 2])
assert mergesort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
2) Implement quick-sort.
	ex: quicksort([5, 1, 3]) -> [1, 3, 5]
	Efficiency: O(nlogn)
	Difficulty: 3
"""
def quicksort(ar):
	if len(ar) <= 1:
		return ar
	else:
		# Pick pivot as first element.
		pivot = ar[0]
		lower = []
		higher = []
		# Loop through elements and place in lower or higher array
		for i in range(1, len(ar)):
			if ar[i] < pivot:
				lower.append(ar[i])
			else:
				higher.append(ar[i])
		# Recurse and merge.
		result = quicksort(lower)
		result.append(pivot)
		result.extend(quicksort(higher))
		return result
# Tests:
assert quicksort([]) == sorted([])
assert quicksort([1]) == sorted([1])
assert quicksort([2, 1]) == sorted([2, 1])
assert quicksort([3, 1, 2]) == sorted([3, 1, 2])
assert quicksort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
3) Implement binary search (returns True or False).
	ex: binSearch([1, 3, 9], 9) -> True
	Efficiency: O(logn)
	Difficulty: 3 
"""
def binSearch(ar, val):
	# low: lowest possible index
	# high: highest possible index + 1
	low = 0
	high = len(ar)
	while(True):
		# Round down.
		curElem = (low+high)/2
		# Not found.
		if low >= high:
			return False
		# Found.
		elif ar[curElem] == val:
			return True
		# Recurse right.
		elif ar[curElem] < val:
			low = curElem + 1
		# Recruse left.
		elif ar[curElem] > val:
			high = curElem
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
4) Determine if 2 arrays are rotated versions of each other.
	ex: rotatedArray([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) -> True
	Efficiency: O(n^2)
	Difficulty: 4
"""
def rotatedArray(ar1, ar2):
	if len(ar1) != len(ar2):
		return False
	# Try all starting positions in ar2.
	for i in range(len(ar2)):
		ar2Pos = i
		ar1Pos = 0
		# Go through all positions to make sure they match.
		while(ar1[ar1Pos] == ar2[ar2Pos]):
			ar1Pos += 1
			ar2Pos += 1
			# Finished.
			if ar1Pos == len(ar1):
				return True
			# Reached end of ar2, move to index 0.
			if (ar2Pos == len(ar2)):
				ar2Pos = 0
	return False
# Tests:
assert rotatedArray([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3])
assert rotatedArray([1, 1, 1, 2, 1, 1, 2, 1, 2], [1, 2, 1, 1, 1, 2, 1, 1, 2])
assert not rotatedArray([1, 1, 2, 1, 1, 2], [1, 2, 1, 2, 1, 1])
assert not rotatedArray([1, 2, 3, 4, 6, 6], [6, 5, 6, 1, 2, 3])


"""
5) Find all permutations of a string
	ex: permutationsString("aab") -> ["aab", "aba", "baa"]
	Efficiency: O(n!)
	Difficulty: 4
"""
def permutationsString(str):
	previousPerm = ['']
	# Add characters one by one.
	for curPos in range(len(str)):
		newPermutations = set()
		# Loop through all previous permutations and 
		# add the new char in all possible positions.
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
6) Given a 2d array of ints, return a 2d array where if an element in the original array is 0,
	then, its entire row and column become 0.
	ex: setZeroesGrid([[1, 1, 0],  		 [[0, 0, 0],
										 [1, 1, 1],   ->	[1, 1, 0],
										 [1, 1, 1]]) 	 		[1, 1, 0]]
	Efficiency: O(n^2)
	Difficulty: 4
"""
def setZeroesGrid(grid):
	#add rows anc columns with 0's
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
7) Remove duplicates in an array with one buffer space
	ex: removeDuplicates([1, 1, 2, 3, 1, 2, 4, 4, 1, 5]) -> [1, 2, 3, 4, 5]
	Efficiency: O(n^2)
	Difficulty: 5
"""
def removeDuplicates(ar):
	curIndex = 1
	while curIndex < len(ar):
		dup = False
		for j in range(curIndex):
			if ar[curIndex] == ar[j]:
				dup = True
				ar.pop(curIndex)
				break
		if not dup:
			curIndex += 1
	return ar
#tests:
assert removeDuplicates([1, 1, 2, 3, 1, 2, 4, 4, 1, 5]) == [1, 2, 3, 4, 5]

