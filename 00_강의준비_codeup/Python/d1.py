# 기존에 있는 딕셔너리에 새로운 키/값을 추가하려고 한다.
# 이 때 이미 있는 키에 새로운 값을 덮어씌우면 낭패이므로
# 추가하려는 키들이 기존 딕셔너리에 있는지 확인하고자 한다.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
test = [1,4,11]

for i in range(0, len(test), 1):
    exists = False
    for k in d:
        if k == test[i]:
            exists = True
            break
    if exists:
        print(test[i], '이미 있는 키입니다')
    else:
        print(test[i], '없는 키입니다')