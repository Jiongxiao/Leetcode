class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        string=bin(n)
        result=0
        for i in string:
            if i == '1':
                result+=1
        return result

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        while(n!=0):
            result+=1
            n&=n-1   #####巧妙地删去最地位的1
        return result