class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        if n>10:
            return self.countNumbersWithUniqueDigits(10)
        else:
            return self.countNumbersWithUniqueDigits(n-1)+self.fun(n)

    def fun(self, n):
        if n==2:
            return 9*9
        else:
            return self.fun(n-1)*(11-n)

