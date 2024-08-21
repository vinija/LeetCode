class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create a set to store all the starting cities
        start_cities = set()

        # Add all the starting cities to the set
        for path in paths:
            start_cities.add(path[0])

        # Iterate through the paths to find the destination city
        for path in paths:
            if path[1] not in start_cities:  # If the destination city is not a starting city
                return path[1]  # Return the destination city
