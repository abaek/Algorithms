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
	#found one answer
	if distance == 0:
		return [start]
	else:
		#gather answer recursively
		result = []
		neighbours = graph.nodes[start]
		#recurse through each neighbour
		for neighbour in graph.nodes[start]:
			result.extend(nodesAwayDFS(graph, neighbour, distance-1))
		return result
#tests:
assert nodesAwayDFS(graph1, 1, 2) == [3, 5]
assert nodesAwayDFS(graph1, 1, 3) == [4]

"""
2) Given a graph, find all nodes of distance n away from a starting node using BFS
"""
def nodesAwayBFS(graph, start, distance):
	curLevelNodes = [start]
	while distance != 0:
		children = []
		for node in curLevelNodes:
			#aggregate all children
			children.extend(graph.nodes[node])
		curLevelNodes = children
		distance -= 1
	return curLevelNodes
#tests:
assert nodesAwayBFS(graph1, 1, 2) == [3, 5]
assert nodesAwayBFS(graph1, 1, 3) == [4]

"""
3) Find the nth largest number in a BST
"""
def nthLargest(bst, n):
	curNode = bst.root
	while (True):
		#count all nodes in left (lower than current num)
		countLeft = countNodesTree(curNode.left)
		#found
		if countLeft == n - 1:
			return curNode.value
		#go smaller
		elif countLeft > n - 1:
			curNode = curNode.left
		#go bigger
		else:
			curNode = curNode.right
			n -= countLeft + 1

#helper to count the nodes
def countNodesTree(bst):
	if bst == None:
		return 0
	else:
		return 1 + countNodesTree(bst.left) + countNodesTree(bst.right)
#tests:
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
4) Find the distance between 2 nodes in a graph 
"""
def distanceApart(graph, start, end):
	if start == end:
		return 0
	else:
		#keep track of visited nodes
		visited = set()
		distance = 1
		children = graph.nodes[start]
		while(True):
			#not connected
			if children == []:
				return -1
			#found end
			elif end in children:
				return distance
			#BFS
			else:
				newChildren = []
				for child in children:
					if not child in visited:
						newChildren.extend(graph.nodes[child])
						visited.add(child)
				children = newChildren
				distance += 1
#tests:
assert distanceApart(graph1, 1, 3) == 2
assert distanceApart(graph1, 2, 5) == 1
assert distanceApart(graph1, 4, 5) == 1
assert distanceApart(graph1, 2, 1) == -1

"""
5) Implement Djkastra's Algorithm
"""
def Dijkstra(graph, start, end):
	#set initial path lengths to each node
	pathLengths = [-1 for i in range(len(graph.list))]
	#set start node distance to 0
	pathLengths[start] = 0
	#Also keep track of unvisitedNodes
	unvisitedNodes = [-1 for i in range(len(graph.list))]
	while(True):
		#find min path length
		minNode = 0
		minNodeDistance = -1
		for i in range(len(unvisitedNodes)):
			#must be unvisited, yet have a distance and be min distance
			if unvisitedNodes[i] == -1 and pathLengths[i] >= 0 and (pathLengths[i] < minNodeDistance or minNodeDistance == -1):
				minNodeDistance = pathLengths[i]
				minNode = i
		neighbours = graph.list[minNode]
		#neighbour = (id, distance/weight)
		for neighbour in neighbours:
			#if neighbour hasnt been touched or greater distance than current route, give it a value
			if pathLengths[neighbour[0]] == -1 or pathLengths[neighbour[0]] > minNodeDistance + neighbour[1]:
				pathLengths[neighbour[0]] = minNodeDistance + neighbour[1]
		#mark node as visited
		unvisitedNodes[minNode] = 0
		#if end node is visited, break
		if minNode == end:
			break
	print pathLengths
	return pathLengths[end]

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
assert Dijkstra(graph2, 1, 4) == 9
assert Dijkstra(graph3, 0, 1) == 2






