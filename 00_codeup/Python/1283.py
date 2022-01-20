first_money = int(input())
days = int(input())

changes = input().strip().split(" ")
for i in range(0, days, 1):
    changes[i] = int(changes[i])

pocket = first_money
for change in changes:
    rate = (100 + change)/100
    pocket *= rate

profit = pocket - first_money
profit = round(profit)
print(profit)

if profit > 0:
    print('good')
elif profit < 0:
    print('bad')
else:
    print("same")