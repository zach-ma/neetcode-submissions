class TimeMap:

    def __init__(self):
        # map: key -> list of (timestamp, value) pairs
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        records = self.m[key]
        l, r = 0, len(records) - 1
        while l <= r:
            m = l + (r - l) // 2
            t, v = records[m]
            if t > timestamp:
                r = m - 1
            elif t < timestamp:
                # if m + 1 <= r and records[m + 1][0] <= timestamp:
                #     l = m + 1
                # else:
                #     return records[l][1]
                l = m + 1
            else:
                return v
        # now l == r
        # if l - 1 >= 0:
        #     return records[l-1][1]
        if r >= 0:
            return records[r][1]
        return ""
        # return records[l][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)