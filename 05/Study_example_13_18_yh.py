def split(str, u_list) :

    if str == "" : 
        return u_list
    
    sum = 0
    u = ""
    for idx, char in enumerate(str) :
        
        if char == "(" : sum += 1
        elif char == ")" : sum += -1
        u += char
        
        if sum==0 : 
            u_list.append(u)
            split(str[idx+1:], u_list)
            break
    
    return u_list
    
def edit(u) :
    u_ = ""

    for i,c in enumerate(u) :
        if i == 0 : u_ += "("
        elif i == len(u)-1 : u_ += ")"
        else :
            if c == "(" : u_ += ")"
            if c == ")" : u_ += "("

    return u_


# p = ")()()("
# p = "(()())()"
# p = ")("
p = "))((()((())))(())("

u_list = split(p,list())

for i, u in enumerate(u_list) : 
    if u[0] == ")" :
        u_list[i] = edit(u)
    else : continue
 
answer = "".join(u_list)
print(u_list)
print(answer)