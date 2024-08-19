import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # This will hold the current window
        window = sorted(nums[:k])
        medians = []

        for i in range(k, len(nums) + 1):
            # Compute the median for the current window
            if k % 2 == 1:
                # If k is odd, take the middle element
                medians.append(float(window[k // 2]))
            else:
                # If k is even, take the average of the two middle elements
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            if i == len(nums):
                break

            # Remove the element that's sliding out of the window
            outgoing_element = nums[i - k]
            window.remove(outgoing_element)

            # Insert the new element into the window
            incoming_element = nums[i]
            bisect.insort(window, incoming_element)

        return medians
