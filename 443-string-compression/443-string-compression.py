class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars == None or len(chars) < 1:
            return 0;
        start, end, index =0, 0, 0
        while start< len(chars):
            end=start
            while end< len(chars) and chars[start]==chars[end]:
                end+=1
            chars[index]=chars[start]
            index+=1
            if end-start > 1:
                for s in str(end-start):
                    chars[index]=s
                    index+=1
            start=end
        return index