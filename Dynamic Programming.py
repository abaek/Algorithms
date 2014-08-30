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

#print maxSequence([1, 10, 2, 8, 9, 3, 4, 5, 6, 7, 30, 2, 9, 11])

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