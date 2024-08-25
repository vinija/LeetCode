from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(substring:str, index: int) -> None:
            #exit condition
            if index == len(s):
                result.append(substring)
                return
            
            if s[index].isalpha():
                #lowercase
                backtrack(substring + s[index].lower(), index + 1)

                #uppercase
                backtrack(substring + s[index].upper(), index + 1)
            else:
                backtrack(substring + s[index], index + 1)
        backtrack("", 0)
        return result

            

        return result
        