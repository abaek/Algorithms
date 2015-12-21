"""
You are given the following classes
"""
class Node():
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
	Difficulty: 4
"""
class Stack():
	def __init__(self, top=None):
		self.top = top
	def push(self, elem):
		pass
	def pop(self):
		pass
#tests:
# s = Stack()
# s.push(4)
# s.push(5)
# assert s.pop() == 5
# s.push(6)
# assert s.pop() == 6
# assert s.pop() == 4
# assert s.pop() == None

"""
2) Implement a queue with queue and dequeue functions
	Difficulty: 6
"""
class Queue():
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last
	def queue(self, elem):
		pass
	def dequeue(self):
		pass
#tests:
# q = Queue()
# q.queue(4)
# q.queue(5)
# assert q.dequeue() == 4
# q.queue(6)
# assert q.dequeue() == 5
# assert q.dequeue() == 6
# assert q.dequeue() == None


"""
3) Implement a Binary Min Heap using an array
	(A Min Heap always pops off the smallest element)
	Difficulty: 9
"""
class Heap: #minHeap
	def __init__(self, size=1):
		self.size = size
		self.ar = [-1 for i in range(size)]
	def createFromArray(self, ar):
		pass
	# Efficiency: log(n)
	def push(self, val):
		pass
	# Efficiency: log(n)
	def pop(self):
		pass


