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
	Difficulty: 6
"""
def nodesAwayDFS(graph, start, distance):
	pass
#tests:
# assert nodesAwayDFS(graph1, 1, 2) == [3, 5]
# assert nodesAwayDFS(graph1, 1, 3) == [4]

"""
2) Given a graph, find all nodes of distance n away from a starting node using BFS
	Difficulty: 7
"""
def nodesAwayBFS(graph, start, distance):
	pass
#tests:
# assert nodesAwayBFS(graph1, 1, 2) == [3, 5]
# assert nodesAwayBFS(graph1, 1, 3) == [4]

"""
3) Find the nth largest number in a BST
	Difficulty: 6
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
	Difficulty: 5
"""
def distanceApart(graph, start, end):
	pass
#tests:
# assert distanceApart(graph1, 1, 3) == 2
# assert distanceApart(graph1, 2, 5) == 1
# assert distanceApart(graph1, 4, 5) == 1
# assert distanceApart(graph1, 2, 1) == -1

"""
5) Implement Djkastra's Algorithm
	Difficulty: 10
"""
def Dijkstra(graph, start, end):
	pass

class Graph2:
	#adjList = [ [(2, 3), (3, 4)], [(1, 3), (4, 9)], [(1, 4), (4, 5)], [(2, 9), (3, 5)] ]
	#where adjList[2] = [(neighbour, weight), ..]
	def __init__(self, adjList=[]):
		self.list = adjList

graph2 = Graph2([[], [(2, 3), (3, 4), (5, 4)], 
					[(1, 3), (4, 9)], 
					[(1, 4), (4, 5)], 
					[(2, 9), (3, 5), (4, 4)], 
					[(1, 4), (6, 4)], 
					[(5, 4), (4, 4)]])
graph3 = Graph2([[(1, 4), (2, 1)],
				[(0, 4), (2, 1)],
				[(0, 1), (1, 1)]])
#tests:
# assert Dijkstra(graph2, 1, 4) == 9
# assert Dijkstra(graph3, 0, 1) == 2

