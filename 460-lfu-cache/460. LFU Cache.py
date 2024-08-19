class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() 
        self.usage = collections.defaultdict(collections.OrderedDict)
        self.LF = 0

    def get(self, key: int) -> int:
        if key not in self.cache:return -1
        node = self.cache[key]

        self.update(node, node.val)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key not in self.cache: 
            if len(self.cache) >= self.capacity:
                k, v = self.usage[self.LF].popitem(last=False)
                self.cache.pop(k)
            node = ListNode(key, value)
            self.cache[key] = node
            self.usage[1][key] = value
            self.LF = 1
        else: 
            node = self.cache[key]
            node.val = value
            self.update(node, value)
            
            
    def update(self, node, newVal):
        k, f = node.key, node.freq
        self.usage[f].pop(k)
        if not self.usage[f] and self.LF == f:
            self.LF += 1
        self.usage[f+1][k] = newVal
        node.freq += 1