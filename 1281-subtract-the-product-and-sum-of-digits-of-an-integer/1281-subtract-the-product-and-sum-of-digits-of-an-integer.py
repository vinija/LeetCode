class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        valm = 1
        vals = 0 
        def cal(input_s, valm = 1, vals = 0 ):
            digit = int(input_s[0])
            valm *= digit
            vals += digit
            # print("digit is" + str(digit) + " valm " + str(valm) + " vals" + str(vals))
            if len(input_s) == 1:
                return (valm - vals)

            # print(int(input_s[1:]))
            return cal(input_s[1:], valm, vals)

        x = cal(str(n))
        return (x)