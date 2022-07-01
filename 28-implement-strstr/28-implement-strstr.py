class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)
            
        #needle = "c"
        #haystack = "abc"
        
        if len(needle) == 0 :return 0
        
        lenofNeedle = len(needle)
        
        for i in range(len(haystack) - lenofNeedle + 1):
            print(f'word is {haystack[i:lenofNeedle]} , index {i}')
            if haystack[i:lenofNeedle + i] == needle :
                return i
            
        return - 1