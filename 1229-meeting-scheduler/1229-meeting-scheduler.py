class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(item for item in slots1 if item[1] - item[0] >= duration)
        slots2 = sorted(item for item in slots2 if item[1] - item[0] >= duration)
        
        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            s1,e1 = slots1[p1]
            s2,e2 = slots2[p2]
            if max(s1,s2) + duration <= min(e2,e1):
                return [max(s1,s2), max(s1,s2)+duration]
            
            p1 += s1 <= s2
            p2 += s1 > s2
            
        return []