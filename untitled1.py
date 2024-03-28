graph={
       'a':['b','c'],
       'b':['d','e'],
       'c':['f'],
       'd':[],
       'e':['f'],
       'f':[]
       }
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    print(node)
    for neighbour in graph:
     if neighbour not in visited:
         visited.append(neighbour)
         queue.append(neighbour)
         print(neighbour)
bfs(visited,graph,'a')
            

