n, k = map(int, input().split())

count = 0

while True :
    a = n // k # 몫 구하기(나누기 카운트)
    if a > 1 :
        b = n % k # 나머지 구하기(빼기 카운트)
        count = count + b + 1 # 빼기 카운트와 나누기 카운트를 갱신
        n = a # 나누기 카운트 이후의 n값
    elif a == 1 :
        b = n % k
        count = count + b + 1
        break
    else :
        count = count + n - 1
        break
    
print(count)