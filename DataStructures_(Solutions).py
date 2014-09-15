#-------------------------------------------------------------------------------
# Title: 		Data Structures
# Author:      	Andy Baek
# Created:     	12-09-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	Cracking the Coding Interview (Gayle Laakmann)
#-------------------------------------------------------------------------------


"""
You are given the following classes
"""
class LinkedList():
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class TreeNode:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

"""
1) Implement a stack with push and pop functions
"""
class Stack():
	def __init__(self, top=None):
		self.top = top
	def push(self, elem):
		newLL = LinkedList(elem, self.top)
		self.top = newLL
	def pop(self):
		if self.top != None:
			topElem = self.top.value
			self.top = self.top.next
			return topElem
		else:
			return None

"""
2) Implement a queue with queue and dequeue functions
"""
class Queue():
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last
	def queue(self, elem):
		newElem = LinkedList(elem)
		if self.last == None:
			self.last = newElem
			self.first = newElem
		else:
			self.last.next = newElem
	def dequeue(self):
		if self.first == None:
			return None
		else:
			self.first = self.first.next

"""
3) Implement a binary minheap with ability to add elements
"""
class MinHeap():
	def __init__(self, root=None):
		self.root = root
	def add(self, elem):
		pass



"""
4) Convert a binary min heap into a binary max heap
"""
def minToMaxHeap(heap):
	pass


"""
5) Write a function that sorts a stack using only stacks
"""
def sortStack(stack):
	newStack = Stack()
	while(True):
		pass













		