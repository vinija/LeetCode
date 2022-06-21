class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0])//len(arr)

        if diff==0:
            return arr[0]

        for i in range(1, len(arr)):
            if arr[i-1] + diff != arr[i]:
                return arr[i-1] + diff