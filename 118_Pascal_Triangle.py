class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
        	return []
        if numRows==1:
        	return [[1]]
        else:
        	temp=self.generate(numRows-1)
        	lastTerm=temp[-1]
        	result=[1]
        	for i in range(len(lastTerm)-1):
        		result.append(lastTerm[i]+lastTerm[i+1])
        	result.append(1)
        	final=temp.append(result)
        	return temp


	def generate(numRows):
	    pascal = [[1]*(i+1) for i in range(numRows)]
	    for i in range(numRows):
	        for j in range(1,i):
	            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
	    return pascal