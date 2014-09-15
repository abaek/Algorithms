#-------------------------------------------------------------------------------
# Title: 		Graphs and Trees
# Author:      	Andy Baek
# Created:     	12-09-2014
# Copyright:   	(c) Andy Baek 2014
# Sources:   	http://www.reddit.com/r/cscareerquestions/comments/1jov24/heres_how_to_prepare_for_tech_interviews/
#-------------------------------------------------------------------------------

"""
You are given these structures:
"""
class TreeNode:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class BST:
	def __init__(self, root=None):
		self.root = root
	def add(self, value):
		if self.root == None:
			self.root = TreeNode(value)
		else:
			curNode = self.root
			while(True):
				if (curNode.value > value):
					if curNode.left == None:
						curNode.left = TreeNode(value)
						break
					else:
						curNode = curNode.left
				else:
					if curNode.right == None:
						curNode.right = TreeNode(value)
						break
					else:
						curNode = curNode.right

bst1 = BST(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None)), TreeNode(7, None, None)), TreeNode(15, TreeNode(11, None, TreeNode(12, None, None)), TreeNode(21, None, None))))

class Graph:
	def __init__(self, nodes={}):
		self.nodes = nodes
	def add(self, val, neighbours):
		self.nodes[val] =  neighbours

graph1 = Graph({1: [2, 5], 2: [3, 5], 3: [4], 4: [5], 5: []})

"""
1) Given a graph, find all nodes of distance n away from a starting node using DFS
"""
def nodesAwayDFS(graph, start, distance):
	pass
#tests:
# assert nodesAwayDFS(graph1, 1, 2) == [3, 5]
# assert nodesAwayDFS(graph1, 1, 3) == [4]

"""
2) Given a graph, find all nodes of distance n away from a starting node using BFS
"""
def nodesAwayBFS(graph, start, distance):
	pass
#tests:
# assert nodesAwayBFS(graph1, 1, 2) == [3, 5]
# assert nodesAwayBFS(graph1, 1, 3) == [4]

"""
3) Find the nth largest number in a BST
"""
def nthLargest(bst, n):
	pass
#tests:
# assert nthLargest(bst1, 1) == 2
# assert nthLargest(bst1, 2) == 3
# assert nthLargest(bst1, 3) == 4
# assert nthLargest(bst1, 4) == 5
# assert nthLargest(bst1, 5) == 7
# assert nthLargest(bst1, 6) == 10
# assert nthLargest(bst1, 7) == 11
# assert nthLargest(bst1, 8) == 12
# assert nthLargest(bst1, 9) == 15
# assert nthLargest(bst1, 10) == 21

"""
4) Find the distance between 2 nodes in a graph 
"""
def distanceApart(graph, start, end):
	pass
#tests:
# assert distanceApart(graph1, 1, 3) == 2
# assert distanceApart(graph1, 2, 5) == 1
# assert distanceApart(graph1, 4, 5) == 1
# assert distanceApart(graph1, 2, 1) == -1

