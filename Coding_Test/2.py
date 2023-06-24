def police(n, singos):
    singo_counts = [0]*(n+1)
    police_counts = 0
    for i in range(len(singos)):
        singo_counts[singos[i][1]] += 1
        if singo_counts[singos[i][1]] >= 2:
            if singos[i][0] != singos[i-1][0]:
                police_counts += 1
                singo_counts[singos[i][1]] = 0
    return police_counts

n, k = map(int, input().split())
singos = []
for _ in range(k):
    singo = list(map(int, input().split()))
    singos.append(singo)

print(police(n, singos))
