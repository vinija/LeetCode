import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Pattern to match a valid number as defined
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        
        # Using fullmatch to ensure the entire string must match the pattern
        return bool(re.fullmatch(pattern, s))
