class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Use a set to track the top 3 unique maximum numbers
        top3 = set()

        for num in nums:
            top3.add(num)
            # If the set has more than 3 elements, remove the smallest one
            if len(top3) > 3:
                top3.remove(min(top3))

        # If there are fewer than 3 unique numbers, return the maximum
        if len(top3) < 3:
            return max(top3)
        else:
            return min(top3)
