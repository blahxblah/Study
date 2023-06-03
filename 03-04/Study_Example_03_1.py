import random as rand

moneytype = [500, 100, 50, 10, 5, 1]
price = rand.randrange(1, 1000)
changes = 1000 - price
cal_changes = changes
count = 0
for i in range(len(moneytype)):
    count = count + cal_changes // moneytype[i]
    cal_changes = cal_changes % moneytype[i]

print(f"price : {price} / changes : {changes} / count : {count}")