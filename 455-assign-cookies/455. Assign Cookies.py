from typing import List

class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        # Step 1: Sort the greed factors of children and the sizes of cookies
        greed.sort()
        sizes.sort()

        # Step 2: Initialize pointers for children and cookies
        child = 0
        cookie = 0
        content_children = 0

        # Step 3: Iterate through the cookies and try to satisfy the children
        while child < len(greed) and cookie < len(sizes):
            # If the current cookie can satisfy the current child
            if sizes[cookie] >= greed[child]:
                # Increase the number of content children
                content_children += 1
                # Move to the next child
                child += 1

            # Move to the next cookie
            cookie += 1

        # Step 4: Return the total number of content children
        return content_children
