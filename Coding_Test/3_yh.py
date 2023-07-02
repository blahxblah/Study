(n, m) = tuple(map(int, input().split()))
s = input()
danger = tuple(map(int, input().split()))

def east(p) :
    return [p, (p[0]+1, p[1])]
def west(p) :
    return [p, (p[0]-1, p[1])]
def south(p) :
    return [p, (p[0], p[1]-1)]
def north(p) :
    return [p, (p[0],p[1]+1)]

def update(pos) :
    p_list.append(pos[0])
    if pos[1] not in danger :
        p_list.append(pos[1])

p_list = list()
p_list.append((0,0))
for char in s :
    pos = p_list.pop()
    if char == "E" : 
        update(east(pos))
    elif char == "W" : 
        update(west(pos))
    elif char == "S" : 
        update(south(pos))
    elif char == "N" : 
        update(north(pos))

p_list = set(p_list)
print(len(p_list))