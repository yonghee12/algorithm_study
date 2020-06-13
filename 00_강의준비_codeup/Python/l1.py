# 리스트 안의 수 중
# 가장 큰 수를 출력하시오

# 입력
a = [20,30,10,70]

# 출력예시
70

# 아래 코드 작성
biggest = a[0]
for i in range(1, len(a), 1):
    if a[i] > biggest:
        biggest = a[i]

print(biggest)