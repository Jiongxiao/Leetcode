class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic=set()
        while n!=1:
        	n=sum([int(i)**2 for i in str(n)])
        	if n in dic:
        		return False
        	dic.add(n)
        return True