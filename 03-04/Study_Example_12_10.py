#def rotation_90(key) :
#    n = len(key)
#    m = len(key[0])
#    result = [[0]*n for _ in range(m)]
#    for i in range(n) :
#        for j in range(m) :
#            result[j][n - i - 1] = key[i][j]
def rotation_90(key) :
    result = [list(reversed(i)) for i in zip(*key)]
    return result

def 

def solution(key, lock):
    
    if :
        answer = True
    else:
        answer = False
    return answer

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

result = solution(key, lock)
print(result)