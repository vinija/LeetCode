from collections import defaultdict, deque
import heapq
from typing import List

class Twitter:

    def __init__(self):
        # Initialize a dictionary to keep track of tweets by each user
        self.tweets = defaultdict(deque)
        # Initialize a dictionary to keep track of followees for each user
        self.followees = defaultdict(set)
        # Initialize a timestamp to order tweets
        self.timestamp = 0
        # Maximum number of tweets in the news feed
        self.MAX_FEED_SIZE = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add the tweet to the user's list of tweets with a timestamp
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        # Increment the timestamp for the next tweet
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create a min-heap to fetch the 10 most recent tweets
        min_heap = []
        
        # Fetch the user's tweets
        for tweet in list(self.tweets[userId])[:self.MAX_FEED_SIZE]:
            heapq.heappush(min_heap, tweet)
            if len(min_heap) > self.MAX_FEED_SIZE:
                heapq.heappop(min_heap)
        
        # Fetch the tweets of all followees
        for followeeId in self.followees[userId]:
            for tweet in list(self.tweets[followeeId])[:self.MAX_FEED_SIZE]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > self.MAX_FEED_SIZE:
                    heapq.heappop(min_heap)
        
        # Extract the tweetIds from the min-heap, sorted by timestamp in descending order
        return [tweetId for timestamp, tweetId in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        # A user cannot follow themselves
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee if the follower is currently following them
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Example usage:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
