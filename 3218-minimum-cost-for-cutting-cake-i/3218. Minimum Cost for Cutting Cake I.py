class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort the horizontal and vertical cuts in descending order
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        # Initialize pointers for both horizontal and vertical cuts
        h_ptr, v_ptr = 0, 0
        
        # Initialize the number of horizontal and vertical pieces
        horizontal_pieces, vertical_pieces = 1, 1
        
        # Initialize total cost to 0
        total_cost = 0
        
        # While there are cuts remaining in either horizontal or vertical arrays
        while h_ptr < len(horizontalCut) and v_ptr < len(verticalCut):
            # If the current horizontal cut is more expensive, make the horizontal cut
            if horizontalCut[h_ptr] >= verticalCut[v_ptr]:
                total_cost += horizontalCut[h_ptr] * vertical_pieces
                h_ptr += 1
                horizontal_pieces += 1
            # Otherwise, make the vertical cut
            else:
                total_cost += verticalCut[v_ptr] * horizontal_pieces
                v_ptr += 1
                vertical_pieces += 1
        
        # Process any remaining horizontal cuts
        while h_ptr < len(horizontalCut):
            total_cost += horizontalCut[h_ptr] * vertical_pieces
            h_ptr += 1
        
        # Process any remaining vertical cuts
        while v_ptr < len(verticalCut):
            total_cost += verticalCut[v_ptr] * horizontal_pieces
            v_ptr += 1
        
        return total_cost
