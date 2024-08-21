# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create a map for quick access to employees by their ID
        employee_map = {employee.id: employee for employee in employees}
        
        # Helper function to recursively calculate total importance
        def dfs(emp_id):
            employee = employee_map[emp_id]
            # Start with the importance of the current employee
            total_importance = employee.importance
            # Recursively add the importance of each subordinate
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        
        # Start the DFS with the given employee ID
        return dfs(id)
