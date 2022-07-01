class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x**n
      
        def pow(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return pow(base * base, exponent // 2)
            else:
                return base * pow(base * base, (exponent - 1) // 2)

        if n >= 0:
            return pow()
        else:
            return 1/pow()