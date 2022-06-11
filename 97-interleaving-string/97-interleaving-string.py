class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # just interleave two linked list... let a,b,c be the head of linked list
        @cache
        def dp(a,b,c): # not O(N^3) but O(N^2) since 'c' is dependent -> 'a'+'b'
            
            # base cases
            if c == len(s3) and b == len(s2) and a==len(s1): return True
            elif c==len(s3): return False
            
            # if - TAKE THE NEXT VALUE FROM `A`
            if a<len(s1) and \
            s1[a] == s3[c] and dp(a+1,b,c+1): # took from `A`; move the head pointers 
                return True
            
            # if - TAKE THE NEXT VALUE FROM `B`
            if b< len(s2) and \
            s2[b] == s3[c] and dp(a,b+1,c+1): # took from `B`; move the head pointers 
                return True
            
            return False
        
        return dp(0,0,0)