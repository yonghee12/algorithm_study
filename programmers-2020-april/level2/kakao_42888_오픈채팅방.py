# https://programmers.co.kr/learn/courses/30/lessons/42888
"""
Lesson
한번 돌고 다시 돌아도 됨
2n 두려워하지 말고
커맨드 나뉘면 무조건 해시
"""

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    footer = {"Enter": "님이 들어왔습니다.",
              "Leave": "님이 나갔습니다."}
    ids = {}
    actions = []
    for r in record:
        line = r.split(" ")
        if line[0] != "Change":
            actions.append((line[0], line[1]))
        if line[0] != "Leave":
            ids[line[1]] = line[2]
    answer = [ids[uid] + footer[act] for act, uid in actions]
    return answer


solution(record)
