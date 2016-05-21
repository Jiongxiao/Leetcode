class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n!=1:
        	n=sum([int(i)**2 for i in str(n)])
        return True