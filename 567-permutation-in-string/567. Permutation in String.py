from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        # Frequency count of s1
        s1_count = Counter(s1)
        # Frequency count of the first window in s2
        window_count = Counter(s2[:len_s1])

        # Check the first window
        if s1_count == window_count:
            return True

        # Slide the window over s2
        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]  # Character going out of the window
            new_char = s2[i]             # Character coming into the window

            # Update the window count
            window_count[new_char] += 1
            window_count[start_char] -= 1

            # Remove the character count from dictionary if it reaches zero
            if window_count[start_char] == 0:
                del window_count[start_char]

            # Compare the frequency counts
            if s1_count == window_count:
                return True

        return False
