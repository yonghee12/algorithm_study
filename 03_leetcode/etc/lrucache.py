# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3309/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}

    def get(self, key: int) -> int:
        value = self.hash.get(key)
        if value:
            del self.hash[key]
            self.hash[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        retrieved_value = self.hash.get(key)
        if retrieved_value:
            del self.hash[key]
        else:
            if len(self.hash.keys()) == self.capacity:
                firstkey = list(self.hash.keys())[0]
                del self.hash[firstkey]
        self.hash[key] = value


# 다른 이 풀이
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(1,1)
obj.hash

obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
obj.put(3, 2)
obj.put(4, 2)
param_1 = obj.get(1)
# obj.put(key,value)