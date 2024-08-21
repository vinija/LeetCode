class MapSum:

    def __init__(self):
        # Dictionary to store the key-value pairs
        self.map = {}
        # Dictionary to store the prefix sums
        self.prefix_map = {}

    def insert(self, key: str, val: int) -> None:
        # Calculate the difference if the key already exists
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        # Update the prefix_map for every prefix of the key
        prefix = ""
        for char in key:
            prefix += char
            if prefix in self.prefix_map:
                self.prefix_map[prefix] += delta
            else:
                self.prefix_map[prefix] = val

    def sum(self, prefix: str) -> int:
        # Return the sum for the given prefix
        return self.prefix_map.get(prefix, 0)
