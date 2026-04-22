class MyHashMap:

    def __init__(self):
        self.array = []

    def put(self, key: int, value: int) -> None:
        for i, kv in enumerate(self.array):
            k = self.array[i][0]
            if k == key:
                self.array[i] = (k, value) 
                return
        
        self.array.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.array:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        if len(self.array) == 0:
            return 

        if key == self.array[-1][0]:
            self.array.pop()
        else:
            end = self.array[-1] 

            for i, kv in enumerate(self.array):
                k = kv[0] 
                v = kv[1] 

                if k == key:
                    self.array[i] = end 
                    self.array.pop()
                    return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)