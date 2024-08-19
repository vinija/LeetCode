class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 3:
            return 1
        
        #inital string 122
        magical_str = [1, 2, 2]
        index = 2
        current_num = 1

        while len(magical_str) < n:
            next_count = magical_str[index]
            magical_str.extend([current_num] * next_count)
            index += 1
            current_num = 3 - current_num
        
        return magical_str[:n].count(1)