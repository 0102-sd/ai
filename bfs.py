

graph = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

defbfs(visited, graph, node):
visited.append(node)
queue.append(node)

while queue:
    s = queue.pop(0) 
print (s, end = " ") 

forneighbour in graph[s]:
ifneighbour not in visited:
visited.append(neighbour)
queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')
