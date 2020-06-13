# https://programmers.co.kr/learn/courses/30/lessons/17681

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]


def get_binary_array(decimal_list: list, fill: int) -> list:
    return [bin(d)[2:].zfill(fill) for d in decimal_list]


def decode_map(obj1: str, obj2: str) -> str:
    decoded_agg = ''
    for i, j in zip(obj1, obj2):
        code = int(i) or int(j)
        decoded = "#" if code == 1 else ' '
        decoded_agg += decoded
    return decoded_agg


def solution(n, arr1, arr2):
    arr1, arr2 = [get_binary_array(arr, n) for arr in (arr1, arr2)]
    answer = [decode_map(m, n) for m, n in zip(arr1, arr2)]
    return answer


solution(6, arr1, arr2)
