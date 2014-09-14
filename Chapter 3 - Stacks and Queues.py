class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def appendEnd(self, value):
        newNode = Node(value)
        curNode = self
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = newNode
    def deleteNode(self, head, value):
        if head.value == value:
            head = head.next
        else:
            previousNode = head
            while(previousNode.next != None):
                if previousNode.next.value == value:
                    peviousNode.next = previousNode.next.next
                    break
                previousNode = previousNode.next
    def printLL(self):
        string = ''
        if self != None:
            string = str(self.value)
            self = self.next
            while (self != None):
                string = string + ' -> ' + str(self.value)
                self = self.next
        return string
    def __str__(self):
        return str(self.value)

class Stack:
    def __init__(self, top=None):
        self.top = None
    def push(self, item):
        newNode = Node(item, self)
        self.top = newNode
    def pop(self):
        if(self != None):
            poppedTop = self.top
            self.top = self.next
            return poppedTop
        else:
            return None

class Queue:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = first
    def add(self, item):
        newNode = Node(item)
        if (self.first == None):
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
    def remove(self):
        if (self.last == None):
            return None
        else:
            value = self.first.value
            self.first = self.first.next
            if (self.first == None):
                self.last = self.first
            return value



#3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
#Push, pop and min should all operate in O(1) time.
class Stack2:
    def __init__(self, top=None):
        self.top = None
        self.min = Node(self.top)
    def push(self, item):
        newNode = Node(item, self)
        self.top = newNode
        if(self.min.value == None or self.min.value > item):
            newMin = Node(item, self.min)
            self.min = newMin
    def pop(self):
        if(self != None):
            poppedTop = self.top
            self.top = self.next
            if (poppedTop == self.min):
                self.min = self.min.next
            return poppedTop
        else:
            return None
    def getMin(self):
        return self.min.value


#3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
#we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
#SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the
#previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
#(that is, pop() should return the same values as it would if there were just a single stack).
#FOLLOW UP Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.



#3.4 In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower.
#The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one).
#You have the following constraints:
#(A) Only one disk can be moved at a time.
#(B) A disk is slid off the top of one rod onto the next rod.
#(C) A disk can only be placed on top of a larger disk.
#Write a program to move the disks from the first rod to the last using Stacks.

#3.5 Implement a MyQueue class which implements a queue using two stacks.

#3.6 Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented.
#The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.










