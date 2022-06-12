class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s)
        opened = 0
        
        #lets convert our string into a list and only keep track of opened
        #wherever opened goes negative, we add a blank "" into the list which will classify as a removal
        for index, char in enumerate(sList):
            if char == "(":
                opened +=1
            elif char == ")":
                opened -=1
            
            if opened < 0:
                sList[index] = ""
                opened +=1
                
        #if we have opened > 0, then we need to start removing some ( from the end
        if opened > 0:
            for index in range(len(sList)-1,-1,-1):
                if sList[index] == "(":
                    sList[index] = ""
                    opened -=1
                if opened == 0: break
        
        return "".join(sList)