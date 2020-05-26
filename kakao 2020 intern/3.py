from collections import deque
from copy import deepcopy

def get_small_cart(answer, gems):
    i, j = answer
    cart_big = gems[i:j + 1]
    cart_l = len(set(cart_big))
    start_i = 0
    for k in range(len(cart_big)):
        if len(set(cart_big[k:])) == cart_l:
            start_i = k
    answer = [i + start_i, j]
    return answer


def solution(gems):
    buylist = {}
    for gem in gems:
        if buylist.get(gem) is None:
            buylist[gem] = 0

    answer = [0, 0]
    smallest = len(gems)
    cart_key = {}
    start_i = 0
    matched = []
    for idx, gem in enumerate(gems):
        if cart_key.get(gem) is None:
            cart_key[gem] = 1
            answer = [answer[0], idx]
            if len(cart_key) == len(buylist) and answer[1] - answer[0] < smallest:
                matched = deepcopy(answer)
                smallest = matched[1] - matched[0]
                answer = [idx]
                cart_key = {}
        else:
            answer[1] = idx
            answer = get_small_cart(answer, gems)

    return list(map(lambda x: x+1, matched))


gemss = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]
for gems in gemss:
    print(solution(gems))
# solution(gemss[0])


# 원래 코드

# def solution(gems):
#     buylist = {}
#     for gem in gems:
#         if buylist.get(gem) is None:
#             buylist[gem] = 1
#     answer = []
#     smallest = len(gems)
#     for i in range(len(gems)):
#         cart = {}
#         for j in range(i, len(gems)):
#             if cart.get(gems[j]) is None:
#                 cart[gems[j]] = 1
#                 if len(cart) == len(buylist):
#                     break
#             if j - i > smallest:
#                 break
#         if j - i < smallest and len(cart) == len(buylist):
#             answer = [i, j]
#         smallest = answer[1] - answer[0]
#     return [answer[0] + 1, answer[1] + 1]