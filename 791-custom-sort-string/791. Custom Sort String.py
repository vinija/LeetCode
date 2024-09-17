from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        Sort the strings in custom order as defined by input params.
        :param order: str - The sorting order given
        :param s: str - The string to be sorted
        :return :str - The sorted output of s
        '''

        count = Counter(s)
        outputString = []

        for char in order:
            if char in count:
                outputString.append(char * count[char])
                del count[char]
        
        for char, freq in count.items():
            outputString.append(char * freq)
            

   
        

        return ''.join(outputString)

        