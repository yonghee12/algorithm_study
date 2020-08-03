# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
from collections import deque
from copy import deepcopy
from itertools import permutations


def calc(nums, ops, prt):
    operators = ['-', '*', '+']
    n_nums, n_ops = [], []
    for p in prt:
        qn = deque(nums)
        qo = deque(ops)
        this_op = operators[p]
        while qn:
            if len(qn) == 1:
                n_nums.append(qn.pop())
                break
            num1, num2 = qn.popleft(), qn.popleft()
            op = qo.popleft()
            if op == this_op:
                qn.appendleft(str(eval(num1 + op + num2)))
            else:
                n_nums.append(num1)
                n_ops.append(op)
                qn.appendleft(num2)

        nums, ops = deepcopy(n_nums), deepcopy(n_ops)
        n_nums, n_ops = [], []
    return abs(int(nums[0]))


def solution(expression):
    nums = re.findall('\d+', expression)
    ops = re.findall('[-+*]', expression)

    prts = list(permutations(range(3), 3))
    sums = []
    for prt in prts:
        sums.append(calc(nums, ops, prt))
    return max(sums)


exp = "100-200*300-500+20"
# exp = "50*6-3*2"
# exp = '100-200'
print(solution(exp))
