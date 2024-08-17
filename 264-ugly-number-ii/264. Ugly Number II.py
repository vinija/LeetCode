class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        ugly_numbers = [1]

        #init pointers for 2, 3, 5
        i2 = i3 = i5 = 0

        #initialize multiples of 2, 3, 5
        next_2 = 2
        next_3 = 3
        next_5 = 5

        for _ in range(1, n):
            next_ugly = min(next_2, next_3, next_5)
            ugly_numbers.append(next_ugly)

            if next_ugly == next_2:
                i2 +=1
                next_2 = ugly_numbers[i2] * 2
            if next_ugly == next_3:
                i3 += 1
                next_3 = ugly_numbers[i3] * 3
            if next_ugly == next_5:
                i5 += 1
                next_5 = ugly_numbers[i5] * 5
        

        return ugly_numbers[-1]
