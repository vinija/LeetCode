class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return list(seen)
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         counter = Counter(nums)
#         n= 2
#         #reverse most common
#         output = counter.most_common()[:-n-1:-1]
#         ret = []
#         for item, freq in output:
#             ret.append(item)
        
#         return ret
        