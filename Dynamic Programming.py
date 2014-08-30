#source: http://people.cs.clemson.edu/~bcdean/dp_practice/

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


def maxSequence(ar):
    paths = {}
    curPath = []
    max = helper(ar, None, 0, paths, curPath)
    print curPath
    print paths
    return max

def helper(ar, curEnd, index, paths, curPath):
    if len(ar) == index:
        return 0
    elif curEnd is None or ar[index] > curEnd:
        if not index in paths:
            newPath = curPath[:]
            newPath.append(ar[index])
            paths[index] = 1 + helper(ar, ar[index], index+1, paths, newPath)
        leaveItem = helper(ar, curEnd, index+1, paths)
        return max(leaveItem, paths[index])
    else:
        return helper(ar, curEnd, index+1, paths, curPath)


#print maxSequence([1, 10, 2, 8, 9, 3, 4, 5, 6, 7, 30, 2, 9, 11])
#print maxSequence([7, 30, 2, 9])

def maxSequence2(ar):
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

print maxSequence2([1, 10, 2, 8, 9, 3, 4, 5, 6, 7, 30, 2, 9, 11])


