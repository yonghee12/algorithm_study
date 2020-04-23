# https://programmers.co.kr/learn/courses/30/lessons/42576

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def get_not_completed(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic.keys():
            dic[p] = 1
        else:
            dic[p] += 1

    for p in completion:
        dic[p] -= 1
        if dic[p] <= 0:
            del dic[p]
    return dic.popitem()[0]


get_not_completed(participant, completion)
