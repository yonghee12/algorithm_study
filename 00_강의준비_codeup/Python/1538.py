def main():
    n = int(input())
    print(f(n))

def f(n):
    if n%2 == 0:
        return 'even'
    elif n%2 == 1:
        return 'odd'

main()