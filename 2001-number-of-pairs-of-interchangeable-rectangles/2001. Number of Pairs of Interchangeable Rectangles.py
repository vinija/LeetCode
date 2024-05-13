class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratioCount = {}
        interchangeablePairs = 0

        for w, h in rectangles:
            gcd = math.gcd(w,h)
            normalizedRatio = (w // gcd, h // gcd)

            if normalizedRatio in ratioCount:
                ratioCount[normalizedRatio] += 1
            else:
                ratioCount[normalizedRatio] = 1
        
        for count in ratioCount.values():
            if count > 1:
                interchangeablePairs += count * (count -1) // 2
        
        return interchangeablePairs