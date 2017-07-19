from Queue import *

adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
];


class Data:
	def __init__(self):
		self.dist = None
		self.pre = None

def bfs(graph,start):
	# queue and bfsData init
	qu = Queue()
	bfsData = []
	# initialization of bfs data for each vertex in graph
	for i in range(len(graph)):
		bfsData.append(Data())

	bfsData[start].dist = 0
	qu.put(start)

	while(not qu.empty()):
		u = qu.get()
		for v in range(len(graph[u])):
			element = graph[u][v]
			if bfsData[element].dist == None :
				bfsData[element].pre = u
				bfsData[element].dist = bfsData[u].dist + 1
				qu.put(element) 
	return bfsData   
		


okay =  bfs(adjList,3)

for i in range(len(adjList)):
    print "vertex %r distance = %r predecessor = %r" % (i,okay[i].dist,okay[i].pre)





