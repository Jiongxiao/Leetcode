class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not (num&(num-1)) and (num&0x55555555!=0)
