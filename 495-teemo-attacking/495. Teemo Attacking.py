class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_poisoned_time = 0

        for i in range(len(timeSeries) - 1):
            time_diff = timeSeries[i + 1] - timeSeries[i]

            total_poisoned_time += min(time_diff, duration)
        
        total_poisoned_time += duration

        return total_poisoned_time