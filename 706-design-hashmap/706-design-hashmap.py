class MyHashMap:

    def __init__(self):
        self.myMap = {}

    def put(self, key: int, value: int) -> None:
        self.myMap[key] = value
        

    def get(self, key: int) -> int:
        if key in self.myMap:
            return self.myMap[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.myMap:
           del self.myMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)