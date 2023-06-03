n, m = map(int, input().split())
row, col, dir = map(int, input().split())

gamemap = []
for _ in range(n) :
    gamemap = [dot for dot in list(map(int, input().split()))]
    
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

log = [[0]*m for _ in range(n)]
log[row][col] = 1

while True :
    if dir == 0 :
        dir = 3
    else:
        dir = dir - 1
    t_row = row + drow[dir]
    t_col = col + dcol[dir]
    
    if log[t_row][t_col] == 1 or 
    if log[t_row][t_col] == 0 :
        row = t_row
        col = t_col
        log[row][col] = 1
    else:
           