class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1 
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] 
        self.followerMap[userId].add(userId)
        res = []  

        for user in self.followerMap[userId]:
            tweetList = self.tweetMap[user] 
            if tweetList:
                index = len(tweetList) - 1 
                count = tweetList[-1][0]
                tweetId = tweetList[-1][1]
                heapq.heappush(heap, (count, index, tweetId, user))

        while heap and len(res) < 10: 
            count, index, tweetId, user = heapq.heappop(heap) 
            index -= 1 
            res.append(tweetId)
            tweetList = self.tweetMap[user] 

            if index >= 0: 
                count = tweetList[index][0]
                tweetId = tweetList[index][1]
                heapq.heappush(heap, (count, index, tweetId, user))
        
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followerMap[followerId] and followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)