s1, s2, s3 = input(), input(), input()

arr = [s1, s2, s3]

def f(arr):
    for i in range(len(arr)):
        if arr[i][-1] != arr[(i+1)%3][0]:
            return "bad"
    return "good"

print(f(arr))