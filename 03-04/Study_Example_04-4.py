n, m = map(int, input().split())
row, col, dir = map(int, input().split())

gamemap = []
for i in range(n) :
    gamemap.append(list(map(int, input().split())))
    
# 북, 서, 남, 동 
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

log = [[0]*m for _ in range(n)]
log[row][col] = 1

turn_count = 0

while True :
    if dir == 0 :
        dir = 3
    else:
        dir = dir - 1
    
    t_row = row + drow[dir]
    t_col = col + dcol[dir]
    b_row = row - drow[dir]
    b_col = col - dcol[dir]
             
    if log[t_row][t_col] == 0 and gamemap[t_row][t_col] == 0:
        row = t_row
        col = t_col
        log[row][col] = 1
        turn_count = 0
    else :
        row = row
        col = col
        turn_count += 1
    
    if turn_count == 4 :
        if gamemap[b_row][b_col] == 0 :
            row = b_row
            col = b_col
            turn_count = 0
        else :
            break

count = sum(row.count(1) for row in log)
print(count)
    