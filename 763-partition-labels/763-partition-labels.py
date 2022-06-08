class Solution(object):
    def partitionLabels(self, S):
        #create a whole dictionary with key = letter value = index of last element of times that letter appears
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            #keep track of max frequency only
            j = max(j, last[c])
            #make sure we met the max freq
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans