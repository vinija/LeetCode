from typing import List


class UnionFind:
    """
    Disjoint Set Union (Union-Find) data structure with
    path compression and union by rank.
    """

    def __init__(self, size: int) -> None:
        self.parent: List[int] = list(range(size))
        self.rank: List[int] = [0] * size

    def find(self, x: int) -> int:
        """
        Find the root of x with path compression.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Union the sets containing x and y.
        """
        root_x: int = self.find(x)
        root_y: int = self.find(y)

        if root_x == root_y:
            return

        # Union by rank to keep tree shallow
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        Returns the last day where it is possible to walk
        from the top row to the bottom row using only land cells.
        """

        # Validate inputs
        if row <= 0 or col <= 0:
            raise ValueError("Row and column must be positive integers.")
        if not cells or len(cells) != row * col:
            raise ValueError("Cells list must contain exactly row * col entries.")

        # Total grid cells + 2 virtual nodes (top and bottom)
        total_cells: int = row * col
        top_virtual: int = total_cells
        bottom_virtual: int = total_cells + 1

        uf: UnionFind = UnionFind(total_cells + 2)

        # Track which cells are currently land
        is_land: List[List[bool]] = [[False] * col for _ in range(row)]

        # Directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Helper to convert 2D to 1D index
        def index(r: int, c: int) -> int:
            return r * col + c

        # Process days in reverse
        for day in range(len(cells) - 1, -1, -1):
            r: int = cells[day][0] - 1
            c: int = cells[day][1] - 1

            if is_land[r][c]:
                raise RuntimeError("Cell state corruption detected.")

            # Unflood the cell
            is_land[r][c] = True
            current_index: int = index(r, c)

            # Connect to adjacent land cells
            for dr, dc in directions:
                nr: int = r + dr
                nc: int = c + dc
                if 0 <= nr < row and 0 <= nc < col and is_land[nr][nc]:
                    uf.union(current_index, index(nr, nc))

            # Connect top row cells to top virtual node
            if r == 0:
                uf.union(current_index, top_virtual)

            # Connect bottom row cells to bottom virtual node
            if r == row - 1:
                uf.union(current_index, bottom_virtual)

            # If top and bottom are connected, crossing is possible
            if uf.find(top_virtual) == uf.find(bottom_virtual):
                return day

        # If never connected (should not happen per problem constraints)
        return 0
