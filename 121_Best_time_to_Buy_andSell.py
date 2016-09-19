class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n=len(prices)
        smallest=prices[0]
        profit=0
        for i in prices:
            if i<smallest:
                smallest=i 
            if i-smallest>profit:
                profit=i-smallest
        return profit



