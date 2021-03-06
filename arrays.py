"""
1) Implement merge-sort.
	ex: mergesort([5, 1, 3]) -> [1, 3, 5]
	Efficiency: O(nlogn)
	Difficulty: 3
"""
def mergesort(ar):
	pass
#tests:
# assert mergesort([]) == sorted([])
# assert mergesort([1]) == sorted([1])
# assert mergesort([2, 1]) == sorted([2, 1])
# assert mergesort([3, 1, 2]) == sorted([3, 1, 2])
# assert mergesort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
# assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
# assert mergesort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
2) Implement quick-sort.
	ex: quicksort([5, 1, 3]) -> [1, 3, 5]
	Efficiency: O(nlogn)
	Difficulty: 3
"""
def quicksort(ar):
	pass
#tests:
# assert quicksort([]) == sorted([])
# assert quicksort([1]) == sorted([1])
# assert quicksort([2, 1]) == sorted([2, 1])
# assert quicksort([3, 1, 2]) == sorted([3, 1, 2])
# assert quicksort([4, 1, 3, 2]) == sorted([4, 1, 3, 2])
# assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0])
# assert quicksort([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10]) == sorted([3, 5, 4, 1, 7, 9, 8, 6, 2, 0, 10])


"""
3) Implement binary search (returns True or False).
	ex: binSearch([1, 3, 9], 9) -> True
	Efficiency: O(logn)
	Difficulty: 3 
"""
def binSearch(ar, val):
	pass
#tests:
# assert binSearch([1], 1) 
# assert binSearch([1, 3], 1)
# assert binSearch([1, 3], 3)
# assert binSearch([1, 3, 5], 1)
# assert binSearch([1, 3, 5], 3)
# assert binSearch([1, 3, 5], 5)
# assert not binSearch([], 1)
# assert not binSearch([1], 2)
# assert not binSearch([1], 0)
# assert not binSearch([1, 3], 2)
# assert not binSearch([1, 3], 0)
# assert not binSearch([1, 3], 4)
# assert not binSearch([1, 3, 5], 0)
# assert not binSearch([1, 3, 5], 2)
# assert not binSearch([1, 3, 5], 4)
# assert not binSearch([1, 3, 5], 6)


"""
4) Determine if 2 arrays are rotated versions of each other.
	ex: rotatedArray([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) -> True
	Efficiency: O(n^2)
	Difficulty: 4
"""
def rotatedArray(ar1, ar2):
	pass
#tests:
# assert rotatedArray([1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3])
# assert rotatedArray([1, 1, 1, 2, 1, 1, 2, 1, 2], [1, 2, 1, 1, 1, 2, 1, 1, 2])
# assert not rotatedArray([1, 1, 2, 1, 1, 2], [1, 2, 1, 2, 1, 1])
# assert not rotatedArray([1, 2, 3, 4, 6, 6], [6, 5, 6, 1, 2, 3])


"""
5) Find all permutations of a string
	ex: permutationsString("aab") -> ["aab", "aba", "baa"]
	Efficiency: O(n!)
	Difficulty: 4
"""
def permutationsString(str):
	pass
#tests:
# assert sorted(permutationsString('abc')) == sorted(['acb', 'abc', 'bca', 'cba', 'bac', 'cab'])
# assert sorted(permutationsString('aab')) == sorted(['aba', 'aab', 'baa'])
# assert permutationsString('aa') == ['aa']
# assert permutationsString('') == ['']


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
	pass
# Tests:
# assert setZeroesGrid([[1, 1, 0], [1, 1, 1], [1, 0, 1]]) == [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
# assert setZeroesGrid([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# assert setZeroesGrid([[0, 1, 1], [1, 1, 1], [1, 1, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# assert setZeroesGrid([[0, 1], [1, 1]]) == [[0, 0], [0, 1]]
# assert setZeroesGrid([[1, 1], [1, 1]]) == [[1, 1], [1, 1]]

"""
7) Remove duplicates in an array with O(1) buffer space (ie: don't create a new array)
	ex: removeDuplicates([1, 1, 2, 3, 1, 2, 4, 4, 1, 5]) -> [1, 2, 3, 4, 5]
	Efficiency: O(n^2)
	Difficulty: 5
"""
def removeDuplicates(ar):
    pass
#tests:
# assert removeDuplicates([]) == []
# assert removeDuplicates([1, 1, 2, 3, 1, 2, 4, 4, 1, 5]) == [1, 2, 3, 4, 5]
# assert removeDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
