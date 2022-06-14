class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips)
        start, end = 0, 0
        cnt = 0
        idx = 0
        while start <= end:
            cnt += 1
            newstart, newend = end + 1, end
            while idx < len(clips) and start <= clips[idx][0] <= end:
                newend = max(newend, clips[idx][1])
                if newend >= T:
                    return cnt
                idx += 1
            start, end = newstart, newend
        return -1
        