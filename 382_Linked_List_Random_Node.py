# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        node=self.head.next ###important     reservoir sampling
        result=self.head
        i=1
        while(node):
            rand=random.randint(0,i)
            if rand==0:
                result=node
            i+=1
            node=node.next
        return result.val


        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()