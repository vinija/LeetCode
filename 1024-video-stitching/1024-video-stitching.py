class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= time or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= time else -1
        