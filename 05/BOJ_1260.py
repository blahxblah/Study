from collections import deque

n, m, v = map(int, input().split())

graph = [[]]
for i in range(m):
    graph.append(list(map(int, input().split())))
    
visited = [False]*(m+1)

search_dfs = []
search_bfs = []

def dfs(graph, v, visited):
    visited[v] = True
    search_dfs.append(v)
    #print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return search_dfs
            
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        search_bfs.append(v)
        #print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append[i]
                visited[i] = True
    return search_bfs
                
result_dfs = dfs(graph, v, visited)
result_bfs = bfs(graph, v, visited)

print(result_dfs)
print(result_bfs)