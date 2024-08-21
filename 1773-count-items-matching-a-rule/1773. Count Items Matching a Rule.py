class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Determine the index to check based on the ruleKey
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:  # ruleKey == "name"
            index = 2
        
        # Count the number of items that match the rule
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        
        return count  # Return the total count of matching items
