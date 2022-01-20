n = int(input())
temp = (n%10)*10 + n//10
temp = temp * 2

temp = temp % 100

print(temp)