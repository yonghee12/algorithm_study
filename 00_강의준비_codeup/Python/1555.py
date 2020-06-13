def f(n):
    total = 0
    for i in range(1, n+1, 1):
        total += i
    return total
    
# Execution
n = int(input())
print(f(n))