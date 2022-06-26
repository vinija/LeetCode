class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        #two pointer approach
        left = 0
        right = len(height) - 1
        answer = 0
        
        #when water is greater at one end, left or right, we only need to subtract it from that direction
        leftMax = height[left]
        rightMax = height[right]
        
        while left < right:
            #calculate left side
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax,height[left] )
                answer += leftMax - height[left]
            #add in right side so its all in one pass
            else:
                right -=1
                rightMax = max(rightMax, height[right])
                answer += rightMax - height[right]
        
        return answer