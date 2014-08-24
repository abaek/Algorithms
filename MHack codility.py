def solution(T):
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
