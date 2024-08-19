class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # If s2 contains any characters not in s1, return 0 immediately
        if not set(s2).issubset(set(s1)):
            return 0

        # Initialize variables to keep track of repetition counts
        s1_count, s2_count = 0, 0  # Counts of how many times s1 and s2 are used
        index_s2 = 0  # Pointer in s2

        # Dictionary to store state to detect cycles
        recall = {}

        while s1_count < n1:
            s1_count += 1  # We are processing one more s1

            # Process each character in s1
            for char in s1:
                if char == s2[index_s2]:
                    index_s2 += 1
                    # If we've matched all of s2, reset index_s2 and increment s2_count
                    if index_s2 == len(s2):
                        index_s2 = 0
                        s2_count += 1

            # If we've seen this state (index_s2) before, cycle detected
            if index_s2 in recall:
                # Previous cycle state
                s1_prev, s2_prev = recall[index_s2]
                # Length of the cycle
                s1_cycle_len = s1_count - s1_prev
                s2_cycle_len = s2_count - s2_prev

                # Number of full cycles we can skip
                remaining_cycles = (n1 - s1_count) // s1_cycle_len

                # Skip the cycles
                s1_count += remaining_cycles * s1_cycle_len
                s2_count += remaining_cycles * s2_cycle_len

            # Store the current state
            recall[index_s2] = (s1_count, s2_count)

        # The number of full sequences of str2 we can get from str1 is s2_count // n2
        return s2_count // n2
