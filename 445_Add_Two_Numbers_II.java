/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l=l1;
        ListNode r=l2;
        StringBuilder s1=new StringBuilder();
        StringBuilder s2=new StringBuilder();
        while(l!=null){
            s1.append(l.val);
            l=l.next;
        }
        while(r!=null){
            s2.append(r.val);
            r=r.next;
        }
        int len1=s1.length();
        int len2=s2.length();
        int resi=0;
        ListNode front= null;
        int temp;
        while(len1>0 && len2>0){
            temp=Integer.parseInt(String.valueOf(s1.charAt(len1-1)))+Integer.parseInt(String.valueOf (s2.charAt(len2-1)))+resi;
            resi=temp/10;
            ListNode cur=new ListNode(temp%10);
            cur.next=front;
            front=cur;
            len1--;
            len2--;
        }
        if(len1>0){
            while(len1>0){
                temp=Integer.parseInt(String.valueOf(s1.charAt(len1-1)))+resi;
                resi=temp/10;
                ListNode cur=new ListNode(temp%10);
                cur.next=front;
                front=cur;
                len1--;
            }
        }
        if(len2>0){
            while(len2>0){
                temp=Integer.parseInt(String.valueOf(s2.charAt(len2-1)))+resi;
                resi=temp/10;
                ListNode cur=new ListNode(temp%10);
                cur.next=front;
                front=cur;
                len2--;
            }
        }
        if (resi>0) {ListNode cur=new ListNode(resi);
            cur.next=front;
            front=cur;}
            
            return front;
        }
    }