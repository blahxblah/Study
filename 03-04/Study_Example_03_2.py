n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

set_first_second = k+1

set_value = (k * first) + second
set_count = m // set_first_second

last_count = m % set_first_second

result = (set_value * set_count) + (first * last_count)

print(result)
