class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {} 
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        nxt = node.next 
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        node.prev = prev 
        prev.next = node
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)