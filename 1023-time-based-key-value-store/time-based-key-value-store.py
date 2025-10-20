class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage: 
            self.storage[key] = []

        self.storage[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        res = ""  

        values = self.storage[key]


        l = 0 
        r = len(values) - 1 

        while l <= r: 

            mid = (l + r) // 2 

            if values[mid][1] == timestamp: 
                return values[mid][0]
            elif values[mid][1] < timestamp: 
                res = values[mid][0] 
                l = mid + 1 
            else: 
                r = mid - 1

        return res
        # highest = 0 

        # for i in range(len(values)):
        #     curr_time = values[i][1]
        #     curr_label = values[i][0]

        #     if curr_time == timestamp:
        #         return curr_label 
        #     elif curr_time < timestamp: 
        #         if curr_time > highest:
        #             highest = curr_time 
        #             res = curr_label 
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)