# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# author: TJX 
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if node ==None or node.next==None:
        	return
        else:
        	temp=node.next
        	node.val,node.next=temp.val,temp.next