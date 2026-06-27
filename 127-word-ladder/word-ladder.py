class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        nei = defaultdict(list) 


        if endWord not in wordList:
            return 0 

        for word in wordList:

            for j in range(len(word)):
                pattern =  word[:j] + "*"  + word[j + 1:] 
                nei[pattern].append(word) 


        queue = deque()
        queue.append(beginWord) 
        visited = set() 

        visited.add(beginWord) 

        length = 1 

        while queue: 

            for i in range(len(queue)): 
                word = queue.popleft() 

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for w in nei[pattern]: 
                        if w == endWord:
                            length += 1 
                            return length 

                        if w not in visited:
                            queue.append(w) 
                            visited.add(w) 
            

            length += 1 

        return 0