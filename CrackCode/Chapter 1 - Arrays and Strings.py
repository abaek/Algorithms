#def 1.0 implement a hash map
def fn1(ar):
    hashMap = {}
    for i in ar:
        val = hashfn(i)
        if val in hashMap:
            hashMap[val].append(i)
        else:
            hashMap[val] = [i]
    return hashMap

#1.1 Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
def fn2(string):
    set1 = set()
    for i in string:
        if i in set1:
            return false
            break
        else:
            set1.add(i)
    return true

#1.2 Write code to reverse a C-Style String. (C-String means that ?abcd? is represented as five characters, including the null character.)
def fn3(CString):
    #turns a string into an array or characters
    li =[]
    li.extend(CString)
    lastPos = len(li)-2
    for i in range((lastPos+1)/2):
        temp = li[i]
        li[i] = li[lastPos-i]
        li[lastPos-i] = temp
    #back into string
    return ''.join(li)

#1.3 Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
#NOTE: One or two additional variables are fine. An extra copy of the array is not.
#Write the test cases for this method.
def fn4(s):
    li =[]
    li.extend(s)
    tail = 1
    for i in range(1, len(li)):
        val = li[i]
        dup = False
        for j in range(tail):
            if val == li[j]:
                dup = True
                break
        if not dup:
            li[tail] = val
            tail += 1
    li2 = li[:tail]
    return ''.join(li2)

#1.4 Write a method to decide if two strings are anagrams or not.
def fn5(str1, str2):
    a = sorted(str1)
    b = sorted(str2)
    if (a == b):
        return True
    else:
        return False

#1.5 Write a method to replace all spaces in a string with ?%20?.
def fn6(str1):
    li = []
    li.extend(str1)
    newString = ''
    for i in li:
        if i == ' ':
            newString += '%20'
        else:
            newString += i
    return ''.join(newString)

#1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def fn7(image):
    numRings = len(image)/2
    end = len(image)-1
    for i in range(numRings):
        TL = i, i
        TR = i, end - i
        BL = end - i, i
        BR = end - i, end - i
        for j in range(len(image)-2*numRings):
            pos1 = TL[0], TL[1]+j
            pos2 = TR[0] + j, TR[1]
            pos3 = BR[0], BR[1] - j
            pos4 = BL[0]-j, BL[1]
        #... you get the idea

#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
def fn8(grid):
    notZeroCol = range(len(grid[0]))
    zeroRow = set()
    for row in range(len(grid)):
        for col in notZeroCol:
            if grid[row][col] == 0:
                notZeroCol.pop(col)
                zeroRow.add(row)
    lenRow = len(grid[0])
    lenCol = len(grid)
    for row in zeroRow:
        for i in range(lenCol):
            grid[row][i] = 0

    zeroCol = range(len(grid[0]))
    zeroCol = list(set(zeroCol) - set(notZeroCol))
    for col in zeroCol:
        for i in range(lenRow):
            grid[i][col] = 0
    return grid


#1.8 Assume you have a method isSubstring which checks if one word is a substring of another.
#Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., ?waterbottle? is a rotation of ?erbottlewat?).
def fn9(s1, s2):
    if len(s1) != len(s2):
        return False
    elif s1 == s2:
        return True
    else:
        endPos = len(s1)
        for i in range(1, endPos+1):
            if (not isSubstring(s1[0: i], s2)):
                if (isSubstring(s1[0:i-1], s2) and isSubstring(s1[i-1: endPos], s2)):
                    return True
                else:
                    return False
                break

#BETTER: concatenate s1 with itself and check for substring
def fn9b(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        news1 = s1+s1
        if (isSubstring(s2, news1)):
            return True
        else:
            return False

def isSubstring(s1, s2):
    if s1 in s2:
        return True
    else:
        return False










