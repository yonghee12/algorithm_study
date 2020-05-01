# https://programmers.co.kr/learn/courses/30/lessons/17680
'''
정답률 45.26
이전에 리트코드에서 lru를 해 봐서 쉽게 풀 수 있었다.
다만 프로그래머스 내부 파이썬 버전이 3.6 이상이 아닌 것 같다.
시간복잡도가 말도 안 되지 않는다면 collection을 사용하는게 나을 듯.
그래도 30분만에 풀 수 있었던 운좋은 문제.
'''

from collections import OrderedDict

class Cache:
    def __init__(self, cachesize):
        self.size = cachesize
        self.cache = OrderedDict()

    def process_time(self, item):
        if self.cache.get(item):
            del self.cache[item]
            self.cache[item] = True
            # 한번에 : self.cache.move_to_end(item, last=True)
            return 1
        else:
            self.cache[item] = True
            if len(self.cache) > self.size:
                firstkey = list(self.cache.keys())[0]
                del self.cache[firstkey]
                # 한번에 : self.cache.popitem(last=False)
            return 5

def solution(cacheSize, cities):
    cache = Cache(cacheSize)
    return sum([cache.process_time(city.lower()) for city in cities])

cities = ["Jeju", "pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
solution(3, cities)