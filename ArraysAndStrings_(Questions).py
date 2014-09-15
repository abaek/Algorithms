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
2) Implement quick-sort	
	Efficiency: O(nlogn)
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
3) Implement binary search
	#Efficiency: O(logn)
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
4) Determine if 2 arrays are rotated versions of each other
	Efficiency: O(n^2)
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
	Efficiency: O(n!)
"""
def permutationsString(str):
	pass
#tests:
# assert sorted(permutationsString('abc')) == sorted(['acb', 'abc', 'bca', 'cba', 'bac', 'cab'])
# assert sorted(permutationsString('aab')) == sorted(['aba', 'aab', 'baa'])
# assert permutationsString('aa') == ['aa']
# assert permutationsString('') == ['']


"""
6) Reverse the words in a setence with one buffer space
	Efficiency: O(n)
"""
def reverseSentence(sentence):
	pass
#tests:
# assert reverseSentence('hey how is it going everyone yo') == 'yo everyone going it is how hey'


"""
7) Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
	Efficiency: O(MxN)
"""
def setZeroesGrid(grid):
	pass
#tests:
# assert setZeroesGrid([[1, 1, 0], [1, 1, 1], [1, 0, 1]]) == [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
# assert setZeroesGrid([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# assert setZeroesGrid([[0, 1, 1], [1, 1, 1], [1, 1, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# assert setZeroesGrid([[0, 1], [1, 1]]) == [[0, 0], [0, 1]]
# assert setZeroesGrid([[1, 1], [1, 1]]) == [[1, 1], [1, 1]]

"""
8) Remove duplicates in a string with one buffer space
	Efficiency: O(n^2)
"""
def removeDuplicates(s):
    pass
#tests:
# assert removeDuplicates('abcbdaaefgahbhhbhbcefdfde') == 'abcdefgh'






