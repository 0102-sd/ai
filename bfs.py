nodes=int(input("Enter number of nodes in the graph\n"))
graph={}
print("Enter the vertices in alphabetical order starting from A")
for i in range(nodes):
    v=input("Enter Vertex\n")
    print("Enter the neighbours of",v)
    neighbours=list(map(str,input().split()))
    graph.update({v:neighbours})
print("The Graph is:")
print(graph)

print("----BFS Traversal----")
visited=[]
q=[]
def bfs(graph,start):
    visited.append(start)
    q.append(start)
    print("The BFS Path is:\n")
    while q:
        vertex=q.pop(0)
        print(vertex, end=" ")
        
        for adjacent in graph[vertex]:
            if adjacent not in visited:
                visited.append(adjacent)
                q.append(adjacent)

bfs(graph,'A')


