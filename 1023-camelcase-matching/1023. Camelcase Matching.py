class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query: str, pattern: str) -> bool:
            i, j = 0, 0 #init pointers for query and pattern

            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].islower():
                    i += 1
                else:
                    return False
            
            #check if all characters of the pattern are matched
            if j != len(pattern):
                return False
            
            #check if rest of query only has lowercase letters
            while i < len(query):
                if query[i].isupper():
                    return False
                i += 1
            
            return True
        return [matches(query, pattern) for query in queries]