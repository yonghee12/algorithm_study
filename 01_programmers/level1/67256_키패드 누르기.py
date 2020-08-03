# https://programmers.co.kr/learn/courses/30/lessons/67256

phone = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}

def solution(numbers, hand):
    hands = {'left': phone['*'], 'right': phone['#']}
    answer = ''
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            hands['left'] = phone[n]
        elif n in (3, 6, 9):
            answer += 'R'
            hands['right'] = phone[n]
        else:
            x, y = phone[n][0], phone[n][1]
            ldist = abs(hands['left'][0] - x) + abs(hands['left'][1] - y)
            rdist = abs(hands['right'][0] - x) + abs(hands['right'][1] - y)
            if ldist < rdist:
                answer += 'L'
                hands['left'] = phone[n]
            elif rdist < ldist:
                answer += 'R'
                hands['right'] = phone[n]
            else:
                answer += hand[0].upper()
                hands[hand] = phone[n]
    return answer
