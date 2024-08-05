class Solution:
    def maximumSwap(self, num: int) -> int:
        #Convert the num to a list of characters -> digits
        digits = list(str(num))

        #dic store last occurence of each digit
        last = {int(x): i for i, x in enumerate(digits)}

        #Traverse list of digits
        for i, digit in enumerate(digits):
            #check for viable swap
            for d in range(9, int(digit), -1):
                #if larger exists later in number

                if last.get(d, -1) > i:
                    #swap the digits
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    #return the result as an int
                    return int(''.join(digits))
        
        return num
        