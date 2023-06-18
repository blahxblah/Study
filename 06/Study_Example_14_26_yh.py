fn = 7
a,b,c,d,e,f,g = 10,20,40,30,50,55,60
input = [a,b,c,d,e,f,g]

# import sys
# n = int(sys.stdin.readline())
# input = [int(sys.stdin.readline()) for _ in range(n)]

# import heapq
# arr = list()
# heapq.heappush(arr, input)
# sum_last = 0
# while True :
#     one = heapq.heappop(arr)
#     two = heapq.heappop(arr)
#     heapq.heappush(one+two)
#     if len(arr) == 1 : break

# 삽입 정렬
def sort_insertion(arr:list) :
    arr_copied = arr.copy()
    arr_sorted = list()

    for _ in arr :
        min_e = min(arr_copied)
        arr_sorted.append(min_e)
        arr_copied.remove(min_e)
    
    return arr_sorted

def calculate(arr_sorted:list) :
    arr = arr_sorted.copy()
    res = [0]
    while True :
        try :
            res.append(res[-1]+arr[0])
            arr = arr[1:]
        except IndexError as e :
            break
    res = res[2:]
    return sum(res)

answer = calculate(sort_insertion(input))

print(answer)
print('end')