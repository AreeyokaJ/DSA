class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = "" 

        if key not in self.storage:
            return ans 

        values = self.storage[key]

        l = 0 
        r = len(values) - 1 

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else: 
                r = mid - 1
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)