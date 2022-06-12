class RandomizedSet:

    def __init__(self):
        self.items = []

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            index = self.items.index(val)
            del self.items[index]
            return True
        return False

    def getRandom(self) -> int:
        rando = random.randint(0, len(self.items)-1)
        return self.items[rando]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()