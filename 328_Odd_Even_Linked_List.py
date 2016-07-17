# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        odd=p=head
        even=q=head.next
        while(q.next):
            p.next=q.next
            q.next=p.next.next
            p=p.next
            q=q.next
            if not q:
                break
        p.next=even
        return odd