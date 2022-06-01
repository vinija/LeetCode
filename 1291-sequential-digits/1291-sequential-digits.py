class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        nums = []
        
        iterate = 10 # can only go 0 - 10
        
        for length in range(len(str(low)), len(str(high))+1):
            for start in range(iterate-length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums