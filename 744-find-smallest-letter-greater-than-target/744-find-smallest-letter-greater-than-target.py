class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #binary search that if i get to the end return the first 
        n = len(letters)
        # if target>= letters[n-1]: return letters[0]
        l, h = 0,n
        
        while l< h:
            mid = (l+h)//2
            if letters[mid] > target:
                h = mid
            else:
                l = mid+1
        return letters[l%n] 