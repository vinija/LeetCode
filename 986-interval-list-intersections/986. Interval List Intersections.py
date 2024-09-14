class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        retList : List[List[int]] = []
        
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
        
            i_start, i_end = firstList[i]
            j_start, j_end = secondList[j]

            #Two possible conditions, either first starts first, or second starts first
            #Check if first starts first

            start_max = max(i_start, j_start)
            end_min = min(i_end,j_end)

            #Check if there is an overlap
            if start_max <= end_min:
                retList.append([start_max, end_min])
            
            #move pointers
            if i_end < j_end:
                i+= 1
            else:
                j+=1



        return retList