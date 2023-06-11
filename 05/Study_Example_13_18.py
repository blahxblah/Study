def solution(p):
    w = p
    if p == "": # 1번 과정
        return ""
    else:
        for i in range(1,len(p),2): # 2번 과정
            u = w[:i+1]
            v = w[i+1:]
            if u.count("(") == u.count(")"):
                if u[0] == "(" and u[i] == ")": # 3-1
                    return u + solution(v)           
                else: # 4번 과정
                    u = list(u[1:-1]) # 4-4
                    for j in range(len(u)):
                        if u[j] == "(":
                            u[j] = ")"
                        elif u[j] == ")":
                            u[j] = "("
                    return "(" + solution(v) + ")" + "".join(u) # 4-5
            

p = "))((()((())))(())("

result = solution(p)

print(result)