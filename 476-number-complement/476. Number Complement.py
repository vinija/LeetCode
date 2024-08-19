class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Convert the number to its binary string representation (without the '0b' prefix)
        binary_str = bin(num)[2:]
        
        # Step 2: Flip the bits (change '0' to '1' and '1' to '0')
        complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        
        # Step 3: Convert the flipped binary string back to an integer
        return int(complement_str, 2)
