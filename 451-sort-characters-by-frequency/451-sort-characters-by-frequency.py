class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        output = ""
        
        for char, times in freq.most_common():
            
            output+= (char * times)
        return output
        
        #return "".join([char * times for char, times in collections.Counter(str).most_common()])