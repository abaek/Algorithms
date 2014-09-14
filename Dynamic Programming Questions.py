#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     25-08-2014
# Copyright:   (c) Andy Baek 2014
# Questions:   http://people.cs.clemson.edu/~bcdean/dp_practice/
#-------------------------------------------------------------------------------

"""
1) Maximum Sum Continuous SubSequence
	Given a sequence, find the maximum sum of a continuous (consecutive) subsequence
	Efficiency: O(n)
"""
def maxConsecutiveSum(ar):
	pass
#tests:
assert maxConsecutiveSum([1, 5, -4, 3, 2, -9]) == 7
assert maxConsecutiveSum([1, 5, -6, 3, 2, -9]) == 6
assert maxConsecutiveSum([-1, 3, -1, 1, 5, -6, 3, 2, -9]) == 8
assert maxConsecutiveSum([-1, -1, 2, -1, 3]) == 4

"""
2) Maximum Increasing SubSequence (Discontinuous)
	Given a sequence, find the length of the longest increasing subsequence, 
	not necessarily consecutive terms.
	Efficiency: O(n^2) or O(nlogn)
"""
def incSubSeq(ar):
	pass
#tests:
assert incSubSeq([1, 10, 2, 8, 9, 3, 4, 5, 6, 7, 30, 2, 9, 11]) == 9
assert incSubSeq([10, 11, 7, 56, 8, 9, 1, 2, 3, 4, 5, 30, 7, 0]) == 6

"""
3) Change Making
	Given a list of coin denominations and an unlimited amount of each coin,
	find the minimum number of coins to make exact change for a target value
	Efficiency: O(n*m) n=#coins, m=change value
"""
def changeMaking(coins, target):
	pass
#tests:
assert changeMaking([1, 5, 10, 25, 100], 280) == 6
assert changeMaking([2, 99, 100], 198) == 2


"""
4) Box Stacking
	Given a list of 3-D boxes with dimensions (height, width, depth), determine
	the height of the tallest tower you can create by stacking boxes with the following constraints:
	- You can only stack a box if both of it's 2-D dimensions are strictly less than the box below it
	- You can rotate boxes in whichever way you like
	- You can use multiple instances of the same box.
	Efficiency: O(n^2)
"""
def boxStacking(boxes):
	pass
#tests:
assert boxStacking([(1,2,3), (5, 2, 7), (9, 1, 1)]) == 18

"""
5) Building Bridges
	Consider a 2-D map with a horizontal river passing through its center.
    There are n cities on the southern bank with corresponding pairs on the northern bank. 
    (ex: South: [1, 2, 3, 4, 5, 6], North: [5, 2, 3, 4, 6, 1])
    What is the maxmimum number of north-south pairs of cities you can connect such that
    such that no two bridges cross.
    Efficiency: O(n^2)
"""
def bridges(north, south):
	pass
#tests:
assert bridges([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 9, 1, 10, 3, 2, 8, 7]) == 5


"""
6) Knapsack With Duplicates
	Given a list of items each with a weight and value, mfind the maximum value you could
	hold in a backpack of a certain max weight.
	(ALLOWED DUPLICATE ITEMS)
	Efficiency: O(n^m) : n=#items, m=max weight
"""
def backpackWithDup(items, target):
	pass
#tests:
assert backpackWithDup([(20, 10), (15, 5), (7, 3), (12, 4)], 39) == 17
assert backpackWithDup([(10, 10), (5, 4), (2, 1)], 39) == 36
assert backpackWithDup([(10, 10), (9, 7), (7, 4)], 16) == 11
assert backpackWithDup([(10, 10), (9, 7), (7, 4), (1, 4)], 17) == 17*4


"""
7) Knapsack Without Duplicates
	Given a list of items each with a weight and value, mfind the maximum value you could
	hold in a backpack of a certain max weight.
	(NO DUPLICATE ITEMS)
	Efficiency: O(n*m) : n=#items, m=max weight
"""
def backpackNoDup(items, target):
	pass
#tests:
assert backpackNoDup([(20, 10), (15, 5), (7, 3), (12, 4)], 39) == 17
assert backpackNoDup([(10, 10), (9, 7), (7, 4)], 16) == 11
assert backpackNoDup([(10, 10), (9, 7), (7, 4), (1, 2)], 17) == 14
assert backpackNoDup([(10, 10), (9, 7), (7, 4), (1, 4)], 17) == 15

"""
8) Partition In Half
	Given a set of n positive integers, partition these integers into two subsets 
	such that you minimize |S1 - S2|, where S1 and S2 denote the sums of the elements 
	in each of the two subsets. Return |S1 - S2|.
	Efficiency: O(n^m) : n=# numbers, m=total sum
"""
def balancedPartition(ar):
	pass
#tests:
assert balancedPartition([9, 7, 3]) == 1


