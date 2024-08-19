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
        
        # While there are cuts remaining in both horizontal and vertical arrays
        while h_ptr < len(horizontalCut) and v_ptr < len(verticalCut):
            # If the current horizontal cut is more expensive, make the horizontal cut
            if horizontalCut[h_ptr] >= verticalCut[v_ptr]:
                # Add the cost of making the horizontal cut
                total_cost += horizontalCut[h_ptr] * vertical_pieces
                # Move the pointer to the next horizontal cut
                h_ptr += 1
                # Increase the number of horizontal pieces after the cut
                horizontal_pieces += 1
            else:
                # Otherwise, make the vertical cut
                total_cost += verticalCut[v_ptr] * horizontal_pieces
                # Move the pointer to the next vertical cut
                v_ptr += 1
                # Increase the number of vertical pieces after the cut
                vertical_pieces += 1
        
        # Process any remaining horizontal cuts after all vertical cuts are done
        while h_ptr < len(horizontalCut):
            total_cost += horizontalCut[h_ptr] * vertical_pieces
            h_ptr += 1
        
        # Process any remaining vertical cuts after all horizontal cuts are done
        while v_ptr < len(verticalCut):
            total_cost += verticalCut[v_ptr] * horizontal_pieces
            v_ptr += 1
        
        # Return the total minimum cost to cut the entire cake into 1x1 pieces
        return total_cost
