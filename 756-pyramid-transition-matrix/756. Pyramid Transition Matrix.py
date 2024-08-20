class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Create a dictionary to store the allowed transitions
        # Key: (char1, char2), Value: set of possible chars on top
        transitions = {}
        for triplet in allowed:
            key = (triplet[0], triplet[1])
            if key not in transitions:
                transitions[key] = set()
            transitions[key].add(triplet[2])

        # Helper function to recursively check if the pyramid can be built
        def canBuild(current: str, next_level: str, index: int) -> bool:
            # If we successfully built the top of the pyramid, return True
            if len(current) == 1:
                return True
            
            # If we filled the next level, move to the next level of the pyramid
            if index == len(current) - 1:
                return canBuild(next_level, "", 0)
            
            # Get the possible characters that can be placed on top
            key = (current[index], current[index + 1])
            if key in transitions:
                for char in transitions[key]:
                    # Recursively attempt to build the next level with the current choice
                    if canBuild(current, next_level + char, index + 1):
                        return True
            
            # If no valid pyramid can be formed, return False
            return False

        # Start the pyramid building process from the bottom
        return canBuild(bottom, "", 0)
