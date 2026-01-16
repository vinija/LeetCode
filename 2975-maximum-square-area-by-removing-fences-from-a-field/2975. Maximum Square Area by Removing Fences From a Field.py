from typing import List, Set


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        """
        Computes the maximum possible square area that can be formed by removing fences.

        :param m: Maximum x-coordinate (height of field)
        :param n: Maximum y-coordinate (width of field)
        :param hFences: Positions of horizontal fences
        :param vFences: Positions of vertical fences
        :return: Maximum square area modulo 1e9+7, or -1 if impossible
        """

        MOD: int = 10**9 + 7

        # Defensive checks for invalid inputs
        if m < 3 or n < 3:
            raise ValueError("Field dimensions must be at least 3.")

        # Add the fixed boundary fences
        horizontal: List[int] = [1, m]
        vertical: List[int] = [1, n]

        horizontal.extend(hFences)
        vertical.extend(vFences)

        # Sort fence positions to ensure correct difference calculations
        horizontal.sort()
        vertical.sort()

        # Compute all possible horizontal distances
        horizontal_distances: Set[int] = set()
        h_len: int = len(horizontal)

        for i in range(h_len):
            for j in range(i + 1, h_len):
                horizontal_distances.add(horizontal[j] - horizontal[i])

        # Compute vertical distances and find the maximum common side length
        max_side: int = 0
        v_len: int = len(vertical)

        for i in range(v_len):
            for j in range(i + 1, v_len):
                side_length: int = vertical[j] - vertical[i]
                if side_length in horizontal_distances:
                    if side_length > max_side:
                        max_side = side_length

        # If no square can be formed
        if max_side == 0:
            return -1

        # Compute area modulo MOD
        return (max_side * max_side) % MOD


# -----------------------------
# Test cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    m1, n1 = 4, 3
    hFences1 = [2, 3]
    vFences1 = [2]
    print(sol.maximizeSquareArea(m1, n1, hFences1, vFences1))  # Expected: 4

    # Test case 2
    m2, n2 = 6, 7
    hFences2 = [2]
    vFences2 = [4]
    print(sol.maximizeSquareArea(m2, n2, hFences2, vFences2))  # Expected: -1
