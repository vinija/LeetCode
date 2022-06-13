class Solution:
    def calculate(self, s: str) -> int:
            num = 0
            res = 0
            pre_op = '+'
            s+='+'
            stack = []
            for c in s:
                #if the number is greater than 10
                if c.isdigit():
                    num = num*10 + int(c)
                elif c == ' ':
                        continue
                else:
                    if pre_op == '+':
                        stack.append(num)
                    elif pre_op == '-':
                        stack.append(-num)
                    elif pre_op == '*':
                        operant = stack.pop()
                        stack.append((operant*num))
                    elif pre_op == '/':
                        operant = stack.pop()
                        stack.append(math.trunc(operant/num))
                    num = 0
                    pre_op = c
            return sum(stack)