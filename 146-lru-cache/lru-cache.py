class Node: 
    
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.left = Node(0, 0) 
        self.right = Node(0, 0) 
        self.left.next = self.right
        self.right.prev = self.left 
        self.cache = {} 

    def delete(self, node):
        nxt = node.next 
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev
        

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right  

        prev.next = node
        node.prev = prev
        node.next = nxt 
        nxt.prev = node
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.next 
            self.delete(node)
            del self.cache[node.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)