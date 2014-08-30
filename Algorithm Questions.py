##General
#Find the most frequent integer in an array
def fn1(ar):
    numcount = {}
    maxnum = 0
    maxfreq = 0
    for num in ar:
        if num in numcount:
            numcount[num] += 1
        else:
            numcount[num] = 1
        if numcount[num] > maxfreq:
            maxfreq = numcount[num]
            maxnum = num
    return maxnum, maxfreq

#print fn1([1, 2, 3, 3, 3, 4, 3])

#Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
def fn2(ar):
    pairs = []
    singlesToFind = set()
    for num in ar:
        if num in singlesToFind:
            pairs.append((num, 10-num))
        else:
            singlesToFind.add(10-num)
    return pairs

#print fn2([1, 2, 3, 4, 5, 8, 9, 0, -10, 20])


#Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array.
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
def fn3(ar1, ar2):
    if len(ar1) != len(ar2):
        return False
    firstElem = ar1[0]
    for i in range(1, len(ar2)):
        if ar2[i] == firstElem:
            same = True
            ar2Pos = i
            for ar1Pos in range(len(ar2)):
                if ar1[ar1Pos] != ar2[ar2Pos]:
                    same = False
                    break
                ar2Pos += 1
                if ar2Pos >= len(ar2):
                    ar2Pos = 0
            if same:
                return True
    return False

# print fn3([1, 2, 3, 5, 6, 7, 8], [5, 6, 7, 8, 1, 2, 3])
# print fn3([1, 2, 3, 5, 6, 7, 8], [5, 6, 7, 8, 1, 4, 3])
# print fn3([1, 2, 1, 2, 1, 1], [1, 1, 1, 2, 1, 2])
# print fn3([1, 2, 1, 2, 1, 1], [1, 1, 1, 2, 1, 1])

#Write fibbonaci iteratively and recursively (bonus: use dynamic programming)
def fn4Iter(n):
    if n == 1 or n == 2:
        return 1
    prev1 = 1
    prev2 = 1
    for i in range(n-2):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp
    return prev2

def fn4Rec(n):
    visited = {}
    return fn4RecHelp(n, visited)

def fn4RecHelp(n, visited):
    if n == 1 or n == 2:
        return 1
    if n in visited:
        return visited[n]
    else:
        visited[n] = fn4RecHelp(n-1, visited) + fn4RecHelp(n-2, visited)
        return visited[n]

# print fn4Iter(100)
# print fn4Rec(100)


#Find the only element in an array that only occurs once.
def fn5(ar):
    visited = set()
    onlyOnce = set()
    for elem in ar:
        if elem in visited:
            if elem in onlyOnce:
                onlyOnce.remove(elem)
        else:
            visited.add(elem)
            onlyOnce.add(elem)
    return list(onlyOn4ce)[0]

# print fn5([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 6])


#Find the common elements of 2 int arrays
def fn6(ar1, ar2):
    set1 = set(ar1)
    set2 = set(ar2)
    common = list(set1 & set2)
    return common

# print fn6([1, 2, 3, 4, 5, 6, 7, 9], [1, 3, 5, 8, 9, 10])

#Implement binary search of a sorted array of integers
def fn7(ar, key):
    low = 0
    high = len(ar)-1
    if (key > ar[high] or key < ar[low]):
        return False
    while(True):
        if high == low:
            return key == ar[low]
        curIndex = (high+low)/2
        curElem = ar[curIndex]
        if curElem == key:
            return True
        elif key > curElem:
            low = curIndex+1
        else:
            high = curIndex


# for i in range(16):
#     print fn7([1, 3, 5, 7, 9, 11, 13, 15], i)

#Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
# def fn8(ar, key):
#     #find start
#     low = len(ar)/3
#     high = (len(ar)*2)/3
#     while True:
#         if ar[low] > ar[high]:
#
#     #do bin search
#     if key > ar[-1]:
#         return fn7(ar[:lowestPos])
#     else:
#         return fn7(ar[lowestPos:])

#Use dynamic programming to find the first X prime numbers
def fn9(i):
    primes = []
    numPrimes = 0
    if i == 1:
        return [2]
    curNum = 3
    while numPrimes < i:
        isPrime = True
        maxDivisor = curNum**0.5
        for prime in primes:
            if prime > maxDivisor:
                break
            if curNum % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(curNum)
            numPrimes += 1
        curNum += 2
    return primes

#print fn9(1000)

#Write a function that prints out the binary form of an int
def fn10(num):
    print bin(num)

#Implement parseInt
def fn11()

#Implement squareroot function

#Implement an exponent function (bonus: now try in log(n) time)

#Write a multiply function that multiples 2 integers without using *

#HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()

#HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)

##Strings
#Find the first non-repeated character in a String

#Reverse a String iteratively and recursively
#Determine if 2 Strings are anagrams

#Check if String is a palindrome

#Check if a String is composed of all unique characters

#Determine if a String is an int or a double

#HARD: Find the shortest palindrome in a String

#HARD: Print all permutations of a String

#HARD: Given a single-line text String and a maximum width value, write the function
# 'String justify(String text, int maxWidth)' that formats the input text using full-justification,
# i.e., extra spaces on each line are equally distributed between the words; the first word on each line
# is flushed left and the last word on each line is flushed right


##Trees
#Implement a BST with insert and delete functions

#Print a tree using BFS and DFS

#Write a function that determines if a tree is a BST

#Find the smallest element in a BST

#Find the 2nd largest number in a BST

#Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine
# whether the tree is a valid sum tree

#Find the distance between 2 nodes in a BST and a normal binary tree

#Print the coordinates of every node in a binary tree, where root is 0,0

#Print a tree by levels

#Given a binary tree which is a sum tree, write an algorithm to determine whether the tree is a valid sum tree

#Given a tree, verify that it contains a subtree.

#HARD: Find the max distance between 2 nodes in a BST.

#HARD: Construct a BST given the pre-order and in-order traversal Strings



##Stacks, Queues, and Heaps

#Implement a stack with push and pop functions

#Implement a queue with queue and dequeue functions

#Find the minimum element in a stack in O(1) time

#Write a function that sorts a stack (bonus: sort the stack in place without extra memory)

#Implement a binary min heap. Turn it into a binary max heap

#HARD: Implement a queue using 2 stacks



##Linked Lists

#Implement a linked list (with insert and delete functions)

#Find the Nth element in a linked list

#Remove the Nth element of a linked list

#Check if a linked list has cycles

#Given a circular linked list, find the node at the beginning of the loop.
# Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop

#Check whether a link list is a palindrome

#Reverse a linked list iteratively and recursively



##Sorting

#Implement bubble sort

#Implement selection sort

#Implement insertion sort

#Implement merge sort

#Implement quick sort
