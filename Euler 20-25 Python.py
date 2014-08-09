#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andy
#
# Created:     19-01-2014
# Copyright:   (c) Andy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


#Euler 20
#Calculates the sum of the digits in the number 100!

def prob20():
    product = 1
    sum = 0

    for i in range(1, 101):
        product *= i

    for x in range(0, len(str(product))):
        sum += int(str(product)[x])

    return sum


#Euler 21
#Evaluates the sum of all amicable numbers under 10000

def prob21():
    amicable = []

    for i in range(2, 10000):
        if i == sum(factors(sum(factors(i)))) and not(i == sum(factors(i))):
            amicable.append(i)

    return sum(amicable)

def factors(x):
    factors = []
    for i in range(1, x/2 + 1):
        if x%i == 0:
            factors.append(i)
    return factors


#Euler 22
#Sorts 5000 names lexographically then adds their values

def prob22():
    names = open("C:\Users\Andy\Documents\\1A\Programming\prob22.txt", "r")
    for line in names:
        lonames = line.split(",")
    listofNames= [name[1:len(name)-1] for name in lonames]

    points = scoreDictionary()
    sortedNames = []

    sortedNames = mergesort(listofNames) #choose sort here

    sum = 0
    for i in range(len(sortedNames)):
        sum += (scoreWord(sortedNames[i], points)*(i+1))

    return sum

def scoreDictionary():
    points = {}
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(26):
        points[alphabet[i]] = i+1
    return points

def scoreWord(word, points):
    sum = 0
    for i in list(word):
        sum += points[i]
    return sum


#Option 1: merge sort
def mergeNoRecurse(l1, l2):
    second = 0
    first = 0
    newlist = []
    while True:
        if second >= len(l2):
            newlist.extend(l1[first:])
            break
        elif first >= len(l1):
            newlist.extend(l2[second:])
            break
        elif l1[first]<l2[second]:
            newlist.append(l1[first])
            first += 1
        elif l1[first]>=l2[second]:
            newlist.append(l2[second])
            second += 1
    return newlist

def mergesort(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        return mergeNoRecurse(mergesort(lst[:len(lst)/2]), mergesort(lst[len(lst)/2:]))


#Option 2: quicksort
def choosePivot(lst):
    lower = []
    higher = []
    pivot = lst[0]
    for i in lst[1:]:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)
    newlist = quicksort(lower)
    newlist.append(pivot)
    newlist.extend(quicksort(higher))
    return newlist

def quicksort(lst):
    if not lst:
        return []
    else:
        newlist = choosePivot(lst)
        return newlist


#Euler 23
#Returns the sum of all integers which cannot be written as a sum of two abundant numbers
#Problem!

def prob23():
    loa = listAbundant()
    sums = set([])
    for elem1 in loa:
        for elem2 in loa:
            curSum = elem1 + elem2
            if curSum < 28124:
                sums.add(curSum)
    total = (1 +28123)*(28123/2) - sum(sums) #arithmetic series
    return total

def propDiv(x):
    Div = []
    for i in range(1, x/2 + 1):
        if x%i == 0:
            Div.append(i)
    return Div

def abundant(x):
    if sum(propDiv(x)) > x:
        return True
    else:
        return False

def listAbundant():
    loa = []
    for i in range(1, 28124):
        if abundant(i):
            loa.append(i)
    return loa


#Euler 24:
#Returns the millionth permutation of the digits {0...9}

def prob24():
    listofperm = []
    Digitfn(10, range(10), 0, listofperm)
    return listofperm[999999]

def Digitfn(pos, curSet, summ, listofperm):
    if pos == 1:
        num = curSet[0]
        summ += num
        listofperm.append(summ)
        summ -= num
    else:
        for a in range(pos):
            num = curSet[a]
            set2 = curSet[:]
            set2.pop(a)
            #Adds then substracts itself after all possibilities
            summ += num*(10**(pos-1))
            Digitfn(pos - 1, set2, summ, listofperm)
            summ -= num*(10**(pos-1))


#Euler 25
#Returns the first term in the Fibonacci sequence to contain 1000 digits
def prob25():
    i = 1
    while len(str(Fib(i)))<1000:
        i+=1
    return i

def Fib(termNum):
    term1, term2 = 1, 1
    termNum -= 2
    while termNum > 0:
        term3 = term1 + term2
        term1 = term2
        term2 = term3
        termNum -=1
    return term2