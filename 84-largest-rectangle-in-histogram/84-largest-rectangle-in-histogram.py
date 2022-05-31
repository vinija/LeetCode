class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
                ## LOGIC ##
        ## 1. Before Solving this problem, go through Monotone stack.
        ## 2. Using Monotone Stack we can solve 1) Next Greater Element 2) Next Smaller Element 3) Prev Greater Element 4) Prev Smaller Element
        ## 3. Using 'NSE' Monotone Stack concept, we can find width of rectangles, height obviously will be the minimum of those. Thus we can calculate the area
        ## 4. As we are using NSE concept, adding 0 to the end, will make sure that stack is EMPTY at the end. ( so all the areas can be calculated while popping )
        
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        heights.pop()
        return ans
        