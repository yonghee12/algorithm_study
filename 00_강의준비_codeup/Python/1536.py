def f(arr):
    target = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < target:
            target = arr[i]
        else:
            pass
    return target

def main():
    n = int(input())
    arr = input().strip().split(" ")
    
    for i in range(n):
        arr[i] = int(arr[i])
    print(f(arr), end="")

main()