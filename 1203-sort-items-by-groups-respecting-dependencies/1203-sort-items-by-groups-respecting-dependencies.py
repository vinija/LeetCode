from collections import defaultdict
from collections.abc import Iterable

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # add missing groups
        for i in range(n):
            if group[i] == -1:
                group[i], m = m, m+1

        # translate beforeItems to group dependencies
        group_deps = [set() for _ in range(m)]
        for i in range(n):
            for j in beforeItems[i]:
                # don't add own group as a dependency
                if group[i] != group[j]:
                    group_deps[group[i]].add(group[j])

        def topo_order(deps: list[Iterable[int]]):
            order = []
            visited = set()
            stack = set()
            def dfs(i):  # return True if cycle detected
                if i in stack:
                    return True
                if i in visited:
                    return False
                visited.add(i)
                stack.add(i)
                for dep in deps[i]:
                    if dfs(dep):
                        return True
                # topological ordering is post-order DFS
                order.append(i)
                stack.remove(i)
            for i in range(len(deps)):
                if dfs(i):
                    return None  # if cycle detected return None
            return order

        group_order = topo_order(group_deps)
        item_order = topo_order(beforeItems)
        # if a cycle is detected in groups or items, return []
        if group_order is None or item_order is None:
            return []
        # regroup items by group num
        group_items = defaultdict(list)
        for i in item_order:
            group_items[group[i]].append(i)
        return [i for g in group_order for i in group_items[g]]