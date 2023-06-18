n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
result = []
stack = array[0]
for i in range(n-1):
    stack = stack + array[i+1]
    result.append(stack)
    
#sum_list = []
#
#sum_list.append(n-1)
#for i in range(n-1):
#    sum_list.append(n-i-1)
#
#result = [x*y for x, y in zip(array, sum_list)]
#print(result)
print(sum(result))

