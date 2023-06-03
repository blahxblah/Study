n = int(input())
plan = list(map(str, input().split()))

direction = {'L':0, 'R':1, 'U':2, 'D':3}
grid_x = [0, 0, -1, 1]
grid_y = [-1, 1, 0, 0]

x, y = 1, 1

for i in plan :
    temp_x = x + grid_x[direction[i]]
    temp_y = y + grid_y[direction[i]]
    if temp_x < 1 or temp_x > n or temp_y < 1 or temp_y > n :
        x, y = x, y
    else:
        x, y = temp_x, temp_y
        
print(x, y)

