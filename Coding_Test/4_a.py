n, m = map(int, input().split())
goorm = set()
friend  = set()
for i in range(n):
    goorm.add(input())
for i in range(m):
    friend.add(input())
ans = sorted(list(goorm&friend))
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)