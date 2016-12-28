class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    result.append('FizzBuzz')
                else: result.append('Fizz')
            else:
                if i%5==0:
                    result.append('Buzz')
                else:
                    result.append('%d' % i)
        return result