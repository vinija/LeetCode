class HitCounter:

    def __init__(self):
        self.hits = {}
        

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp ] = 0
        self.hits[timestamp] +=1

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300
        hits_for_ts = 0
        for i in range(begin+1, timestamp+1):
            if i in self.hits:
                hits_for_ts += self.hits[i]
        return hits_for_ts

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)