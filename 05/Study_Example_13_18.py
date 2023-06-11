def solution(p):
    w = p
    global answer
    if p is None: # 1번 과정
        return ""
    else:
        for i in range(1,len(p),2): # 2번 과정
            u = w[:i+1]
            v = w[i+1:]
            if u.count("(") == u.count(")"):
                if u[0] == "(" and u[i] == ")": # 3-1
                    for k in range(len(u)):
                        answer.append(u[k])
                        
                    answer.extend(solution(v))                    
                else: # 4번 과정
                    answer.append("(") # 4-1
                    answer.extend(solution(v)) # 4-2
                    answer.append(")") # 4-3
                    u = u[1:-1] # 4-4
                    for j in range(len(u)):
                        if u[j] == "(":
                            u[j] = ")"
                        else:
                            u[j] = "("
                    answer.extend(u)
                    return answer # 4-5
            

p = list(map(str, input()))
print(p)
answer = []

result = solution(p)

print(result)