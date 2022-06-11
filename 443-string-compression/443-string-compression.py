class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # count: record the times one element had appeared. 
        count = 1
        # currentIdx: the idx ready to be modified.
        currentIdx = 0
        
        for i in range(1, len(chars)+1): 
            # check for valid index and if current char matches the previous char
            # if so, add to count
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
            # When we find a new element
            else: 
                # 1) update letter
                chars[currentIdx] = chars[i-1] # we modify char[currentIdx] to the .
                currentIdx += 1
                
                # 2) append count to string after char
                if count == 1:
                    # if the previous element only appear once, skip below.
                    continue
                # add count digit by digit
                for ch in str(count):
                    chars[currentIdx] = ch
                    currentIdx += 1
                    
                # 3) reset count because we're done with the current element
                count = 1
        return currentIdx 