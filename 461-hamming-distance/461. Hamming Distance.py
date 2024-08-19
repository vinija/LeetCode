class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor_result = x ^ y

        hamming_distance = bin(xor_result).count('1')

        return hamming_distance
        