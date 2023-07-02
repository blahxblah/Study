n, k = 5, 4
arr = [
    (1,4),
    (4,2),
    (3,4),
    (5,2)
]

# (n, k) = tuple(map(int, input().split()))
# arr = [tuple(map(int,input().split())) for _ in range(k)]

hist = set(arr)

report = dict()
police = 0
for h in hist :
    home = h[1]
    if report.get(home) is None :
        report[home] = set()
    report[home].add(h[0])
    if len(report[home]) > 1 :
        police += 1
        del report[home]
print(police)