#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     25-08-2014
# Copyright:   (c) Andy Baek 2014
# Questions:   http://people.cs.clemson.edu/~bcdean/dp_practice/
#-------------------------------------------------------------------------------

"""
1) Maximum Value Contiguous Subsequence
    Given a sequence of n real numbers A(1) ... A(n),
    determine a contiguous subsequence A(i) ... A(j)
    for which the sum of elements in the subsequence is maximized.
"""
def maxValueInSequence(ar):
    maxAtIndex = [-1 for i in range(len(ar))]
    if ar[0] > 0:
        maxAtIndex[0] = ar[0]
    else:
        maxAtIndex[0] = 0
    for i in range(1, len(ar)):
        maxAtIndex[i] = max(maxAtIndex[i-1] + ar[i], ar[i])
    return max(maxAtIndex)

#print maxValueInSequence([1, 5, -4, 3, 2, -9])

"""
2) Longest Increasing Subsequence
    Given a sequence of n real numbers A(1) ... A(n),
    determine a subsequence (not necessarily contiguous) of
    maximum length in which the values in the subsequence form
    a strictly increasing sequence.
"""
def maxIncSubsequence(ar):
    lastIndexOfLength = [-1 for i in range(len(ar)+1)]
    lastElemOfLength = [-1 for i in range(len(ar)+1)]
    parent = [-1 for i in range(len(ar))]
    lastIndexOfLength[1] = 0
    lastElemOfLength[1] = ar[0]
    maxLength = 1
    for i in range(1, len(ar)):
        curElem = ar[i]
        if curElem > ar[lastIndexOfLength[maxLength]]:
            parent[i] = lastIndexOfLength[maxLength]
            maxLength += 1
            lastIndexOfLength[maxLength] = i
            lastElemOfLength[maxLength] = ar[i]
        else:
            pos = indexJustGreater(curElem, lastElemOfLength, maxLength)
            parent[i] = lastIndexOfLength[pos-1]
            lastIndexOfLength[pos] = i
            lastElemOfLength[pos] = ar[i]
    longestIncSeq = []
    curIndex = lastIndexOfLength[maxLength]
    while curIndex != -1:
        longestIncSeq.append(ar[curIndex])
        curIndex = parent[curIndex]
    longestIncSeq = longestIncSeq[::-1]
    return maxLength, longestIncSeq

def indexJustGreater(val, ar, maxLength):
    maxPos = maxLength
    minPos = 1
    while maxPos > minPos:
        curPos = (maxPos + minPos) / 2
        if ar[curPos] == val:
            return curPos
            break
        elif ar[curPos] > val:
            maxPos = curPos
        else:
            minPos = curPos+1
    return maxPos

#O(n^2)
def maxSequence(ar):
    bestPath = {}
    for i in range(len(ar)):
        elem = ar[i]
        curMax = 0
        for j in range(i):
            if ar[j] < elem:
                if bestPath[j] > curMax:
                    curMax = bestPath[j]
        bestPath[i] = curMax + 1
    print bestPath
    return max(bestPath.values())

# print maxIncSubsequence([1, 10, 2, 8, 9, 3, 4, 5, 6, 7, 30, 2, 9, 11])
# print maxIncSubsequence([10, 11, 7, 56, 8, 9, 1, 2, 3, 4, 5, 30, 7, 0])
#print indexJustGreater(2, [-1, 1, 3, 5, 7, 9, 11, -1, -1, -1, -1], 6)

"""
3) Making Change
    You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all integers).
    Assume v(1) = 1, so you can always make change for any amount of money C. Give an algorithm
    which makes change for an amount of money C with as few coins as possible.
"""
def makingChange(coins, target):
    table = [[-1 for i in range(target+1)] for j in range(len(coins))]
    table[0] = [i for i in range(target+1)]
    for coin in range(1, len(coins)):
        currentCoinValue = coins[coin]
        for value in range(target+1):
            if value < currentCoinValue:
                table[coin][value] = table[coin-1][value]
            else:
                table[coin][value] = min(table[coin-1][value], table[coin][value-currentCoinValue]+1)
    for line in table: print line
    return table[len(coins)-1][target]

#print makingChange([1, 5, 10, 25, 100], 280)


"""
4) Box Stacking.
    You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i),
    width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes which is as tall as possible,
    but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each
    strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side
    functions as its base. It is also allowable to use multiple instances of the same type of box.
"""
#boxes = [(1, 2, 3), (6, 1, 8), (2, 3, 6), ... , (h, w, d)]
def boxStacking(boxes):
    allBoxes = []
    for box in boxes:
        allBoxes.append((box))
        allBoxes.append((box[0], box[2], box[1]))
        allBoxes.append((box[1], box[2], box[0]))
        allBoxes.append((box[1], box[0], box[1]))
        allBoxes.append((box[2], box[1], box[0]))
        allBoxes.append((box[2], box[0], box[1]))
    allBoxes.sort(key=lambda x: (x[0], x[1]), reverse = True)
    print allBoxes
    bestAtIndex = [-1 for box in range(len(allBoxes))]
    for i in range(len(allBoxes)):
        curMax = 0
        width = allBoxes[i][1]
        curLength = allBoxes[i][0]
        for j in range(i):
            if allBoxes[j][0] == curLength:
                break
            elif allBoxes[j][1] > width:
                if bestAtIndex[j] > curMax:
                    curMax = bestAtIndex[j]
        bestAtIndex[i] = curMax + allBoxes[i][2]
    print bestAtIndex
    return max(bestAtIndex)

#print boxStacking([(1,2,3), (5, 2, 7), (9, 1, 1)])

"""
5) Building Bridges.
    Consider a 2-D map with a horizontal river passing through its center.
    There are n cities on the southern bank with x-coordinates a(1) ... a(n) and n cities on the
    northern bank with x-coordinates b(1) ... b(n). You want to connect as many north-south pairs
    of cities as possible with bridges such that no two bridges cross. When connecting cities,
    you can only connect city i on the northern bank to city i on the southern bank.
"""
def bridges(north, south):
    northToSouthMap = {}
    numCities = len(north)
    for i in range(numCities):
        currentCity = north[i]
        for j in range(numCities):
            if south[j] == currentCity:
                northToSouthMap[i] = j
                break
    connections = [-1 for i in range(len(north))]
    for i in range(len(north)):
        southConnect = northToSouthMap[i]
        curMax = 0
        for j in range(i):
            if northToSouthMap[j] < southConnect:
                if connections[j] > curMax:
                    curMax = connections[j]
        connections[i] = curMax + 1
    print connections
    return max(connections)

#print bridges([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 9, 1, 10, 3, 2, 8, 7])


"""
6) Integer Knapsack Problem (with duplicates)
"""
#items = [(weight, value), (weight, value)]
def knapsack(capWeight, items):
    values = [[-1 for i in range(capWeight+1)] for j in range(len(items))]
    firstItemWeight = items[0][0]
    firstItemValue = items[0][1]
    curValue = 0
    values[0][0] = 0
    for weight in range(1, capWeight + 1):
        if weight % firstItemWeight == 0:
            curValue += firstItemValue
        values[0][weight] = curValue
    for item in range(1, len(items)):
        itemWeight = items[item][0]
        itemValue = items[item][1]
        for weight in range(1, capWeight+1):
            if weight < itemWeight:
                values[item][weight] = values[item-1][weight]
            else:
                values[item][weight] = max(values[item-1][weight], values[item][weight - itemWeight] + itemValue)
    for line in values: print line
    return values[len(items)-1][capWeight]

#print knapsack(39, [(10, 10), (5, 4), (2, 1)])


"""
7) Integer Knapsack Problem (no duplicates)
"""
def knapsackNoDup(capWeight, items):
    values = [[-1 for i in range(capWeight+1)] for j in range(len(items))]
    for weight in range(items[0][0]):
        values[0][weight] = 0
    for weight in range(items[0][0], capWeight+1):
        values[0][weight] = items[0][1]
    for item in range(1, len(items)):
        itemWeight = items[item][0]
        itemValue = items[item][1]
        for weight in range(1, capWeight+1):
            if weight < itemWeight:
                values[item][weight] = values[item-1][weight]
            else:
                values[item][weight] = max(values[item-1][weight], values[item-1][weight - itemWeight] + itemValue)
    for line in values: print line
    return values[len(items)-1][capWeight]

#print knapsackNoDup(39, [(20, 10), (15, 5), (7, 3), (12, 4)])

"""
8) Balanced Partition.
    You have a set of n integers each in the range 0 ... K. Partition these
    integers into two subsets such that you minimize |S1 - S2|, where S1 and
    S2 denote the sums of the elements in each of the two subsets.
"""
def balancedPartition(ar):
    total = sum(ar)
    half = total / 2
    sumPossible = [[-1 for i in range(half+1)] for j in range(len(ar))]
    sumPossible[0] = [0 for i in range(half+1)]
    sumPossible[0][0] = 1
    if ar[0] <= half:
        sumPossible[0][ar[0]] = 1
    for elem in range(1, len(ar)):
        curValue = ar[elem]
        sumPossible[elem][0] = 1
        for cursum in range(1, half+1):
            if cursum < curValue:
                sumPossible[elem][cursum] = sumPossible[elem-1][cursum]
            else:
                sumPossible[elem][cursum] = max(sumPossible[elem-1][cursum], sumPossible[elem-1][cursum-curValue])

    for line in sumPossible: print line

    for cursum in range(half, -1, -1):
        if sumPossible[len(ar)-1][cursum] == 1:
            return cursum, total-cursum
            break

print balancedPartition([9, 7, 3])




