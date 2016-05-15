class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)
        result=0
        for i in range(size):
        	result+=(ord(s[i])-ord('A')+1)*(26**(size-i))
        return result


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=len(s)
        result=0
        for i in range(size):
        	result=result*26+ord(s[i])-ord('A')+1
        return result