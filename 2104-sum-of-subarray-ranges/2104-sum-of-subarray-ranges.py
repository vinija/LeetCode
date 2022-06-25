class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

            ans = 0
            for i in range(len(nums)):
                max_heap = []
                min_heap = []
                heapq.heappush(min_heap,nums[i])
                heapq.heappush(max_heap, -nums[i])
                for j in range(i+1, len(nums)):
                    heapq.heappush(min_heap,nums[j])
                    heapq.heappush(max_heap, -nums[j])

                    ans += -max_heap[0] - min_heap[0]

            return ans