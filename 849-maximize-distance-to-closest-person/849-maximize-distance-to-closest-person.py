class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = 0
        result = 1
        flag = 0
        for i in range(len(seats)):
            count += 1
            if seats[i] == 1:
                if flag:
                    result = max(result, (count/2))
                else:
                    result = max(result, count - 1)
                    flag = 1
                count = 0
        result = max(result, count)
        return int(result)