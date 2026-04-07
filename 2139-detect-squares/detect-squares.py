class DetectSquares:


    def __init__(self):
        self.hashmap = defaultdict(int) 

    def add(self, point: List[int]) -> None:
        self.hashmap[tuple(point)] += 1 

    def count(self, point: List[int]) -> int:
        px, py = point

        res = 0 

        for x, y in self.hashmap: 
            if abs(px - x) != abs(py - y) != 0 or x == px or y == py: 
                continue 

            if (x, py) in self.hashmap and (px, y) in self.hashmap:
                res += self.hashmap[(x, py)] * self.hashmap[(px, y)] * self.hashmap[(x, y)]

            
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)