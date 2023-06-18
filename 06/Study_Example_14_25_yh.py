n = 5
stages = [2,1,2,6,2,4,3,3]

# n = 4
# stages = [4,4,4,4,4]

# import sys
# n = int(sys.stdin.readline())
# input = [int(sys.stdin.readline()) for _ in range(n)]

arr_count = [0 for _ in range(n+1)]
for lv in stages :
    if lv <= n :
        i = lv-1
    else : i = n
    arr_count[i] += 1

arr_rate = [0 for _ in range(n+1)]
for idx, cnt in enumerate(arr_count) :
    try :
        arr_rate[idx] = cnt / sum(arr_count[idx:])
    except ZeroDivisionError :
        arr_rate[idx] = 0

# dict = dict()
# for idx, rate in enumerate(arr_rate) :
#     dict[rate] = idx
# arr_rate[:-1].sort(reverse=True)
# answer = [dict[rate] for rate in arr_rate]

rate = list(set(arr_rate[:n]))
rate.sort(reverse=True)

order = list()
for rr in rate :
    ord = list()
    for i, r in enumerate(arr_rate[:n]) :
        if r == rr : ord.append(i)
    ord.sort()
    for o in ord :
        order.append(o+1)

print(order)
print('end')