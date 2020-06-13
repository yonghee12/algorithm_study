# https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from copy import deepcopy


def gotcha(user_id_list, ban_id):
    res = []
    for user in user_id_list:
        if len(user) != len(ban_id):
            continue
        elif ban_id == '*' * len(ban_id):
            if len(ban_id) == len(user):
                res.append(user)
            continue
        got = True
        for b, u in zip(ban_id, user):
            if b == '*':
                continue
            if b != u:
                got = False
                break
        if got:
            res.append(user)
    return res


def solution(user_id, banned_id):
    combs = [gotcha(user_id, banned) for banned in banned_id]
    sets = [[]]
    for comb in combs:
        new_set = []
        for sett in sets:
            for item in comb:
                new_set.append(sett + [item])
        sets = deepcopy(new_set)
    res = []
    for s in sets:
        realset = set(s)
        if len(realset) == len(banned_id) and realset not in res:
            res.append(realset)
    return len(res)


users = [
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"]

]

bans = [
    ["*rodo", "*rodo", "******"],
    ["fr*d*", "*rodo", "******", "******"]

]
for i in range(len(users)):
    print(solution(users[i], bans[i]))
