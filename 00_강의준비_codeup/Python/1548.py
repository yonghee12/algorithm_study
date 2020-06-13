def main():
    n = int(input())
    print(f(n))

def f(n):
    if n>=90 and n<=100:
        return 'A'
    elif n>=80 and n<90:
        return 'B'
    elif n>=70 and n<80:
        return 'C'
    elif n>=60 and n<70:
        return 'D'
    elif n<60:
        return 'F'
    
main()