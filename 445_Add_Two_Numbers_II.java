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

// Stack

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
            Stack <Integer> s1=new Stack<>();
            Stack <Integer> s2=new Stack<>();
            while(l1!=null){
                s1.push(l1.val);
                l1=l1.next;
            }
            while(l2!=null){
                s2.push(l2.val);
                l2=l2.next;
            }
            int sum=0;
            ListNode front=null;
            while(!s1.empty() || !s2.empty()){
                if (!s1.empty()) sum+=s1.pop();
                if (!s2.empty()) sum+=s2.pop();
                ListNode cur=new ListNode(sum%10);
                cur.next=front;
                front=cur;
                sum=sum/10;
            }
            if (sum>0){
                ListNode cur=new ListNode(sum);
                cur.next=front;
                front=cur;
            }
            return front;
    }
}