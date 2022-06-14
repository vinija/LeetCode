class Solution:
    def maximumSwap(self, num: int) -> int:
        #idea: from right to left, have a max at hand, each smaller one is a candidate to swith
        # 98368: 8 -> 6 -> 3
        digits = list(str(num))
        max_digit = (-1, -1) #val, index
        candidate = (-1, -1) # candidate pair of indexes
        for i in range(len(digits)-1, -1, -1):
            if int(digits[i]) > max_digit[0]:
                max_digit = (int(digits[i]), i)
            elif int(digits[i]) < max_digit[0]: #smaller one found, but this can be replaced with a even smaller one
                candidate = (i, max_digit[1])
                
        digits[candidate[0]], digits[candidate[1]] = digits[candidate[1]], digits[candidate[0]]
        return int(''.join(digits))