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
"""
class Stack():
	def __init__(self, top=None):
		self.top = top
	def push(self, elem):
		newLL = Node(elem, self.top)
		self.top = newLL
	def pop(self):
		if self.top != None:
			topElem = self.top.value
			self.top = self.top.next
			return topElem
		else:
			return None
#tests
s = Stack()
s.push(4)
s.push(5)
assert s.pop() == 5
s.push(6)
assert s.pop() == 6
assert s.pop() == 4
assert s.pop() == None

"""
2) Implement a queue with queue and dequeue functions
"""
class Queue():
	# First: newest element
	def __init__(self, first=None, last=None):
		self.first = first
		self.last = last
	def queue(self, elem):
		newElem = Node(elem)
		if self.first == None:
			self.last = newElem
		else:
			self.first.next = newElem
		self.first = newElem
	def dequeue(self):
		if self.last == None:
			return None
		else:
			ret = self.last.value
			self.last = self.last.next
			return ret
#tests:
q = Queue()
q.queue(4)
q.queue(5)
assert q.dequeue() == 4
q.queue(6)
assert q.dequeue() == 5
assert q.dequeue() == 6
assert q.dequeue() == None


"""
3) Implement a Binary Min Heap using an array
"""
class Heap: #minHeap
	def __init__(self, size=1):
		self.size = size
		self.ar = [-1 for i in range(size)]

	#build up
	def createFromArray(self, ar):
		self.size = len(ar)
		#loop through indexes backwards starting from midpoint
		for i in range(len(ar)/2, -1 , -1):
			index = i
			#coninually swap down left side of heap until property statisfied
			while(index < self.size):
				print ar, index, 'l'
				left = index*2 + 1
				right = index*2 + 2
				if left < self.size and ar[left] < ar[index]:
					#swap
					temp = ar[index]
					ar[index] = ar[left]
					ar[left] = temp
					#for every swap left, make sure right still holds
					indexRight = index
					while(indexRight < self.size):
						print ar, index, 'r - in'
						right = indexRight*2 + 2
						if right < self.size and ar[right] < ar[indexRight]:
							#swap
							temp = ar[indexRight]
							ar[indexRight] = ar[right]
							ar[right] = temp
							indexRight = right
						else:
							break
					index = left
				elif right < self.size and ar[right] < ar[index]:
					print ar, index, 'r - out'
					#swap
					temp = ar[index]
					ar[index] = ar[right]
					ar[right] = temp
					index = right
				else:
					break
		self.ar = ar

	def push(self, val):
		#insert into first instance of -1
		newPos = -1
		for i in range(self.size):
			if self.ar[i] == -1:
				newPos = i
				break
		#double length of heap
		if newPos == -1:
			newPos = self.size
			self.ar.extend([-1 for i in range(self.size)])
			self.size = self.size * 2
		#insert
		self.ar[newPos] = val
		#swap backwards until fit
		curPos = newPos
		while(curPos > 0):
			if curPos%2 == 0:
				parent = (curPos-2)/2
			else:
				parent = (curPos-1)/2
			if self.ar[curPos] > self.ar[parent]:
				break
			#swap
			self.ar[curPos] = self.ar[parent]
			self.ar[parent] = val
			curPos = parent
			

	#Always pop root
	def pop(self):
		index = 0
		#pop root and swap down heap
		while index*2+1 < self.size:
			#right is too big
			if index*2+2 >= self.size:
				#left DNE
				if self.ar[index*2+1] == -1:
					break
				#swap left
				self.ar[index] = self.ar[index*2 + 1]
				index = index*2+1
			else:
				#left does not exist
				if self.ar[index*2+1] == -1:
					#right DNE
					if self.ar[index*2+2] == -1:
						break
					#swap right
					self.ar[index] = self.ar[index*2 + 2]
					index=index*2+2
				#right DNE, swap left
				elif self.ar[index*2+2] == -1:
					self.ar[index] = self.ar[index*2 + 1]
					index=index*2+1
				#both exist
				else:
					if self.ar[index*2 + 1] < self.ar[index*2 + 2]:
						self.ar[index] = self.ar[index*2 + 1]
						index = index*2 + 1
					else:
						self.ar[index] = self.ar[index*2 + 2]
						index = index*2 + 2
		self.ar[index] = -1


		