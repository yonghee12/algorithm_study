def main():
    string = input().strip()
    bomb = input().strip()
    bombl = list(bomb)
    b_last = bomb[-1]
    bl = len(bomb)

    ans = []
    for l in string:
        ans.append(l)
        if b_last == l and bombl == ans[-bl:]:
            del ans[-bl:]

    print(''.join(ans) if ans else "FRULA")


if __name__ == '__main__':
    main()

"""
0. 통과했으나 로직상 놓친 것
    - 스택 마지막이 같을 때만 비교하면 된다
1. stdin 별로 안빠름
2. 단순 비교의 경우 스트링 비교가 리스트보다 빠름
    - 하지만 그렇다고 join해서 스트링 비교하는건 무식한 일
    - 비교대상 스트링을 리스트로 만들어놓고 리스트 비교하는게 나음 (join은 매번 연산)
3. 하지만 pop을 해야하는경우 스트링 슬라이싱은 매우 느림
4. 리스트 비교 후 지울 때 가장 빠른 것
    - 비교는 그냥 슬라이싱 : list[-k:] 일 때 일반적으로 O(k)
    - 지울 때 for _ in range(k): list.pop()이 스트링 슬라이싱보단 빠름
    - 지울 때 del list[-k:] 하는게 가장 빠름
5. 모든 비교용 변수는 전역변수로 쓰는게 가장 빠름
    - 배열 접근이라고 무조건 빠르다고 생각하지 말고 계속 쓰는거면 전역변수
6. 그냥 스택같은 느낌 : 스택을 사용
7. 이상하지만 def main() 으로 감싸고 main() 실행하는게 속도를 개선
8. print문 안에 삼항 연산자를 쓸 수 있음
"""
