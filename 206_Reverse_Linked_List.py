#206. Reverse_Linked_List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        cur=head
        while cur:
           temp=cur.next
           cur.next=prev
           prev=cur
           cur=temp
        return prev


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None:
        #     return head
        # Vals=[]
        # copy=head
        # result=copy
        # while head:
        #     Vals.append(head.val)
        #     head=head.next
        # while copy:
        #     copy.val=Vals.pop()
        #     copy=copy.next
        # return result
        if head is None or head.next is None:
            return head
        result=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return result
