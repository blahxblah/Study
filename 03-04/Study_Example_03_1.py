import random as rand

money = [500, 100, 50, 10, 5, 1]
cash = rand.randrange(1, 1001)
c_cash = cash
count = 0
for i in range(len(money)):
    count = count + c_cash // money[i]
    c_cash = c_cash % money[i]

print(f"cash : {cash} / count : {count}")

