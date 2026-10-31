class Graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range(n)]
    
    def edge(self,x,y):
        self.adj[x].append(y)
        self.adj[y].append(x)
    
    def bfs_traversal(self,source):
        visited = [False] * self.n
        result = []
        q=[]
        q.append(source)
        visited[source] = True
        while len(q) > 0:
            e1=q[0]
            q.pop(0)
            result.append(e1)
            for i in self.adj[e1]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
        return result
    
g=Graph(4)
g.edge(0,1)
g.edge(0,2)
g.edge(2,1)
g.edge(1,3)

print(g.bfs_traversal(0))