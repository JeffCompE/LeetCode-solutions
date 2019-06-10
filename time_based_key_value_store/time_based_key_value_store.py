class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        history = self.hash_set.get(key, None)
        if not history:
            self.hash_set[key] = [(timestamp, value)]
        else:
            if value != history[-1][1]:
                history.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self.hash_set.get(key, None)
        # edge cases
        if not history:
            return ''
        if timestamp >= history[-1][0]:
            return history[-1][1]
        if timestamp < history[0][0]:
            return ''

        # do a binary search
        l = 0
        r = len(history) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if history[mid][0] == timestamp:
                return history[mid][1]
            elif history[mid][0] < timestamp:
                l = mid
            elif history[mid][0] > timestamp:
                r = mid
        return history[l][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
