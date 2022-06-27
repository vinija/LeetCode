class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        for index in range(1, n+1):
            if n % index == 0:
                k -= 1
                if k == 0:  #  No need to find more than kth  factor, we can simply return it  once we reached.
                    return index
        return -1