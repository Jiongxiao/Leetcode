class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        n=len(people)
        res=[]
        for i in range(1,n):
            j=i
            while(j>0 and self.compare(people[j],people[j-1])):
                people[j],people[j-1]=people[j-1],people[j]
                j=j-1
        for p in people:
            res.insert(p[1],p)
        return res


    def compare(self,a,b):
        if a[0]>b[0]:
            return True
        elif a[0]==b[0]:
            return True if a[1]<b[1] else False
        else: return False
