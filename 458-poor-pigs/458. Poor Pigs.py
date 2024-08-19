class Solution:
    def poorPigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        pigs = log(buckets, minutes_to_test // minutes_to_die + 1)
        return round(pigs) if isclose(pigs, round(pigs)) else ceil(pigs)
