# 355. Design Twitter

class Twitter:

    def __init__(self):
        self.counter = -1
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.counter,tweetId))
        self.counter = -1* (self.counter*-1 +1)

    def getNewsFeed(self, userId: int) -> list[int]:
        list_users = [userId]+list(self.following[userId])
        # collect newsfeed only from the above users list
        pq = []
        # print(list_users)
        for user in list_users:
            if len(self.tweet[user])>0:
                heapq.heappush(pq,(self.tweet[user][-1][0],self.tweet[user][-1][1],len(self.tweet[user])-1,user))
        count = 10
        res = []
        while pq and count>0:
            counter,tweetID,ind,user = heapq.heappop(pq)
            res.append(tweetID)
            if ind>0:
                heapq.heappush(pq,(self.tweet[user][ind-1][0],self.tweet[user][ind-1][1],ind-1,user))
            count -=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
