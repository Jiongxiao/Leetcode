# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None or l2 is None:
        	return l1 or l2
        
        list1=[]
        list2=[]
        while l1:
        	list1.append(l1.val)
        	l1=l1.next
        while l2:
        	list2.append(l2.val)
        	l2=l2.next
        array=[]
        i=0;j=0
        while i<len(list1) and j<len(list2):
        	if list1[i]<list2[j]:
        		array.append(list1[i])
        		i+=1
        	else:
        		array.append(list2[j])
        		j+=1
        if i>=len(list1):
        	array.extend(list2[j:])
        else:
        	array.extend(list1[i:])
        cur=ListNode(array[0])
        head=cur
        for num in array[1:]:
        	cur.next=ListNode(num)
        	cur=cur.next
        return head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
        	return l1 or l2
        head=ListNode(0)
        p=head
        while l1 and l2:
        	if l1.val<l2.val:
        		p.next=ListNode(l1.val)
        		l1=l1.next
        		p=p.next
        	else:
        		p.next=ListNode(l2.val)
        		l2=l2.next
        		p=p.next
        if l1:
        	p.next=l1
        else:
        	p.next=l2
        return head.next

##更优化方法: 前两种方法可能不对，题目好像要求不能重建node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 is None): return l2
        if(l2 is None): return l1
        if (l1.val<l2.val):
        	l1.next=self.mergeTwoLists(l1.next,l2)
        	return l1
        else:
        	l2.next=self.mergeTwoLists(l2.next,l1)
        	return l2
        	
