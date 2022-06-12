class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = slots1 + slots2
        slots.sort()
        lastSlot = None
        for start, end in slots:
            if end - start < duration:
                continue
            if lastSlot and lastSlot[1] >= start + duration:
                return [start, start + duration]
            lastSlot = (start, end)
        return []
            