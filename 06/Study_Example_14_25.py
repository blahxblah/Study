def solution(N, stages):
    count = [0]*(N+2)
    
    for i in range(len(stages)):
        count[stages[i]] += 1
        
    failed = [0]*N
    bunmo = len(stages)
    
    for i in range(N):
        try:
            failed[i] = count[i+1] / bunmo
            bunmo = bunmo - count[i+1]
        except:
            failed[i] = 0
            
    result = list(enumerate(failed, start=1))
    result = sorted(result, key=lambda x : x[1], reverse=True)
    
    answer = [index for index, per in result]   
    
    return answer

N = 5
stages = [2,1,2,6,2,4,3,3]
answer = solution(N, stages)
print(answer)