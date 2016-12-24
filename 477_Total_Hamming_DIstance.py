class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        n=len(nums)
        for i in range(32):
            bit=0
            for num in nums:
                if (num>>i)&1==1:
                    bit+=1
            result+=bit*(n-bit)
        return result



class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        bit=[0]*32
        for num in nums:
            i=0
            while(num>0):
                if num&1==1:
                    bit[i]+=1
                i+=1
                num=num>>1
        return sum(x*(n-x) for x in bit)


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [ [0,0] for _ in xrange(32) ]
        for x in A:
          for i in xrange(32):
            bits[i][x%2] += 1
            x /= 2
        return sum( x*y for x,y in bits )