class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        from collections import deque

        stack=deque()
        graph=dict()
        indegree=dict()
        count=0
        nodes=[]
        for edge in prerequisites:
            nodes.extend(edge)
            if edge[1] in graph:
                if edge[0] in graph[edge[1]]:       #########very important  (prevent repetitive edges)
                    continue
                graph[edge[1]].add(edge[0])
            else:
                graph[edge[1]]={edge[0]}
            
            indegree[edge[0]]=indegree.get(edge[0],0)+1
        for node in graph.keys():
            if node not in indegree:
                stack.append(node)
        while(stack):
            p=stack.pop()
            count+=1
            if p in graph:
                for j in graph[p]:
                    indegree[j]-=1
                    if indegree[j]==0:
                        stack.append(j)
        nodes=set(nodes)
        num_of_nodes=len(nodes)


        if count<num_of_nodes:
            return False
        if count>numCourses:
            return False
        else:
            return True




            