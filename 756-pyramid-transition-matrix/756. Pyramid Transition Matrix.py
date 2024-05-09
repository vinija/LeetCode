class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        allowed_dict = defaultdict(list)
        for pattern in allowed:
            allowed_dict[pattern[0:2]].append(pattern[2])

        
        def canBuild(current_row: str, next_row: str, index: int) -> bool:
            if len(current_row) == 1:
                return True
            if index == len(current_row) - 1: 
                return canBuild(next_row, "", 0)
            
            base = current_row[index:index+2]
            if base in allowed_dict:
                for top_block in allowed_dict[base]:
                    if canBuild(current_row, next_row + top_block, index + 1):
                        return True
            return False
        
        return canBuild(bottom, "", 0)
        