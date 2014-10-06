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
		pass
	def pop(self):
		pass

"""
2) Implement a queue with queue and dequeue functions
"""
class Queue():
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last
	def queue(self, elem):
		pass
	def dequeue(self):
		pass

"""
3) Implement a Binary Min Heap using an array
"""
class Heap: #minHeap
	def __init__(self, size=1):
		self.size = size
		self.ar = [-1 for i in range(size)]
	def createFromArray(self, ar):
		pass
	def push(self, val):
		pass
	def pop(self):
		pass


