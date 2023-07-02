# n = int(input().split().pop())
# arr = [int(i) for i in input().split()]
# arr = map(int, input().split())

n = 5
arr = [8,4,1,8,1]

nums = set(arr)

x = [num for num in nums if arr.count(num) == 1]
x = x.pop()