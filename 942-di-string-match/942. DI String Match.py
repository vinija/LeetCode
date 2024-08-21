class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1
        
        perm.append(low)  # Append the last remaining number
        return perm
