#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     12-09-2014
# Copyright:   (c) Andy Baek 2014
# Source:   http://www.reddit.com/r/cscareerquestions/comments/1jov24/heres_how_to_prepare_for_tech_interviews/
#-------------------------------------------------------------------------------

"""
1) Implement a Node class for a Tree
"""
class Node:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

"""
2) Implement a BST tree class with an add function
"""
class BST:
	def __init__(self, root=None):
		self.root = root
	def add(self, val):
		pass

"""
3) Implement a graph class (create, add)
"""
class Graph:
	def __init__(self, nodes={}):
		self.nodes = nodes
	def add(self, val, neighbours):
		self.nodes.append((val, neighbours))

"""
4) Given a graph, find all nodes of distance n away from a starting node using DFS
"""
def nodesAwayDFS(graph, start, distance):
	pass

#tests:
graph1 = Graph({1: [2, 5], 2: [3, 5], 3: [4], 4: [5], 5: []})
assert nodesAwayDFS(graph1, 1, 2) == [3, 5]
assert nodesAwayDFS(graph1, 1, 3) == [4]

"""
5) Given a graph, find all nodes of distance n away from a starting node using BFS
"""
def nodesAwayBFS(graph, start, distance):
	pass
#tests:
assert nodesAwayBFS(graph1, 1, 2) == [3, 5]
assert nodesAwayBFS(graph1, 1, 3) == [4]

"""
Find the nth largest number in a BST
"""
def nthLargest(bst, n):
	pass

#tests:
bst1 = BST(Node(10, Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, None)), Node(15, Node(11, None, Node(12, None, None)), Node(21, None, None))))
assert nthLargest(bst1, 1) == 2
assert nthLargest(bst1, 2) == 3
assert nthLargest(bst1, 3) == 4
assert nthLargest(bst1, 4) == 5
assert nthLargest(bst1, 5) == 7
assert nthLargest(bst1, 6) == 10
assert nthLargest(bst1, 7) == 11
assert nthLargest(bst1, 8) == 12
assert nthLargest(bst1, 9) == 15
assert nthLargest(bst1, 10) == 21

"""
Find the distance between 2 nodes in a graph 
"""
def distanceApart(graph, start, end):
	pass
#tests:
assert distanceApart(graph1, 1, 3) == 2
assert distanceApart(graph1, 2, 5) == 1
assert distanceApart(graph1, 4, 5) == 1
assert distanceApart(graph1, 2, 1) == -1