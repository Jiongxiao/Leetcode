class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n-1
        r=n%3
        e=n/3
        if r<=1:
            e-=1
            r+=3
        return 3**e*r
    