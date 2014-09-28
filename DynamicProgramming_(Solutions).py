#-------------------------------------------------------------------------------
# Title: 		Dynamic Programming
# Author:      	Andy Baek
# Created:     	25-08-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	http://people.cs.clemson.edu/~bcdean/dp_practice/
#-------------------------------------------------------------------------------

"""
1) Maximum Sum Continuous SubSequence
	Given a sequence, find the maximum sum of a continuous (consecutive) subsequence
	Efficiency: O(n)
"""
def maxConsecutiveSum(ar):
	#result[i] = max sum ending at index i
	result = [-1 for i in range(len(ar))]
	result[0] = max(ar[0], 0)
	#result[i] = max(just i alone, result[i-1] + i)
	for i in range(1, len(ar)):
		result[i] = max(ar[i], result[i-1] + ar[i])
	#since the subsequence can end anywhere
	return max(result)
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
	#result[i] = max increasing subsequence ending on i
	result = [-1 for i in range(len(ar))]
	result[0] = 1
	#result[i] = max(for all result[j] where j < i)
	for i in range(1, len(ar)):
		curMax = 0
		for j in range(i):
			if ar[j] < ar[i] and result[j] > curMax:
				curMax = result[j]
		result[i] = curMax + 1
	return max(result)
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
	#result[i] = min coins needed for exact change i
	result = [-1 for i in range(target + 1)]
	result[0] = 0
	#loop through each value
	for val in range(1, target + 1):
		#loop through each coin
		for coin in range(len(coins)):
			#result[val] = min(result[val-coinValue] + 1) for all coins
			#must check that coin value is small enough to subtract
			if coins[coin] <= val and result[val-coins[coin]] != -1:
				#If unvisited before
				if result[val] == -1:
					result[val] = result[val-coins[coin]] + 1
				else:
					result[val] = min(result[val-coins[coin]] + 1, result[val])
	return result[target]
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
	#allBoxes = all rotations of boxes
    allBoxes = []
    for box in boxes:
        allBoxes.append((box))
        allBoxes.append((box[0], box[2], box[1]))
        allBoxes.append((box[1], box[2], box[0]))
        allBoxes.append((box[1], box[0], box[1]))
        allBoxes.append((box[2], box[1], box[0]))
        allBoxes.append((box[2], box[0], box[1]))
    #sort by (not strictly) increasing 2-D base
    allBoxes.sort(key=lambda x: (x[0], x[1]), reverse = True)
    #bestAtIndex[i] = best height stack with last box at index i
    bestAtIndex = [-1 for box in range(len(allBoxes))]
    #loop through boxes
    for i in range(len(allBoxes)):
        curMax = 0
        width = allBoxes[i][1]
        curLength = allBoxes[i][0]
        #loop through boxes before it
        for j in range(i):
            if allBoxes[j][0] == curLength:
                break
            elif allBoxes[j][1] > width:
                if bestAtIndex[j] > curMax:
                    curMax = bestAtIndex[j]
        #append height
        bestAtIndex[i] = curMax + allBoxes[i][2]
    return max(bestAtIndex)
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
	#northToSouthMap[i] = corresponding index of north city i in southern bank
    northToSouthMap = {}
    numCities = len(north)
    for i in range(numCities):
        currentCity = north[i]
        for j in range(numCities):
            if south[j] == currentCity:
                northToSouthMap[i] = j
                break
    #connections[i] = max bridges by connection city i in north and no more cities after i
    connections = [-1 for i in range(len(north))]
    #loop through north cities
    for i in range(len(north)):
        southConnect = northToSouthMap[i]
        curMax = 0
        #loop through north cities before i
        for j in range(i):
        	#corresponding south connection must be less than city i
            if northToSouthMap[j] < southConnect:
                if connections[j] > curMax:
                	#already built partial solution
                    curMax = connections[j]
        connections[i] = curMax + 1
    #last connection could be any city, therefore find max
    return max(connections)
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
	#result[i] = max value with max weight i
	result = [-1 for i in range(target+1)]
	result[0] = 0
	#loop through weights
	for curWeight in range(1, target + 1):
		result[curWeight] = result[curWeight-1]
		#per weight, loop through items
		for item in range(len(items)):
			if items[item][0] <= curWeight:
				result[curWeight] = max(result[curWeight], result[curWeight-items[item][0]] + items[item][1])
	return result[target]
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
	#result[i][j] = mac value with first i items and j max weight
	result = [[-1 for i in range(target+1)] for j in range(len(items))]
	#first row
	for i in range(target+1):
		result[0][i] = items[0][1] * (i/items[0][0])
	#rest of rows
	for i in range(1, len(items)):
		for j in range(target + 1):
			#if current item weight less than current max weight
			if items[i][0] <= j:
				result[i][j] = max(result[i-1][j], result[i-1][j-items[i][0]] + items[i][1])
			else:
				result[i][j] = result[i-1][j]
	#result
	return result[len(items)-1][target]
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
	total = sum(ar)
	#result[cap][sum] = 1 if exact sum is possible using subset of integers from 0 to cap
	result = [[-1 for i in range((total/2)+1)] for j in range(len(ar))] 
	#using only first element
	result[0] = [False for i in range((total/2)+1)]
	result[0][ar[0]] = True
	#loop through each element
	for cap in range(1, len(ar)):
		#loop through different curSums
		for curSum in range((total/2)+1):
			#works with cap-1 elements
			if (result[cap-1][curSum]):
				result[cap][curSum] = True
			#current element greater than current curSum or doesn't fit in
			elif ar[cap] > curSum or (not result[cap-1][curSum-ar[cap]]):
				result[cap][curSum] = False
			#current element usable
			else:
				result[cap][curSum] = True
	#return least difference between 2 sets
	for curSum in range(total/2, -1, -1):
		if result[len(ar)-1][curSum]:
			return ((total - curSum) - curSum)
#tests:
assert balancedPartition([9, 7, 3]) == 1

"""
9)
"""
def candies(scores):
    #if no kids, 0 candies
    if scores == []:
        return 0
    #result[i] = min candies given to student #i-1
    result = [-1 for i in range(len(scores))]
    result[0] = 1
    #lastBreak = last time when consecutive scores were equal (partition)
    lastBreak = 0
    for i in range(1, len(scores)):
    	#add one candy
        if scores[i] > scores[i-1]:
            result[i] = result[i-1] + 1
        #scores are same, add breakpoint
        elif scores[i] == scores[i-1]:
            result[i] = 1
            lastBreak = i
        else:
        	#decrement by 1 if possible
            if result[i-1] >= 2:
                result[i] = 1
            else:
            	result[i] = 0
                childIndex = i
                while (childIndex > lastBreak) and (result[childIndex-1] == result[childIndex] + 1):
                    result[childIndex] += 1
                    childIndex -= 1
                result[childIndex] += 1
    print scores
    print result
    return sum(result)


#[2, 4, 2, 6, 1, 7, 8, 9, 2, 1]


"""
10) Given an array of numbers and a sum, list all
	permutations of the numbers that sum to the
	given sum
"""
def sumPerms(ar, target):
	#table[num][val] = all permutations using first num numbers to make val
	table = [[[] for i in range(target+1)] for j in range(len(ar))]
	#set first row
	if ar[0] <= target:
		table[0][ar[0]].append([ar[0]])
	#set table[i][0] to [] for all i
	for i in range(len(ar)):
		table[i][0].append([])
	#loop through numbers in array
	for num in range(1, len(ar)):
		numVal = ar[num]
		#loop through all values up to target
		for val in range(target + 1):
			#take all permutations from row above
			table[num][val] = (table[num-1][val])[:]
			#if possible, add the new number as well
			if numVal <= val:
				for perm in table[num-1][val-numVal]:
					#make copy
					newPerm = perm[:]
					newPerm.append(numVal)
					table[num][val].append(newPerm)
	return table[len(ar)-1][target]

#tests:
# print sumPerms([0,1], 5)
assert len(sumPerms([0,1,2,3,5,6,7,11,12,14,20], 20)) == 26
