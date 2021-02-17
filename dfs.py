n=int(input("Enter Number of nodes in the Graph\n"))
graph={}
print("Enter vertices in alphabetical order starting from A")
for i in range(n):
    v=input("Enter the vertice \n")
    print("Enter the Neighbours of",v)
    neighbours=[]
    neighbours=list(map(str,input().split()))
    graph.update({v:neighbours})
   
print("The Graph is:")
print(graph)

visited=[]
print("\nDFS Traversal is :")
def dfs(graph,start):
    if start not in visited:
        print(start,end=" ")
        visited.append(start)
        for adjacent in graph[start]:
            dfs(graph,adjacent)

dfs(graph,'A')


