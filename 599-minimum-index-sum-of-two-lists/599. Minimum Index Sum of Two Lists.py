class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create a dictionary to store the index of each restaurant in list1
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        # Iterate through list2 to find common restaurants and calculate the index sum
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = j + index_map[restaurant]
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_sum:
                    result.append(restaurant)
        
        return result
