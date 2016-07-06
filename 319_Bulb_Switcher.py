class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulb=[True]*(n+1)
        for i in range(2,len(bulb)):
        	for j in range(i,len(bulb)):
        		if j%i==0:
        			bulb[j]=not bulb[j]
        result=-1
        for i in bulb:
        	if i==True:
        		result+=1
        return result
######妥妥超时#######

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
###只有平方数是奇数个因数