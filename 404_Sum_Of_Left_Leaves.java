/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return sumOfNode(root);
    }
    public int sumOfNode(TreeNode node){
        if (node==null) return 0;
        if (node.left!=null && node.left.left==null && node.left.right==null) return node.left.val+sumOfNode(node.right);
        else return sumOfNode(node.left)+sumOfNode(node.right);
    }
}