class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        
        jobs = sorted(jobs)
        #job = (2, 10)
# (4, 20)
# (6, 30)
# (8, 40)
# (10, 50)

        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
