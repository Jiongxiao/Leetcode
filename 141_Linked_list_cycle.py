# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
        	return False
        fast=head.next
        slow=head
        while(fast and fast.next):
        	if fast==slow:
        		return True
        	else:
        		fast=fast.next.next
        		slow=slow.next
        return False
####快追慢


####把每个访问过的节点都做上记号
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
        	return False
        cur=head
        while(cur):
        	if cur.next==head:
        		return True
        	else:
        		pre=cur
        		cur=cur.next
        		pre.next=head
        return False
