from typing import List, Tuple, Dict, Set
from collections import defaultdict

class Solution:
    def gridIllumination(
        self,
        n: int,
        lamps: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:
        """
        Determines whether queried cells are illuminated in an n x n grid.

        A cell is illuminated if there exists an active lamp in the same row,
        column, diagonal, or anti-diagonal.

        After each query, the lamp at the queried cell and its 8 neighbors
        (if present) are turned off.

        Raises:
            ValueError: If n <= 0 or coordinates are out of bounds.

        Returns:
            List[int]: 1 if illuminated, 0 otherwise for each query.
        """

        if n <= 0:
            raise ValueError("Grid size n must be positive.")

        # Active lamp positions
        active_lamps: Set[Tuple[int, int]] = set()

        # Counters for rows, columns, diagonals, anti-diagonals
        row_count: Dict[int, int] = defaultdict(int)
        col_count: Dict[int, int] = defaultdict(int)
        diag_count: Dict[int, int] = defaultdict(int)       # r - c
        anti_diag_count: Dict[int, int] = defaultdict(int)  # r + c

        # Initialize lamp data
        for r, c in lamps:
            if not (0 <= r < n and 0 <= c < n):
                raise ValueError("Lamp coordinates out of grid bounds.")

            # Avoid double-counting duplicate lamps
            if (r, c) not in active_lamps:
                active_lamps.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag_count[r - c] += 1
                anti_diag_count[r + c] += 1

        result: List[int] = []

        # Directions for the 3x3 neighborhood
        directions = [
            (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for r, c in queries:
            if not (0 <= r < n and 0 <= c < n):
                raise ValueError("Query coordinates out of grid bounds.")

            # Check illumination
            illuminated = (
                row_count[r] > 0 or
                col_count[c] > 0 or
                diag_count[r - c] > 0 or
                anti_diag_count[r + c] > 0
            )

            result.append(1 if illuminated else 0)

            # Turn off lamps in the 3x3 area
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in active_lamps:
                    active_lamps.remove((nr, nc))

                    row_count[nr] -= 1
                    col_count[nc] -= 1
                    diag_count[nr - nc] -= 1
                    anti_diag_count[nr + nc] -= 1

                    # Optional cleanup to keep maps small
                    if row_count[nr] == 0:
                        del row_count[nr]
                    if col_count[nc] == 0:
                        del col_count[nc]
                    if diag_count[nr - nc] == 0:
                        del diag_count[nr - nc]
                    if anti_diag_count[nr + nc] == 0:
                        del anti_diag_count[nr + nc]

        return result
