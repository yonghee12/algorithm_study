def f(n):
    temp = 0
    result = 0
    while n>0:
        temp = n % 10
        result = result * 10 + temp
        n = n // 10
    return result
    
# Execution
n = int(input())
print(f(n))