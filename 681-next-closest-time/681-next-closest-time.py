class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(':')
        
        # generate sorted permutations of the input digits
        # in both hour and minute
        nums = sorted(set(hour+minute))
        all_time = [a+b for a in nums for b in nums]
        
        # the only change needed is minutes
        # hour remains the same
        i = all_time.index(minute)
        if i+1 < len(all_time) and all_time[i+1] < '60':
            return hour+':'+all_time[i+1]

        # we need to change both the hour and minute
        # change minutes to the smallest value available
        # change hour to the next value available
        # for e.g., 12:59 -> 15:11
        i = all_time.index(hour)
        if i+1 < len(all_time) and all_time[i+1] < '24':
            return all_time[i+1]+':'+all_time[0]
        
        # it's not possible to find another time in the same day
        # so find the smallest in the next day
        # for e.g., 23:59 -> 22:22
        return all_time[0]+':'+all_time[0]