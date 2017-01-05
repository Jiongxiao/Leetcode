class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<2:
            return 0
        res=0
        front=1
        back=0
        while(front<n):
            if prices[front]>prices[back]:
                res+=prices[front]-prices[back]
                front+=1
                back+=1
            else:
                back=front
                front+=1
        return res


        