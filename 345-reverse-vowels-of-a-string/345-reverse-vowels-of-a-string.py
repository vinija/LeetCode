class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}        
        s = list(s)
        
        while i < j:
            while i < j and s[i] not in vowels:                
                i+=1                        
            
            while i < j and s[j] not in vowels:                
                j-=1
            
            if i<j:
                s[j], s[i] = s[i], s[j]   
            
            i+=1
            j-=1
        
        return ''.join(s) 