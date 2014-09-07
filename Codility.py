

# Find the longest increasing sequence in a grid where you can start and end
# anywhere and go right or down any spaces

def grid(A):
    numRows = len(A)
    numCols = len(A[0])
    #holds longest sequences ending at index (i, j)
    longest = [[-1 for i in range(numCols)] for j in range(numRows)]
    for row in range(numRows):
        for col in range(numCols):
            curVal = A[row][col]
            maxSequenceLength = 0
            for rowBefore in range(row+1):
                for colBefore in range(col+1):
                    if rowBefore == row and colBefore == col:
                        break
                    elif A[rowBefore][colBefore] < curVal and longest[rowBefore][colBefore] > maxSequenceLength:
                        maxSequenceLength = longest[rowBefore][colBefore]
            longest[row][col] = maxSequenceLength + 1
    largestSequenceLength = 0
    for line in range(numRows): print longest[line], A[line]
    for row in range(numRows):
        maxInRow = max(longest[row])
        if maxInRow > largestSequenceLength:
            largestSequenceLength = maxInRow
    return largestSequenceLength

#print grid([[7, -2, 0, 4, 2], [-1, 0, 1, 3, 1], [1, 2, 1, -1, 2], [4, 0, 0, -3, 0]])


# Find XOR from M to N
# Ex: Xor 5-8 = 5 XOR 6 XOR 7 XOR 8
# Use O(logn)

def XORProduct(M, N):
    product = M
    for i in range(M+1, N):
        product = product ^ i
    return product

#print XORProduct(3, 7)



# Given a graph of cities connected to each other, return an array
# with the shortest distance from each city to Ann Arbor

def AnnArbor(T):
    Ann = 0
    for i in range(len(T)):
        if i == T[i]:
            Ann = i
            break
    paths = {}
    newArray = []
    for i in range(len(T)-1):
        newArray.append(0)
    for i in range(len(T)):
        if i != Ann:
            distance = findDistance(T, i, paths, Ann) - 1
            newArray[distance] += 1
    return newArray

def findDistance(T, start, paths, Ann):
    if start == Ann:
        return 0
    else:
        if not (start in paths):
            paths[start] = 1 + findDistance(T, T[start], paths, Ann)
            return paths[start]
        else:
            return paths[start]

A = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
