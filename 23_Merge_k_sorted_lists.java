/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        ListNode head = new ListNode(0);
        return helper(0,lists.length-1, lists);
        
    }
    public ListNode helper(int start, int end,ListNode[] lists){
        if (start == end) return lists[start];
        if (start + 1 == end ) return merge2(lists[start], lists[end]);
        ListNode left = helper(start, (start + end)/2, lists);
        ListNode right = helper((start + end) / 2 + 1, end, lists);
        return merge2(left, right);
    }
    
    public ListNode merge2(ListNode l, ListNode r){
        if (l == null) return r;
        if (r == null) return l;
        ListNode head = new ListNode(0);
        ListNode cur = head;
        while(l != null && r != null){
            if (l.val < r.val){
                cur.next = l;
                l = l.next;
            }
            else{
                cur.next = r;
                r = r.next;
            }
            cur = cur.next;
        }
        cur.next = l == null ? r:l;
        return head.next;
    }
}