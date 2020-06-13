def main():
    n = int(input())
    print(f(n))

def f(n):
    if n == 1:
        return 'hello'
    elif n == 2:
        return 'world'

main()