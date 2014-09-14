import copy

class Tree:
    def __init__(self, value= None, left=None, right=None):
        self.value= value
        self.left = left
        self.right = right
        self.parent = None
    def printTree(self):
        nodes = [self]
        while(True):
            row = ''
            children = []
            for node in nodes:
                row += str(node.value) + ' '
                if (node.left != None):
                    children.append(node.left)
                if (node.right != None):
                    children.append(node.right)
            print(row)
            if children == []:
                break
            nodes = children[:]

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


#sample trees:
myUnbalancedTree = Tree(9, Tree(5, Tree(3, Tree(1), Tree(4)), Tree(7)), Tree(13, None, Tree(14, None, Tree(15))))
myBalancedTree = Tree(9, Tree(5, Tree(3, Tree(1), Tree(4)), Tree(7)), Tree(13, Tree(12), Tree(14, None, Tree(15))))


#4.1 Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined
#to be a tree such that no two leaf nodes differ in distance from the root by more than one.
def fn1(tr):
    nodes = [tr]
    end = False
    while(True):
        children = []
        if end:
            for node in nodes:
                if (node.left != None or node.right != None):
                    return False
                break
            return True
            break
        else:
            for node in nodes:
                if (node.left == None):
                    end = True
                else:
                    children.append(node.left)
                if (node.right == None):
                    end = True
                else:
                    children.append(node.right)
            nodes = children


#4.2 Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

#sample graphs:
graph1 = Graph({'A':['B'],
                'B':['C', 'D'],
                'C':['E'],
                'D':['A'],
                'E':['B', 'F'],
                'F':['A', 'D']})

graph2 = Graph({'A':['B'],
                'B':['C', 'D'],
                'C':[],
                'D':['A'],
                'E':['B', 'F'],
                'F':['A', 'D']})

notCyclicGraph = Graph({'A':['B'],
                        'B':['C', 'D'],
                        'C':['E'],
                        'D':[],
                        'E':['D', 'F'],
                        'F':[]})

notCyclicGraph2 = Graph({'A':['B'],
                        'B':['C', 'D'],
                        'C':['D'],
                        'D':[],
                        'E':['D', 'F'],
                        'F':[]})

def fn2(graph, start, end):
    visited = set()
    return fn2Help(graph, start, end, visited)

def fn2Help(graph, start, end, visited):
    if start == end:
        return True
    elif graph.nodes[start] == []:
        return False
    else:
        pathExists = False
        for i in graph.nodes[start]:
            if not i in visited:
                newVisited = copy.deepcopy(visited)
                newVisited.add(i)
                if fn2Help(graph, i, end, newVisited):
                    pathExists = True
                    break
        return pathExists

#4.3 Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
def fn3(ar):
    if ar == []:
        return None
    else:
        middlePos = len(ar)/2
        middle = ar[middlePos]
        return Tree(middle, fn3(ar[:middlePos]), fn3(ar[middlePos+1:]))


#4.4 Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
#(i.e., if you have a tree with depth D, you?ll have D linked lists).
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

#not tested
def fn4(bst):
    nodes = Node(bst)
    depths = {}
    depth = 0
    while(True):
        depthLL = None
        if nodes != None:
            depths[depth] = []
        while(nodes != None):
            depths[depth].append(nodes.value)
            if node.left != None:
                newNode = Node(node.left)
                if depthLL == None:
                    depthLL = newNode
                else:
                    depthLL.next = newNode
            if node.right != None:
                newNode = Node(node.right)
                if depthLL == None:
                    depthLL = newNode
                else:
                    depthLL.next = newNode
            nodes = nodes.next
        depth+=1
        if depthLL == None:
            break
        nodes = depthLL
    return depths



#4.5 Write an algorithm to find the ?next? node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.
#Let's assume it\s not the right most node
def fn5(bst):
    if bst.right != None:
        return bst.right.value
    elif bst.parent.left.value == bst.value:
        return bst.parent.vaue
    else:
        curNode = bst
        while curNode.parent.parent.left.value != curNode.parent.value:
            curNode = curNode.parent
        return curNode.parent.parent.value


#part 2: find the success of a node given a bst
def fn5b(bst, node):
    successor = bst.right.value
    curNode = bst
    while(curNode.value != node):
        if curNode.value > node:
            temp = curNode.value
            curNode = curNode.left
            if curNode.right == None:
                successor = temp
            else:
                successor = curNode.right.value
        else:
            curNode = curNode.right
            successor = bst.right.value
    return successor


#4.6 Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
#NOTE: This is not necessarily a binary search tree.
def fn6(node1, node2):
    parents1 = set()
    parents2 = set()
    while(True):
        parents1.add(node1.value)
        parents2.add(node2.value)
        if parents1 & parents2 != set():
            return list(parents1 & parents2)[0]
            break
        if node1.parent != None:
            node1 = node1.parent
        if node2.parent != None:
            node2 = node2.parent


#4.7 You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.



#4.8 You are given a binary tree in which each node contains a value. Design an algorithm to print all paths which sum up to that value.
#Note that it can be any path in the tree - it does not have to start at the root.


