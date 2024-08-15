from typing import List

class Solution:
    def maximumSwap(self, num: int) -> int:

        #convert num to a list of digits
        numList = list(str(num))
        n = len(numList)

        #create a list to store the position of each digit
        last = {int(numList[i]): i for i in range(n) }
        print(last)

        #traverse list and check for swap opportunity
        for i in range(n):
            #check if larger digit in future to swap with
            for d in range(9, int(numList[i]), -1):
                if last.get(d, -1) > i:
                    #conduct the swap
                    numList[i], numList[last[d]] = numList[last[d]], numList[i]
                    #convert to int and return
                    return int("".join(numList))

        return num
        