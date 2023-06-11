from collections import deque

n, m, v = map(int, input().split())

'''
graph = [[]]
for i in range(m):
    graph.append(list(map(int, input().split())))
'''    
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False]*(m+1)
visited_bfs = [False]*(m+1)

search_dfs = []
search_bfs = []

'''
def dfs(graph, v, visited):
    visited[v] = True
    search_dfs.append(v)
    #print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return search_dfs
'''

def dfs(graph, v, visited):
    visited[v] = True  # 해당 V값 방문처리
    search_dfs.append(v)
    #print(v, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)
    return search_dfs


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        y = queue.popleft()
        search_bfs.append(y)
        #print(v, end=' ')
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True
    return search_bfs
                
result_dfs = dfs(graph, v, visited_dfs)
result_bfs = bfs(graph, v, visited_bfs)

for i in range(len(result_dfs)):
    print(result_dfs[i], end=' ')
print()
for i in range(len(result_bfs)):
    print(result_bfs[i], end=' ')

#print(graph)