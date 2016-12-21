class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        result=0
        root=int(math.sqrt(2*n))+1
        for i in range(root,0,-1):
            if i*(i+1)/2<=n:
                result=i
                return result

        return result