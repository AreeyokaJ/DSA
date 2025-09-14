class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indicies = defaultdict(set)

    
    def insert(self, val: int) -> bool:
        self.nums.append(val)

                            
        self.indicies[val].add(len(self.nums) - 1)
        
        return True if len(self.indicies[val]) == 1 else False


    def remove(self, val: int) -> bool:
        if val not in self.indicies:
            return False 
        
        index = self.indicies[val].pop()
        last = self.nums[-1]

        if index != len(self.nums) - 1:
            self.nums[index] = self.nums[-1]
            self.indicies[last].remove(len(self.nums) - 1)
            self.indicies[last].add(index)
            
        self.nums.pop() 

        if len(self.indicies[val]) == 0: 
            del self.indicies[val] 

    
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()