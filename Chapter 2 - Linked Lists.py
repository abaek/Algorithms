import copy

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

def createLL(ar):
    newLL = Node()
    curNode = newLL
    for i in ar:
        newNode = Node(i)
        curNode.next = newNode
        curNode = newNode
    return newLL.next

#2.1 Write code to remove duplicates from an unsorted linked list.
def fn1(ll):
    items = set()
    if ll == None or ll.next == None:
        return ll
    curNode = ll
    items.add(curNode.value)
    while(curNode != None and curNode.next != None):
        if curNode.next.value in items:
            curNode.next = curNode.next.next
        else:
            items.add(curNode.next.value)
            curNode = curNode.next
    return ll


#2.2 Implement an algorithm to find the nth to last element of a singly linked list.
def fn2(ll, n):
    count = 0
    curNode = copy.deepcopy(ll)
    while(curNode != None):
        count+=1
        curNode = curNode.next
    elem = count - n
    curNode = ll
    for i in range(elem):
        curNode = curNode.next
    return curNode.value


#2.3 Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
#EXAMPLE
#Input: the node ?c? from the linked list a->b->c->d->e
#Result: nothing is returned, but the new linked list looks like a->b->d->e
def fn3(ll):
    ll.value = ll.next.value
    ll.next = ll.next.next


#2.4 You have two numbers represented by a linked list, where each node contains a single digit.
#The digits are stored in reverse order, such that the 1?s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#Output: 8 -> 0 -> 8
def fn4(l1, l2):
    newLL = Node()
    curNode = newLL
    carry = 0
    while (l1 != None and l2 != None):
        curSum = l1.value + l2.value + carry
        if curSum > 9:
            carry = 1
            curSum -= 10
        else:
            carry = 0
        newNode = Node(curSum)
        curNode.next = newNode
        curNode = curNode.next
        l1 = l1.next
        l2 = l2.next
    if carry == 1:
        newNode = Node(1)
        curNode.next = newNode
    return newLL.next