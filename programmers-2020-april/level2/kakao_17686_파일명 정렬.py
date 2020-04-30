# https://programmers.co.kr/learn/courses/30/lessons/17686
'''
축배를 들자!
앞선 다트문제에서 정규표현식을 활용하여 튜플 찢는 방법을 잘 익혔다.
sorted에서 key 사용도 빠르게 알아내서 풀었다.
정규표현식 자체를 조금 더 연습하면 좋겠다.
'''


import re


def solution(files):
    re_spl = re.compile('(^[a-z|A-Z|\s|\.|\-]+)(\d+)(.*)')
    spl = [re_spl.findall(file)[0] for file in files]
    sort = sorted(spl, key=lambda x: (str(x[0]).lower(), int(x[1])))
    return [''.join(s) for s in sort]

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

solution(files)


# 배워야 할 코드
def solution(files):
    a = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])
    return b


'''
배울점
정렬 순위가 1 - 2면 실제로는 2 - 1로 정렬하면 된다.
앞선 정렬 중 높은 우선순위로 뒤집는 효과.
'''
