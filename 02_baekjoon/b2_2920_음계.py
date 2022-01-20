# https://www.acmicpc.net/problem/2920

ascending = "1 2 3 4 5 6 7 8"
descending = "8 7 6 5 4 3 2 1"

line = input().strip()
if line == ascending:
    print("ascending")
elif line == descending:
    print("descending")
else:
    print("mixed")