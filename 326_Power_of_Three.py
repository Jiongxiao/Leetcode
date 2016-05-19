class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
        	return False
        import math
        maxInteger=0xffffff
        maxPower=int 
        return math.pow(3,int(math.log(maxInteger,3))) % n==0