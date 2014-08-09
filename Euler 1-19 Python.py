#Euler 1
#Returns the sum of all multiples of 3 or 5

def prob1():
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        sum += i
    for i in range(15, 1000, 15):
        sum -= i
    print sum


#Euler 4
#Returns the largest palindrome that is a product of two 3-digit integers

def prob4():
    largest = 0
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            product = num1*num2
            if product > largest and palindrome(product):
                largest = product
    return largest

def palindrome(x):
    origStr = str(x)
    reverseStr = ''.join(curChar for curChar in origStr[::-1])
    if int(reverseStr) == x:
        return True
    else:
        return False


#Euler 8
#Finds the largest product of 5 consecutive digits in the 1000 digit number

def prob8():
    numStr = convNumStr(open("C:\Users\Andy\Documents\\1A\Programming\prob8.txt", "r"))

    largest = 0
    for i in range(0, len(numStr)-4):
        current = int(numStr[i])*int(numStr[i+1])*int(numStr[i+2])*int(numStr[i+3])*int(numStr[i+4])
        if current > largest:
            largest = current
    return largest

#converts file containing number broken into lines into a single string
def convNumStr(file):
    lstNum = []
    numStr = ""
    for line in file:
        lstNum.append(line)
    #skips every \n in ever line except the last line
    lastLine = len(lstNum) -1
    for line in range(lastLine + 1):
        if line == lastLine:
            numStr += lstNum[line]
        else:
            numStr += lstNum[line][:-1]
    return numStr

#Euler 9
#Finds the Pythagorean triplet where a+b+c = 1000

def prob9():
    a = 1
    b = 2
    c = 997

    while not(a**2 + b**2 == c**2):
        if c > b:
            c -= 1
            b += 1
        else:
            a += 1
            b = a + 1
            c = 1000 - a - b
    return a*b*c


#Euler 11
#Returns the largest product of 4 adjacent numbers in a 20x20 grid (vertical, horizontal, diagonal)

def prob11():
    nestedli = convFile(open("C:\Users\Andy\Documents\\1A\Programming\prob11.txt", "r"))

    greatest = 0
    #checks rows
    for row in nestedli:
        curProduct = accross(row)
        if curProduct > greatest:
            greatest = curProduct

    #checks columns
    for pos in range(len(nestedli[0])):
        currentCol = [row[pos] for row in nestedli]
        curProduct = accross(currentCol)
        if  curProduct > greatest:
            greatest = curProduct

    #checks diagonals
    #top right triangle
    def topright(grid, greatest):
        for x in range(16):
            row = [grid[i][x+i] for i in range(20 - x)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest

    #top left triangle
    def topleft(grid, greatest):
        for x in range(3, 20):
            row = [grid[i][x-i] for i in range(x+1)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest

    greatest = topright(nestedli, greatest) #top right
    greatest = topleft(nestedli, greatest) #top left

    #reverse list vertically
    nestedli = nestedli[::-1]

    greatest = topright(nestedli, greatest) #bottom right
    greatest = topleft(nestedli, greatest) #bottom left

    return greatest


#convert file to nested list of numbers
def convFile(x):
    masterli = []
    for strline in x:
        numline = [int(a) for a in strline.split()]
        masterli.append(numline)
    return masterli

#Gets largest 4 consecutive number product in list
def accross(row):
    greatest = 0
    for x in range(len(row) - 3):
        product = 1
        for i in range(x, x+4):
            product *= row[i]
        if product > greatest:
            greatest = product
    return greatest



#Euler 13
#Returns the first 10 digits of a sum of 100 fifty digit numbers

def prob13():
    file = open("C:\Users\Andy\Documents\\1A\Programming\prob13.txt", "r")
    listNum = [line for line in file]
    #skips \n character in each line except last line
    filteredList = [listNum[lineNum][:-1] for lineNum in range(len(listNum) - 1)]
    filteredList.append(listNum[-1])
    sum = 0
    for num in filteredList:
        sum += int(num)
    return str(sum)[:10]


#Euler 14
#Returns the longest collatz sequence with starting term up to one million

#This version uses a set of all the visited terms
def prob14():
    visitedVal = set()
    longestSeq = 0
    startingNum = 0
    for term in range(999999, 0, -2):
        collatzLength = collatzlen(term, visitedVal)
        if collatzLength > longestSeq:
            longestSeq = collatzLength
            startingNum = term
    return startingNum

def collatzlen(x, setVisited):
    numTerms = 1
    curVal = x
    if x in setVisited:
        curVal = 1
    while not curVal == 1:
        if curVal%2 == 0:
            curVal /= 2
        else:
            curVal = curVal * 3 + 1
        numTerms += 1
        setVisited.add(curVal)
    return numTerms

#This verion does not have a set of visited terms
def prob14NoSet():
    longestSeq = 0
    startingNum = 0
    for term in range(999999, 0, -2):
        collatzLength = collatzlenNoSet(term)
        if collatzLength > longestSeq:
            longestSeq = collatzLength
            startingNum = term
    return startingNum

def collatzlenNoSet(x):
    numTerms = 1
    curVal = x
    while not curVal == 1:
        if curVal%2 == 0:
            curVal /= 2
        else:
            curVal = curVal * 3 + 1
        numTerms += 1
    return numTerms


#Euler 17
#Return the length of the numbers up to 1000 in words

def prob17():
    upTo9 = 3*3 + 4*3 + 5*3
    upTo19 = upTo9 + len('tenElevenTwelveThirteenFourteenFifteenSixteenSeventeenEighteenNineteen')
    upTo99 = upTo19 + (10 * len('twentyThirtyFortyFiftySixtySeventyEightyNinety')) + (8 * upTo9)
    upTo999 = upTo99 + (len('hundredand') * 99 * 9) + (upTo9 * 100) + (len('hundred') * 9) + (upTo99 * 9)
    upTo1000 = upTo999 + len('onethousand')
    print upTo1000


#Euler 18
#Returns the largest sum working down a triangle (tree)

def prob18():
    #convert file to nested list of numbers
    def convFile(x):
        masterli = []
        for strline in x:
            line = strline.split()
            numline = []
            for i in line:
                numline.append(int(i))
            masterli.append(numline)
        return masterli

    tree = convFile(open("C:\Users\Andy\Documents\\1A\Programming\prob18.txt", "r"))

    def takesum(row, pos, total):
        if row < len(tree):
            return max(takesum(row+1, pos, total+tree[row][pos]), takesum(row+1, pos+1, total+tree[row][pos]))
        else:
            return total

    return takesum(0, 0, 0)


#Euler 19
#Returns the number of intersections of sundays and the first day of the month since 1900

def prob19():
    numSun = 0
    firstDays = set()
    daycounter = 1
    months31 = set([1, 3, 5, 7, 8, 10, 12])

    for year in range(1901, 2001):
        for month in range(1, 13):
            firstDays.add(daycounter)
            if month in months31:
                daycounter += 31
            elif not month == 2:
                 daycounter += 30
            elif year%4 == 0 and (not(year%100 == 0) or year%400 == 0):
                daycounter += 29
            else:
                daycounter += 28

    for sunday in range(1, 36496, 7):
        if sunday in firstDays:
            numSun += 1

    return numSun
