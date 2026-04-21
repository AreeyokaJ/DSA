class MyHashSet:

    def __init__(self):
        self.array = []

    def add(self, key: int) -> None:
        if key not in self.array:
            self.array.append(key) 

    def remove(self, key: int) -> None:
        if len(self.array) == 0:
            return 
        end = self.array[-1]
        
        if key == end:
            self.array.pop()
            
        for i, item in enumerate(self.array):
            if key == item:
                self.array[i] = end
                self.array.pop()

    def contains(self, key: int) -> bool:
        for item in self.array:
            if key == item:
                return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)