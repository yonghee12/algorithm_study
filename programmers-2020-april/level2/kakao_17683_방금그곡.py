# https://programmers.co.kr/learn/courses/30/lessons/17683
# 50
'''
정답률 47.50%
숏코딩하느라 파이써닉하지 않아지는 것 어디까지 감내해야 할 것인지?
이번에도 sorted가 큰 일 했다.
애매한 문자열이라 해시, 스플릿, regex같은 고급개념 말고 replace로 간편하게 하는 접근 먹힘
프로그래머스 웬만한 풀이는 더럽고 파이썬을 다른언어처럼 사용하는
'''

def replace_sharps(notes):
    replace_dict = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for k, v in replace_dict.items():
        notes = notes.replace(k, v)
    return notes


def solution(m, musicinfos):
    m = replace_sharps(m)
    musicinfos = [song.split(",") for song in musicinfos]
    songinfos = []
    for song in musicinfos:
        timeinfos = list(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), song[:2]))
        duration = timeinfos[1] - timeinfos[0]
        notes = replace_sharps(song[3])
        notes = notes * (duration // len(notes) + 1)
        notes = notes[:duration]
        songinfos.append({'duration': duration, 'songname': song[2], 'notes': notes, 'is_in': m in notes})
    candidate = sorted(songinfos, key=lambda x: (x['is_in'], x['duration']), reverse=True)[0]
    if candidate.get("is_in"):
        return candidate["songname"]
    else:
        return "(None)"


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

solution(m, musicinfos)
