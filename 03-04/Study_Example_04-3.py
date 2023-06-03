position = str(input())

row = int(position[1:])
col = position[:1]

dict_col = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
col = int(dict_col[col])

row_c = [-1, -1, 1, 1, -2, -2, 2, 2]
col_c = [-2, 2, -2, 2, -1, 1, -1, 1]

count = 0

for i in range(8) :
    t_row = row + row_c[i]
    t_col = col + col_c[i]
    if t_row < 1 or t_row > 8 or t_col < 1 or t_col > 8 :
        continue
    else:
        count += 1
        
print(count)

