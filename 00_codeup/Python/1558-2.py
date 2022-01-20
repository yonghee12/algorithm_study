def f(n):
    s = str(n)
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result
    
# Execution
n = int(input())
print(f(n))