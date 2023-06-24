def visit_history(s, dangers):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    vt = ['W', 'S', 'E', 'N']
    x, y = 0, 0
    visited = [[0,0]]
    for i in s:
        x += dx[vt.index(i)]
        y += dy[vt.index(i)]
        if [x, y] not in dangers:
            if [x, y] not in visited:
                visited.append([x, y])
        else:
            x -= dx[vt.index(i)]
            y -= dy[vt.index(i)]
                
    return len(visited)


n, m = map(int, input().split())
s = str(input())
dangers = []
for _ in range(m):
    danger = list(map(int, input().split()))
    dangers.append(danger)

print(visit_history(s, dangers))