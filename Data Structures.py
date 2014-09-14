#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     12-09-2014
# Copyright:   (c) Andy Baek 2014
# Questions:   Cracking the Coding Interview
#-------------------------------------------------------------------------------

"""
Implement a linked list (with insert and delete functions)
"""
class LinkedList():
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

"""
Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop
"""
def circularLL(LL):
	pass


"""
Implement a stack with push and pop functions
"""
class Stack():
	def __init__(self, top=None):
		self.top = top
	def push(self, elem):
		newLL = LinkedList(elem, self.top)
		self.top = newLL
	def pop(self):
		topElem = self.top.value
		self.top = self.top.next
		return topElem

"""
Implement a queue with queue and dequeue functions
"""
class Queue():
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last
	def add(self, elem):
		newElem = Node(elem)
		self.next = newElem


"""
Write a function that sorts a stack using only stacks
"""
def sortStack(stack):
	newStack = Stack()
	while(True):
		pass


"""
Implement a binary min heap. Turn it into a binary max heap
"""
class MinHeap():
	pass

def minToMaxHeap(heap):
	pass