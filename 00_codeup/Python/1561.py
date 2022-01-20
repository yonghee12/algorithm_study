m, n = input().strip().split(" ")
m, n = int(m), int(n)

def bigger(a, b):
    if a >= b:
        return a
    elif b > a:
        return b

print(bigger(m, n))