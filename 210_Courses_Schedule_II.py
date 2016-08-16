class Solution(object):
    def findOrder(self, numCourses, prerequisites):  
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        from collections import deque

        indegree=[0]*numCourses
        stack=deque()
        for i,j in prerequisites:
            indegree[i]+=1
        for k in range(len(indegree)):
            if indegree[k]==0:
                stack.append(k)
        
        while(stack):
            p=stack.pop()
            result.append(p)
            for i,j in prerequisites:   ###太耗时间了
                if p==j:
                    indegree[i]-=1
                    if indegree[i]==0:
                        stack.append(i)
        for i in indegree:
            if i:
                return []
        return result

class Solution(object):
    def findOrder(self, numCourses, prerequisites):  
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        count=0
        import collections
        from collections import deque
        graph={i: set() for i in range(numCourses)}
        indegree=collections.defaultdict(set)
        for i, j in prerequisites:
            graph[j].add(i)
            indegree[i].add(j)
        stack=deque([i for i in graph if i not in indegree])
        while(stack):
            p=stack.pop()
            result.append(p)
            count+=1
            for j in graph[p]:
                indegree[j].remove(p)
                if indegree[j]==0:
                    stack.append(j)
        return result if count==numCourses else []
