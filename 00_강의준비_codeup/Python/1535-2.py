def f(arr):
    biggest_number = 0
    biggest_index = 0
    for i in range(len(arr)):
        if biggest_number < arr[i]:
            biggest_number = arr[i]
            biggest_index = i
        else:
            pass
    return biggest_index + 1

def main():
    n = int(input())
    arr = input().strip().split(" ")
    
    for i in range(n):
        arr[i] = int(arr[i])
    # print(arr)
    print(f(arr), end="")

main()