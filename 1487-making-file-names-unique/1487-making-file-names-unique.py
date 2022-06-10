class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # names : array of names
        # n : size of names
        
        # create folders at the i'th minute for each name = names[i]
        # If name was used previously, append a suffix "(k)" - note parenthesis - where k is the smallest pos int
        
        # return an array of strings where ans[i] is the actual saved variant of names[i]
        
        n = len(names)
        
        dictNames = {}
        ans = ['']*n
        
        # enumerate to grab index so we can return ans list in order
        for idx, name in enumerate(names):
            # check if we have seen this name before
            if name in dictNames:
                # if we have grab the next k using last successful low (k) suffix
                k = dictNames[name]
                # track the name we started so we can update the dict
                namestart = name
                # cycle through values of increasing k until we are not in a previously used name
                while name in dictNames:
                    name = namestart + f"({k})"
                    k += 1
                # update the name we started with to the new lowest value of k
                dictNames[namestart] = k
                # add the new name with k = 1 so if we see this name with the suffix
                dictNames[name] = 1
            else:
                # we havent seen this name so lets start with 1
                dictNames[name] = 1
            # build the solution
            ans[idx] = name
        return ans