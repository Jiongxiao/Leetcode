class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a= x^y
        return bin(a).count('1')

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a= x^y
        result=0
        while(a):
            if (a>>1)<<1 != a:
                result+=1
            a=a>>1
        return result