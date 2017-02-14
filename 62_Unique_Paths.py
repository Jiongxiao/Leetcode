class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        res=[[1]*n]*m
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=res[i][j-1]+res[i-1][j]
        return res[m-1][n-1]

