from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counts = Counter(tasks)
        #find max freq of any task
        max_count = max(task_counts.values())
        #how many tasks have the max
        max_count_tasks = list(task_counts.values()).count(max_count)

        intervals = (max_count - 1) * (n+1) + max_count_tasks

        return max(intervals, len(tasks))