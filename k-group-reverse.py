class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = next_head = ListNode(0)
        dummy.next = head
        left = right = head
        
        while True:
            c = 0
            while c < k and right:   
                right = right.next
                c += 1
            if c == k:  
                pre, cur = right, left
                for i in range(k):   # reverse k nodes
                    cur.next, cur, pre = pre, cur.next, cur  
                next_head.next, next_head, left = pre, left, right  #link two groups
            else:  # if num of left nodes < k, skip reversing and return result
                return dummy.next